import boto3

session = boto3.Session(region_name="us-east-1")

ec2 = session.client('ec2')

# VPC creation
vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')

vpc_id = vpc['Vpc']['VpcId']

# vpc-0eb12afd59e72baf7
# Enable DNS support and DNS hostnames in the VPC

ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

# Step 2: Create Subnets (2 Public and 4 Private)
subnet_public_1 = ec2.create_subnet(CidrBlock='192.168.1.0/28', VpcId=vpc_id, AvailabilityZone='us-east-1a')
subnet_public_2 = ec2.create_subnet(CidrBlock='192.168.2.0/28', VpcId=vpc_id, AvailabilityZone='us-east-1b')

subnet_private_1 = ec2.create_subnet(CidrBlock='192.168.3.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1a')
subnet_private_2 = ec2.create_subnet(CidrBlock='192.168.4.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1b')
subnet_private_3 = ec2.create_subnet(CidrBlock='192.168.5.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1a')
subnet_private_4 = ec2.create_subnet(CidrBlock='192.168.6.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1b')

# Step 3: Create an Internet Gateway (IGW) and Attach it to the VPC

igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)

# Step 4: Create Route Tables and Routes
# Public Route Table

route_table_public = ec2.create_route_table(VpcId=vpc_id)
route_table_public_id = route_table_public['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=route_table_public_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)

# Private Route Table (one for simplicity; in a real-world scenario, consider more specific routing needs)
route_table_private = ec2.create_route_table(VpcId=vpc_id)
route_table_private_id = route_table_private['RouteTable']['RouteTableId']

# Step 5: Associate Route Tables with Subnets
ec2.associate_route_table(RouteTableId=route_table_public_id, SubnetId=subnet_public_1['Subnet']['SubnetId'])
ec2.associate_route_table(RouteTableId=route_table_public_id, SubnetId=subnet_public_2['Subnet']['SubnetId'])

ec2.associate_route_table(RouteTableId=route_table_private_id, SubnetId=subnet_private_1['Subnet']['SubnetId'])
ec2.associate_route_table(RouteTableId=route_table_private_id, SubnetId=subnet_private_2['Subnet']['SubnetId'])
ec2.associate_route_table(RouteTableId=route_table_private_id, SubnetId=subnet_private_3['Subnet']['SubnetId'])
ec2.associate_route_table(RouteTableId=route_table_private_id, SubnetId=subnet_private_4['Subnet']['SubnetId'])

# Step 6: Create a NAT Gateway in one of the Public Subnets
# Allocate an Elastic IP for the NAT Gateway
allocation = ec2.allocate_address(Domain='vpc')
nat_gateway = ec2.create_nat_gateway(SubnetId=subnet_public_1['Subnet']['SubnetId'], AllocationId=allocation['AllocationId'])
nat_gateway_id = nat_gateway['NatGateway']['NatGatewayId']

# Update the private route table to route through the NAT Gateway for internet access
ec2.create_route(RouteTableId=route_table_private_id, DestinationCidrBlock='0.0.0.0/0', NatGatewayId=nat_gateway_id)

# Step 7: Create Network Access Control Lists (NACL)
nacl_public = ec2.create_network_acl(VpcId=vpc_id)
nacl_public_id = nacl_public['NetworkAcl']['NetworkAclId']

nacl_private = ec2.create_network_acl(VpcId=vpc_id)
nacl_private_id = nacl_private['NetworkAcl']['NetworkAclId']

# Step 8: Associate NACLs with Subnets
ec2.associate_network_acl(NetworkAclId=nacl_public_id, SubnetId=subnet_public_1['Subnet']['SubnetId'])
ec2.associate_network_acl(NetworkAclId=nacl_public_id, SubnetId=subnet_public_2['Subnet']['SubnetId'])

ec2.associate_network_acl(NetworkAclId=nacl_private_id, SubnetId=subnet_private_1['Subnet']['SubnetId'])
ec2.associate_network_acl(NetworkAclId=nacl_private_id, SubnetId=subnet_private_2['Subnet']['SubnetId'])
ec2.associate_network_acl(NetworkAclId=nacl_private_id, SubnetId=subnet_private_3['Subnet']['SubnetId'])
ec2.associate_network_acl(NetworkAclId=nacl_private_id, SubnetId=subnet_private_4['Subnet']['SubnetId'])

# Step 9: Create Security Groups
security_group_public = ec2.create_security_group(GroupName='PublicSG', Description='Public Security Group', VpcId=vpc_id)
security_group_private = ec2.create_security_group(GroupName='PrivateSG', Description='Private Security Group', VpcId=vpc_id)

# Add rules to security groups as needed
# Example: Allow inbound SSH traffic for the public security group
ec2.authorize_security_group_ingress(
    GroupId=security_group_public['GroupId'],
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)

# Example: Allow inbound HTTP traffic for the public security group
ec2.authorize_security_group_ingress(
    GroupId=security_group_public['GroupId'],
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 80,
         'ToPort': 80,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)

ec2.authorize_security_group_ingress(
    GroupId=security_group_private['GroupId'],
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '192.168.0.0/16'}]}
    ]
)

# Example: Allow inbound HTTP traffic for the public security group
ec2.authorize_security_group_ingress(
    GroupId=security_group_private['GroupId'],
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 80,
         'ToPort': 80,
         'IpRanges': [{'CidrIp': '192.168.0.0/16'}]}
    ]
)

print("Three-tier architecture created successfully!")