"""The following file is released under the Apache 2 Licence, see LICENCE.txt."""

import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="vpn_example",
    version="0.0.1",

    description="A Cloud Gurus Transit Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Phil Basford",

    package_dir={"": "vpn_example"},
    packages=setuptools.find_packages(where="vpn_example"),

    install_requires=[
        "aws-cdk.core==1.109.0",
        "aws-cdk.aws_ec2",
        "aws-cdk.aws_ecs",
        "aws-cdk.aws_ecs_patterns",
        "aws-cdk.aws_rds",
        "aws_cdk.aws_secretsmanager"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
