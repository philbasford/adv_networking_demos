"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    core as cdk
)
from transitgw.private_vpc import PrivateVPC


class Region2Stack(cdk.Stack):
    """This is Region 2, containing 1 private VPC with a Ping Server in it.

    Args:
        ec2 ([type]): The base Stack class that we will extend to customise to add resources
    """

    cidr_d = "10.60.0.0/22"

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PrivateVPC(self, "vpc-d-", self.cidr_d)
