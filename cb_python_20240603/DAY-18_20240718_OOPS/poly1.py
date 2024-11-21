'''
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the 
same name that can be executed on many objects or classes.

Function Polymorphism

An example of a Python function that can be used on different objects is the len() function.




'''

import boto3
from abc import ABC, abstractmethod

class AWSResourceManager(ABC):
    def __init__(self, service_name, region_name='us-west-2'):
        self.client = boto3.client(service_name, region_name=region_name)

    @abstractmethod
    def list_resources(self):
        pass

class IAMManager(AWSResourceManager):
    def __init__(self, region_name='us-east-1'):
        super().__init__('iam', region_name)

    def list_resources(self):
        response = self.client.list_users()
        return [user['UserName'] for user in response['Users']]

def list_all_resources(managers):
    for manager in managers:
        print(f"Listing resources for {manager.__class__.__name__}:")
        resources = manager.list_resources()
        for resource in resources:
            print(resource)
        print()

if __name__ == "__main__":
    region = 'us-east-1'

    iam_manager = IAMManager(region_name=region)
    managers = [iam_manager]

    list_all_resources(managers)
