#### Session Video:

```
https://drive.google.com/file/d/1xS1L7Wy2VcAauRFcs-QTwxu_xPDWBTwm/view?usp=sharing
```

#### AWS Services - Security, Identity, and Compliance:

```

1. Amazon Cognito : : Hands-On

    Secure identity and access management for apps
    
    Amazon Cognito user pools let you add registration and sign-in to your apps. With Amazon Cognito identity pools, you can provide AWS credentials for access to your cloud resources.

    Google Authentication:

    Microsoft Authentication:

    Cognito Authentication:

User --> https://portal.cloudbinary.io/login --> Authentication(Google/Microsoft/Cognito) --> UserName & Passwords will be verified then it will allows you to access "portal.cloudbinary.io" To login to your application again it has 2 ways :

Solution-1 :  kesav@cloudbinary.io
1. User Access : Is Allowed using Authentication(Google/Microsoft/Cognito)
2. User Login : Is Allowed using Authentication(Google/Microsoft/Cognito)

Solution-2 :
1. User Access : Is Allowed using Authentication(Google/Microsoft/Cognito)
2. User Login : Is Allowed using Application User Mgmt Module 



STEP-1 -------------------------->STEP-2--------------------------------> SSO or App Based Logins 
https://portal.cloudbinary.io ---> oidc.conf --> UserName/Email/Phone --> https://portal.cloudbinary.io

https://dev.netflix.com/      ---> oidc.conf --> UserName/Email/Phone --> https://dev.netflix.com/

EC2 instance(Linux-Httpd-/etc/httpd/conf.d/oidc.conf)

UI Code: --> Valid domain: cloudbinary.io(100 Emp)


https://cloudbinary/login?response_type=code&client_id=2nsr13hifjkh938qphcf8iro4l&redirect_uri=https://portal.cloudbinary.io/login

From a Specific Network only : VPC (10.0.0.0/8) --> NetFlix Network --> VPN Services 
    https://dev.netflix.com/ : DevOps Engineers
    https://qa.netflix.com/  : DevOps Engineers
    https://acc.netflix.com/ : DevOps Engineers

https://netflix.com/ : 00:00:00 

CI/CD Pipeline : Dev To Production 
--------------------------------
VPC : 10.0.0.0/16 
    - Public Subnet : Bastion/Proxy/JumpBox(Any OS) - 13.100.3.6
    - Private Subnet: 10.0.2.23 (Linux)

Windows: GitBash --> ssh centos@13.100.3.6 --> centos@10.0.2.23
Password : *************
--------------------------------

User Case :

Can you pull out end to end analysis of a User in aws?

    - CloudTrail(90Days)(IAM --> users--> Permissions --> Access Advisor-->CustomCloudTrail()-->S3-->Athena(select * from where username like varaprasad))

loadbalancer: http://alb-awsamazon.com/cloudbinary --> https://alb-awsamazon.com/cloudbinary
    - 80 listner 
    - 443 listner and map SSL Certificate --> ACM 

EC2 --> ALB --> ROUTE53 

cloudfront: https://  --> ROUTE53 --> ACM

s3 static website hosting: http://clodubinary-us-east-1.awsamazon.com



```
