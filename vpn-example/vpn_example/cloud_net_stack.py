"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    core as cdk
)
from vpn_example.private_vpc import PrivateVPC


class CloudNetStack(cdk.Stack):
    """This is CloudNet, containing a private instance that will only reached over the VPN).

    Args:
        ec2 ([type]): The base Stack class that we will extend to customise to add resources
    """

    cidr_d = "10.40.0.0/22"

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PrivateVPC(self, "cloud-net-", self.cidr_d)
