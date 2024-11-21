import boto3

rds = boto3.client('rds')

# Create a new RDS instance
response = rds.create_db_instance(
    DBName='c3ops',
    DBInstanceIdentifier='c3opsdev',
    MasterUsername='admin',
    MasterUserPassword='password',
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    AllocatedStorage=20
)

print(f'RDS instance created with identifier: {response["DBInstance"]["DBInstanceIdentifier"]}')
