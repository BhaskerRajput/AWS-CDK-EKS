#!/usr/bin/env python3

from aws_cdk import core

#import VPC and EKS stack

from stacks.vpc_stack import VPCStack
from stacks.eks_stack import EKSStack
env = core.Environment(account='<account_id>', region='us-east-1')
app = core.App()

#VPC and EKS stack instance creation

vpc_stack = VPCStack(app, 'vpc')
eks_stack = EKSStack(app, 'eks', vpc=vpc_stack.vpc)
app.synth()