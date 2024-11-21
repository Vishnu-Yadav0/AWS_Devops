'''
AWS Boto3:
    Boto3 is the Amazon Web Services (AWS) SDK for Python, 
    which allows Python developers to write software that makes use of services 
    like Amazon S3 and Amazon EC2.

'''

import boto3

ec2 = boto3.resource('ec2')

# Create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-04b70fa74e45c3917',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='nv_amazlinux'
)

for instance in instances:
    print(f'Created instance with ID: {instance.id}')
