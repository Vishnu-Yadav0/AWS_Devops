import boto3

class S3Paginator:
    def __init__(self, bucket_name, region_name='us-east-1'):
        self.s3_client = boto3.client('s3', region_name=region_name)
        self.bucket_name = bucket_name

    def list_objects(self, prefix='', page_size=100):
        paginator = self.s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(
            Bucket=self.bucket_name,
            Prefix=prefix,
            PaginationConfig={'PageSize': page_size}
        )

        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    yield obj['Key']

# Usage Example
if __name__ == "__main__":
    bucket_name = '8amcloudbinary'
    s3_paginator = S3Paginator(bucket_name)

    print(f"Listing objects in bucket: {bucket_name}")
    for obj_key in s3_paginator.list_objects():
        print(obj_key)
