# AWS-CDK-EKS

Task Details - Deploy eks cluster using AWS CDK in AWS.

DEPLOYMENT DETAILS:-

Python code files:-

app.py --> main file
vpc_stack.py --> vpc stack code
eks_stack.py --> eks stack code



Commands used:

cdk ls --> to list all stacks

cdk synth eks --> to transfer python code (eks and vpc) into cloudformation templates

cdk deploy eks --profile <profile_name> --> to deploy EKS cluster
