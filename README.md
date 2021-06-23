
# Welcome to Advance Networking Demos!

The following demos are based on the https://acloudguru.com/course/aws-certified-advanced-networking-specialty-2 @ 22 June 2021. I have VPN and Transit GW demos and I have redone them in CDK.

## Why
I did this during the course to get more into depths of the CDK and to help build a better understanding of the examples. So I wanted to share it.

# Some Tips

* Your need to allow the VPN Instance the UDP ports needed to initiate a the phase 1 and 2 tunnels. I wont' tell you what they are as it helps your learning
* You will still need to setup the VPN and Transit GW yourself
* Sometimes the User Data for the VPN Instance does not work. As per demo just rerun them over RDP or Session Manager
* update the key pair to your own and your need a key pair for each region
* there is one route table per AZ, so you need to add static routes twice

