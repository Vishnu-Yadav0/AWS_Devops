#### Session Video:

```
https://drive.google.com/file/d/1yuMYUQKizZmcygIfgQbn_vkKwvX44sLX/view?usp=sharing
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

7. AWS Identity and Access Management (IAM)

11. AWS Network Firewall

12. AWS Resource Access Manager (AWS RAM)

13. AWS Secrets Manager

15. AWS Security Token Service (AWS STS) : Hands-On

16. AWS Shield

17. AWS Single Sign-On : Hands-On

18. AWS WAF


```

#### AWS Single Sign-On : Hands-On

```
STEP-1 : Login to 2 AWS Accounts

1. Account-A(10200202020) : Primary/Mgmt Account :

2. Account-B(49499494949) : Dev/QA/ACC/Prod 

STEP-2 : Create Organisations Part of Account-A Account 

STEP-3 :  Send Inviation to Account-B To join the Organisations from Account-A 

STEP-4 : Login to Account-B and Accept the Inviation

STEP-5 : Go Account-A and Create Users, Groups & Roles 

STEP-6 : Then test the connection by login to custom URL and try validating Console access and Access Keys 

STEP-7 : Summary 

```

```

AWS Security Token Service(STS):

- Grants Users limited and temporary access to AWS resouces.
- Users can come from three sources:
    1. Federation(Active Directory):
        1.1 Uses Security Assertion Markup Language(SAML)
        1.2 Grants temporary access based on the USERS Active Directory credentials.
        1.3 Does not need to be a user in IAM
        1.4 Single Sign on allows users to log in to AWS console without assigning IAM credentials.

    2. Fedration with Mobile Apps:
        2.1 Use Facebook/Amazon/Google or other OPENID providers to log in

    3. Cross Account Access:
        3.1 Let's users from one AWS Account access resources in another

Key Terms:
    1. Federation: Combining or joining a list of users in one domain(such as IAM) with a list of users in another domain(such as Active Directory, Facebook etc..)

    2. Identity Broker: A Service that allows you to take an identity from POINT-A and join it(Federate it) to POINT-B

    3. Identity Store: Services like Active Directory, Facebook, Google etc

    4. Identities : A user of a Service like Facebook etc..

aws sts get-session-token --duration-seconds 129600 --serial-number  arn:aws:iam::848438388448:mfa/joel.kummari@gmail.com --token-code 113811 --no-verify-ssl
```