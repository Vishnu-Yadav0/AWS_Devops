#### Session Video

```
https://drive.google.com/file/d/10YOjVN_LzqtFwpFjaYUj1USNH8954E5s/view?usp=sharing
```

#### Day 1: Introduction to AWS and Core Services

#### Objective: Familiarise students with the basics of AWS, account setup, and core services like EC2, S3, and IAM.

#### Additional Resources:

```
AWS Documentation: https://docs.aws.amazon.com/
AWS Free Tier: https://aws.amazon.com/free/
AWS Training and Certification: https://aws.amazon.com/training/
```

#### 1. Introduction to Cloud Computing and AWS 

#### Topics Covered:

```
1. What is Cloud Computing?
2. Benefits of Cloud Computing
3. Introduction to AWS
4. Overview of AWS Global Infrastructure (Regions and Availability Zones)

```

#### Activities:
- Discussion on how cloud computing is transforming industries
- Examples of companies using AWS

#### 2. Setting Up an AWS Account

#### Topics Covered:

```
1. Steps to create an AWS account
2. Understanding AWS Free Tier
3. Setting up billing alerts and cost management
```

#### Activities:
- Guide students through the account creation process
- Setting up billing alerts

#### 3. AWS Management Console

#### Topics Covered:

```
1. Navigating the AWS Management Console
2. Understanding the Dashboard
3. Using the search bar and service menu
4. Exploring key services: EC2, S3, RDS, and IAM
```

#### Activities:
- Live demonstration of the AWS Management Console
- Hands-on navigation exercise


#### Day 1: Introduction to AWS and Core Services - Detailed Modules
#### Module 1: What is Cloud Computing?
#### Objective: Understand the fundamental concept of cloud computing.

#### Definition:

```
Cloud computing is the on-demand delivery of IT resources and services over the internet with pay-as-you-go pricing. Instead of owning and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like AWS.

```

#### Key Concepts:

```
On-Demand Self-Service: Users can provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.

Broad Network Access: Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).

Resource Pooling: The provider's computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand.

Rapid Elasticity: Capabilities can be elastically provisioned and released to scale rapidly outward and inward commensurate with demand.

Measured Service: Cloud systems automatically control and optimize resource use by leveraging a metering capability at some level of abstraction appropriate to the type of service (e.g., storage, processing, bandwidth).
```

#### Types of Cloud Computing:

```
Public Cloud: Services are delivered over the public internet and shared across organizations.

Private Cloud: Services are maintained on a private network and used exclusively by one organization.

Hybrid Cloud: Combines public and private clouds, allowing data and applications to be shared between them.

```

#### Module 2: Benefits of Cloud Computing
#### Objective: Identify the key advantages of adopting cloud computing.

#### Cost Efficiency:

```
Pay-as-you-go: Only pay for what you use, reducing upfront capital expenses.

Lower operational costs: Reduce the need for hardware, software, and in-house data centers.

Scalability and Flexibility:
    - Elasticity: Scale resources up or down based on demand without overprovisioning.

    - Global Reach: Deploy applications in multiple regions worldwide with just a few clicks.
Performance and Reliability:

High Availability: Use multiple redundant sites to ensure continuous availability.

Disaster Recovery: Built-in capabilities for backup and disaster recovery, minimizing downtime.

Security:
    - Data Security: Robust security measures including encryption, identity and access management, and compliance with global standards.

Physical Security: Cloud providers have state-of-the-art physical security at their data centers.

Innovation:
    - Rapid Deployment: Quickly deploy and iterate on applications and services.
    
    - Access to Cutting-Edge Technologies: Utilize the latest technologies, such as machine learning, AI, and big data analytics, without the need for significant investment.
```

#### Module 3: Introduction to AWS

#### Objective: Gain an overview of AWS and its core offerings.

####  What is AWS?
```
Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments. It was launched in 2006 and has since become a leader in the cloud services market.
```

#### Core Services:

```

Compute Services: EC2 (Elastic Compute Cloud), Lambda (serverless computing), ECS (Elastic Container Service).

Storage Services: S3 (Simple Storage Service), EBS (Elastic Block Store), Glacier (long-term archival storage).

Database Services: RDS (Relational Database Service), DynamoDB (NoSQL database), Aurora (high-performance database).

Networking Services: VPC (Virtual Private Cloud), Route 53 (DNS service), CloudFront (Content Delivery Network).

Management Tools: CloudWatch (monitoring), CloudFormation (infrastructure as code), IAM (Identity and Access Management).

AWS Ecosystem:
AWS has a vast ecosystem of tools and services designed to support various workloads and applications, from web and mobile applications to data processing and machine learning.

Market Leadership:
AWS is a market leader due to its extensive service offerings, global reach, robust security, and continuous innovation.


```

#### Module 4: Overview of AWS Global Infrastructure (Regions and Availability Zones)
#### Objective: Understand the structure and components of AWS's global infrastructure.

#### Global Infrastructure Components:

```
Regions: AWS has multiple geographic regions around the world. Each region is a separate geographic area with multiple, isolated locations known as Availability Zones.

Availability Zones (AZs): Each region consists of multiple, isolated locations within that region. Each AZ is a distinct data center with redundant power, networking, and connectivity. This isolation is crucial for fault tolerance and high availability.

Edge Locations: AWS has a network of edge locations that are used by AWS services such as Amazon CloudFront to cache copies of your content closer to your users for faster delivery.
```

#### Regions:

```
Each region is completely independent, enhancing fault tolerance and stability.
Customers can choose a region to store their data, run their applications, and serve their end users with lower latency.
Examples: US East (N. Virginia), EU (Ireland), Asia Pacific (Sydney).
```

#### AWS Global Infrastructure Map
```
The AWS Cloud spans 105 Availability Zones within 33 geographic regions, with announced plans for 18 more Availability Zones and six more AWS Regions in Malaysia, Mexico, New Zealand, the Kingdom of Saudi Arabia, Thailand, and the AWS European Sovereign Cloud.

https://aws.amazon.com/about-aws/global-infrastructure/

```

#### Availability Zones:

```
AZs are designed to be isolated from failures in other AZs, providing inexpensive, low-latency network connectivity to other AZs in the same region.
By launching instances in separate AZs, customers can protect their applications from failure in a single location.
```

#### Edge Locations:

```
AWS edge locations help deliver content with low latency to users by caching copies closer to their geographic location.
These are part of the Amazon CloudFront content delivery network (CDN).
```

#### Global Reach and Redundancy:

```
AWS's global infrastructure is designed to provide high availability, reliability, and scalability.
Using multiple regions and AZs, customers can design resilient architectures that can withstand failures at various levels.
```

