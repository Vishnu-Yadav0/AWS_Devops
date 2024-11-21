import boto3

s3 = boto3.client('s3')

# Create a new S3 bucket
bucket_name = 'c3ops-devpython'

response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created.')
