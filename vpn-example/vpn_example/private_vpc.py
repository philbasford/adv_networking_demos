"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    aws_ec2 as ec2,
    core as cdk
)
from vpn_example.ping_server import PingServer


class PrivateVPC(ec2.Vpc):
    """A VPC that only contains 3 private subnets with not NATs (ISOLATED).

    Args:
        ec2 ([type]): The base VPC class that we will extend to customise the VPC
    """

    def __init__(self, stack: cdk.Stack, prefix, cidr, **kwargs) -> None:

        super().__init__(
            stack,
            id=prefix,
            cidr=cidr,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='private-subnet',
                    subnet_type=ec2.SubnetType.ISOLATED,
                    cidr_mask=24
                )
            ],
            max_azs=3
        )

        PingServer(stack, prefix, self)
