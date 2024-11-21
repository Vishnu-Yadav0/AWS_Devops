import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Specify the instance IDs you want to check the status for
instance_ids = ['i-018f66fa3498620ab', 'i-05008be0440f4d602']

# Describe the instance status
response = ec2.describe_instance_status(InstanceIds=instance_ids)

# Print the status of each instance
for instance in response['InstanceStatuses']:
    instance_id = instance['InstanceId']
    state = instance['InstanceState']['Name']
    status = instance['InstanceStatus']['Status']
    print(f'Instance ID: {instance_id}, State: {state}, Status: {status}')
