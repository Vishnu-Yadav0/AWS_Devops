#### Session Video:

```
https://drive.google.com/file/d/1ffmdFW3RpvpHCUiOE6iiqaYUfZnmZXGi/view?usp=sharing
```

#### Hashicorp Terraform
```
What is Terraform?
    
    - Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently. 
    
    - This includes low-level components like compute instances, storage, and networking; and high-level components like DNS entries and SaaS features.

    Hands On: Try the Get Started tutorials to start managing infrastructure on popular cloud providers: 
        1. Amazon Web Services, 
        2. Azure, 
        3. Google Cloud Platform, 
        4. Oracle Cloud Infrastructure, and 
        5. Docker.

```

#### How does Terraform work?

    - Terraform creates and manages resources on cloud platforms and other services through their application programming interfaces (APIs). 
    
    - Providers enable Terraform to work with virtually any platform or service with an accessible API.

    <image>

    - HashiCorp and the Terraform community have already written thousands of providers to manage many different types of resources and services. 
    
    - You can find all publicly available providers on the Terraform Registry, including Amazon Web Services (AWS), Azure, Google Cloud Platform (GCP), Kubernetes, Helm, GitHub, Splunk, DataDog, and many more.


The core Terraform workflow consists of three stages:

    Write: 
        - You define resources, which may be across multiple cloud providers and services. 
            For example, you might create a configuration to deploy an application on virtual machines in a Virtual Private Cloud (VPC) network with security groups and a load balancer.
    
    Plan: 
        Terraform creates an execution plan describing the infrastructure it will create, update, or destroy based on the existing infrastructure and your configuration.
    
    Apply: 
        On approval, Terraform performs the proposed operations in the correct order, respecting any resource dependencies. 
        
        For example, if you update the properties of a VPC and change the number of virtual machines in that VPC, Terraform will recreate the VPC before scaling the virtual machines.

    <image>

#### Why Terraform?

    1. Manage any infrastructure :
        
        Find providers for many of the platforms and services you already use in the Terraform Registry. 
        
        You can also write your own. 
        
        Terraform takes an immutable approach to infrastructure, reducing the complexity of upgrading or modifying your services and infrastructure.


    2. Track your infrastructure :
        
        Terraform generates a plan and prompts you for your approval before modifying your infrastructure. 
        
        It also keeps track of your real infrastructure in a state file, which acts as a source of truth for your environment. 
        
        Terraform uses the state file to determine the changes to make to your infrastructure so that it will match your configuration.


    4. Automate changes :

        Terraform configuration files are declarative, meaning that they describe the end state of your infrastructure. 
        
        You do not need to write step-by-step instructions to create resources because Terraform handles the underlying logic. 
        
        Terraform builds a resource graph to determine resource dependencies and creates or modifies non-dependent resources in parallel. 
        
        This allows Terraform to provision resources efficiently.

    5. Standardize configurations :

        Terraform supports reusable configuration components called modules that define configurable collections of infrastructure, saving time and encouraging best practices. 
        
        You can use publicly available modules from the Terraform Registry, or write your own.

    6. Collaborate :

        Since your configuration is written in a file, you can commit it to a Version Control System (VCS) and use Terraform Cloud to efficiently manage Terraform workflows across teams. 
        
        Terraform Cloud runs Terraform in a consistent, reliable environment and provides secure access to shared state and secret data, role-based access controls, a private registry for sharing both modules and providers, and more.

    7. Community :

        We welcome questions, suggestions, and contributions from the community.

        Ask questions in HashiCorp Discuss.
    
        Read our contributing guide.
    
        Submit an issue for bugs and feature requests.

#### Download Install and Configure 

```
Go to the Terraform downloads page at https://www.terraform.io/downloads.html and download the appropriate Windows version of Terraform. You can choose between 32-bit and 64-bit versions depending on your system.

Extract the contents of the downloaded ZIP file to a directory of your choice. 

For example, you can extract it to C:\Program Files\terraform

Add the Terraform binary to your system's PATH environment variable so that you can run it from any directory. To do this, follow these steps:

Open the Start menu and search for "environment variables".

Click on "Edit the system environment variables".

Click on the "Environment Variables" button.

Under "System Variables", scroll down until you find the "Path" variable and click on "Edit".

Click on "New" and enter the path to the directory where you extracted the Terraform binary, 

e.g. C:\Program Files\terraform

Click on "OK" to close all the windows.

Open a new command prompt or PowerShell window to ensure that the updated PATH environment variable is loaded.

Run the terraform command to verify that Terraform is installed correctly. You should see the Terraform help output.

That's it! You have successfully installed Terraform on Windows. You can now start using Terraform to manage your infrastructure.


```

#### Links

```

https://www.terraform.io/

https://registry.terraform.io/browse/providers

https://registry.terraform.io/providers/hashicorp/aws/latest

https://registry.terraform.io/

https://developer.hashicorp.com/terraform/install

https://registry.terraform.io/providers/hashicorp/aws/latest/docs

https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance


```

#### TF Examples:

```

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}


# Configure the AWS Provider
provider "aws" {
  region     = "us-east-1"
  access_key = ""
  secret_key = ""
}


resource "aws_instance" "web" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name      = "web"
    CreatedBy = "Terraform"
  }
}

variable "ami" { 
    default = "ami-053b0d53c279acc90"
}

variable "instance_type" {
    default = "t3.micro"
}

output "public_ip" {
    value = aws_instance.web.public_ip
}

```

#### Terraform Commands

```
$ terraform init

$ terraform fmt

$ terraform validate

$ terraform plan 

$ terraform apply 

$ terraform destroy 

```

