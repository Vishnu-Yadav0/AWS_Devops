import boto3
from datetime import datetime, timezone

# Initialize boto3 client for CloudTrail
client = boto3.client('cloudtrail')

# Define the specific user you want to filter events for
specific_user = 'svc-c3ops'  # Replace with the actual username you want to filter by

# Get the current UTC time
end_time = datetime.now(timezone.utc)

# Calculate 7 days ago by subtracting the seconds equivalent to 7 days
start_time_epoch = end_time.timestamp() - (7 * 24 * 60 * 60)

# Convert the start time from epoch to datetime
start_time = datetime.fromtimestamp(start_time_epoch, tz=timezone.utc)

# Function to print events related to S3 service and a specific user
def print_user_s3_events(start_time, end_time, specific_user):
    try:
        # Paginate through the events
        paginator = client.get_paginator('lookup_events')
        response_iterator = paginator.paginate(
            StartTime=start_time,
            EndTime=end_time,
            LookupAttributes=[
                {
                    'AttributeKey': 'EventSource',
                    'AttributeValue': 's3.amazonaws.com'
                },
                {
                    'AttributeKey': 'Username',
                    'AttributeValue': specific_user
                }
            ]
        )
        
        # Iterate over the pages of events
        for page in response_iterator:
            for event in page['Events']:
                print(f"Event ID: {event['EventId']}")
                print(f"Event Name: {event['EventName']}")
                print(f"Event Time: {event['EventTime']}")
                print(f"User: {event['Username']}")
                print(f"Request Parameters: {event['CloudTrailEvent']}")
                print("-" * 60)
    
    except Exception as e:
        print(f"Error retrieving S3 events: {str(e)}")

# Call the function with the specified user
print_user_s3_events(start_time, end_time, specific_user)
