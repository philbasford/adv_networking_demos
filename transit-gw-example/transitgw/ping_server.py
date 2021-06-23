"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core as cdk
)


class PingServer(ec2.Instance):
    """The Ping Server.

    This is just a standard Amazon Linux instance the accepts ICMP.

    Args:
        ec2 ([type]): The base EC2 class that we will extend to customise to a EC2 resouce
    """

    def __init__(self, stack: cdk.Stack, prefix, vpc, **kwargs) -> None:

        amqlin2_image = ec2.MachineImage.latest_amazon_linux(
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        )

        # Instance Role and SSM Managed Policy
        role = iam.Role(
            stack, prefix + "IamSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(
            "service-role/AmazonEC2RoleforSSM"))

        # SecurityGroup
        sg = ec2.SecurityGroup(
            stack, prefix + "SecurityGroup",
            vpc=vpc,
            description=f"{prefix}Access",
            security_group_name=f"{prefix}SG"
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.all_icmp()
        )

        super().__init__(
            stack, prefix + "Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=amqlin2_image,
            vpc=vpc,
            role=role,
            source_dest_check=False,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.ISOLATED
            ),
            key_name='vpc-lab',
            security_group=sg
        )
