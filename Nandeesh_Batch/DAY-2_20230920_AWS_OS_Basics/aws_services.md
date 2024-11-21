#### Session Video:
    https://drive.google.com/file/d/1hNB-bAjKizvJCag_OwN2QZfYx5S8Trax/view?usp=sharing

#### Launch a Windows instance in aws nv region

#### EC2 Instance 

#### Create EC2 Instance in AWS 

    STEP-1 : Login to AWS 

    STEP-2 : Go to Mumbai Region

    STEP-3 : Go to EC2 Dashboard

    STEP-4 : Click on EC2 Instance

    STEP-5 : Fill the Details & Launch EC2 Instance 

        - Name : Linux

        - AMI  : Linux

        - Instance Type : t2.micro

        - KeyPair : nv_aws_linux

        - Network : Default VPC :
        
        - Subnet : Public Subnet : 

        - Security Group : Port-22/TCP 
        
        - Storage / Volume : 8 GB 

        - No Of Instances : 1

    STEP-6 : Connect Remote Linux EC2 Instance From Local Machine using GitBash

    STEP-7 : Validate & CleanUp!



#### Launch EC2 Instance on AWS :

```
Here are the step-by-step instructions for launching an AWS EC2 instance:

    STEP-1 : Log in to the AWS Management Console and navigate to the EC2 Dashboard.

    STEP-2 : Click the "Launch Instance" button to start the instance creation process.

    STEP-3 : Choose an Amazon Machine Image (AMI) for your instance. 
    
        - An AMI is a pre-configured virtual machine image that contains an operating system, application server, and any required software. 
    
        - You can choose from a variety of pre-built AMIs, or create your own custom AMI.

    STEP-4 : Select an instance type for your instance. 
        - This determines the resources (CPU, memory, storage, etc.) allocated to the instance. 
        - You can choose from a range of instance types based on your workload requirements and budget.

    STEP-5 : Configure the instance details, such as the number of instances to launch, network settings, security groups, and IAM roles.   
        - You can also enable detailed monitoring, tags, and user data scripts here.

    STEP-6 : Choose a storage option for your instance. You can select from Amazon Elastic Block Store (EBS) volumes, instance store volumes, or a combination of both. You can also configure the storage size, type, and encryption options.

    STEP-7 : Configure any additional options, such as instance metadata, user data, and advanced settings. 
        - You can also set up auto-scaling and load balancing for your instance if required.

    STEP-8 : Review your instance configuration and launch the instance. 
        - You will need to create or select a key pair for SSH access to the instance.

    STEP-9 : Once the instance is launched, you can connect to it using SSH or Remote Desktop, depending on the operating system and instance type.

    That's it! You have successfully launched an EC2 instance in AWS.

```