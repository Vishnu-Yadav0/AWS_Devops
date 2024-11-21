cloudbinary@Clouds-MacBook-Pro cb_python_20240603 % /usr/local/bin/python /Users/ck/repos/cb_python_20240603/DAY-15_20240626_Part-2_Recap/py
thon_aws_3Tier_dynamic.py
Enter the CIDR block for the VPC (e.g., 10.0.0.0/16): 10.0.0.0/16
Enter the CIDR block for the first public subnet (e.g., 10.0.1.0/24): 10.0.1.0/24
Enter the CIDR block for the second public subnet (e.g., 10.0.2.0/24): 10.0.2.0/24
Enter the CIDR block for the first private subnet (e.g., 10.0.3.0/24): 10.0.3.0/24
Enter the CIDR block for the second private subnet (e.g., 10.0.4.0/24): 10.0.4.0/24
Enter the CIDR block for the third private subnet (e.g., 10.0.5.0/24): 10.0.5.0/24
Enter the CIDR block for the fourth private subnet (e.g., 10.0.6.0/24): 10.0.6.0/24
Enter the first availability zone (e.g., ap-south-2a): ap-south-2a
Enter the second availability zone (e.g., ap-south-2b): ap-south-2b
VPC created with ID: vpc-0c46a91a4aa936fbf
Subnet created with ID: subnet-020d4207fd927a31b in AZ: ap-south-2a
Subnet created with ID: subnet-007f15af8e4bc1305 in AZ: ap-south-2b
Subnet created with ID: subnet-08d08d5cb91d993ae in AZ: ap-south-2a
Subnet created with ID: subnet-0d64ee8c676927b6a in AZ: ap-south-2b
Subnet created with ID: subnet-046069c3fc2b3583e in AZ: ap-south-2a
Subnet created with ID: subnet-0d6a474307c15f5f5 in AZ: ap-south-2b
Internet Gateway created and attached with ID: igw-0faf291788d86581b
Route Table created with ID: rtb-08251dd25b0588f81
Route Table created with ID: rtb-021c151d636531cc7
NAT Gateway created with ID: nat-0fe460fd99ddf9078
NACL (Public) created with ID: acl-0b71948867dbda85c
NACL (Private) created with ID: acl-0eb0d856b3863a2d2
Traceback (most recent call last):
  File "/Users/ck/repos/cb_python_20240603/DAY-15_20240626_Part-2_Recap/python_aws_3Tier_dynamic.py", line 145, in <module>
    main()
  File "/Users/ck/repos/cb_python_20240603/DAY-15_20240626_Part-2_Recap/python_aws_3Tier_dynamic.py", line 113, in main
    ec2.associate_network_acl(NetworkAclId=nacl_public_id, SubnetId=subnet_id)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/botocore/client.py", line 838, in __getattr__
    raise AttributeError(
AttributeError: 'EC2' object has no attribute 'associate_network_acl'. Did you mean: 'create_network_acl'?

associate_network_acl 
create_network_acl


Correct Method for Associating a Network ACL
In Boto3, to associate a Network ACL with a subnet, you should use the replace_network_acl_association method under the EC2 client.

Here's how you can do it:

Identify the Subnet Association ID: Before associating a new Network ACL, you need to get the current association ID of the Network ACL for the subnet.

Replace the Association: Use the replace_network_acl_association method to replace the current association with the new Network ACL.



# 

cloudbinary@Clouds-MacBook-Pro cb_python_20240603 % /usr/local/bin/python /Users/ck/repos/cb_python_20240603/DAY-16_20240627_UseCases/3Tier.
py
Enter the CIDR block for the VPC (e.g., 10.0.0.0/16): 10.0.0.0/16
Enter the CIDR block for the first public subnet (e.g., 10.0.1.0/28): 10.0.1.0/28
Enter the CIDR block for the second public subnet (e.g., 10.0.2.0/28): 10.0.2.0/28
Enter the CIDR block for the first private subnet (e.g., 10.0.3.0/24): 10.0.3.0/24
Enter the CIDR block for the second private subnet (e.g., 10.0.4.0/24): 10.0.4.0/24
Enter the CIDR block for the third private subnet (e.g., 10.0.5.0/24): 10.0.5.0/24
Enter the CIDR block for the fourth private subnet (e.g., 10.0.6.0/24): 10.0.6.0/24
Enter the first availability zone (e.g., us-east-1a): us-east-1a
Enter the second availability zone (e.g., us-east-1b): us-east-1b
VPC created with ID: vpc-07ee7637e0dfe5e4c
VPC vpc-07ee7637e0dfe5e4c is now available
Subnet created with ID: subnet-0d1b0f561e301a609 in AZ: us-east-1a
Subnet subnet-0d1b0f561e301a609 is now available
Subnet created with ID: subnet-0294a8a3f51421574 in AZ: us-east-1b
Subnet subnet-0294a8a3f51421574 is now available
Subnet created with ID: subnet-06a066880c87f9527 in AZ: us-east-1a
Subnet subnet-06a066880c87f9527 is now available
Subnet created with ID: subnet-03d0ac021800460aa in AZ: us-east-1b
Subnet subnet-03d0ac021800460aa is now available
Subnet created with ID: subnet-0fc4d05e6a0606580 in AZ: us-east-1a
Subnet subnet-0fc4d05e6a0606580 is now available
Subnet created with ID: subnet-06bd0555456fed18b in AZ: us-east-1b
Subnet subnet-06bd0555456fed18b is now available
Internet Gateway created and attached with ID: igw-063080b98cfeddad0
Internet Gateway igw-063080b98cfeddad0 is now attached
Route Table created with ID: rtb-0b637f30de7de431e
Route Table created with ID: rtb-040c631aa8ba1b9d0
NAT Gateway created with ID: nat-03cfba2b543fcf54b
NAT Gateway nat-03cfba2b543fcf54b is now available
NACL (Public) created with ID: acl-05e88d4faaf5acb36
NACL (Private) created with ID: acl-00cb4c0e61780936d
Traceback (most recent call last):
  File "/Users/ck/repos/cb_python_20240603/DAY-16_20240627_UseCases/3Tier.py", line 194, in <module>
    main()
  File "/Users/ck/repos/cb_python_20240603/DAY-16_20240627_UseCases/3Tier.py", line 137, in main
    current_association_id = ec2.response['NetworkAcls'][0]['Associations'][0]['NetworkAclAssociationId']
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/botocore/client.py", line 838, in __getattr__
    raise AttributeError(
AttributeError: 'EC2' object has no attribute 'response'

