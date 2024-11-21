import boto3

class RDSManager:
    def __init__(self, region_name):
        self.rds_client = boto3.client('rds', region_name=region_name)

    def start_db_instance(self, db_instance_identifier):
        response = self.rds_client.start_db_instance(
            DBInstanceIdentifier=db_instance_identifier
        )
        return response

    def stop_db_instance(self, db_instance_identifier):
        response = self.rds_client.stop_db_instance(
            DBInstanceIdentifier=db_instance_identifier
        )
        return response

    def describe_db_instance(self, db_instance_identifier):
        response = self.rds_client.describe_db_instances(
            DBInstanceIdentifier=db_instance_identifier
        )
        if 'DBInstances' in response and len(response['DBInstances']) > 0:
            return response['DBInstances'][0]
        else:
            return None

    def list_db_instances(self):
        response = self.rds_client.describe_db_instances()
        db_instances = []
        for db_instance in response['DBInstances']:
            db_instances.append(db_instance)
        return db_instances

# Usage Example
if __name__ == "__main__":
    rds_manager = RDSManager(region_name='us-east-1')

    # Start an RDS instance
    db_instance_identifier = 'cloudbinaryportal'
    # print(f"Starting RDS instance {db_instance_identifier}")
    # start_response = rds_manager.start_db_instance(db_instance_identifier)
    # print(start_response)

    # Stop an RDS instance
    # print(f"Stopping RDS instance {db_instance_identifier}")
    # stop_response = rds_manager.stop_db_instance(db_instance_identifier)
    # print(stop_response)

    # Describe an RDS instance
    print(f"Describing RDS instance {db_instance_identifier}")
    db_instance_description = rds_manager.describe_db_instance(db_instance_identifier)
    print(db_instance_description)

    # List all RDS instances
    # print("Listing all RDS instances")
    # db_instances = rds_manager.list_db_instances()
    # for db_instance in db_instances:
    #     print(db_instance['DBInstanceIdentifier'], db_instance['DBInstanceStatus'])
