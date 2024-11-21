# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
# x.printname()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
  pass

'''
Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
'''

import boto3

class AWSManager:
    def __init__(self, service_name, region_name):
        self.client = boto3.client(service_name, region_name=region_name)

    def get_client(self):
        return self.client

class S3Manager(AWSManager):
    def __init__(self, region_name):
        super().__init__('s3', region_name)

    def create_bucket(self, bucket_name):
        response = self.client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': self.client.meta.region_name}
        )
        return response

    def upload_file(self, file_name, bucket_name, object_name=None):
        if object_name is None:
            object_name = file_name
        response = self.client.upload_file(file_name, bucket_name, object_name)
        return response

    def download_file(self, bucket_name, object_name, file_name):
        response = self.client.download_file(bucket_name, object_name, file_name)
        return response

    def list_objects(self, bucket_name):
        response = self.client.list_objects_v2(Bucket=bucket_name)
        return response.get('Contents', [])


if __name__ == "__main__":
    region = 'us-east-1'
    s3_manager = S3Manager(region_name=region)

    # Create a bucket
    bucket_name = '8amcloudbinary'
    # print(f"Creating bucket: {bucket_name}")
    # create_bucket_response = s3_manager.create_bucket(bucket_name)
    # print(create_bucket_response)

    # Upload a file
    # file_name = 'example.txt'
    # print(f"Uploading file: {file_name} to bucket: {bucket_name}")
    # upload_file_response = s3_manager.upload_file(file_name, bucket_name)
    # print(upload_file_response)

    # List objects in the bucket
    print(f"Listing objects in bucket: {bucket_name}")
    objects = s3_manager.list_objects(bucket_name)
    for obj in objects:
        print(obj['Key'])

    # Download a file
    #download_file_name = 'downloaded_example.txt'
    #print(f"Downloading file: {file_name} from bucket: {bucket_name} to {download_file_name}")
    # download_file_response = s3_manager.download_file(bucket_name, file_name, download_file_name)
    # print(download_file_response)
