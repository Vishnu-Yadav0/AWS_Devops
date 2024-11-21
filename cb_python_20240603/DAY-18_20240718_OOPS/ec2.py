import boto3

class EC2Manager:
    def __init__(self, region_name):
        self.ec2_client = boto3.client('ec2', region_name=region_name)

    def start_instance(self, instance_id):
        response = self.ec2_client.start_instances(
            InstanceIds=[instance_id]
        )
        return response

    def stop_instance(self, instance_id):
        response = self.ec2_client.stop_instances(
            InstanceIds=[instance_id]
        )
        return response

    def describe_instance(self, instance_id):
        response = self.ec2_client.describe_instances(
            InstanceIds=[instance_id]
        )
        if 'Reservations' in response and len(response['Reservations']) > 0:
            return response['Reservations'][0]['Instances'][0]
        else:
            return None

    def list_instances(self):
        response = self.ec2_client.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)
        return instances

# Usage Example
if __name__ == "__main__":
    ec2_manager = EC2Manager(region_name='ap-south-2')

    # Start an instance
    instance_id = 'i-0e3dc64f7c7283c72'
    print(f"Starting instance {instance_id}")
    start_response = ec2_manager.start_instance(instance_id)
    print(start_response)

    # # Stop an instance
    # print(f"Stopping instance {instance_id}")
    # stop_response = ec2_manager.stop_instance(instance_id)
    # print(stop_response)

    # Describe an instance
    print(f"Describing instance {instance_id}")
    instance_description = ec2_manager.describe_instance(instance_id)
    print(instance_description)

    # List all instances
    print("Listing all instances")
    instances = ec2_manager.list_instances()

    for instance in instances:
        print(instance['InstanceId'], instance['State']['Name'])
