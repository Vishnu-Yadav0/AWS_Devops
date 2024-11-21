import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Specify the instance ID to terminate
instance_id = 'i-018f66fa3498620ab'

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

# Check the response
for instance in response['TerminatingInstances']:
    print(f'Instance ID: {instance["InstanceId"]}, Previous State: {instance["PreviousState"]["Name"]}, Current State: {instance["CurrentState"]["Name"]}')
