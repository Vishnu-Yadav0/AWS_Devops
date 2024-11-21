import boto3

# Create an S3 resource
s3_resource = boto3.resource('s3')

# List S3 buckets
for bucket in s3_resource.buckets.all():
    print(bucket.name)

 