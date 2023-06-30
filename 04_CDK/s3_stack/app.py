#!/usr/bin/env python3

import aws_cdk as cdk

from s3_stack.s3_stack_stack import S3StackStack


app = cdk.App()
S3StackStack(app, "s3-stack")

app.synth()
