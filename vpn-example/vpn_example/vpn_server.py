"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core as cdk
)


class VPNServer(ec2.Instance):
    """The VPN Server.

    This is just a Windows Server 2016 instance install and running VPN Service

    Args:
        ec2 ([type]): The base EC2 class that we will extend to customise to a EC2 resouce
    """

    def __init__(self, stack: cdk.Stack, prefix, vpc, **kwargs) -> None:

        windows_image = ec2.MachineImage.latest_windows(
            version=ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
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
            connection=ec2.Port.tcp(3389)
        )

        super().__init__(
            stack, prefix + "Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=windows_image,
            vpc=vpc,
            role=role,
            source_dest_check=False,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            key_name='vpc-lab',
            security_group=sg
        )

        self.user_data.add_commands(
            'Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}" -Name "IsInstalled" -Value 0 -Force',
            'Stop-Process -Name iexplore -ErrorAction SilentlyContinue',
            'Set-NetAdapterAdvancedProperty -DisplayName "IPv4 Checksum Offload" -DisplayValue "Disabled"',
            'Set-NetAdapterAdvancedProperty -DisplayName "TCP Checksum Offload (IPv4)" -DisplayValue "Disabled"',
            'Set-NetAdapterAdvancedProperty -DisplayName "UDP Checksum Offload (IPv4)" -DisplayValue "Disabled"',
            'Invoke-WebRequest https://steveatacg.s3-us-west-1.amazonaws.com/advnetspec/Win2019VPNServerConfig.xml -OutFile c:\config.xml',
            'Install-WindowsFeature -ConfigurationFilePath c:\config.xml -computername $env:COMPUTERNAME -Restart',
            'Install-RemoteAccess -VpnType VpnS2S # doing this on 2019 (and 2016 apparenlty) restricts RRAS management to PS tools.  This seems to have no impact on AWS configuration steps'
        )
