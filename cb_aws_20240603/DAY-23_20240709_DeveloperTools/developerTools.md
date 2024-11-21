#### Session Video:

```

https://drive.google.com/file/d/16H4BaQz58btl2kQYRxMJbH6jv-bd3nJN/view?usp=sharing

https://drive.google.com/file/d/1wCb8S0E3n3vdKuZAGzspDC3W3ncl9W2X/view?usp=sharing


```

#### Developer Tools - DevOps Ci/Cd Pipeline in AWS

```

AWS Developer Tools 

1. AWS Cloud Development Kit (AWS CDK) : Example Python With Boto3
2. AWS CloudShell : Execute AWS CLI Commands
3. AWS CodeArtifact == Jfrog/NexusSonaType (Store Binary Files)
4. AWS CodeBuild    == Jenkins/GitHubActions/GitLabCI/Bamboo etc...
5. AWS CodeCommit   == GitHub/GitLab/BitBucket/Azure Repos
6. AWS CodeDeploy   == Jenkins/GitHubActions/GitLabCI/Bamboo etc...
7. Amazon CodeGuru  == Detect, track, and fix code security vulnerabilities anywhere in the development cycle using ML and automated reasoning
8. AWS CodePipeline == Jenkins/GitHubActions/GitLabCI/Bamboo etc...
9. AWS CodeStar     == Sample Code i.e. Java/.net/Python/Go etc...
10. AWS Command Line Interface (AWS CLI) == 
11. AWS SDKs and Tools == Boto3
12. AWS X-Ray == Analyze and debug production and distributed applications

```

#### 

```

STEP-1 : Application Source Code for example Java Application / Angular / React / .net :
  Source Code : Developer == AWS CodeStar

STEP-2 : Compile the Source Code and Generate artifact 
  Build Lifecycles : 

main.tf 
var.tf

terraform init 
terraform fmt
terraform validate
terraform plan 
terraform apply
terraform refresh
terraform destroy 

Connect with Developer and understand the build lifecycles for his language:
  
  Ui : Spring Boot
  
  Backend / Services : Java
  
  Database : RDBMS(oracle/mysql)

Compile : 
  - ui & services using lifecycles :
    1. Ant, 2. Maven or 3. Gradel 

Gradle. Gradle is one of the open-source Java build tools for developers.
Apache Maven. Apache Maven is an open-source software project management tool.
Apache Ant. Apache Ant is yet another best Java build tool for developers.

STEP-3 : 

Create Code Repository : GitHub/GitLab/Bitbucket/Azure Repos/AWS CodeCommit

Copy the code from developers:
  
  Ui : Spring Boot
  
  Backend / Services : Java
  
  Database : RDBMS(oracle/mysql)

  DevOps : infrastructure code i.e. terraform 


```


#### Use Case 
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
