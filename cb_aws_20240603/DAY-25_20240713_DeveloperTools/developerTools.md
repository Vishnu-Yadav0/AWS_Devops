#### Session Video:

```
https://drive.google.com/file/d/19sq3eQ9EscgRK8qLrnxYfihWFU6QEqFK/view?usp=sharing

```

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
# resource "aws_vpc" "cloudbinary" {
#   cidr_block           = var.cidr
#   instance_tenancy     = "default"
#   enable_dns_support   = var.enable_dns_support
#   enable_dns_hostnames = var.enable_dns_hostnames

#   tags = {
#     Name      = "cloudbinary_VPC"
#     CreatedBy = "iac - terraform"
#   }
# }

# Subnet - Public-1 
# resource "aws_subnet" "cloudbinary_public_subnet_1" {
#   vpc_id                  = aws_vpc.cloudbinary.id
#   cidr_block              = "192.168.1.0/28"
#   map_public_ip_on_launch = true
#   availability_zone       = "us-east-1a"

#   tags = {
#     Name      = "cloudbinary_public_subnet_1"
#     CreatedBy = "iac - terraform"
#   }

# }
# Subnet - Public-2
# resource "aws_subnet" "cloudbinary_public_subnet_2" {
#   vpc_id                  = aws_vpc.cloudbinary.id
#   cidr_block              = "192.168.2.0/28"
#   map_public_ip_on_launch = true
#   availability_zone       = "us-east-1b"

#   tags = {
#     Name      = "cloudbinary_public_subnet_2"
#     CreatedBy = "iac - terraform"
#   }
# }

# Subnet - private-1 
# resource "aws_subnet" "cloudbinary_private_subnet_1" {
#   vpc_id            = aws_vpc.cloudbinary.id
#   cidr_block        = "192.168.3.0/24"
#   availability_zone = "us-east-1a"

#   tags = {
#     Name      = "cloudbinary_private_subnet_1"
#     CreatedBy = "iac - terraform"
#   }
# }
# Subnet - private-2 
# resource "aws_subnet" "cloudbinary_private_subnet_2" {
#   vpc_id            = aws_vpc.cloudbinary.id
#   cidr_block        = "192.168.4.0/24"
#   availability_zone = "us-east-1b"

#   tags = {
#     Name      = "cloudbinary_private_subnet_2"
#     CreatedBy = "iac - terraform"
#   }

# }

# IGW 
# resource "aws_internet_gateway" "cloudbinary_igw" {
#   vpc_id = aws_vpc.cloudbinary.id

#   tags = {
#     Name      = "cloudbinary_igw"
#     CreatedBy = "iac - terraform"
#   }

# }

# RTB - Public-1
# resource "aws_route_table" "cloudbinary_public_rtb" {
#   vpc_id = aws_vpc.cloudbinary.id

#   tags = {
#     Name      = "cloudbinary_public_rtb"
#     CreatedBy = "iac - terraform"
#   }
# }

# RTB - Private-1
# resource "aws_route_table" "cloudbinary_private_rtb" {
#   vpc_id = aws_vpc.cloudbinary.id

#   tags = {
#     Name      = "cloudbinary_private_rtb"
#     CreatedBy = "iac - terraform"
#   }
# }

# Create Routing to Public-RTB From IGW
# resource "aws_route" "cloudbinary_rtb_igw" {
#   route_table_id         = aws_route_table.cloudbinary_public_rtb.id
#   destination_cidr_block = "0.0.0.0/0"
#   gateway_id             = aws_internet_gateway.cloudbinary_igw.id

# }

# # Subnet Association with Public Route Table
# resource "aws_route_table_association" "cloudbinary_public_subnet_1_association" {
#   subnet_id      = aws_subnet.cloudbinary_public_subnet_1.id
#   route_table_id = aws_route_table.cloudbinary_public_rtb.id
# }
# # Subnet Association with Public Route Table
# resource "aws_route_table_association" "cloudbinary_public_subnet_2_association" {
#   subnet_id      = aws_subnet.cloudbinary_public_subnet_2.id
#   route_table_id = aws_route_table.cloudbinary_public_rtb.id
# }

# # Subnet Association with Private Route Table
# resource "aws_route_table_association" "cloudbinary_private_subnet_1_association" {
#   subnet_id      = aws_subnet.cloudbinary_private_subnet_1.id
#   route_table_id = aws_route_table.cloudbinary_private_rtb.id
# }
# # Subnet Association with Private Route Table
# resource "aws_route_table_association" "cloudbinary_private_subnet_2_association" {
#   subnet_id      = aws_subnet.cloudbinary_private_subnet_2.id
#   route_table_id = aws_route_table.cloudbinary_private_rtb.id
# }

# resource "aws_eip" "cloudbinary_eip" {
#   domain = "vpc"
# }

# # NAT Gateway & Attach EIP to NAT GATEWAY
# resource "aws_nat_gateway" "cloudbinary_natgw" {
#   allocation_id = aws_eip.cloudbinary_eip.id
#   subnet_id     = aws_subnet.cloudbinary_public_subnet_1.id

#   tags = {
#     Name      = "cloudbinary_natgw"
#     CreatedBy = "iac - terraform"
#   }
# }

# # Allow  Nat Gateway To Private Route Table
# resource "aws_route" "cloudbinary_allow_natgw" {
#   route_table_id         = aws_route_table.cloudbinary_private_rtb.id
#   destination_cidr_block = "0.0.0.0/0"
#   gateway_id             = aws_nat_gateway.cloudbinary_natgw.id

# }

# # SG For WebServer
# resource "aws_security_group" "cloudbinary_sg_web" {
#   vpc_id      = aws_vpc.cloudbinary.id
#   name        = "sg_web"
#   description = "Allow SSH - RDP - HTTP - DB "

#   ingress {
#     cidr_blocks = ["0.0.0.0/0"]
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#   }
#   ingress {
#     cidr_blocks = ["0.0.0.0/0"]
#     from_port   = 3389
#     to_port     = 3389
#     protocol    = "tcp"
#   }
#   ingress {
#     cidr_blocks = ["0.0.0.0/0"]
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#   }
#   ingress {
#     cidr_blocks = ["0.0.0.0/0"]
#     from_port   = 8080
#     to_port     = 8080
#     protocol    = "tcp"
#   }
#   ingress {
#     cidr_blocks = ["0.0.0.0/0"]
#     from_port   = 3306
#     to_port     = 3306
#     protocol    = "tcp"
#   }
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     Name        = "cloudbinary_sg_web"
#     Description = "Allow SSH - RDP - HTTP - DB - TOMCAT"
#     CreatedBy   = "IAC - Terraform"
#   }

# }

# # EC2 Instance in Private Subnet
# resource "aws_instance" "cloudbinary_web" {
#   ami                    = "ami-0e001c9271cf7f3b9"
#   instance_type          = "t2.micro"
#   key_name               = "tf-windows"
#   subnet_id              = aws_subnet.cloudbinary_private_subnet_1.id
#   vpc_security_group_ids = ["${aws_security_group.cloudbinary_sg_web.id}"]
#   #user_data              = file("install_apache2.sh")

#   iam_instance_profile = aws_iam_role.cloudbinary_dev_role.name


#   user_data = <<-EOF
#   #!/bin/bash
#   apt-get update
#   apt-get install -y apache2
#   systemctl start apache2
#   EOF

#   tags = {
#     Name      = "cloudbinary_web"
#     CreatedBy = "IAC - Terraform"
#     OSType    = "Linux - Ubuntu 20.04"
#   }
# }



# EC2 Instance in Private Subnet
resource "aws_instance" "cloudbinary_web" {
  ami                    = "ami-01fccab91b456acc2"
  instance_type          = "t2.micro"
  key_name               = "tf-windows"
  subnet_id              = "subnet-0075dcc070cf14233"
  vpc_security_group_ids = ["sg-0a3fe1b73a2b3e0d2"]
  #user_data              = file("install_apache2.sh")

  #iam_instance_profile = "arn:aws:iam::420815905200:role/8amSSMEC2"
  #iam_instance_profile = aws_iam_role.cloudbinary_dev_role.name


  user_data = <<-EOF
  #!/bin/bash
  # Install apache httpd 
  yum -y install httpd-2.4.52

  # Set up proxy for Tomcat server
  cat <<EOT >> /etc/httpd/conf/httpd.conf
  LoadModule proxy_module modules/mod_proxy.so
  LoadModule proxy_http_module modules/mod_proxy_http.so

  ProxyRequests Off
  ProxyPass / http://localhost:8080/
  ProxyPassReverse / http://localhost:8080/

  <Location "/">
    Order allow,deny
    Allow from all
  </Location>
  EOT

  yum -y install java-11-amazon-corretto-headless-11.0.13+8-2.amzn2.x86_64 log4j-cve-2021-44228-hotpatch

  cd /home/ec2-user

  # Install python3
  yum -y install python3-3.7.9-1.amzn2.0.2

  # Install pip
  yum -y install python3-pip-9.0.3
  pip3 install -Iv --upgrade pip==20.2.1

  # Install awscli and python dev libraries
  pip3 install awscli==1.27.84
  pip3 install boto3==1.26.84
  pip3 install pycryptodome==3.9.7
  yum clean all
  amazon-linux-extras install tomcat8.5=8.5.50
  alternatives --set java  /usr/lib/jvm/java-11-amazon-corretto.x86_64/bin/java
  service tomcat start
  service httpd start

  aws s3 cp s3://8amcloudbinary/c3ops-java-src.zip /home/ec2-user/
  unzip /home/ec2-user/c3ops-java-src.zip
  mv /home/ec2-user/c3ops-java-src/target/ROOT.war /var/lib/tomcat/webapps/
  service tomcat start

  EOF

  tags = {
    Name      = "cloudbinary_web"
    CreatedBy = "IAC - Terraform"
    OSType    = "Linux - Ubuntu 20.04"
  }
}

# resource "aws_iam_role" "cloudbinary_dev_role" {
#   path = "/"
#   assume_role_policy = jsonencode({
#     Version = "2012-10-17",
#     Statement = [
#       {
#         Effect = "Allow",
#         Principal = {
#           Service = "ec2.amazonaws.com"
#         },
#         Action = "sts:AssumeRole"
#       }
#     ]
#   })
# }

# resource "aws_iam_policy" "cloudbinary_dev_policy" {
#   name        = "cloudbinary_dev_policy"
#   description = "Example policy for EC2 instances"

#   policy = jsonencode({
#     Version = "2012-10-17",
#     Statement = [
#       {
#         Effect   = "Allow",
#         Action   = "s3:GetObject",
#         Resource = ["arn:aws:s3:::*"]
#       }
#     ]
#   })
# }

# resource "aws_iam_role_policy_attachment" "cloudbinary_attachment" {
#   role       = aws_iam_role.cloudbinary_dev_role.name
#   policy_arn = aws_iam_policy.cloudbinary_dev_policy.arn
# }




```

# dod file
```
version: 0.2 
phases:
  install:
    runtime-versions:
      java : corretto17
  pre_build:
    commands:
      - echo "Download JQ"
      - curl -qL -o jq https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && chmod +x ./jq
      - mv jq /usr/local/bin 
      - echo "Install Hashicorp Terraform"
      - wget https://releases.hashicorp.com/terraform/1.1.0/terraform_1.1.0_linux_amd64.zip
      - unzip terraform_1.1.0_linux_amd64.zip
      - pwd
      - ls -lrt
      - mv terraform /usr/local/bin/
      - pwd
      - ls -lrt /usr/local/bin/terraform
      - ls -lrt $CODEBUILD_SRC_DIR/iac-tf
      - cd $CODEBUILD_SRC_DIR/iac-tf
      - terraform -v 
      - terraform init 
      - terraform fmt
      - terraform validate 
  build:
    commands:
      - echo "Executing Build Phase"
      - ls -lrt $CODEBUILD_SRC_DIR
      - pwd
      - ls -lrta
      - terraform plan
      - terraform apply -auto-approve 
  post_build:
    commands:
      - echo "Infra Job is completed on `date`"


```


# src dod file

```
version: 0.2 
phases:
  install:
    runtime-versions:
      java : corretto17
  pre_build:
    commands:
      - echo "pre-build started"
      - pwd
      - ls -lrta
  build:
    commands:
      - echo Build started on `date`
      #- mvn clean validate compile test install verify package deploy 
      - mvn package 
      - echo Build completed on `date`
  post_build:
    commands:
      - echo Deliver Artifact To Remote Tomcat Server `date`
      #- curl -u admin:redhat@123 -T target/**.war "http://54.82.55.29:8080/manager/text/deploy?path=/cloudbinary&update=true"
      #- curl --retry-delay 10 --retry 5 "http://54.82.55.29:8080/cloudbinary"
artifacts:
  files:
    - '**/*'
```