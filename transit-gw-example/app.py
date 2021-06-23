"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

from aws_cdk import core as cdk
from transitgw.region_1_stack import Region1Stack
from transitgw.region_2_stack import Region2Stack


app = cdk.App()
Region1Stack(
    app, "TransitGWStack1",
    env=cdk.Environment(region='eu-west-1'),
)
Region2Stack(
    app, "TransitGWStack2",
    env=cdk.Environment(region='eu-central-1'),
)

app.synth()
