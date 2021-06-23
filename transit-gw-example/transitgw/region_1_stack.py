"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    core as cdk
)
from transitgw.private_vpc import PrivateVPC
from transitgw.public_vpc import PublicVPC


class Region1Stack(cdk.Stack):
    """This is Region 1, containing a public VPC with the Jump Server, and 2 private VPCs with a Ping Server in each.

    Args:
        ec2 ([type]): The base Stack class that we will extend to customise to add resources
    """

    cidr_a = "10.30.0.0/22"
    cidr_b = "10.40.0.0/22"
    cidr_c = "10.50.0.0/22"

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PublicVPC(self, "vpc-a-", self.cidr_a)
        PrivateVPC(self, "vpc-b-", self.cidr_b)
        PrivateVPC(self, "vpc-c-", self.cidr_c)
