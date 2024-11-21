import boto3
import time

def create_vpc(ec2, cidr_block):
    response = ec2.create_vpc(CidrBlock=cidr_block)
    vpc_id = response['Vpc']['VpcId']
    print(f"VPC created with ID: {vpc_id}")

    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

    # Wait for the VPC to be available
    waiter = ec2.get_waiter('vpc_available')
    waiter.wait(VpcIds=[vpc_id])
    print(f"VPC {vpc_id} is now available")

    return vpc_id

def create_subnet(ec2, vpc_id, cidr_block, az):
    response = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id, AvailabilityZone=az)
    subnet_id = response['Subnet']['SubnetId']
    print(f"Subnet created with ID: {subnet_id} in AZ: {az}")

    # Wait for the subnet to be available
    waiter = ec2.get_waiter('subnet_available')
    waiter.wait(SubnetIds=[subnet_id])
    print(f"Subnet {subnet_id} is now available")

    return subnet_id

def create_internet_gateway(ec2, vpc_id):
    response = ec2.create_internet_gateway()
    igw_id = response['InternetGateway']['InternetGatewayId']
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f"Internet Gateway created and attached with ID: {igw_id}")

    # No explicit waiter for Internet Gateway attachment, sleep to allow attachment process to complete
    time.sleep(10)
    print(f"Internet Gateway {igw_id} is now attached")

    return igw_id

def create_route_table(ec2, vpc_id):
    response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = response['RouteTable']['RouteTableId']
    print(f"Route Table created with ID: {route_table_id}")
    return route_table_id

def create_nat_gateway(ec2, subnet_id):
    allocation = ec2.allocate_address(Domain='vpc')
    nat_gateway = ec2.create_nat_gateway(SubnetId=subnet_id, AllocationId=allocation['AllocationId'])
    nat_gateway_id = nat_gateway['NatGateway']['NatGatewayId']
    print(f"NAT Gateway created with ID: {nat_gateway_id}")

    # Wait for the NAT Gateway to be available
    waiter = ec2.get_waiter('nat_gateway_available')
    waiter.wait(NatGatewayIds=[nat_gateway_id])
    print(f"NAT Gateway {nat_gateway_id} is now available")

    return nat_gateway_id

def create_nacl(ec2, vpc_id, name):
    response = ec2.create_network_acl(VpcId=vpc_id)
    nacl_id = response['NetworkAcl']['NetworkAclId']
    print(f"NACL ({name}) created with ID: {nacl_id}")
    return nacl_id

def create_security_group(ec2, vpc_id, name, description):
    response = ec2.create_security_group(GroupName=name, Description=description, VpcId=vpc_id)
    sg_id = response['GroupId']
    print(f"Security Group {name} created with ID: {sg_id}")
    return sg_id

def main():
    # Initialize session and EC2 client
    session = boto3.Session(region_name='us-east-1')
    ec2 = session.client('ec2')

    # Get user input for CIDR blocks and availability zones
    vpc_cidr = input("Enter the CIDR block for the VPC (e.g., 10.0.0.0/16): ")
    public_subnet_cidr_1 = input("Enter the CIDR block for the first public subnet (e.g., 10.0.1.0/28): ")
    public_subnet_cidr_2 = input("Enter the CIDR block for the second public subnet (e.g., 10.0.2.0/28): ")
    private_subnet_cidr_1 = input("Enter the CIDR block for the first private subnet (e.g., 10.0.3.0/24): ")
    private_subnet_cidr_2 = input("Enter the CIDR block for the second private subnet (e.g., 10.0.4.0/24): ")
    private_subnet_cidr_3 = input("Enter the CIDR block for the third private subnet (e.g., 10.0.5.0/24): ")
    private_subnet_cidr_4 = input("Enter the CIDR block for the fourth private subnet (e.g., 10.0.6.0/24): ")

    az_1 = input("Enter the first availability zone (e.g., us-east-1a): ")
    az_2 = input("Enter the second availability zone (e.g., us-east-1b): ")

    # Step 1: Create a VPC
    vpc_id = create_vpc(ec2, vpc_cidr)

    # Step 2: Create Subnets (2 Public and 4 Private)
    subnets = {}
    subnets['public'] = [
        create_subnet(ec2, vpc_id, public_subnet_cidr_1, az_1),
        create_subnet(ec2, vpc_id, public_subnet_cidr_2, az_2)
    ]
    subnets['private'] = [
        create_subnet(ec2, vpc_id, private_subnet_cidr_1, az_1),
        create_subnet(ec2, vpc_id, private_subnet_cidr_2, az_2),
        create_subnet(ec2, vpc_id, private_subnet_cidr_3, az_1),
        create_subnet(ec2, vpc_id, private_subnet_cidr_4, az_2)
    ]

    # Step 3: Create an Internet Gateway (IGW) and Attach it to the VPC
    igw_id = create_internet_gateway(ec2, vpc_id)

    # Step 4: Create Route Tables and Routes
    # Public Route Table
    route_table_public_id = create_route_table(ec2, vpc_id)
    ec2.create_route(RouteTableId=route_table_public_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)

    # Private Route Table
    route_table_private_id = create_route_table(ec2, vpc_id)

    # Step 5: Associate Route Tables with Subnets
    for subnet_id in subnets['public']:
        ec2.associate_route_table(RouteTableId=route_table_public_id, SubnetId=subnet_id)

    for subnet_id in subnets['private']:
        ec2.associate_route_table(RouteTableId=route_table_private_id, SubnetId=subnet_id)

    # Step 6: Create a NAT Gateway in one of the Public Subnets
    nat_gateway_id = create_nat_gateway(ec2, subnets['public'][0])
    ec2.create_route(RouteTableId=route_table_private_id, DestinationCidrBlock='0.0.0.0/0', NatGatewayId=nat_gateway_id)

    # Step 7: Create Network Access Control Lists (NACL)
    nacl_public_id = create_nacl(ec2, vpc_id, "Public")
    nacl_private_id = create_nacl(ec2, vpc_id, "Private")

    # Step 1: Describe the subnet to get the current Network ACL association
    response = ec2.describe_network_acls(Filters=[{'Name': 'association.subnet-id', 'Values': [subnet_id]}])
    
    # Extract the Network ACL association ID
    current_association_id = ec2.response['NetworkAcls'][0]['Associations'][0]['NetworkAclAssociationId']

    # Step 8: Associate NACLs with Subnets
    for subnet_id in subnets['public']:
        #ec2.associate_network_acl(NetworkAclId=nacl_public_id, SubnetId=subnet_id)
        ec2.replace_network_acl_association(AssociationId=current_association_id,NetworkAclId=nacl_public_id)

    for subnet_id in subnets['private']:
        #ec2.associate_network_acl(NetworkAclId=nacl_private_id, SubnetId=subnet_id)
        ec2.replace_network_acl_association(AssociationId=current_association_id,NetworkAclId=nacl_private_id)

    # Step 9: Create Security Groups
    security_group_public_id = create_security_group(ec2, vpc_id, 'PublicSG', 'Public Security Group')
    security_group_private_id = create_security_group(ec2, vpc_id, 'PrivateSG', 'Private Security Group')

    # Example rules for security groups
    ec2.authorize_security_group_ingress(
        GroupId=security_group_public_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )
    ec2.authorize_security_group_ingress(
        GroupId=security_group_public_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )

    # Example rules for security groups
    ec2.authorize_security_group_ingress(
        GroupId=security_group_private_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )
    ec2.authorize_security_group_ingress(
        GroupId=security_group_private_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )
    print("Three-tier architecture created successfully!")

if __name__ == "__main__":
    main()
