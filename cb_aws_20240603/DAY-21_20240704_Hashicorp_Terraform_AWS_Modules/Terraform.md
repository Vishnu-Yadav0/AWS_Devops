#### Session Video:

```

https://drive.google.com/file/d/1ADNsYbOgvo-C6xdW0_Qipq70MMT5zbN0/view?usp=sharing
```
# Use Case 
```

https://github.com/kesavkummari/terraform-module-c3ops.git


You have an existing resources like 

1.VPC : dev 
    2.Public-Subnet-1, 
    3.Public-Subnet-2, 
    4.private-Subnet-1, 
    5.private-Subnet-2
    6. IGW
    7. NAT Gw
    8. Public RTB
    9. Private RTB
    10. NACL
    11. keypair
    12. security group 


Using an existing resources you have deploy 6 applications in 4 stages:

Account : 1. dev, 2. qa, 3. acc, 4. prod 
DevOps Account : 5
Mgmt Account : 6 

Only 1 Account:
  VPC     : 1. dev, 2. qa, 3. acc, 4. prod 

  Stages  : 1. dev, 2. qa, 3. acc, 4. prod 

1. cloudbinary :
    ec2 instance : 2
    security group : 1
    iam_instance_profile : 1
    user_data : 1
    
2. portal
3. c3ops
4. lms
5. kesavkummari
6. aws.cloudbinary

1. dev, 
https://dev.netflix.com

2. qa, 
https://qa.netflix.com

3. acc, 
https://acc.netflix.com

4. prod 
https://netflix.com

SDLC --> Agile --> Scrum Framework :
  1 Sprint : 2 Weeks i.e. 10 Days | Sat & Sun 
  1 Sprint : 4 Weeks i.e. 20 Days | Sat & Sun 


```

#### Hashicorp Terraform

# main.tf

```
# Versions
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Providers
provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

terraform {
  backend "s3" {
    bucket  = "8amcloudbinary"
    key     = "c3ops-iac/dev/terraform.state"
    region  = "us-east-1"
    profile = "default"
  }
}

# VPC
resource "aws_vpc" "cloudbinary" {
  cidr_block           = var.cidr
  instance_tenancy     = "default"
  enable_dns_support   = var.enable_dns_support
  enable_dns_hostnames = var.enable_dns_hostnames

  tags = {
    Name      = "cloudbinary_VPC"
    CreatedBy = "iac - terraform"
  }
}

# Subnet - Public-1 
resource "aws_subnet" "cloudbinary_public_subnet_1" {
  vpc_id                  = aws_vpc.cloudbinary.id
  cidr_block              = "192.168.1.0/28"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"

  tags = {
    Name      = "cloudbinary_public_subnet_1"
    CreatedBy = "iac - terraform"
  }

}
# Subnet - Public-2
resource "aws_subnet" "cloudbinary_public_subnet_2" {
  vpc_id                  = aws_vpc.cloudbinary.id
  cidr_block              = "192.168.2.0/28"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1b"

  tags = {
    Name      = "cloudbinary_public_subnet_2"
    CreatedBy = "iac - terraform"
  }
}

# Subnet - private-1 
resource "aws_subnet" "cloudbinary_private_subnet_1" {
  vpc_id            = aws_vpc.cloudbinary.id
  cidr_block        = "192.168.3.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name      = "cloudbinary_private_subnet_1"
    CreatedBy = "iac - terraform"
  }
}
# Subnet - private-2 
resource "aws_subnet" "cloudbinary_private_subnet_2" {
  vpc_id            = aws_vpc.cloudbinary.id
  cidr_block        = "192.168.4.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name      = "cloudbinary_private_subnet_2"
    CreatedBy = "iac - terraform"
  }

}

# IGW 
resource "aws_internet_gateway" "cloudbinary_igw" {
  vpc_id = aws_vpc.cloudbinary.id

  tags = {
    Name      = "cloudbinary_igw"
    CreatedBy = "iac - terraform"
  }

}

# RTB - Public-1
resource "aws_route_table" "cloudbinary_public_rtb" {
  vpc_id = aws_vpc.cloudbinary.id

  tags = {
    Name      = "cloudbinary_public_rtb"
    CreatedBy = "iac - terraform"
  }
}

# RTB - Private-1
resource "aws_route_table" "cloudbinary_private_rtb" {
  vpc_id = aws_vpc.cloudbinary.id

  tags = {
    Name      = "cloudbinary_private_rtb"
    CreatedBy = "iac - terraform"
  }
}

# Create Routing to Public-RTB From IGW
resource "aws_route" "cloudbinary_rtb_igw" {
  route_table_id         = aws_route_table.cloudbinary_public_rtb.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.cloudbinary_igw.id

}

# Subnet Association with Public Route Table
resource "aws_route_table_association" "cloudbinary_public_subnet_1_association" {
  subnet_id      = aws_subnet.cloudbinary_public_subnet_1.id
  route_table_id = aws_route_table.cloudbinary_public_rtb.id
}
# Subnet Association with Public Route Table
resource "aws_route_table_association" "cloudbinary_public_subnet_2_association" {
  subnet_id      = aws_subnet.cloudbinary_public_subnet_2.id
  route_table_id = aws_route_table.cloudbinary_public_rtb.id
}

# Subnet Association with Private Route Table
resource "aws_route_table_association" "cloudbinary_private_subnet_1_association" {
  subnet_id      = aws_subnet.cloudbinary_private_subnet_1.id
  route_table_id = aws_route_table.cloudbinary_private_rtb.id
}
# Subnet Association with Private Route Table
resource "aws_route_table_association" "cloudbinary_private_subnet_2_association" {
  subnet_id      = aws_subnet.cloudbinary_private_subnet_2.id
  route_table_id = aws_route_table.cloudbinary_private_rtb.id
}

resource "aws_eip" "cloudbinary_eip" {
  domain = "vpc"
}

# NAT Gateway & Attach EIP to NAT GATEWAY
resource "aws_nat_gateway" "cloudbinary_natgw" {
  allocation_id = aws_eip.cloudbinary_eip.id
  subnet_id     = aws_subnet.cloudbinary_public_subnet_1.id

  tags = {
    Name      = "cloudbinary_natgw"
    CreatedBy = "iac - terraform"
  }
}

# Allow  Nat Gateway To Private Route Table
resource "aws_route" "cloudbinary_allow_natgw" {
  route_table_id         = aws_route_table.cloudbinary_private_rtb.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_nat_gateway.cloudbinary_natgw.id

}

# SG For WebServer
resource "aws_security_group" "cloudbinary_sg_web" {
  vpc_id      = aws_vpc.cloudbinary.id
  name        = "sg_web"
  description = "Allow SSH - RDP - HTTP - DB "

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
  }
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 3389
    to_port     = 3389
    protocol    = "tcp"
  }
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
  }
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
  }
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "cloudbinary_sg_web"
    Description = "Allow SSH - RDP - HTTP - DB - TOMCAT"
    CreatedBy   = "IAC - Terraform"
  }

}

# EC2 Instance in Private Subnet
resource "aws_instance" "cloudbinary_web" {
  ami                    = "ami-0e001c9271cf7f3b9"
  instance_type          = "t2.micro"
  key_name               = "tf-windows"
  subnet_id              = aws_subnet.cloudbinary_private_subnet_1.id
  vpc_security_group_ids = ["${aws_security_group.cloudbinary_sg_web.id}"]
  #user_data              = file("install_apache2.sh")

  iam_instance_profile = aws_iam_role.cloudbinary_dev_role.name


  user_data = <<-EOF
  #!/bin/bash
  apt-get update
  apt-get install -y apache2
  systemctl start apache2
  EOF

  tags = {
    Name      = "cloudbinary_web"
    CreatedBy = "IAC - Terraform"
    OSType    = "Linux - Ubuntu 20.04"
  }
}


resource "aws_iam_role" "cloudbinary_dev_role" {
  name = "cloudbinary_dev_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "cloudbinary_dev_policy" {
  name        = "cloudbinary_dev_policy"
  description = "Example policy for EC2 instances"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = "s3:GetObject",
        Resource = ["arn:aws:s3:::*"]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "cloudbinary_attachment" {
  role       = aws_iam_role.cloudbinary_dev_role.name
  policy_arn = aws_iam_policy.cloudbinary_dev_policy.arn
}
```

# var.tf

```
variable "cidr" {
  default = "192.168.0.0/16"
}

variable "enable_dns_support" {
  default = true
}

variable "enable_dns_hostnames" {
  default = true
}
```

# user data

```
#!/bin/bash
apt-get update
apt-get install -y apache2
systemctl start apache2
```