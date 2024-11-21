import boto3
import time
# python3 -m pip install boto3
# Initialize a session using Amazon EC2
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'  # Change to your preferred region
)

# Initialize the EC2 client
ec2_client = session.client('ec2')

# Function to get instance status
def get_instance_status(instance_id):
    response = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    if response['InstanceStatuses']:
        return response['InstanceStatuses'][0]['InstanceState']['Name']
    else:
        return None

# Start an instance and wait until it's running
def start_instance(instance_id):
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance {instance_id}...")

    while True:
        status = get_instance_status(instance_id)
        if status == 'running':
            print(f"Instance {instance_id} is running.")
            break
        elif status == 'pending':
            print(f"Instance {instance_id} is still pending...")
            time.sleep(5)
            continue
        else:
            print(f"Unexpected status: {status}")
            break

# Example EC2 instance IDs
instance_ids = ['i-0abcd1234efgh5678', 'i-0hijk1234lmno5678']

# Main logic
for instance_id in instance_ids:
    status = get_instance_status(instance_id)
    
    if status is None:
        print(f"Instance {instance_id} does not exist.")
        pass  # Normally, you might handle this case properly
    elif status == 'stopped':
        print(f"Instance {instance_id} is stopped.")
        start_instance(instance_id)
    elif status == 'running':
        print(f"Instance {instance_id} is already running.")
    else:
        print(f"Instance {instance_id} is in status: {status}.")
