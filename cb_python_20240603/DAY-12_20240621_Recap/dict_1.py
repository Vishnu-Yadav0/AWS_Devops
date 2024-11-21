
aws = {

    "ec2": "Virtual Machines",
    "ec2_year": 2006,
    "s3": "Simple Storage Service",
    "s3_year": 2006.07, 
    "route53": "DNS",
    "route53": "DNS",
    "container_services_in_aws": ["ecs","ecr",'eks','fargte'],
    "compute_services_in_aws": ("ec2","lambda",'apprunner','elasticbeanstack'),
    "storage_services": {"s3","efs","fsx","ebs","ebs"},
    "iaas": "true"
}
print(aws)
print(aws["ec2"])
print(len(aws))
print(type(aws))