"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    core as cdk
)
from vpn_example.public_vpc import PublicVPC


class OnPremStack(cdk.Stack):
    """This is OnPrem, containing a public Windows Server instance to be used as the Customer Gatewat device).

    Args:
        ec2 ([type]): The base Stack class that we will extend to customise to add resources
    """

    cidr = "10.30.0.0/22"

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PublicVPC(self, "on-prem-", self.cidr)
