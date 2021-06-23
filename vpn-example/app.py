"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import core as cdk
from vpn_example.cloud_net_stack import CloudNetStack
from vpn_example.on_prem_stack import OnPremStack


app = cdk.App()
CloudNetStack(
    app, "CloudNetStack",
    env=cdk.Environment(region='eu-west-1')
)
OnPremStack(
    app, "OnPremStack",
    env=cdk.Environment(region='eu-central-1')
)

app.synth()
