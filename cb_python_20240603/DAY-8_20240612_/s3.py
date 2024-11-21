# import boto3

# # Create an S3 client
# s3_client = boto3.client('s3')

# # List S3 buckets
# response = s3_client.list_buckets()
# for bucket in response['Buckets']:
#     print(bucket['Name'])

import boto3

# Create an S3 resource
s3_resource = boto3.resource('s3')

# List S3 buckets
for bucket in s3_resource.buckets.all():
    print(bucket.name)


"""
Boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. Boto3 has three main components to interact with AWS services: Clients, Resources, and Sessions. Each component serves different purposes and provides different levels of abstraction.

1. Boto3 Clients
Clients provide a low-level interface to AWS services. They map 1:1 with the service's API. This means that you can call every operation available in the service directly. Clients return dictionary-like objects that mirror the JSON responses from the AWS service APIs.

"""
# Example: Using a Client to List Buckets in S3

import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# List S3 buckets
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

'''
2. Boto3 Resources
Resources provide a higher-level, more object-oriented API. They are designed to make it easier to work with AWS services by abstracting some of the low-level details and providing attributes and methods for interacting with AWS resources. Resources expose the objects and attributes in a more Pythonic way compared to clients.

'''

# Example: Using a Resource to List Buckets in S3
import boto3

# Create an S3 resource
s3_resource = boto3.resource('s3')

# List S3 buckets
for bucket in s3_resource.buckets.all():
    print(bucket.name)


"""
3. Boto3 Sessions
Sessions allow you to manage AWS credentials and configurations. A session represents a connection to AWS, and you can create multiple sessions if you need to manage multiple accounts or regions. Clients and resources are created from sessions. If you don’t explicitly create a session, Boto3 uses the default session.


"""
# Example: Using a Session to Create a Client and Resource

import boto3

# Create a session
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Create an S3 client from the session
s3_client = session.client('s3')

# Create an S3 resource from the session
s3_resource = session.resource('s3')

# List S3 buckets using the client
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# List S3 buckets using the resource
for bucket in s3_resource.buckets.all():
    print(bucket.name)


'''

Key Differences
Level of Abstraction:

Clients: Provide low-level access to AWS services. Every method corresponds to a single API call.
Resources: Provide a higher-level, object-oriented API. Methods and attributes may abstract multiple API calls.
Sessions: Manage AWS credentials and configurations. They serve as a factory for creating clients and resources.

Return Types:

Clients: Return dictionary-like responses directly from AWS service APIs.
Resources: Return resource instances and attributes, offering a more intuitive interface.

Use Cases:

Clients: Best for scenarios where you need direct access to AWS service APIs or need to use service-specific features not covered by resources.

Resources: Best for common operations where an object-oriented approach is more convenient and readable.

Sessions: Useful when working with multiple AWS accounts, regions, or needing more control over credentials and configuration.
By understanding these components, you can choose the most appropriate one for your specific use case when working with AWS services in Python using Boto3.

'''