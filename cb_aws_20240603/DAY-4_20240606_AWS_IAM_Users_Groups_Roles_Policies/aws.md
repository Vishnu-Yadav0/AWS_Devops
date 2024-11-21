#### Session Video

```
https://drive.google.com/file/d/13VhCfqaUZgRcJalgUp5YKPd697FfPMdF/view?usp=sharing
```

#### DAY-3

```
Overview of AWS Global Infrastructure (Regions and Availability Zones)
Login to AWS as Root and Enable MFA

1. Navigating the AWS Management Console
2. Understanding the Dashboard
3. Using the search bar and service menu
4. Exploring key services: EC2, S3, RDS, and IAM

AWS :
    - IAM :
        - User 
        - Group
        - Policies
        - Roles
        - SSO 
        Switch Role


IAM User
IAM Policies
IAM Roles
IAM MFA for Root 
Log Mgmt: CloudTrail

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html

https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Operations.html

https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html

https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ec2.html



```

#### Sample Policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "cloudbinaryops",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "elasticloadbalancing:DescribeLoadBalancers",
                "autoscaling:DescribeAutoScalingGroups",
                "iam:*"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:RequestedRegion": "us-east-1"
                }
            }
        },
        {
            "Sid": "cloudbinaryops1",
            "Effect": "Allow",
            "Action": "route53:*",
            "Resource": "*"
        }
    ]
}

```

```
The information in a statement is contained within a series of elements.

Version – Specify the version of the policy language that you want to use. We recommend that you use the latest 2012-10-17 version. For more information, see IAM JSON policy elements: Version

Statement – Use this main policy element as a container for the following elements. You can include more than one statement in a policy.

Sid (Optional) – Include an optional statement ID to differentiate between your statements.

Effect – Use Allow or Deny to indicate whether the policy allows or denies access.

Principal (Required in only some circumstances) – If you create a resource-based policy, you must indicate the account, user, role, or federated user to which you would like to allow or deny access. If you are creating an IAM permissions policy to attach to a user or role, you cannot include this element. The principal is implied as that user or role.

Action – Include a list of actions that the policy allows or denies.

Resource (Required in only some circumstances) – If you create an IAM permissions policy, you must specify a list of resources to which the actions apply. If you create a resource-based policy, this element is optional. If you do not include this element, then the resource to which the action applies is the resource to which the policy is attached.

Condition (Optional) – Specify the circumstances under which the policy grants permission.
```