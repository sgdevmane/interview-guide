# AWS Cloud Interview Questions

## Table of Contents
1. [Q1: Explain AWS Global Infrastructure and its components.](#q1-explain-aws-global-infrastructure-and-its-components)
2. [Q2: What is the difference between AWS Regions and Availability Zones?](#q2-what-is-the-difference-between-aws-regions-and-availability-zones)
3. [Q3: Explain the AWS Shared Responsibility Model.](#q3-explain-the-aws-shared-responsibility-model)
4. [Q4: Compare EC2, Lambda, and Fargate. When would you use each?](#q4-compare-ec2-lambda-and-fargate-when-would-you-use-each)
5. [Q5: How do you implement Auto Scaling in AWS?](#q5-how-do-you-implement-auto-scaling-in-aws)
6. [Q6: Compare S3 storage classes and their use cases.](#q6-compare-s3-storage-classes-and-their-use-cases)
7. [Q7: How do you implement cross-region replication in S3?](#q7-how-do-you-implement-cross-region-replication-in-s3)
8. [Q8: Compare RDS, DynamoDB, and Aurora. When would you use each?](#q8-compare-rds-dynamodb-and-aurora-when-would-you-use-each)
9. [Q9: How do you implement VPC networking with public and private subnets?](#q9-how-do-you-implement-vpc-networking-with-public-and-private-subnets)
10. [Q10: How do you implement IAM policies and roles for least privilege access?](#q10-how-do-you-implement-iam-policies-and-roles-for-least-privilege-access)
11. [Q11: How do you implement AWS WAF for web application security?](#q11-how-do-you-implement-aws-waf-for-web-application-security)
12. [Q12: How do you build a serverless application with Lambda, API Gateway, and DynamoDB?](#q12-how-do-you-build-a-serverless-application-with-lambda-api-gateway-and-dynamodb)
13. [Q13: How do you implement ECS with Fargate for containerized applications?](#q13-how-do-you-implement-ecs-with-fargate-for-containerized-applications)
14. [Q14: How do you implement CI/CD pipeline using CodePipeline, CodeBuild, and CodeDeploy?](#q14-how-do-you-implement-ci-cd-pipeline-using-codepipeline-codebuild-and-codedeploy)
15. [Q15: How do you implement Infrastructure as Code using CloudFormation and CDK?](#q15-how-do-you-implement-infrastructure-as-code-using-cloudformation-and-cdk)
16. [Q16: How do you implement comprehensive monitoring with CloudWatch, X-Ray, and AWS Config?](#q16-how-do-you-implement-comprehensive-monitoring-with-cloudwatch-x-ray-and-aws-config)
17. [Q17: How do you implement cost optimization strategies in AWS?](#q17-how-do-you-implement-cost-optimization-strategies-in-aws)
18. [Q18: How do you implement disaster recovery and backup strategies in AWS?](#q18-how-do-you-implement-disaster-recovery-and-backup-strategies-in-aws)
19. [Q19: How do you implement advanced security with AWS WAF, GuardDuty, and Security Hub?](#q19-how-do-you-implement-advanced-security-with-aws-waf-guardduty-and-security-hub)
20. [Q20: How do you implement multi-account governance with AWS Organizations and Control Tower?](#q20-how-do-you-implement-multi-account-governance-with-aws-organizations-and-control-tower)
21. [Q21: What is the difference between EBS and EFS?](#q21-what-is-the-difference-between-ebs-and-efs)
22. [Q22: What is the difference between Security Groups and NACLs?](#q22-what-is-the-difference-between-security-groups-and-nacls)
23. [Q23: What is the difference between an IAM User and an IAM Role?](#q23-what-is-the-difference-between-an-iam-user-and-an-iam-role)
24. [Q24: What is the difference between SQS and SNS?](#q24-what-is-the-difference-between-sqs-and-sns)
25. [Q25: What is the difference between a launch template and a launch configuration?](#q25-what-is-the-difference-between-a-launch-template-and-a-launch-configuration)
26. [Q26: What is AWS Shield and how does it work?](#q26-what-is-aws-shield-and-how-does-it-work)
27. [Q27: What is the difference between Amazon RDS and Amazon Aurora?](#q27-what-is-the-difference-between-amazon-rds-and-amazon-aurora)
28. [Q28: What is AWS Lambda and what are its benefits?](#q28-what-is-aws-lambda-and-what-are-its-benefits)
29. [Q29: What is the difference between an Application Load Balancer and a Network Load Balancer?](#q29-what-is-the-difference-between-an-application-load-balancer-and-a-network-load-balancer)
30. [Q30: What is Amazon S3 Transfer Acceleration?](#q30-what-is-amazon-s3-transfer-acceleration)
31. [Q31: What is AWS Global Accelerator?](#q31-what-is-aws-global-accelerator)
32. [Q32: What is Amazon CloudFront and how does it work?](#q32-what-is-amazon-cloudfront-and-how-does-it-work)
33. [Q33: What is the difference between a stateful and a stateless application?](#q33-what-is-the-difference-between-a-stateful-and-a-stateless-application)
34. [Q34: What is AWS Elastic Beanstalk?](#q34-what-is-aws-elastic-beanstalk)
35. [Q35: What is the difference between horizontal and vertical scaling?](#q35-what-is-the-difference-between-horizontal-and-vertical-scaling)
36. [Q36: What is Amazon ElastiCache?](#q36-what-is-amazon-elasticache)
37. [Q37: What is AWS Snowball?](#q37-what-is-aws-snowball)
38. [Q38: What is AWS Storage Gateway?](#q38-what-is-aws-storage-gateway)
39. [Q39: What is Amazon EKS?](#q39-what-is-amazon-eks)
40. [Q40: What is Amazon ECS?](#q40-what-is-amazon-ecs)
41. [Q41: What is the difference between Amazon ECS and Amazon EKS?](#q41-what-is-the-difference-between-amazon-ecs-and-amazon-eks)
42. [Q42: What is AWS Fargate?](#q42-what-is-aws-fargate)
43. [Q43: What is AWS CloudFormation?](#q43-what-is-aws-cloudformation)
44. [Q44: What is AWS CDK and how does it differ from CloudFormation?](#q44-what-is-aws-cdk-and-how-does-it-differ-from-cloudformation)
45. [Q45: What is AWS SAM?](#q45-what-is-aws-sam)
46. [Q46: What is AWS CodeCommit?](#q46-what-is-aws-codecommit)
47. [Q47: What is AWS CodeBuild?](#q47-what-is-aws-codebuild)
48. [Q48: What is AWS CodeDeploy?](#q48-what-is-aws-codedeploy)
49. [Q49: What is AWS CodePipeline?](#q49-what-is-aws-codepipeline)
50. [Q50: How do AWS CodeCommit, CodeBuild, CodeDeploy, and CodePipeline work together?](#q50-how-do-aws-codecommit-codebuild-codedeploy-and-codepipeline-work-together)
51. [Q51: How do you automate AWS infrastructure management using AWS CLI?](#q51-how-do-you-automate-aws-infrastructure-management-using-aws-cli)
52. [Q52: What is AWS Step Functions and when should you use it?](#q52-what-is-aws-step-functions-and-when-should-you-use-it)
53. [Q53: What is Amazon EventBridge and how does it differ from CloudWatch Events?](#q53-what-is-amazon-eventbridge-and-how-does-it-differ-from-cloudwatch-events)
54. [Q54: Compare Amazon SQS, SNS, and Kinesis.](#q54-compare-amazon-sqs-sns-and-kinesis)
55. [Q55: What are the different types of API Gateway endpoints?](#q55-what-are-the-different-types-of-api-gateway-endpoints)
56. [Q56: What are Lambda Layers and why should you use them?](#q56-what-are-lambda-layers-and-why-should-you-use-them)
57. [Q57: How do DynamoDB Global Tables work?](#q57-how-do-dynamodb-global-tables-work)
58. [Q58: What are DynamoDB Streams?](#q58-what-are-dynamodb-streams)
59. [Q59: Compare Amazon Cognito User Pools and Identity Pools.](#q59-compare-amazon-cognito-user-pools-and-identity-pools)
60. [Q60: What is AWS AppSync?](#q60-what-is-aws-appsync)
61. [Q61: What is Amazon Athena?](#q61-what-is-amazon-athena)
62. [Q62: What is AWS Glue and its components?](#q62-what-is-aws-glue-and-its-components)
63. [Q63: What is Amazon Redshift Spectrum?](#q63-what-is-amazon-redshift-spectrum)
64. [Q64: Compare Kinesis Data Streams and Kinesis Data Firehose.](#q64-compare-kinesis-data-streams-and-kinesis-data-firehose)
65. [Q65: What is AWS Lake Formation?](#q65-what-is-aws-lake-formation)
66. [Q66: What is Amazon EMR (Elastic MapReduce)?](#q66-what-is-amazon-emr-elastic-mapreduce)
67. [Q67: What is Amazon OpenSearch Service?](#q67-what-is-amazon-opensearch-service)
68. [Q68: What is AWS DMS (Database Migration Service)?](#q68-what-is-aws-dms-database-migration-service)
69. [Q69: What is Amazon QuickSight?](#q69-what-is-amazon-quicksight)
70. [Q70: What is Amazon MSK?](#q70-what-is-amazon-msk)
71. [Q71: What is AWS Transit Gateway?](#q71-what-is-aws-transit-gateway)
72. [Q72: What are VPC Endpoints and what types exist?](#q72-what-are-vpc-endpoints-and-what-types-exist)
73. [Q73: Compare AWS Direct Connect and AWS VPN.](#q73-compare-aws-direct-connect-and-aws-vpn)
74. [Q74: Explain Route 53 Routing Policies.](#q74-explain-route-53-routing-policies)
75. [Q75: Compare VPC Peering and Transit Gateway.](#q75-compare-vpc-peering-and-transit-gateway)
76. [Q76: Compare Amazon EFS and Amazon FSx.](#q76-compare-amazon-efs-and-amazon-fsx)
77. [Q77: What are EC2 Placement Groups?](#q77-what-are-ec2-placement-groups)
78. [Q78: What are EC2 Spot Instances and when should you use them?](#q78-what-are-ec2-spot-instances-and-when-should-you-use-them)
79. [Q79: How do S3 Lifecycle Policies work?](#q79-how-do-s3-lifecycle-policies-work)
80. [Q80: What is AWS Outposts?](#q80-what-is-aws-outposts)
81. [Q81: What is AWS Systems Manager (SSM) and its key capabilities?](#q81-what-is-aws-systems-manager-ssm-and-its-key-capabilities)
82. [Q82: Compare AWS Secrets Manager and Systems Manager Parameter Store.](#q82-compare-aws-secrets-manager-and-systems-manager-parameter-store)
83. [Q83: What is the difference between AWS KMS and CloudHSM?](#q83-what-is-the-difference-between-aws-kms-and-cloudhsm)
84. [Q84: Compare AWS CloudTrail and AWS Config.](#q84-compare-aws-cloudtrail-and-aws-config)
85. [Q85: What is AWS Trusted Advisor?](#q85-what-is-aws-trusted-advisor)
86. [Q86: What are the pillars of the AWS Well-Architected Framework?](#q86-what-are-the-pillars-of-the-aws-well-architected-framework)
87. [Q87: What is Amazon Macie?](#q87-what-is-amazon-macie)
88. [Q88: What is Amazon Inspector?](#q88-what-is-amazon-inspector)
89. [Q89: What is AWS Service Catalog?](#q89-what-is-aws-service-catalog)
90. [Q90: What is AWS Compute Optimizer?](#q90-what-is-aws-compute-optimizer)
91. [Q91: Compare AWS Cost Explorer and Cost & Usage Report (CUR).](#q91-compare-aws-cost-explorer-and-cost-and-usage-report-cur)
92. [Q92: What is AWS Budgets and Cost Anomaly Detection?](#q92-what-is-aws-budgets-and-cost-anomaly-detection)
93. [Q93: What is CloudWatch Logs Insights?](#q93-what-is-cloudwatch-logs-insights)
94. [Q94: What is the difference between AWS Shield Standard and Advanced?](#q94-what-is-the-difference-between-aws-shield-standard-and-advanced)
95. [Q95: What is AWS Firewall Manager?](#q95-what-is-aws-firewall-manager)
96. [Q96: What is S3 Object Lock and when would you use it?](#q96-what-is-s3-object-lock-and-when-would-you-use-it)
97. [Q97: Does DynamoDB support ACID transactions?](#q97-does-dynamodb-support-acid-transactions)
98. [Q98: What is AWS Backup?](#q98-what-is-aws-backup)
99. [Q99: What is AWS App Runner?](#q99-what-is-aws-app-runner)
100. [Q100: Scenario: You are experiencing high latency on your application hosted on EC2. How do you troubleshoot?](#q100-scenario:-you-are-experiencing-high-latency-on-your-application-hosted-on-ec2-how-do-you-troubleshoot)

---

## AWS Fundamentals

### Q1: Explain AWS Global Infrastructure and its components.
**Difficulty: Medium**

**Answer:**
AWS Global Infrastructure consists of Regions, Availability Zones, Edge Locations, and Regional Edge Caches that provide a highly available, fault-tolerant, and scalable cloud computing platform worldwide.

**AWS Global Infrastructure Components:**

```yaml
# AWS Infrastructure as Code (CloudFormation) Example
# This demonstrates a multi-region, highly available architecture

AWSTemplateFormatVersion: '2010-09-09'
Description: 'Multi-Region AWS Infrastructure with High Availability'

Parameters:
  Environment:
    Type: String
    Default: production
    AllowedValues: [development, staging, production]
    Description: Environment name
  
  KeyPairName:
    Type: AWS::EC2::KeyPair::KeyName
    Description: EC2 Key Pair for SSH access
  
  DBPassword:
    Type: String
    NoEcho: true
    MinLength: 8
    Description: Database password

Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0abcdef1234567890
      AZ1: us-east-1a
      AZ2: us-east-1b
      AZ3: us-east-1c
    us-west-2:
      AMI: ami-0fedcba0987654321
      AZ1: us-west-2a
      AZ2: us-west-2b
      AZ3: us-west-2c
    eu-west-1:
      AMI: ami-0123456789abcdef0
      AZ1: eu-west-1a
      AZ2: eu-west-1b
      AZ3: eu-west-1c

Resources:
  # === VPC AND NETWORKING ===
  
  # Primary VPC
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-vpc'
        - Key: Environment
          Value: !Ref Environment

  # Internet Gateway
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-igw'

  InternetGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      InternetGatewayId: !Ref InternetGateway
      VpcId: !Ref VPC

  # Public Subnets (Multi-AZ)
  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ1]
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-public-subnet-1'
        - Key: Type
          Value: Public

  PublicSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ2]
      CidrBlock: 10.0.2.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-public-subnet-2'
        - Key: Type
          Value: Public

  PublicSubnet3:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ3]
      CidrBlock: 10.0.3.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-public-subnet-3'
        - Key: Type
          Value: Public

  # Private Subnets (Multi-AZ)
  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ1]
      CidrBlock: 10.0.11.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-private-subnet-1'
        - Key: Type
          Value: Private

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ2]
      CidrBlock: 10.0.12.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-private-subnet-2'
        - Key: Type
          Value: Private

  PrivateSubnet3:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ3]
      CidrBlock: 10.0.13.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-private-subnet-3'
        - Key: Type
          Value: Private

  # Database Subnets (Multi-AZ)
  DatabaseSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ1]
      CidrBlock: 10.0.21.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-database-subnet-1'
        - Key: Type
          Value: Database

  DatabaseSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ2]
      CidrBlock: 10.0.22.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-database-subnet-2'
        - Key: Type
          Value: Database

  DatabaseSubnet3:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !FindInMap [RegionMap, !Ref 'AWS::Region', AZ3]
      CidrBlock: 10.0.23.0/24
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-database-subnet-3'
        - Key: Type
          Value: Database

  # NAT Gateways for Private Subnets
  NatGateway1EIP:
    Type: AWS::EC2::EIP
    DependsOn: InternetGatewayAttachment
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-nat-eip-1'

  NatGateway2EIP:
    Type: AWS::EC2::EIP
    DependsOn: InternetGatewayAttachment
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-nat-eip-2'

  NatGateway1:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGateway1EIP.AllocationId
      SubnetId: !Ref PublicSubnet1
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-nat-gateway-1'

  NatGateway2:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGateway2EIP.AllocationId
      SubnetId: !Ref PublicSubnet2
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-nat-gateway-2'

  # Route Tables
  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-public-routes'

  DefaultPublicRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  PublicSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet1

  PublicSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet2

  PublicSubnet3RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet3

  PrivateRouteTable1:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-private-routes-1'

  DefaultPrivateRoute1:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable1
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway1

  PrivateSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable1
      SubnetId: !Ref PrivateSubnet1

  PrivateRouteTable2:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-private-routes-2'

  DefaultPrivateRoute2:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway2

  PrivateSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      SubnetId: !Ref PrivateSubnet2

  PrivateSubnet3RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      SubnetId: !Ref PrivateSubnet3

  # === SECURITY GROUPS ===
  
  # Application Load Balancer Security Group
  ALBSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub '${Environment}-alb-sg'
      GroupDescription: Security group for Application Load Balancer
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
          Description: HTTP access from anywhere
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
          Description: HTTPS access from anywhere
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
          Description: All outbound traffic
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-alb-sg'

  # Web Server Security Group
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub '${Environment}-web-sg'
      GroupDescription: Security group for web servers
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          SourceSecurityGroupId: !Ref ALBSecurityGroup
          Description: HTTP from ALB
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          SourceSecurityGroupId: !Ref ALBSecurityGroup
          Description: HTTPS from ALB
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          SourceSecurityGroupId: !Ref BastionSecurityGroup
          Description: SSH from Bastion
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-web-sg'

  # Application Server Security Group
  AppServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub '${Environment}-app-sg'
      GroupDescription: Security group for application servers
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 8080
          ToPort: 8080
          SourceSecurityGroupId: !Ref WebServerSecurityGroup
          Description: Application port from web servers
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          SourceSecurityGroupId: !Ref BastionSecurityGroup
          Description: SSH from Bastion
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-app-sg'

  # Database Security Group
  DatabaseSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub '${Environment}-db-sg'
      GroupDescription: Security group for database servers
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 3306
          ToPort: 3306
          SourceSecurityGroupId: !Ref AppServerSecurityGroup
          Description: MySQL from application servers
        - IpProtocol: tcp
          FromPort: 5432
          ToPort: 5432
          SourceSecurityGroupId: !Ref AppServerSecurityGroup
          Description: PostgreSQL from application servers
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-db-sg'

  # Bastion Host Security Group
  BastionSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub '${Environment}-bastion-sg'
      GroupDescription: Security group for bastion host
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
          Description: SSH access from anywhere (restrict in production)
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-bastion-sg'

  # === COMPUTE RESOURCES ===
  
  # Launch Template for Web Servers
  WebServerLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: !Sub '${Environment}-web-server-template'
      LaunchTemplateData:
        ImageId: !FindInMap [RegionMap, !Ref 'AWS::Region', AMI]
        InstanceType: t3.medium
        KeyName: !Ref KeyPairName
        SecurityGroupIds:
          - !Ref WebServerSecurityGroup
        IamInstanceProfile:
          Arn: !GetAtt WebServerInstanceProfile.Arn
        UserData:
          Fn::Base64: !Sub |
            #!/bin/bash
            yum update -y
            yum install -y httpd
            systemctl start httpd
            systemctl enable httpd
            
            # Install CloudWatch agent
            wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
            rpm -U ./amazon-cloudwatch-agent.rpm
            
            # Configure CloudWatch agent
            cat > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json << EOF
            {
              "metrics": {
                "namespace": "AWS/EC2/Custom",
                "metrics_collected": {
                  "cpu": {
                    "measurement": ["cpu_usage_idle", "cpu_usage_iowait", "cpu_usage_user", "cpu_usage_system"],
                    "metrics_collection_interval": 60
                  },
                  "disk": {
                    "measurement": ["used_percent"],
                    "metrics_collection_interval": 60,
                    "resources": ["*"]
                  },
                  "mem": {
                    "measurement": ["mem_used_percent"],
                    "metrics_collection_interval": 60
                  }
                }
              },
              "logs": {
                "logs_collected": {
                  "files": {
                    "collect_list": [
                      {
                        "file_path": "/var/log/httpd/access_log",
                        "log_group_name": "${Environment}-web-access-logs",
                        "log_stream_name": "{instance_id}"
                      },
                      {
                        "file_path": "/var/log/httpd/error_log",
                        "log_group_name": "${Environment}-web-error-logs",
                        "log_stream_name": "{instance_id}"
                      }
                    ]
                  }
                }
              }
            }
            EOF
            
            # Start CloudWatch agent
            /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
              -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json -s
            
            # Create simple index page
            cat > /var/www/html/index.html << EOF
            <!DOCTYPE html>
            <html>
            <head>
                <title>AWS Infrastructure Demo</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .container { max-width: 800px; margin: 0 auto; }
                    .info { background: #f0f0f0; padding: 20px; border-radius: 5px; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>AWS Multi-Region Infrastructure</h1>
                    <div class="info">
                        <h2>Instance Information</h2>
                        <p><strong>Region:</strong> ${AWS::Region}</p>
                        <p><strong>Environment:</strong> ${Environment}</p>
                        <p><strong>Instance ID:</strong> <span id="instance-id">Loading...</span></p>
                        <p><strong>Availability Zone:</strong> <span id="az">Loading...</span></p>
                        <p><strong>Local IP:</strong> <span id="local-ip">Loading...</span></p>
                        <p><strong>Public IP:</strong> <span id="public-ip">Loading...</span></p>
                    </div>
                    
                    <h2>Health Check</h2>
                    <div id="health-status">Checking...</div>
                    
                    <h2>Database Connection</h2>
                    <div id="db-status">Testing...</div>
                </div>
                
                <script>
                    // Fetch instance metadata
                    fetch('http://169.254.169.254/latest/meta-data/instance-id')
                        .then(response => response.text())
                        .then(data => document.getElementById('instance-id').textContent = data);
                    
                    fetch('http://169.254.169.254/latest/meta-data/placement/availability-zone')
                        .then(response => response.text())
                        .then(data => document.getElementById('az').textContent = data);
                    
                    fetch('http://169.254.169.254/latest/meta-data/local-ipv4')
                        .then(response => response.text())
                        .then(data => document.getElementById('local-ip').textContent = data);
                    
                    fetch('http://169.254.169.254/latest/meta-data/public-ipv4')
                        .then(response => response.text())
                        .then(data => document.getElementById('public-ip').textContent = data)
                        .catch(() => document.getElementById('public-ip').textContent = 'N/A');
                    
                    // Health check
                    document.getElementById('health-status').innerHTML = 
                        '<span style="color: green;">✓ Web server is running</span>';
                    
                    // Database connection test (placeholder)
                    document.getElementById('db-status').innerHTML = 
                        '<span style="color: blue;">Database connection configured</span>';
                </script>
            </body>
            </html>
            EOF
            
            # Create health check endpoint
            cat > /var/www/html/health << EOF
            {
              "status": "healthy",
              "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
              "region": "${AWS::Region}",
              "environment": "${Environment}"
            }
            EOF
        TagSpecifications:
          - ResourceType: instance
            Tags:
              - Key: Name
                Value: !Sub '${Environment}-web-server'
              - Key: Environment
                Value: !Ref Environment
              - Key: Type
                Value: WebServer

  # Auto Scaling Group for Web Servers
  WebServerAutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      AutoScalingGroupName: !Sub '${Environment}-web-asg'
      VPCZoneIdentifier:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
        - !Ref PrivateSubnet3
      LaunchTemplate:
        LaunchTemplateId: !Ref WebServerLaunchTemplate
        Version: !GetAtt WebServerLaunchTemplate.LatestVersionNumber
      MinSize: 2
      MaxSize: 10
      DesiredCapacity: 3
      TargetGroupARNs:
        - !Ref WebServerTargetGroup
      HealthCheckType: ELB
      HealthCheckGracePeriod: 300
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-web-asg'
          PropagateAtLaunch: false
        - Key: Environment
          Value: !Ref Environment
          PropagateAtLaunch: true
    UpdatePolicy:
      AutoScalingRollingUpdate:
        MinInstancesInService: 1
        MaxBatchSize: 1
        PauseTime: PT5M
        WaitOnResourceSignals: false

  # Application Load Balancer
  ApplicationLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Name: !Sub '${Environment}-alb'
      Scheme: internet-facing
      Type: application
      SecurityGroups:
        - !Ref ALBSecurityGroup
      Subnets:
        - !Ref PublicSubnet1
        - !Ref PublicSubnet2
        - !Ref PublicSubnet3
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-alb'
        - Key: Environment
          Value: !Ref Environment

  # Target Group for Web Servers
  WebServerTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Name: !Sub '${Environment}-web-tg'
      Port: 80
      Protocol: HTTP
      VpcId: !Ref VPC
      HealthCheckPath: /health
      HealthCheckProtocol: HTTP
      HealthCheckIntervalSeconds: 30
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      UnhealthyThresholdCount: 3
      TargetType: instance
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-web-tg'

  # ALB Listener
  ALBListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref WebServerTargetGroup
      LoadBalancerArn: !Ref ApplicationLoadBalancer
      Port: 80
      Protocol: HTTP

  # === IAM ROLES AND POLICIES ===
  
  # IAM Role for Web Servers
  WebServerRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub '${Environment}-web-server-role'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      Policies:
        - PolicyName: S3Access
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:PutObject
                Resource:
                  - !Sub '${S3Bucket}/*'
              - Effect: Allow
                Action:
                  - s3:ListBucket
                Resource:
                  - !Ref S3Bucket

  WebServerInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: !Sub '${Environment}-web-server-profile'
      Roles:
        - !Ref WebServerRole

  # === STORAGE ===
  
  # S3 Bucket for application assets
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub '${Environment}-app-assets-${AWS::AccountId}-${AWS::Region}'
      VersioningConfiguration:
        Status: Enabled
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      LifecycleConfiguration:
        Rules:
          - Id: DeleteOldVersions
            Status: Enabled
            NoncurrentVersionExpirationInDays: 30
          - Id: TransitionToIA
            Status: Enabled
            TransitionInDays: 30
            StorageClass: STANDARD_IA
          - Id: TransitionToGlacier
            Status: Enabled
            TransitionInDays: 90
            StorageClass: GLACIER
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-app-assets'
        - Key: Environment
          Value: !Ref Environment

  # === DATABASE ===
  
  # DB Subnet Group
  DatabaseSubnetGroup:
    Type: AWS::RDS::DBSubnetGroup
    Properties:
      DBSubnetGroupName: !Sub '${Environment}-db-subnet-group'
      DBSubnetGroupDescription: Subnet group for RDS database
      SubnetIds:
        - !Ref DatabaseSubnet1
        - !Ref DatabaseSubnet2
        - !Ref DatabaseSubnet3
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-db-subnet-group'

  # RDS Database Instance
  DatabaseInstance:
    Type: AWS::RDS::DBInstance
    DeletionPolicy: Snapshot
    Properties:
      DBInstanceIdentifier: !Sub '${Environment}-database'
      DBInstanceClass: db.t3.micro
      Engine: mysql
      EngineVersion: '8.0.35'
      AllocatedStorage: 20
      StorageType: gp2
      StorageEncrypted: true
      MasterUsername: admin
      MasterUserPassword: !Ref DBPassword
      DBSubnetGroupName: !Ref DatabaseSubnetGroup
      VPCSecurityGroups:
        - !Ref DatabaseSecurityGroup
      BackupRetentionPeriod: 7
      PreferredBackupWindow: "03:00-04:00"
      PreferredMaintenanceWindow: "sun:04:00-sun:05:00"
      MultiAZ: true
      PubliclyAccessible: false
      DeletionProtection: true
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-database'
        - Key: Environment
          Value: !Ref Environment

  # === MONITORING ===
  
  # CloudWatch Log Groups
  WebAccessLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub '${Environment}-web-access-logs'
      RetentionInDays: 30

  WebErrorLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub '${Environment}-web-error-logs'
      RetentionInDays: 30

  # CloudWatch Alarms
  HighCPUAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: !Sub '${Environment}-high-cpu'
      AlarmDescription: Alarm when CPU exceeds 80%
      MetricName: CPUUtilization
      Namespace: AWS/EC2
      Statistic: Average
      Period: 300
      EvaluationPeriods: 2
      Threshold: 80
      ComparisonOperator: GreaterThanThreshold
      Dimensions:
        - Name: AutoScalingGroupName
          Value: !Ref WebServerAutoScalingGroup
      AlarmActions:
        - !Ref ScaleUpPolicy

  LowCPUAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: !Sub '${Environment}-low-cpu'
      AlarmDescription: Alarm when CPU is below 20%
      MetricName: CPUUtilization
      Namespace: AWS/EC2
      Statistic: Average
      Period: 300
      EvaluationPeriods: 2
      Threshold: 20
      ComparisonOperator: LessThanThreshold
      Dimensions:
        - Name: AutoScalingGroupName
          Value: !Ref WebServerAutoScalingGroup
      AlarmActions:
        - !Ref ScaleDownPolicy

  # Auto Scaling Policies
  ScaleUpPolicy:
    Type: AWS::AutoScaling::ScalingPolicy
    Properties:
      AdjustmentType: ChangeInCapacity
      AutoScalingGroupName: !Ref WebServerAutoScalingGroup
      Cooldown: 300
      ScalingAdjustment: 1

  ScaleDownPolicy:
    Type: AWS::AutoScaling::ScalingPolicy
    Properties:
      AdjustmentType: ChangeInCapacity
      AutoScalingGroupName: !Ref WebServerAutoScalingGroup
      Cooldown: 300
      ScalingAdjustment: -1

Outputs:
  VPCId:
    Description: VPC ID
    Value: !Ref VPC
    Export:
      Name: !Sub '${Environment}-vpc-id'

  LoadBalancerDNS:
    Description: Application Load Balancer DNS name
    Value: !GetAtt ApplicationLoadBalancer.DNSName
    Export:
      Name: !Sub '${Environment}-alb-dns'

  DatabaseEndpoint:
    Description: RDS Database endpoint
    Value: !GetAtt DatabaseInstance.Endpoint.Address
    Export:
      Name: !Sub '${Environment}-db-endpoint'

  S3BucketName:
    Description: S3 Bucket name
    Value: !Ref S3Bucket
    Export:
      Name: !Sub '${Environment}-s3-bucket'

  Region:
    Description: AWS Region
    Value: !Ref 'AWS::Region'
    Export:
      Name: !Sub '${Environment}-region'
```


### Q2: What is the difference between AWS Regions and Availability Zones?
**Difficulty: Easy**

**Answer:**
- **AWS Regions**: Separate geographic areas around the world where AWS clusters data centers. Each region is completely independent and isolated from other regions.
- **Availability Zones (AZs)**: One or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. AZs are isolated from each other but connected through low-latency links.

```yaml
# Example: Multi-AZ deployment
Resources:
  WebServerAZ1:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-0abcdef1234567890
      InstanceType: t3.micro
      
  WebServerAZ2:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1b
      ImageId: ami-0abcdef1234567890
      InstanceType: t3.micro
```


### Q3: Explain the AWS Shared Responsibility Model.
**Difficulty: Medium**

**Answer:**
The AWS Shared Responsibility Model defines the security responsibilities between AWS and the customer:

**AWS Responsibilities (Security OF the Cloud):**
- Physical security of data centers
- Hardware and software infrastructure
- Network infrastructure
- Virtualization infrastructure
- Managed services security

**Customer Responsibilities (Security IN the Cloud):**
- Operating system patches and updates
- Network and firewall configuration
- Identity and access management
- Data encryption
- Application-level security

```json
{
  "SharedResponsibilityModel": {
    "AWS": {
      "infrastructure": ["hardware", "software", "networking", "facilities"],
      "managedServices": ["RDS", "Lambda", "S3", "DynamoDB"]
    },
    "Customer": {
      "guestOS": ["patches", "updates", "security"],
      "applications": ["code", "runtime", "middleware"],
      "data": ["encryption", "integrity", "classification"],
      "identity": ["IAM", "MFA", "credentials"]
    }
  }
}
```

---

## Compute Services


### Q4: Compare EC2, Lambda, and Fargate. When would you use each?
**Difficulty: Medium**

**Answer:**

| Service | Use Case | Pricing Model | Management |
|---------|----------|---------------|------------|
| **EC2** | Long-running applications, custom environments | Pay for instance time | Full control, manual scaling |
| **Lambda** | Event-driven, short-duration tasks | Pay per request/execution time | Serverless, auto-scaling |
| **Fargate** | Containerized applications without server management | Pay for vCPU and memory | Serverless containers |

```python
# Lambda Function Example
import json
import boto3

def lambda_handler(event, context):
    """
    Process S3 events and resize images
    """
    s3 = boto3.client('s3')
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Process image
        response = process_image(bucket, key)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Images processed successfully')
    }

def process_image(bucket, key):
    # Image processing logic
    pass
```

```yaml
# Fargate Task Definition
TaskDefinition:
  Type: AWS::ECS::TaskDefinition
  Properties:
    Family: web-app
    NetworkMode: awsvpc
    RequiresCompatibilities:
      - FARGATE
    Cpu: 256
    Memory: 512
    ExecutionRoleArn: !Ref TaskExecutionRole
    ContainerDefinitions:
      - Name: web-container
        Image: nginx:latest
        PortMappings:
          - ContainerPort: 80
            Protocol: tcp
        LogConfiguration:
          LogDriver: awslogs
          Options:
            awslogs-group: !Ref LogGroup
            awslogs-region: !Ref AWS::Region
```


### Q5: How do you implement Auto Scaling in AWS?
**Difficulty: Medium**

**Answer:**
AWS Auto Scaling automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost.

```yaml
# Auto Scaling Group with Launch Template
LaunchTemplate:
  Type: AWS::EC2::LaunchTemplate
  Properties:
    LaunchTemplateName: !Sub '${Environment}-launch-template'
    LaunchTemplateData:
      ImageId: ami-0abcdef1234567890
      InstanceType: t3.micro
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          yum update -y
          yum install -y httpd
          systemctl start httpd
          systemctl enable httpd
          echo "<h1>Hello from $(hostname -f)</h1>" > /var/www/html/index.html

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    AutoScalingGroupName: !Sub '${Environment}-asg'
    LaunchTemplate:
      LaunchTemplateId: !Ref LaunchTemplate
      Version: !GetAtt LaunchTemplate.LatestVersionNumber
    MinSize: 2
    MaxSize: 10
    DesiredCapacity: 3
    VPCZoneIdentifier:
      - !Ref PrivateSubnet1
      - !Ref PrivateSubnet2
      - !Ref PrivateSubnet3
    TargetGroupARNs:
      - !Ref TargetGroup
    HealthCheckType: ELB
    HealthCheckGracePeriod: 300
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-web-server'
        PropagateAtLaunch: true

# Scaling Policies
ScaleUpPolicy:
  Type: AWS::AutoScaling::ScalingPolicy
  Properties:
    AdjustmentType: ChangeInCapacity
    AutoScalingGroupName: !Ref AutoScalingGroup
    Cooldown: 300
    ScalingAdjustment: 1
    PolicyType: SimpleScaling

ScaleDownPolicy:
  Type: AWS::AutoScaling::ScalingPolicy
  Properties:
    AdjustmentType: ChangeInCapacity
    AutoScalingGroupName: !Ref AutoScalingGroup
    Cooldown: 300
    ScalingAdjustment: -1
    PolicyType: SimpleScaling

# CloudWatch Alarms
CPUAlarmHigh:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmDescription: Scale up on high CPU
    AlarmActions:
      - !Ref ScaleUpPolicy
    MetricName: CPUUtilization
    Namespace: AWS/EC2
    Statistic: Average
    Period: 300
    EvaluationPeriods: 2
    Threshold: 80
    ComparisonOperator: GreaterThanThreshold
    Dimensions:
      - Name: AutoScalingGroupName
        Value: !Ref AutoScalingGroup

CPUAlarmLow:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmDescription: Scale down on low CPU
    AlarmActions:
      - !Ref ScaleDownPolicy
    MetricName: CPUUtilization
    Namespace: AWS/EC2
    Statistic: Average
    Period: 300
    EvaluationPeriods: 2
    Threshold: 20
    ComparisonOperator: LessThanThreshold
    Dimensions:
      - Name: AutoScalingGroupName
        Value: !Ref AutoScalingGroup
```

---

## Storage Services


### Q6: Compare S3 storage classes and their use cases.
**Difficulty: Medium**

**Answer:**

| Storage Class | Use Case | Retrieval Time | Cost |
|---------------|----------|----------------|------|
| **S3 Standard** | Frequently accessed data | Immediate | Highest |
| **S3 IA** | Infrequently accessed data | Immediate | Medium |
| **S3 One Zone-IA** | Infrequent access, single AZ | Immediate | Lower |
| **S3 Glacier Instant** | Archive with instant access | Immediate | Low |
| **S3 Glacier Flexible** | Archive data | 1-5 minutes | Very Low |
| **S3 Glacier Deep Archive** | Long-term archive | 12 hours | Lowest |

```python
# S3 Lifecycle Policy Example
import boto3
import json

def create_lifecycle_policy():
    s3 = boto3.client('s3')
    
    lifecycle_config = {
        'Rules': [
            {
                'ID': 'DataLifecycleRule',
                'Status': 'Enabled',
                'Filter': {'Prefix': 'documents/'},
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'STANDARD_IA'
                    },
                    {
                        'Days': 90,
                        'StorageClass': 'GLACIER'
                    },
                    {
                        'Days': 365,
                        'StorageClass': 'DEEP_ARCHIVE'
                    }
                ],
                'Expiration': {
                    'Days': 2555  # 7 years
                }
            },
            {
                'ID': 'LogsLifecycleRule',
                'Status': 'Enabled',
                'Filter': {'Prefix': 'logs/'},
                'Transitions': [
                    {
                        'Days': 7,
                        'StorageClass': 'STANDARD_IA'
                    },
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ],
                'Expiration': {
                    'Days': 90
                }
            }
        ]
    }
    
    response = s3.put_bucket_lifecycle_configuration(
        Bucket='my-bucket',
        LifecycleConfiguration=lifecycle_config
    )
    
    return response

# S3 Event Notification
def setup_s3_notifications():
    s3 = boto3.client('s3')
    
    notification_config = {
        'LambdaConfigurations': [
            {
                'Id': 'ProcessImageUpload',
                'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:123456789012:function:ProcessImage',
                'Events': ['s3:ObjectCreated:*'],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'prefix',
                                'Value': 'images/'
                            },
                            {
                                'Name': 'suffix',
                                'Value': '.jpg'
                            }
                        ]
                    }
                }
            }
        ]
    }
    
    response = s3.put_bucket_notification_configuration(
        Bucket='my-bucket',
        NotificationConfiguration=notification_config
    )
    
    return response
```


### Q7: How do you implement cross-region replication in S3?
**Difficulty: Medium**

**Answer:**
S3 Cross-Region Replication (CRR) automatically replicates objects across AWS regions for compliance, lower latency, and disaster recovery.

```yaml
# S3 Bucket with Cross-Region Replication
SourceBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: !Sub '${Environment}-source-bucket-${AWS::AccountId}'
    VersioningConfiguration:
      Status: Enabled
    ReplicationConfiguration:
      Role: !GetAtt ReplicationRole.Arn
      Rules:
        - Id: ReplicateToDestination
          Status: Enabled
          Prefix: documents/
          Destination:
            BucketArn: !Sub 'arn:aws:s3:::${Environment}-dest-bucket-${AWS::AccountId}'
            StorageClass: STANDARD_IA
            ReplicationTime:
              Status: Enabled
              Time:
                Minutes: 15
            Metrics:
              Status: Enabled
              EventThreshold:
                Minutes: 15
    PublicAccessBlockConfiguration:
      BlockPublicAcls: true
      BlockPublicPolicy: true
      IgnorePublicAcls: true
      RestrictPublicBuckets: true

DestinationBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: !Sub '${Environment}-dest-bucket-${AWS::AccountId}'
    VersioningConfiguration:
      Status: Enabled
    PublicAccessBlockConfiguration:
      BlockPublicAcls: true
      BlockPublicPolicy: true
      IgnorePublicAcls: true
      RestrictPublicBuckets: true

# IAM Role for Replication
ReplicationRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            Service: s3.amazonaws.com
          Action: sts:AssumeRole
    Policies:
      - PolicyName: ReplicationPolicy
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - s3:GetObjectVersionForReplication
                - s3:GetObjectVersionAcl
              Resource: !Sub '${SourceBucket}/*'
            - Effect: Allow
              Action:
                - s3:ListBucket
              Resource: !Ref SourceBucket
            - Effect: Allow
              Action:
                - s3:ReplicateObject
                - s3:ReplicateDelete
              Resource: !Sub '${DestinationBucket}/*'
```

---

## Database Services


### Q8: Compare RDS, DynamoDB, and Aurora. When would you use each?
**Difficulty: Medium**

**Answer:**

| Service | Type | Use Case | Scaling | Consistency |
|---------|------|----------|---------|-------------|
| **RDS** | Relational | Traditional RDBMS needs | Vertical | ACID |
| **DynamoDB** | NoSQL | High-scale, low-latency apps | Horizontal | Eventually consistent |
| **Aurora** | Relational | High-performance, cloud-native | Auto-scaling | ACID |

```yaml
# RDS Multi-AZ Setup
RDSInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBInstanceIdentifier: !Sub '${Environment}-database'
    DBInstanceClass: db.t3.micro
    Engine: mysql
    EngineVersion: '8.0.35'
    MasterUsername: admin
    MasterUserPassword: !Ref DBPassword
    AllocatedStorage: 20
    StorageType: gp2
    StorageEncrypted: true
    MultiAZ: true
    VPCSecurityGroups:
      - !Ref DatabaseSecurityGroup
    DBSubnetGroupName: !Ref DBSubnetGroup
    BackupRetentionPeriod: 7
    PreferredBackupWindow: "03:00-04:00"
    PreferredMaintenanceWindow: "sun:04:00-sun:05:00"
    DeletionProtection: true
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-database'

DBSubnetGroup:
  Type: AWS::RDS::DBSubnetGroup
  Properties:
    DBSubnetGroupDescription: Subnet group for RDS
    SubnetIds:
      - !Ref DatabaseSubnet1
      - !Ref DatabaseSubnet2
      - !Ref DatabaseSubnet3
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-db-subnet-group'
```

```python
# DynamoDB Operations
import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
import json

class DynamoDBManager:
    def __init__(self, table_name, region='us-east-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(table_name)
    
    def create_item(self, item):
        """Create a new item"""
        try:
            response = self.table.put_item(
                Item=item,
                ConditionExpression='attribute_not_exists(id)'
            )
            return response
        except Exception as e:
            print(f"Error creating item: {e}")
            return None
    
    def get_item(self, key):
        """Get item by primary key"""
        try:
            response = self.table.get_item(Key=key)
            return response.get('Item')
        except Exception as e:
            print(f"Error getting item: {e}")
            return None
    
    def query_items(self, partition_key, sort_key_condition=None):
        """Query items by partition key"""
        try:
            if sort_key_condition:
                response = self.table.query(
                    KeyConditionExpression=Key('pk').eq(partition_key) & sort_key_condition
                )
            else:
                response = self.table.query(
                    KeyConditionExpression=Key('pk').eq(partition_key)
                )
            return response['Items']
        except Exception as e:
            print(f"Error querying items: {e}")
            return []
    
    def update_item(self, key, update_expression, expression_values):
        """Update an existing item"""
        try:
            response = self.table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_values,
                ReturnValues='UPDATED_NEW'
            )
            return response
        except Exception as e:
            print(f"Error updating item: {e}")
            return None
    
    def scan_with_filter(self, filter_expression):
        """Scan table with filter"""
        try:
            response = self.table.scan(
                FilterExpression=filter_expression
            )
            return response['Items']
        except Exception as e:
            print(f"Error scanning table: {e}")
            return []
    
    def batch_write(self, items):
        """Batch write multiple items"""
        try:
            with self.table.batch_writer() as batch:
                for item in items:
                    batch.put_item(Item=item)
            return True
        except Exception as e:
            print(f"Error batch writing: {e}")
            return False

# Usage Example
if __name__ == "__main__":
    db = DynamoDBManager('users-table')
    
    # Create user
    user = {
        'id': 'user123',
        'email': 'user@example.com',
        'name': 'John Doe',
        'created_at': '2024-01-01T00:00:00Z',
        'status': 'active'
    }
    db.create_item(user)
    
    # Query users
    users = db.query_items('user123')
    
    # Update user
    db.update_item(
        {'id': 'user123'},
        'SET #status = :status, #updated_at = :updated_at',
        {
            ':status': 'inactive',
            ':updated_at': '2024-01-02T00:00:00Z'
        }
    )
```

---

## Networking and Security


### Q9: How do you implement VPC networking with public and private subnets?
**Difficulty: Medium**

**Answer:**
A VPC provides an isolated network environment where you can launch AWS resources with complete control over networking configuration.

```yaml
# Complete VPC Setup with NAT Gateway
VPC:
  Type: AWS::EC2::VPC
  Properties:
    CidrBlock: 10.0.0.0/16
    EnableDnsHostnames: true
    EnableDnsSupport: true
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-vpc'

# Internet Gateway
InternetGateway:
  Type: AWS::EC2::InternetGateway
  Properties:
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-igw'

InternetGatewayAttachment:
  Type: AWS::EC2::VPCGatewayAttachment
  Properties:
    InternetGatewayId: !Ref InternetGateway
    VpcId: !Ref VPC

# NAT Gateway for private subnets
NATGatewayEIP:
  Type: AWS::EC2::EIP
  DependsOn: InternetGatewayAttachment
  Properties:
    Domain: vpc
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-nat-eip'

NATGateway:
  Type: AWS::EC2::NatGateway
  Properties:
    AllocationId: !GetAtt NATGatewayEIP.AllocationId
    SubnetId: !Ref PublicSubnet1
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-nat-gateway'

# Route Tables
PublicRouteTable:
  Type: AWS::EC2::RouteTable
  Properties:
    VpcId: !Ref VPC
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-public-rt'

DefaultPublicRoute:
  Type: AWS::EC2::Route
  DependsOn: InternetGatewayAttachment
  Properties:
    RouteTableId: !Ref PublicRouteTable
    DestinationCidrBlock: 0.0.0.0/0
    GatewayId: !Ref InternetGateway

PrivateRouteTable:
  Type: AWS::EC2::RouteTable
  Properties:
    VpcId: !Ref VPC
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-private-rt'

DefaultPrivateRoute:
  Type: AWS::EC2::Route
  Properties:
    RouteTableId: !Ref PrivateRouteTable
    DestinationCidrBlock: 0.0.0.0/0
    NatGatewayId: !Ref NATGateway

# Route Table Associations
PublicSubnet1RouteTableAssociation:
  Type: AWS::EC2::SubnetRouteTableAssociation
  Properties:
    RouteTableId: !Ref PublicRouteTable
    SubnetId: !Ref PublicSubnet1

PrivateSubnet1RouteTableAssociation:
  Type: AWS::EC2::SubnetRouteTableAssociation
  Properties:
    RouteTableId: !Ref PrivateRouteTable
    SubnetId: !Ref PrivateSubnet1
```


### Q10: How do you implement IAM policies and roles for least privilege access?
**Difficulty: Hard**

**Answer:**
IAM follows the principle of least privilege, granting only the minimum permissions necessary for users and services to perform their tasks.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadOnlyForSpecificBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-app-bucket",
        "arn:aws:s3:::my-app-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:prefix": [
            "user-data/${aws:username}/",
            "shared/"
          ]
        },
        "DateGreaterThan": {
          "aws:CurrentTime": "2024-01-01T00:00:00Z"
        },
        "IpAddress": {
          "aws:SourceIp": ["203.0.113.0/24", "198.51.100.0/24"]
        }
      }
    },
    {
      "Sid": "AllowCloudWatchLogsForApplication",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:/aws/lambda/my-app-*"
    },
    {
      "Sid": "DenyDangerousActions",
      "Effect": "Deny",
      "Action": [
        "iam:CreateUser",
        "iam:DeleteUser",
        "iam:CreateRole",
        "iam:DeleteRole",
        "ec2:TerminateInstances"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```

```python
# IAM Policy Generator
import json
import boto3
from typing import List, Dict, Any

class IAMPolicyBuilder:
    def __init__(self):
        self.policy = {
            "Version": "2012-10-17",
            "Statement": []
        }
    
    def add_statement(self, 
                     effect: str,
                     actions: List[str],
                     resources: List[str],
                     conditions: Dict[str, Any] = None,
                     sid: str = None) -> 'IAMPolicyBuilder':
        """Add a statement to the policy"""
        statement = {
            "Effect": effect,
            "Action": actions,
            "Resource": resources
        }
        
        if sid:
            statement["Sid"] = sid
        
        if conditions:
            statement["Condition"] = conditions
        
        self.policy["Statement"].append(statement)
        return self
    
    def allow_s3_access(self, bucket_name: str, prefix: str = None) -> 'IAMPolicyBuilder':
        """Allow S3 access to specific bucket and prefix"""
        resources = [f"arn:aws:s3:::{bucket_name}"]
        
        if prefix:
            resources.append(f"arn:aws:s3:::{bucket_name}/{prefix}/*")
        else:
            resources.append(f"arn:aws:s3:::{bucket_name}/*")
        
        return self.add_statement(
            effect="Allow",
            actions=[
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            resources=resources,
            sid="AllowS3Access"
        )
    
    def allow_lambda_execution(self, function_name: str) -> 'IAMPolicyBuilder':
        """Allow Lambda execution permissions"""
        return self.add_statement(
            effect="Allow",
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            resources=[f"arn:aws:logs:*:*:log-group:/aws/lambda/{function_name}:*"],
            sid="AllowLambdaLogging"
        )
    
    def deny_without_mfa(self, actions: List[str]) -> 'IAMPolicyBuilder':
        """Deny actions without MFA"""
        return self.add_statement(
            effect="Deny",
            actions=actions,
            resources=["*"],
            conditions={
                "Bool": {
                    "aws:MultiFactorAuthPresent": "false"
                }
            },
            sid="DenyWithoutMFA"
        )
    
    def build(self) -> Dict[str, Any]:
        """Build and return the policy"""
        return self.policy
    
    def to_json(self) -> str:
        """Convert policy to JSON string"""
        return json.dumps(self.policy, indent=2)

# Usage Example
if __name__ == "__main__":
    # Create a policy for a web application
    policy_builder = IAMPolicyBuilder()
    
    policy = (policy_builder
              .allow_s3_access("my-app-bucket", "uploads")
              .allow_lambda_execution("my-app-processor")
              .deny_without_mfa([
                  "iam:CreateUser",
                  "iam:DeleteUser",
                  "ec2:TerminateInstances"
              ])
              .build())
    
    print(json.dumps(policy, indent=2))
```


### Q11: How do you implement AWS WAF for web application security?
**Difficulty: Medium**

**Answer:**
AWS WAF protects web applications from common web exploits and bots that may affect availability, compromise security, or consume excessive resources.

```yaml
# AWS WAF Configuration
WebACL:
  Type: AWS::WAFv2::WebACL
  Properties:
    Name: !Sub '${Environment}-web-acl'
    Scope: REGIONAL  # Use CLOUDFRONT for CloudFront distributions
    DefaultAction:
      Allow: {}
    Rules:
      # Rate limiting rule
      - Name: RateLimitRule
        Priority: 1
        Statement:
          RateBasedStatement:
            Limit: 2000
            AggregateKeyType: IP
        Action:
          Block: {}
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: RateLimitRule
      
      # AWS Managed Rules - Core Rule Set
      - Name: AWSManagedRulesCommonRuleSet
        Priority: 2
        OverrideAction:
          None: {}
        Statement:
          ManagedRuleGroupStatement:
            VendorName: AWS
            Name: AWSManagedRulesCommonRuleSet
            ExcludedRules:
              - Name: SizeRestrictions_BODY
              - Name: GenericRFI_BODY
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: CommonRuleSetMetric
      
      # AWS Managed Rules - Known Bad Inputs
      - Name: AWSManagedRulesKnownBadInputsRuleSet
        Priority: 3
        OverrideAction:
          None: {}
        Statement:
          ManagedRuleGroupStatement:
            VendorName: AWS
            Name: AWSManagedRulesKnownBadInputsRuleSet
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: KnownBadInputsMetric
      
      # Custom IP whitelist rule
      - Name: IPWhitelistRule
        Priority: 4
        Statement:
          IPSetReferenceStatement:
            Arn: !GetAtt IPWhitelist.Arn
        Action:
          Allow: {}
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: IPWhitelistMetric
      
      # Geographic restriction
      - Name: GeoBlockRule
        Priority: 5
        Statement:
          GeoMatchStatement:
            CountryCodes:
              - CN
              - RU
              - KP
        Action:
          Block: {}
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: GeoBlockMetric
    
    VisibilityConfig:
      SampledRequestsEnabled: true
      CloudWatchMetricsEnabled: true
      MetricName: !Sub '${Environment}WebACL'

# IP Set for whitelisting
IPWhitelist:
  Type: AWS::WAFv2::IPSet
  Properties:
    Name: !Sub '${Environment}-ip-whitelist'
    Scope: REGIONAL
    IPAddressVersion: IPV4
    Addresses:
      - 203.0.113.0/24
      - 198.51.100.0/24
      - 192.0.2.44/32

# Associate WAF with Application Load Balancer
WebACLAssociation:
  Type: AWS::WAFv2::WebACLAssociation
  Properties:
    ResourceArn: !Ref ApplicationLoadBalancer
    WebACLArn: !GetAtt WebACL.Arn
```

---

## Serverless and Containers


### Q12: How do you build a serverless application with Lambda, API Gateway, and DynamoDB?
**Difficulty: Hard**

**Answer:**
A serverless application eliminates server management while providing automatic scaling and pay-per-use pricing.


### Q13: How do you implement ECS with Fargate for containerized applications?
**Difficulty: Medium**

**Answer:**
ECS with Fargate provides serverless container hosting without managing EC2 instances.

```yaml
# ECS Cluster with Fargate
ECSCluster:
  Type: AWS::ECS::Cluster
  Properties:
    ClusterName: !Sub '${Environment}-cluster'
    CapacityProviders:
      - FARGATE
      - FARGATE_SPOT
    DefaultCapacityProviderStrategy:
      - CapacityProvider: FARGATE
        Weight: 1
      - CapacityProvider: FARGATE_SPOT
        Weight: 4
    ClusterSettings:
      - Name: containerInsights
        Value: enabled

# Task Definition
TaskDefinition:
  Type: AWS::ECS::TaskDefinition
  Properties:
    Family: !Sub '${Environment}-app'
    NetworkMode: awsvpc
    RequiresCompatibilities:
      - FARGATE
    Cpu: 512
    Memory: 1024
    ExecutionRoleArn: !Ref TaskExecutionRole
    TaskRoleArn: !Ref TaskRole
    ContainerDefinitions:
      - Name: app
        Image: !Sub '${AWS::AccountId}.dkr.ecr.${AWS::Region}.amazonaws.com/${ECRRepository}:latest'
        Essential: true
        PortMappings:
          - ContainerPort: 3000
            Protocol: tcp
        Environment:
          - Name: NODE_ENV
            Value: !Ref Environment
          - Name: DATABASE_URL
            Value: !Sub 'postgresql://${DBUsername}:${DBPassword}@${RDSInstance.Endpoint.Address}:5432/${DBName}'
        Secrets:
          - Name: JWT_SECRET
            ValueFrom: !Ref JWTSecret
          - Name: API_KEY
            ValueFrom: !Ref APIKeySecret
        LogConfiguration:
          LogDriver: awslogs
          Options:
            awslogs-group: !Ref LogGroup
            awslogs-region: !Ref AWS::Region
            awslogs-stream-prefix: ecs
        HealthCheck:
          Command:
            - CMD-SHELL
            - curl -f http://localhost:3000/health || exit 1
          Interval: 30
          Timeout: 5
          Retries: 3
          StartPeriod: 60

# ECS Service
ECSService:
  Type: AWS::ECS::Service
  DependsOn: LoadBalancerListener
  Properties:
    ServiceName: !Sub '${Environment}-app-service'
    Cluster: !Ref ECSCluster
    TaskDefinition: !Ref TaskDefinition
    DesiredCount: 2
    LaunchType: FARGATE
    PlatformVersion: LATEST
    NetworkConfiguration:
      AwsvpcConfiguration:
        SecurityGroups:
          - !Ref ECSSecurityGroup
        Subnets:
          - !Ref PrivateSubnet1
          - !Ref PrivateSubnet2
        AssignPublicIp: DISABLED
    LoadBalancers:
      - ContainerName: app
        ContainerPort: 3000
        TargetGroupArn: !Ref TargetGroup
    ServiceRegistries:
      - RegistryArn: !GetAtt ServiceDiscovery.Arn
    DeploymentConfiguration:
      MaximumPercent: 200
      MinimumHealthyPercent: 50
      DeploymentCircuitBreaker:
        Enable: true
        Rollback: true
    EnableExecuteCommand: true

# Auto Scaling
ServiceScalingTarget:
  Type: AWS::ApplicationAutoScaling::ScalableTarget
  Properties:
    MaxCapacity: 10
    MinCapacity: 2
    ResourceId: !Sub 'service/${ECSCluster}/${ECSService.Name}'
    RoleARN: !Sub 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService'
    ScalableDimension: ecs:service:DesiredCount
    ServiceNamespace: ecs

ServiceScalingPolicy:
  Type: AWS::ApplicationAutoScaling::ScalingPolicy
  Properties:
    PolicyName: !Sub '${Environment}-cpu-scaling'
    PolicyType: TargetTrackingScaling
    ScalingTargetId: !Ref ServiceScalingTarget
    TargetTrackingScalingPolicyConfiguration:
      PredefinedMetricSpecification:
        PredefinedMetricType: ECSServiceAverageCPUUtilization
      TargetValue: 70.0
      ScaleOutCooldown: 300
      ScaleInCooldown: 300
```

---

## DevOps and CI/CD


### Q14: How do you implement CI/CD pipeline using CodePipeline, CodeBuild, and CodeDeploy?
**Difficulty: Hard**

**Answer:**
AWS CodePipeline orchestrates the entire CI/CD workflow from source code to deployment.

```yaml
# CodeCommit Repository
CodeRepository:
  Type: AWS::CodeCommit::Repository
  Properties:
    RepositoryName: !Sub '${Environment}-app-repo'
    RepositoryDescription: Application source code repository
    Code:
      BranchName: main
      S3:
        Bucket: !Ref SourceCodeBucket
        Key: source-code.zip

# S3 Bucket for Artifacts
ArtifactsBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: !Sub '${Environment}-pipeline-artifacts-${AWS::AccountId}'
    VersioningConfiguration:
      Status: Enabled
    BucketEncryption:
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: AES256
    PublicAccessBlockConfiguration:
      BlockPublicAcls: true
      BlockPublicPolicy: true
      IgnorePublicAcls: true
      RestrictPublicBuckets: true

# CodeBuild Project
CodeBuildProject:
  Type: AWS::CodeBuild::Project
  Properties:
    Name: !Sub '${Environment}-build-project'
    ServiceRole: !GetAtt CodeBuildRole.Arn
    Artifacts:
      Type: CODEPIPELINE
    Environment:
      Type: LINUX_CONTAINER
      ComputeType: BUILD_GENERAL1_MEDIUM
      Image: aws/codebuild/amazonlinux2-x86_64-standard:3.0
      PrivilegedMode: true
      EnvironmentVariables:
        - Name: AWS_DEFAULT_REGION
          Value: !Ref AWS::Region
        - Name: AWS_ACCOUNT_ID
          Value: !Ref AWS::AccountId
        - Name: IMAGE_REPO_NAME
          Value: !Ref ECRRepository
        - Name: IMAGE_TAG
          Value: latest
        - Name: ENVIRONMENT
          Value: !Ref Environment
    Source:
      Type: CODEPIPELINE
      BuildSpec: |
        version: 0.2
        phases:
          pre_build:
            commands:
              - echo Logging in to Amazon ECR...
              - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
              - REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME
              - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
              - IMAGE_TAG=${COMMIT_HASH:=latest}
          build:
            commands:
              - echo Build started on `date`
              - echo Building the Docker image...
              - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
              - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $REPOSITORY_URI:$IMAGE_TAG
              - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $REPOSITORY_URI:latest
              - echo Running tests...
              - npm test
              - echo Running security scan...
              - npm audit
          post_build:
            commands:
              - echo Build completed on `date`
              - echo Pushing the Docker images...
              - docker push $REPOSITORY_URI:$IMAGE_TAG
              - docker push $REPOSITORY_URI:latest
              - echo Writing image definitions file...
              - printf '[{"name":"app","imageUri":"%s"}]' $REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json
        artifacts:
          files:
            - imagedefinitions.json
            - appspec.yml
            - taskdef.json

# CodeDeploy Application
CodeDeployApplication:
  Type: AWS::CodeDeploy::Application
  Properties:
    ApplicationName: !Sub '${Environment}-app'
    ComputePlatform: ECS

CodeDeployDeploymentGroup:
  Type: AWS::CodeDeploy::DeploymentGroup
  Properties:
    ApplicationName: !Ref CodeDeployApplication
    DeploymentGroupName: !Sub '${Environment}-deployment-group'
    ServiceRoleArn: !GetAtt CodeDeployRole.Arn
    DeploymentConfigName: CodeDeployDefault.ECSAllAtOnceBlueGreen
    BlueGreenDeploymentConfiguration:
      TerminateBlueInstancesOnDeploymentSuccess:
        Action: TERMINATE
        TerminationWaitTimeInMinutes: 5
      DeploymentReadyOption:
        ActionOnTimeout: CONTINUE_DEPLOYMENT
      GreenFleetProvisioningOption:
        Action: COPY_AUTO_SCALING_GROUP
    LoadBalancerInfo:
      TargetGroupInfoList:
        - Name: !GetAtt TargetGroup.TargetGroupName
    ECSServices:
      - ServiceName: !GetAtt ECSService.Name
        ClusterName: !Ref ECSCluster

# CodePipeline
CodePipeline:
  Type: AWS::CodePipeline::Pipeline
  Properties:
    Name: !Sub '${Environment}-pipeline'
    RoleArn: !GetAtt CodePipelineRole.Arn
    ArtifactStore:
      Type: S3
      Location: !Ref ArtifactsBucket
      EncryptionKey:
        Id: !GetAtt PipelineKMSKey.Arn
        Type: KMS
    Stages:
      - Name: Source
        Actions:
          - Name: SourceAction
            ActionTypeId:
              Category: Source
              Owner: AWS
              Provider: CodeCommit
              Version: 1
            Configuration:
              RepositoryName: !GetAtt CodeRepository.Name
              BranchName: main
              PollForSourceChanges: false
            OutputArtifacts:
              - Name: SourceOutput
      
      - Name: Build
        Actions:
          - Name: BuildAction
            ActionTypeId:
              Category: Build
              Owner: AWS
              Provider: CodeBuild
              Version: 1
            Configuration:
              ProjectName: !Ref CodeBuildProject
            InputArtifacts:
              - Name: SourceOutput
            OutputArtifacts:
              - Name: BuildOutput
      
      - Name: Deploy
        Actions:
          - Name: DeployAction
            ActionTypeId:
              Category: Deploy
              Owner: AWS
              Provider: CodeDeployToECS
              Version: 1
            Configuration:
              ApplicationName: !Ref CodeDeployApplication
              DeploymentGroupName: !Ref CodeDeployDeploymentGroup
              TaskDefinitionTemplateArtifact: BuildOutput
              TaskDefinitionTemplatePath: taskdef.json
              AppSpecTemplateArtifact: BuildOutput
              AppSpecTemplatePath: appspec.yml
              Image1ArtifactName: BuildOutput
              Image1ContainerName: IMAGE1_NAME
            InputArtifacts:
              - Name: BuildOutput
            Region: !Ref AWS::Region
```

```python
# Pipeline Monitoring and Notifications
import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    """Handle CodePipeline state changes"""
    
    # Parse the event
    detail = event['detail']
    pipeline_name = detail['pipeline']
    execution_id = detail['execution-id']
    state = detail['state']
    
    # Initialize clients
    codepipeline = boto3.client('codepipeline')
    sns = boto3.client('sns')
    
    try:
        # Get pipeline execution details
        response = codepipeline.get_pipeline_execution(
            pipelineName=pipeline_name,
            pipelineExecutionId=execution_id
        )
        
        execution_details = response['pipelineExecution']
        
        # Prepare notification message
        message = {
            'pipeline': pipeline_name,
            'execution_id': execution_id,
            'state': state,
            'timestamp': datetime.utcnow().isoformat(),
            'trigger': execution_details.get('trigger', {}),
            'artifacts': execution_details.get('artifactRevisions', [])
        }
        
        # Determine notification topic based on state
        if state == 'SUCCEEDED':
            topic_arn = os.environ['SUCCESS_TOPIC_ARN']
            subject = f"✅ Pipeline {pipeline_name} succeeded"
        elif state == 'FAILED':
            topic_arn = os.environ['FAILURE_TOPIC_ARN']
            subject = f"❌ Pipeline {pipeline_name} failed"
            
            # Get failure details
            stages_response = codepipeline.get_pipeline_execution(
                pipelineName=pipeline_name,
                pipelineExecutionId=execution_id
            )
            
            message['failure_details'] = get_failure_details(
                codepipeline, pipeline_name, execution_id
            )
        else:
            topic_arn = os.environ['STATUS_TOPIC_ARN']
            subject = f"🔄 Pipeline {pipeline_name} is {state.lower()}"
        
        # Send notification
        sns.publish(
            TopicArn=topic_arn,
            Subject=subject,
            Message=json.dumps(message, indent=2)
        )
        
        # Log metrics to CloudWatch
        cloudwatch = boto3.client('cloudwatch')
        cloudwatch.put_metric_data(
            Namespace='CodePipeline/Executions',
            MetricData=[
                {
                    'MetricName': 'ExecutionState',
                    'Dimensions': [
                        {
                            'Name': 'PipelineName',
                            'Value': pipeline_name
                        },
                        {
                            'Name': 'State',
                            'Value': state
                        }
                    ],
                    'Value': 1,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                }
            ]
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Notification sent successfully')
        }
        
    except Exception as e:
        print(f"Error processing pipeline event: {str(e)}")
        raise e

def get_failure_details(codepipeline, pipeline_name, execution_id):
    """Get detailed failure information"""
    try:
        # Get action executions
        response = codepipeline.list_action_executions(
            pipelineName=pipeline_name,
            filter={
                'pipelineExecutionId': execution_id
            }
        )
        
        failed_actions = []
        for action in response['actionExecutionDetails']:
            if action['status'] == 'Failed':
                failed_actions.append({
                    'actionName': action['actionName'],
                    'stageName': action['stageName'],
                    'errorCode': action.get('output', {}).get('executionResult', {}).get('errorCode'),
                    'errorMessage': action.get('output', {}).get('executionResult', {}).get('errorMessage')
                })
        
        return failed_actions
        
    except Exception as e:
        print(f"Error getting failure details: {str(e)}")
        return []
```


### Q15: How do you implement Infrastructure as Code using CloudFormation and CDK?
**Difficulty: Hard**

**Answer:**
Infrastructure as Code enables version control, repeatability, and automation of infrastructure provisioning.

```python
# AWS CDK Example (Python)
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_rds as rds,
    aws_elasticloadbalancingv2 as elbv2,
    aws_route53 as route53,
    aws_certificatemanager as acm,
    aws_logs as logs,
    aws_iam as iam,
    Duration,
    RemovalPolicy
)
from constructs import Construct

class WebApplicationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # VPC with public and private subnets
        self.vpc = ec2.Vpc(
            self, "VPC",
            max_azs=3,
            cidr="10.0.0.0/16",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="Private",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name="Database",
                    cidr_mask=24
                )
            ],
            nat_gateways=2,
            enable_dns_hostnames=True,
            enable_dns_support=True
        )
        
        # Security Groups
        self.alb_security_group = ec2.SecurityGroup(
            self, "ALBSecurityGroup",
            vpc=self.vpc,
            description="Security group for Application Load Balancer",
            allow_all_outbound=True
        )
        
        self.alb_security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP traffic"
        )
        
        self.alb_security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow HTTPS traffic"
        )
        
        self.ecs_security_group = ec2.SecurityGroup(
            self, "ECSSecurityGroup",
            vpc=self.vpc,
            description="Security group for ECS tasks"
        )
        
        self.ecs_security_group.add_ingress_rule(
            self.alb_security_group,
            ec2.Port.tcp(3000),
            "Allow traffic from ALB"
        )
        
        self.db_security_group = ec2.SecurityGroup(
            self, "DatabaseSecurityGroup",
            vpc=self.vpc,
            description="Security group for RDS database"
        )
        
        self.db_security_group.add_ingress_rule(
            self.ecs_security_group,
            ec2.Port.tcp(5432),
            "Allow database access from ECS"
        )
        
        # RDS Database
        self.database = rds.DatabaseInstance(
            self, "Database",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_13_7
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.MICRO
            ),
            vpc=self.vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_groups=[self.db_security_group],
            database_name="appdb",
            credentials=rds.Credentials.from_generated_secret(
                "dbadmin",
                secret_name="rds-credentials"
            ),
            backup_retention=Duration.days(7),
            deletion_protection=True,
            delete_automated_backups=False,
            storage_encrypted=True,
            monitoring_interval=Duration.seconds(60),
            enable_performance_insights=True,
            cloudwatch_logs_exports=["postgresql"]
        )
        
        # ECS Cluster
        self.cluster = ecs.Cluster(
            self, "Cluster",
            vpc=self.vpc,
            container_insights=True
        )
        
        # Task Definition
        self.task_definition = ecs.FargateTaskDefinition(
            self, "TaskDefinition",
            memory_limit_mib=1024,
            cpu=512
        )
        
        # Container Definition
        self.container = self.task_definition.add_container(
            "app",
            image=ecs.ContainerImage.from_registry("nginx:latest"),
            memory_limit_mib=1024,
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="ecs",
                log_group=logs.LogGroup(
                    self, "LogGroup",
                    log_group_name=f"/ecs/{construct_id}",
                    retention=logs.RetentionDays.ONE_WEEK,
                    removal_policy=RemovalPolicy.DESTROY
                )
            ),
            environment={
                "NODE_ENV": "production",
                "DATABASE_HOST": self.database.instance_endpoint.hostname
            },
            secrets={
                "DATABASE_PASSWORD": ecs.Secret.from_secrets_manager(
                    self.database.secret,
                    "password"
                )
            },
            health_check=ecs.HealthCheck(
                command=["CMD-SHELL", "curl -f http://localhost:3000/health || exit 1"],
                interval=Duration.seconds(30),
                timeout=Duration.seconds(5),
                retries=3,
                start_period=Duration.seconds(60)
            )
        )
        
        self.container.add_port_mappings(
            ecs.PortMapping(
                container_port=3000,
                protocol=ecs.Protocol.TCP
            )
        )
        
        # Application Load Balancer
        self.load_balancer = elbv2.ApplicationLoadBalancer(
            self, "LoadBalancer",
            vpc=self.vpc,
            internet_facing=True,
            security_group=self.alb_security_group
        )
        
        # ECS Service with Load Balancer
        self.service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "Service",
            cluster=self.cluster,
            task_definition=self.task_definition,
            public_load_balancer=True,
            listener_port=80,
            desired_count=2,
            platform_version=ecs.FargatePlatformVersion.LATEST,
            assign_public_ip=False,
            security_groups=[self.ecs_security_group]
        )
        
        # Auto Scaling
        scaling = self.service.service.auto_scale_task_count(
            max_capacity=10,
            min_capacity=2
        )
        
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=70,
            scale_in_cooldown=Duration.seconds(300),
            scale_out_cooldown=Duration.seconds(300)
        )
        
        scaling.scale_on_memory_utilization(
            "MemoryScaling",
            target_utilization_percent=80
        )
        
        # CloudWatch Alarms
        self.service.service.metric_cpu_utilization().create_alarm(
            self, "HighCpuAlarm",
            threshold=80,
            evaluation_periods=2,
            alarm_description="High CPU utilization"
        )
        
        self.service.service.metric_memory_utilization().create_alarm(
            self, "HighMemoryAlarm",
            threshold=85,
            evaluation_periods=2,
            alarm_description="High memory utilization"
        )
        
        # Grant database access to ECS task
        self.database.secret.grant_read(self.task_definition.task_role)
        
        # Output important values
        self.load_balancer_dns = self.service.load_balancer.load_balancer_dns_name
        self.database_endpoint = self.database.instance_endpoint.hostname

# CDK App
from aws_cdk import App, Environment

app = App()

# Development environment
dev_stack = WebApplicationStack(
    app, "WebApp-Dev",
    env=Environment(
        account="123456789012",
        region="us-east-1"
    )
)

# Production environment
prod_stack = WebApplicationStack(
    app, "WebApp-Prod",
    env=Environment(
        account="123456789012",
        region="us-east-1"
    )
)

app.synth()
```

---

## Monitoring and Cost Optimization


### Q16: How do you implement comprehensive monitoring with CloudWatch, X-Ray, and AWS Config?
**Difficulty: Medium**

**Answer:**
Comprehensive monitoring provides visibility into application performance, infrastructure health, and compliance.

```yaml
# CloudWatch Dashboard
CloudWatchDashboard:
  Type: AWS::CloudWatch::Dashboard
  Properties:
    DashboardName: !Sub '${Environment}-application-dashboard'
    DashboardBody: !Sub |
      {
        "widgets": [
          {
            "type": "metric",
            "x": 0,
            "y": 0,
            "width": 12,
            "height": 6,
            "properties": {
              "metrics": [
                [ "AWS/ECS", "CPUUtilization", "ServiceName", "${ECSService}", "ClusterName", "${ECSCluster}" ],
                [ ".", "MemoryUtilization", ".", ".", ".", "." ]
              ],
              "view": "timeSeries",
              "stacked": false,
              "region": "${AWS::Region}",
              "title": "ECS Service Metrics",
              "period": 300
            }
          },
          {
            "type": "metric",
            "x": 12,
            "y": 0,
            "width": 12,
            "height": 6,
            "properties": {
              "metrics": [
                [ "AWS/ApplicationELB", "RequestCount", "LoadBalancer", "${LoadBalancer}" ],
                [ ".", "TargetResponseTime", ".", "." ],
                [ ".", "HTTPCode_Target_2XX_Count", ".", "." ],
                [ ".", "HTTPCode_Target_4XX_Count", ".", "." ],
                [ ".", "HTTPCode_Target_5XX_Count", ".", "." ]
              ],
              "view": "timeSeries",
              "stacked": false,
              "region": "${AWS::Region}",
              "title": "Load Balancer Metrics",
              "period": 300
            }
          },
          {
            "type": "metric",
            "x": 0,
            "y": 6,
            "width": 24,
            "height": 6,
            "properties": {
              "metrics": [
                [ "AWS/RDS", "CPUUtilization", "DBInstanceIdentifier", "${RDSInstance}" ],
                [ ".", "DatabaseConnections", ".", "." ],
                [ ".", "FreeableMemory", ".", "." ],
                [ ".", "ReadLatency", ".", "." ],
                [ ".", "WriteLatency", ".", "." ]
              ],
              "view": "timeSeries",
              "stacked": false,
              "region": "${AWS::Region}",
              "title": "RDS Metrics",
              "period": 300
            }
          }
        ]
      }

# CloudWatch Alarms
HighCPUAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmName: !Sub '${Environment}-high-cpu'
    AlarmDescription: 'High CPU utilization'
    MetricName: CPUUtilization
    Namespace: AWS/ECS
    Statistic: Average
    Period: 300
    EvaluationPeriods: 2
    Threshold: 80
    ComparisonOperator: GreaterThanThreshold
    Dimensions:
      - Name: ServiceName
        Value: !Ref ECSService
      - Name: ClusterName
        Value: !Ref ECSCluster
    AlarmActions:
      - !Ref SNSTopicAlerts
      - !Ref ScaleUpPolicy

HighErrorRateAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmName: !Sub '${Environment}-high-error-rate'
    AlarmDescription: 'High error rate'
    MetricName: HTTPCode_Target_5XX_Count
    Namespace: AWS/ApplicationELB
    Statistic: Sum
    Period: 300
    EvaluationPeriods: 2
    Threshold: 10
    ComparisonOperator: GreaterThanThreshold
    TreatMissingData: notBreaching
    Dimensions:
      - Name: LoadBalancer
        Value: !GetAtt LoadBalancer.LoadBalancerFullName
    AlarmActions:
      - !Ref SNSTopicAlerts

# Custom Metrics
CustomMetricsLambda:
  Type: AWS::Lambda::Function
  Properties:
    FunctionName: !Sub '${Environment}-custom-metrics'
    Runtime: python3.9
    Handler: index.lambda_handler
    Role: !GetAtt CustomMetricsRole.Arn
    Code:
      ZipFile: |
        import boto3
        import json
        import requests
        from datetime import datetime
        
        def lambda_handler(event, context):
            cloudwatch = boto3.client('cloudwatch')
            
            try:
                # Application health check
                response = requests.get('http://internal-alb/health', timeout=5)
                health_status = 1 if response.status_code == 200 else 0
                
                # Business metrics
                active_users = get_active_users()
                transaction_count = get_transaction_count()
                
                # Send custom metrics
                cloudwatch.put_metric_data(
                    Namespace='Application/Health',
                    MetricData=[
                        {
                            'MetricName': 'HealthStatus',
                            'Value': health_status,
                            'Unit': 'Count',
                            'Timestamp': datetime.utcnow()
                        },
                        {
                            'MetricName': 'ActiveUsers',
                            'Value': active_users,
                            'Unit': 'Count',
                            'Timestamp': datetime.utcnow()
                        },
                        {
                            'MetricName': 'TransactionCount',
                            'Value': transaction_count,
                            'Unit': 'Count',
                            'Timestamp': datetime.utcnow()
                        }
                    ]
                )
                
                return {
                    'statusCode': 200,
                    'body': json.dumps('Metrics sent successfully')
                }
                
            except Exception as e:
                print(f"Error: {str(e)}")
                return {
                    'statusCode': 500,
                    'body': json.dumps(f'Error: {str(e)}')
                }
        
        def get_active_users():
            # Implement your logic to get active users
            return 100
        
        def get_transaction_count():
            # Implement your logic to get transaction count
            return 50

# X-Ray Tracing
XRayTracingConfig:
  Type: AWS::ECS::Service
  Properties:
    # ... other properties
    TaskDefinition: !Ref TaskDefinitionWithXRay

TaskDefinitionWithXRay:
  Type: AWS::ECS::TaskDefinition
  Properties:
    # ... other properties
    ContainerDefinitions:
      - Name: app
        # ... other properties
        Environment:
          - Name: _X_AMZN_TRACE_ID
            Value: !Ref AWS::NoValue
        DependsOn:
          - ContainerName: xray-daemon
            Condition: START
      
      - Name: xray-daemon
        Image: amazon/aws-xray-daemon:latest
        Essential: true
        PortMappings:
          - ContainerPort: 2000
            Protocol: udp
        LogConfiguration:
          LogDriver: awslogs
          Options:
            awslogs-group: !Ref XRayLogGroup
            awslogs-region: !Ref AWS::Region
            awslogs-stream-prefix: xray
```


### Q17: How do you implement cost optimization strategies in AWS?
**Difficulty: Medium**

**Answer:**
Cost optimization involves right-sizing resources, using appropriate pricing models, and implementing automated cost controls.

```python
# Cost Optimization Lambda Function
import boto3
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

def lambda_handler(event, context):
    """Main cost optimization function"""
    
    recommendations = []
    
    # EC2 Cost Optimization
    recommendations.extend(analyze_ec2_instances())
    
    # RDS Cost Optimization
    recommendations.extend(analyze_rds_instances())
    
    # S3 Cost Optimization
    recommendations.extend(analyze_s3_buckets())
    
    # EBS Cost Optimization
    recommendations.extend(analyze_ebs_volumes())
    
    # Lambda Cost Optimization
    recommendations.extend(analyze_lambda_functions())
    
    # Send recommendations
    send_cost_recommendations(recommendations)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Cost optimization analysis completed',
            'recommendations_count': len(recommendations)
        })
    }

def analyze_ec2_instances() -> List[Dict[str, Any]]:
    """Analyze EC2 instances for cost optimization"""
    ec2 = boto3.client('ec2')
    cloudwatch = boto3.client('cloudwatch')
    
    recommendations = []
    
    # Get all running instances
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            
            # Get CPU utilization for the last 7 days
            cpu_metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[
                    {'Name': 'InstanceId', 'Value': instance_id}
                ],
                StartTime=datetime.utcnow() - timedelta(days=7),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            
            if cpu_metrics['Datapoints']:
                avg_cpu = sum(dp['Average'] for dp in cpu_metrics['Datapoints']) / len(cpu_metrics['Datapoints'])
                
                # Recommend downsizing if CPU < 20%
                if avg_cpu < 20:
                    recommendations.append({
                        'type': 'EC2_DOWNSIZE',
                        'resource_id': instance_id,
                        'current_type': instance_type,
                        'recommended_action': 'Consider downsizing instance',
                        'avg_cpu_utilization': avg_cpu,
                        'potential_savings': calculate_ec2_savings(instance_type)
                    })
                
                # Recommend Spot instances for non-critical workloads
                if not has_tag(instance, 'Critical', 'true'):
                    recommendations.append({
                        'type': 'EC2_SPOT',
                        'resource_id': instance_id,
                        'current_type': instance_type,
                        'recommended_action': 'Consider using Spot instances',
                        'potential_savings': calculate_spot_savings(instance_type)
                    })
    
    return recommendations

def analyze_rds_instances() -> List[Dict[str, Any]]:
    """Analyze RDS instances for cost optimization"""
    rds = boto3.client('rds')
    cloudwatch = boto3.client('cloudwatch')
    
    recommendations = []
    
    # Get all RDS instances
    response = rds.describe_db_instances()
    
    for db_instance in response['DBInstances']:
        db_identifier = db_instance['DBInstanceIdentifier']
        db_class = db_instance['DBInstanceClass']
        
        # Get CPU utilization
        cpu_metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName='CPUUtilization',
            Dimensions=[
                {'Name': 'DBInstanceIdentifier', 'Value': db_identifier}
            ],
            StartTime=datetime.utcnow() - timedelta(days=7),
            EndTime=datetime.utcnow(),
            Period=3600,
            Statistics=['Average']
        )
        
        # Get connection count
        connection_metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName='DatabaseConnections',
            Dimensions=[
                {'Name': 'DBInstanceIdentifier', 'Value': db_identifier}
            ],
            StartTime=datetime.utcnow() - timedelta(days=7),
            EndTime=datetime.utcnow(),
            Period=3600,
            Statistics=['Average']
        )
        
        if cpu_metrics['Datapoints'] and connection_metrics['Datapoints']:
            avg_cpu = sum(dp['Average'] for dp in cpu_metrics['Datapoints']) / len(cpu_metrics['Datapoints'])
            avg_connections = sum(dp['Average'] for dp in connection_metrics['Datapoints']) / len(connection_metrics['Datapoints'])
            
            # Recommend downsizing if CPU < 30% and connections < 10
            if avg_cpu < 30 and avg_connections < 10:
                recommendations.append({
                    'type': 'RDS_DOWNSIZE',
                    'resource_id': db_identifier,
                    'current_class': db_class,
                    'recommended_action': 'Consider downsizing RDS instance',
                    'avg_cpu_utilization': avg_cpu,
                    'avg_connections': avg_connections,
                    'potential_savings': calculate_rds_savings(db_class)
                })
    
    return recommendations

def analyze_s3_buckets() -> List[Dict[str, Any]]:
    """Analyze S3 buckets for cost optimization"""
    s3 = boto3.client('s3')
    cloudwatch = boto3.client('cloudwatch')
    
    recommendations = []
    
    # Get all buckets
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        try:
            # Check lifecycle configuration
            try:
                s3.get_bucket_lifecycle_configuration(Bucket=bucket_name)
                has_lifecycle = True
            except s3.exceptions.NoSuchLifecycleConfiguration:
                has_lifecycle = False
            
            # Get storage metrics
            storage_metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/S3',
                MetricName='BucketSizeBytes',
                Dimensions=[
                    {'Name': 'BucketName', 'Value': bucket_name},
                    {'Name': 'StorageType', 'Value': 'StandardStorage'}
                ],
                StartTime=datetime.utcnow() - timedelta(days=1),
                EndTime=datetime.utcnow(),
                Period=86400,
                Statistics=['Average']
            )
            
            if storage_metrics['Datapoints'] and not has_lifecycle:
                storage_size = storage_metrics['Datapoints'][0]['Average']
                
                # Recommend lifecycle policy for buckets > 1GB
                if storage_size > 1024**3:  # 1GB
                    recommendations.append({
                        'type': 'S3_LIFECYCLE',
                        'resource_id': bucket_name,
                        'recommended_action': 'Implement S3 lifecycle policy',
                        'storage_size_gb': storage_size / (1024**3),
                        'potential_savings': calculate_s3_lifecycle_savings(storage_size)
                    })
        
        except Exception as e:
            print(f"Error analyzing bucket {bucket_name}: {str(e)}")
    
    return recommendations

def analyze_ebs_volumes() -> List[Dict[str, Any]]:
    """Analyze EBS volumes for cost optimization"""
    ec2 = boto3.client('ec2')
    cloudwatch = boto3.client('cloudwatch')
    
    recommendations = []
    
    # Get all EBS volumes
    response = ec2.describe_volumes()
    
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        volume_type = volume['VolumeType']
        volume_size = volume['Size']
        
        # Check if volume is attached
        if volume['State'] == 'available':
            recommendations.append({
                'type': 'EBS_UNATTACHED',
                'resource_id': volume_id,
                'recommended_action': 'Delete unattached EBS volume',
                'volume_size_gb': volume_size,
                'potential_savings': calculate_ebs_savings(volume_type, volume_size)
            })
        
        # Check IOPS utilization for gp2 volumes
        elif volume_type == 'gp2' and volume_size > 100:
            iops_metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EBS',
                MetricName='VolumeReadOps',
                Dimensions=[
                    {'Name': 'VolumeId', 'Value': volume_id}
                ],
                StartTime=datetime.utcnow() - timedelta(days=7),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Sum']
            )
            
            if iops_metrics['Datapoints']:
                total_iops = sum(dp['Sum'] for dp in iops_metrics['Datapoints'])
                avg_iops_per_hour = total_iops / len(iops_metrics['Datapoints'])
                
                # Recommend gp3 if IOPS usage is low
                if avg_iops_per_hour < 100:
                    recommendations.append({
                        'type': 'EBS_GP3_MIGRATION',
                        'resource_id': volume_id,
                        'current_type': volume_type,
                        'recommended_action': 'Migrate from gp2 to gp3',
                        'avg_iops': avg_iops_per_hour,
                        'potential_savings': calculate_gp3_savings(volume_size)
                    })
    
    return recommendations

def analyze_lambda_functions() -> List[Dict[str, Any]]:
    """Analyze Lambda functions for cost optimization"""
    lambda_client = boto3.client('lambda')
    cloudwatch = boto3.client('cloudwatch')
    
    recommendations = []
    
    # Get all Lambda functions
    response = lambda_client.list_functions()
    
    for function in response['Functions']:
        function_name = function['FunctionName']
        memory_size = function['MemorySize']
        
        # Get duration metrics
        duration_metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/Lambda',
            MetricName='Duration',
            Dimensions=[
                {'Name': 'FunctionName', 'Value': function_name}
            ],
            StartTime=datetime.utcnow() - timedelta(days=7),
            EndTime=datetime.utcnow(),
            Period=3600,
            Statistics=['Average']
        )
        
        if duration_metrics['Datapoints']:
            avg_duration = sum(dp['Average'] for dp in duration_metrics['Datapoints']) / len(duration_metrics['Datapoints'])
            
            # Recommend memory optimization
            if avg_duration < 1000 and memory_size > 512:  # < 1 second, > 512MB
                recommendations.append({
                    'type': 'LAMBDA_MEMORY_OPTIMIZATION',
                    'resource_id': function_name,
                    'current_memory': memory_size,
                    'recommended_action': 'Consider reducing memory allocation',
                    'avg_duration_ms': avg_duration,
                    'potential_savings': calculate_lambda_savings(memory_size, avg_duration)
                })
    
    return recommendations

def send_cost_recommendations(recommendations: List[Dict[str, Any]]):
    """Send cost optimization recommendations"""
    sns = boto3.client('sns')
    
    if not recommendations:
        return
    
    # Group recommendations by type
    grouped_recommendations = {}
    total_potential_savings = 0
    
    for rec in recommendations:
        rec_type = rec['type']
        if rec_type not in grouped_recommendations:
            grouped_recommendations[rec_type] = []
        grouped_recommendations[rec_type].append(rec)
        
        if 'potential_savings' in rec:
            total_potential_savings += rec['potential_savings']
    
    # Create summary message
    message = f"""Cost Optimization Report - {datetime.utcnow().strftime('%Y-%m-%d')}

Total Potential Monthly Savings: ${total_potential_savings:.2f}

Recommendations by Category:
"""
    
    for rec_type, recs in grouped_recommendations.items():
        message += f"\n{rec_type.replace('_', ' ').title()}: {len(recs)} recommendations\n"
        for rec in recs[:5]:  # Show first 5 recommendations
            message += f"  - {rec['resource_id']}: {rec['recommended_action']}\n"
        if len(recs) > 5:
            message += f"  ... and {len(recs) - 5} more\n"
    
    # Send notification
    sns.publish(
        TopicArn=os.environ['COST_OPTIMIZATION_TOPIC'],
        Subject='AWS Cost Optimization Recommendations',
        Message=message
    )

# Helper functions for calculating savings
def calculate_ec2_savings(instance_type: str) -> float:
    """Calculate potential EC2 savings"""
    # Simplified calculation - in reality, use AWS Pricing API
    pricing_map = {
        't3.micro': 8.47,
        't3.small': 16.94,
        't3.medium': 33.89,
        't3.large': 67.78,
        'm5.large': 87.60,
        'm5.xlarge': 175.20
    }
    return pricing_map.get(instance_type, 50) * 0.3  # 30% savings estimate

def calculate_spot_savings(instance_type: str) -> float:
    """Calculate Spot instance savings"""
    # Spot instances typically save 70-90%
    return calculate_ec2_savings(instance_type) * 0.8

def calculate_rds_savings(db_class: str) -> float:
    """Calculate RDS savings"""
    # Simplified RDS pricing
    return 100.0  # Placeholder

def calculate_s3_lifecycle_savings(storage_size: float) -> float:
    """Calculate S3 lifecycle savings"""
    # Assume 50% of data can be moved to IA after 30 days
    monthly_cost = (storage_size / (1024**3)) * 0.023  # $0.023 per GB
    return monthly_cost * 0.5 * 0.6  # 50% data, 60% savings

def calculate_ebs_savings(volume_type: str, volume_size: int) -> float:
    """Calculate EBS savings"""
    if volume_type == 'gp2':
        return volume_size * 0.10  # $0.10 per GB per month
    return volume_size * 0.08

def calculate_gp3_savings(volume_size: int) -> float:
    """Calculate gp3 migration savings"""
    return volume_size * 0.02  # $0.02 per GB savings

def calculate_lambda_savings(memory_size: int, avg_duration: float) -> float:
    """Calculate Lambda memory optimization savings"""
    return (memory_size - 256) * 0.0000166667 * (avg_duration / 1000) * 30 * 24 * 60  # Simplified

def has_tag(instance: Dict, key: str, value: str) -> bool:
    """Check if instance has specific tag"""
    tags = instance.get('Tags', [])
    for tag in tags:
        if tag['Key'] == key and tag['Value'] == value:
            return True
    return False
 ```


### Q18: How do you implement disaster recovery and backup strategies in AWS?
**Difficulty: Hard**

**Answer:**
Disaster recovery ensures business continuity through automated backups, cross-region replication, and failover mechanisms.

```yaml
# Multi-Region Disaster Recovery Setup
PrimaryRegionStack:
  Type: AWS::CloudFormation::Stack
  Properties:
    TemplateURL: !Sub 'https://${TemplatesBucket}.s3.amazonaws.com/primary-region.yaml'
    Parameters:
      Environment: !Ref Environment
      IsSecondaryRegion: false

SecondaryRegionStack:
  Type: AWS::CloudFormation::Stack
  Condition: CreateSecondaryRegion
  Properties:
    TemplateURL: !Sub 'https://${TemplatesBucket}.s3.amazonaws.com/secondary-region.yaml'
    Parameters:
      Environment: !Ref Environment
      IsSecondaryRegion: true
      PrimaryRegion: !Ref AWS::Region

# RDS with Cross-Region Backup
PrimaryDatabase:
  Type: AWS::RDS::DBInstance
  Properties:
    DBInstanceIdentifier: !Sub '${Environment}-primary-db'
    Engine: postgres
    EngineVersion: '13.7'
    DBInstanceClass: db.t3.medium
    AllocatedStorage: 100
    StorageType: gp2
    StorageEncrypted: true
    KmsKeyId: !Ref DatabaseKMSKey
    VPCSecurityGroups:
      - !Ref DatabaseSecurityGroup
    DBSubnetGroupName: !Ref DatabaseSubnetGroup
    BackupRetentionPeriod: 30
    PreferredBackupWindow: '03:00-04:00'
    PreferredMaintenanceWindow: 'sun:04:00-sun:05:00'
    DeletionProtection: true
    EnablePerformanceInsights: true
    MonitoringInterval: 60
    MonitoringRoleArn: !GetAtt RDSEnhancedMonitoringRole.Arn
    Tags:
      - Key: Environment
        Value: !Ref Environment
      - Key: BackupRequired
        Value: 'true'

# Cross-Region Read Replica
ReadReplica:
  Type: AWS::RDS::DBInstance
  Condition: CreateReadReplica
  Properties:
    DBInstanceIdentifier: !Sub '${Environment}-replica-db'
    SourceDBInstanceIdentifier: !Sub 'arn:aws:rds:${AWS::Region}:${AWS::AccountId}:db:${PrimaryDatabase}'
    DBInstanceClass: db.t3.medium
    PubliclyAccessible: false
    Tags:
      - Key: Environment
        Value: !Ref Environment
      - Key: Role
        Value: ReadReplica

# S3 Cross-Region Replication
PrimaryBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: !Sub '${Environment}-primary-data-${AWS::AccountId}'
    VersioningConfiguration:
      Status: Enabled
    ReplicationConfiguration:
      Role: !GetAtt S3ReplicationRole.Arn
      Rules:
        - Id: ReplicateToSecondaryRegion
          Status: Enabled
          Prefix: ''
          Destination:
            Bucket: !Sub 'arn:aws:s3:::${Environment}-secondary-data-${AWS::AccountId}'
            StorageClass: STANDARD_IA
            EncryptionConfiguration:
              ReplicaKmsKeyID: !Sub 'arn:aws:kms:${SecondaryRegion}:${AWS::AccountId}:key/${SecondaryRegionKMSKey}'
    NotificationConfiguration:
      CloudWatchConfigurations:
        - Event: s3:ObjectCreated:*
          CloudWatchConfiguration:
            LogGroupName: !Ref S3AccessLogGroup
    BucketEncryption:
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: aws:kms
            KMSMasterKeyID: !Ref S3KMSKey

SecondaryBucket:
  Type: AWS::S3::Bucket
  Condition: CreateSecondaryRegion
  Properties:
    BucketName: !Sub '${Environment}-secondary-data-${AWS::AccountId}'
    VersioningConfiguration:
      Status: Enabled
    BucketEncryption:
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: aws:kms
            KMSMasterKeyID: !Ref SecondaryRegionKMSKey

# Route 53 Health Checks and Failover
PrimaryHealthCheck:
  Type: AWS::Route53::HealthCheck
  Properties:
    Type: HTTPS
    ResourcePath: /health
    FullyQualifiedDomainName: !GetAtt PrimaryLoadBalancer.DNSName
    Port: 443
    RequestInterval: 30
    FailureThreshold: 3
    Tags:
      - Key: Name
        Value: !Sub '${Environment}-primary-health-check'

DNSRecord:
  Type: AWS::Route53::RecordSet
  Properties:
    HostedZoneId: !Ref HostedZone
    Name: !Sub '${Environment}.${DomainName}'
    Type: A
    SetIdentifier: Primary
    Failover: PRIMARY
    TTL: 60
    ResourceRecords:
      - !GetAtt PrimaryLoadBalancer.DNSName
    HealthCheckId: !Ref PrimaryHealthCheck

SecondaryDNSRecord:
  Type: AWS::Route53::RecordSet
  Condition: CreateSecondaryRegion
  Properties:
    HostedZoneId: !Ref HostedZone
    Name: !Sub '${Environment}.${DomainName}'
    Type: A
    SetIdentifier: Secondary
    Failover: SECONDARY
    TTL: 60
    ResourceRecords:
      - !GetAtt SecondaryLoadBalancer.DNSName
```

```python
# Automated Backup and Recovery Lambda
import boto3
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any

def lambda_handler(event, context):
    """Automated backup and recovery orchestration"""
    
    action = event.get('action', 'backup')
    
    if action == 'backup':
        return perform_backup(event)
    elif action == 'restore':
        return perform_restore(event)
    elif action == 'failover':
        return perform_failover(event)
    else:
        raise ValueError(f"Unknown action: {action}")

def perform_backup(event: Dict[str, Any]) -> Dict[str, Any]:
    """Perform comprehensive backup"""
    
    results = {
        'timestamp': datetime.utcnow().isoformat(),
        'backups': []
    }
    
    # RDS Snapshots
    rds_results = backup_rds_instances()
    results['backups'].extend(rds_results)
    
    # EBS Snapshots
    ebs_results = backup_ebs_volumes()
    results['backups'].extend(ebs_results)
    
    # DynamoDB Backups
    dynamodb_results = backup_dynamodb_tables()
    results['backups'].extend(dynamodb_results)
    
    # S3 Sync to Glacier
    s3_results = archive_s3_data()
    results['backups'].extend(s3_results)
    
    # Send notification
    send_backup_notification(results)
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def backup_rds_instances() -> List[Dict[str, Any]]:
    """Create RDS snapshots"""
    rds = boto3.client('rds')
    results = []
    
    # Get all RDS instances
    response = rds.describe_db_instances()
    
    for db_instance in response['DBInstances']:
        db_identifier = db_instance['DBInstanceIdentifier']
        
        # Skip read replicas
        if 'ReadReplicaDBInstanceIdentifiers' in db_instance:
            continue
            
        snapshot_id = f"{db_identifier}-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
        
        try:
            snapshot_response = rds.create_db_snapshot(
                DBSnapshotIdentifier=snapshot_id,
                DBInstanceIdentifier=db_identifier,
                Tags=[
                    {'Key': 'CreatedBy', 'Value': 'AutomatedBackup'},
                    {'Key': 'CreatedAt', 'Value': datetime.utcnow().isoformat()},
                    {'Key': 'RetentionDays', 'Value': '30'}
                ]
            )
            
            results.append({
                'type': 'RDS_SNAPSHOT',
                'resource_id': db_identifier,
                'snapshot_id': snapshot_id,
                'status': 'INITIATED',
                'arn': snapshot_response['DBSnapshot']['DBSnapshotArn']
            })
            
        except Exception as e:
            results.append({
                'type': 'RDS_SNAPSHOT',
                'resource_id': db_identifier,
                'status': 'FAILED',
                'error': str(e)
            })
    
    return results

def backup_ebs_volumes() -> List[Dict[str, Any]]:
    """Create EBS snapshots"""
    ec2 = boto3.client('ec2')
    results = []
    
    # Get all EBS volumes
    response = ec2.describe_volumes(
        Filters=[
            {'Name': 'state', 'Values': ['in-use']}
        ]
    )
    
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        
        # Get instance information
        instance_id = None
        if volume['Attachments']:
            instance_id = volume['Attachments'][0]['InstanceId']
        
        description = f"Automated snapshot of {volume_id}"
        if instance_id:
            description += f" from instance {instance_id}"
        
        try:
            snapshot_response = ec2.create_snapshot(
                VolumeId=volume_id,
                Description=description,
                TagSpecifications=[
                    {
                        'ResourceType': 'snapshot',
                        'Tags': [
                            {'Key': 'Name', 'Value': f'{volume_id}-{datetime.utcnow().strftime("%Y%m%d-%H%M%S")}'},
                            {'Key': 'CreatedBy', 'Value': 'AutomatedBackup'},
                            {'Key': 'SourceVolumeId', 'Value': volume_id},
                            {'Key': 'CreatedAt', 'Value': datetime.utcnow().isoformat()}
                        ]
                    }
                ]
            )
            
            results.append({
                'type': 'EBS_SNAPSHOT',
                'resource_id': volume_id,
                'snapshot_id': snapshot_response['SnapshotId'],
                'status': 'INITIATED'
            })
            
        except Exception as e:
            results.append({
                'type': 'EBS_SNAPSHOT',
                'resource_id': volume_id,
                'status': 'FAILED',
                'error': str(e)
            })
    
    return results

def backup_dynamodb_tables() -> List[Dict[str, Any]]:
    """Create DynamoDB backups"""
    dynamodb = boto3.client('dynamodb')
    results = []
    
    # Get all tables
    response = dynamodb.list_tables()
    
    for table_name in response['TableNames']:
        backup_name = f"{table_name}-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
        
        try:
            backup_response = dynamodb.create_backup(
                TableName=table_name,
                BackupName=backup_name
            )
            
            results.append({
                'type': 'DYNAMODB_BACKUP',
                'resource_id': table_name,
                'backup_arn': backup_response['BackupDetails']['BackupArn'],
                'status': 'INITIATED'
            })
            
        except Exception as e:
            results.append({
                'type': 'DYNAMODB_BACKUP',
                'resource_id': table_name,
                'status': 'FAILED',
                'error': str(e)
            })
    
    return results

def archive_s3_data() -> List[Dict[str, Any]]:
    """Archive S3 data to Glacier"""
    s3 = boto3.client('s3')
    results = []
    
    # Get buckets with backup tag
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        try:
            # Check if bucket has backup tag
            tags_response = s3.get_bucket_tagging(Bucket=bucket_name)
            backup_required = False
            
            for tag in tags_response.get('TagSet', []):
                if tag['Key'] == 'BackupRequired' and tag['Value'] == 'true':
                    backup_required = True
                    break
            
            if not backup_required:
                continue
            
            # Apply lifecycle policy for archiving
            lifecycle_config = {
                'Rules': [
                    {
                        'ID': 'ArchiveOldObjects',
                        'Status': 'Enabled',
                        'Filter': {'Prefix': ''},
                        'Transitions': [
                            {
                                'Days': 30,
                                'StorageClass': 'STANDARD_IA'
                            },
                            {
                                'Days': 90,
                                'StorageClass': 'GLACIER'
                            },
                            {
                                'Days': 365,
                                'StorageClass': 'DEEP_ARCHIVE'
                            }
                        ]
                    }
                ]
            }
            
            s3.put_bucket_lifecycle_configuration(
                Bucket=bucket_name,
                LifecycleConfiguration=lifecycle_config
            )
            
            results.append({
                'type': 'S3_LIFECYCLE',
                'resource_id': bucket_name,
                'status': 'CONFIGURED'
            })
            
        except Exception as e:
            results.append({
                'type': 'S3_LIFECYCLE',
                'resource_id': bucket_name,
                'status': 'FAILED',
                'error': str(e)
            })
    
    return results

def perform_failover(event: Dict[str, Any]) -> Dict[str, Any]:
    """Perform automated failover to secondary region"""
    
    route53 = boto3.client('route53')
    rds = boto3.client('rds')
    
    results = {
        'timestamp': datetime.utcnow().isoformat(),
        'failover_actions': []
    }
    
    try:
        # Promote read replica to primary
        replica_identifier = event.get('replica_identifier')
        if replica_identifier:
            rds.promote_read_replica(
                DBInstanceIdentifier=replica_identifier
            )
            
            results['failover_actions'].append({
                'action': 'PROMOTE_READ_REPLICA',
                'resource_id': replica_identifier,
                'status': 'INITIATED'
            })
        
        # Update Route 53 records for failover
        hosted_zone_id = event.get('hosted_zone_id')
        secondary_endpoint = event.get('secondary_endpoint')
        
        if hosted_zone_id and secondary_endpoint:
            route53.change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch={
                    'Changes': [
                        {
                            'Action': 'UPSERT',
                            'ResourceRecordSet': {
                                'Name': event.get('domain_name'),
                                'Type': 'A',
                                'SetIdentifier': 'Failover',
                                'Failover': 'PRIMARY',
                                'TTL': 60,
                                'ResourceRecords': [
                                    {'Value': secondary_endpoint}
                                ]
                            }
                        }
                    ]
                }
            )
            
            results['failover_actions'].append({
                'action': 'UPDATE_DNS',
                'resource_id': hosted_zone_id,
                'status': 'COMPLETED'
            })
        
        # Send failover notification
        send_failover_notification(results)
        
    except Exception as e:
        results['failover_actions'].append({
            'action': 'FAILOVER',
            'status': 'FAILED',
            'error': str(e)
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def send_backup_notification(results: Dict[str, Any]):
    """Send backup completion notification"""
    sns = boto3.client('sns')
    
    successful_backups = [b for b in results['backups'] if b['status'] in ['INITIATED', 'COMPLETED', 'CONFIGURED']]
    failed_backups = [b for b in results['backups'] if b['status'] == 'FAILED']
    
    message = f"""Backup Report - {results['timestamp']}

Successful Backups: {len(successful_backups)}
Failed Backups: {len(failed_backups)}

Details:
"""
    
    for backup in results['backups']:
        status_emoji = "✅" if backup['status'] != 'FAILED' else "❌"
        message += f"{status_emoji} {backup['type']}: {backup['resource_id']} - {backup['status']}\n"
    
    sns.publish(
        TopicArn=os.environ['BACKUP_NOTIFICATION_TOPIC'],
        Subject=f"Backup Report - {len(failed_backups)} failures",
        Message=message
    )

def send_failover_notification(results: Dict[str, Any]):
    """Send failover notification"""
    sns = boto3.client('sns')
    
    message = f"""🚨 FAILOVER INITIATED - {results['timestamp']}

Failover actions performed:
"""
    
    for action in results['failover_actions']:
        status_emoji = "✅" if action['status'] != 'FAILED' else "❌"
        message += f"{status_emoji} {action['action']}: {action.get('resource_id', 'N/A')} - {action['status']}\n"
    
    sns.publish(
        TopicArn=os.environ['CRITICAL_ALERTS_TOPIC'],
        Subject='🚨 DISASTER RECOVERY FAILOVER INITIATED',
        Message=message
    )
```


### Q19: How do you implement advanced security with AWS WAF, GuardDuty, and Security Hub?
**Difficulty: Hard**

**Answer:**
Advanced security requires multiple layers of protection including web application firewalls, threat detection, and centralized security monitoring.

```yaml
# AWS WAF v2 Configuration
WebACL:
  Type: AWS::WAFv2::WebACL
  Properties:
    Name: !Sub '${Environment}-web-acl'
    Scope: REGIONAL
    DefaultAction:
      Allow: {}
    Rules:
      # AWS Managed Rules - Core Rule Set
      - Name: AWSManagedRulesCommonRuleSet
        Priority: 1
        OverrideAction:
          None: {}
        Statement:
          ManagedRuleGroupStatement:
            VendorName: AWS
            Name: AWSManagedRulesCommonRuleSet
            ExcludedRules:
              - Name: SizeRestrictions_BODY
              - Name: GenericRFI_BODY
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: CommonRuleSetMetric
      
      # AWS Managed Rules - Known Bad Inputs
      - Name: AWSManagedRulesKnownBadInputsRuleSet
        Priority: 2
        OverrideAction:
          None: {}
        Statement:
          ManagedRuleGroupStatement:
            VendorName: AWS
            Name: AWSManagedRulesKnownBadInputsRuleSet
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: KnownBadInputsMetric
      
      # Rate Limiting Rule
      - Name: RateLimitRule
        Priority: 3
        Action:
          Block: {}
        Statement:
          RateBasedStatement:
            Limit: 2000
            AggregateKeyType: IP
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: RateLimitMetric
      
      # Geo Blocking Rule
      - Name: GeoBlockRule
        Priority: 4
        Action:
          Block: {}
        Statement:
          GeoMatchStatement:
            CountryCodes:
              - CN
              - RU
              - KP
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: GeoBlockMetric
      
      # Custom SQL Injection Rule
      - Name: CustomSQLiRule
        Priority: 5
        Action:
          Block: {}
        Statement:
          SqliMatchStatement:
            FieldToMatch:
              AllQueryArguments: {}
            TextTransformations:
              - Priority: 0
                Type: URL_DECODE
              - Priority: 1
                Type: HTML_ENTITY_DECODE
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: SQLiMetric
      
      # IP Whitelist Rule
      - Name: IPWhitelistRule
        Priority: 6
        Action:
          Allow: {}
        Statement:
          IPSetReferenceStatement:
            Arn: !GetAtt TrustedIPSet.Arn
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: IPWhitelistMetric
    
    VisibilityConfig:
      SampledRequestsEnabled: true
      CloudWatchMetricsEnabled: true
      MetricName: !Sub '${Environment}WebACL'
    
    Tags:
      - Key: Environment
        Value: !Ref Environment
      - Key: Purpose
        Value: WebApplicationFirewall

# Trusted IP Set
TrustedIPSet:
  Type: AWS::WAFv2::IPSet
  Properties:
    Name: !Sub '${Environment}-trusted-ips'
    Scope: REGIONAL
    IPAddressVersion: IPV4
    Addresses:
      - 203.0.113.0/24  # Office IP range
      - 198.51.100.0/24  # VPN IP range
    Tags:
      - Key: Environment
        Value: !Ref Environment

# Associate WAF with Load Balancer
WebACLAssociation:
  Type: AWS::WAFv2::WebACLAssociation
  Properties:
    ResourceArn: !Ref LoadBalancer
    WebACLArn: !GetAtt WebACL.Arn

# GuardDuty Detector
GuardDutyDetector:
  Type: AWS::GuardDuty::Detector
  Properties:
    Enable: true
    FindingPublishingFrequency: FIFTEEN_MINUTES
    DataSources:
      S3Logs:
        Enable: true
      KubernetesConfiguration:
        AuditLogs:
          Enable: true
      MalwareProtection:
        ScanEc2InstanceWithFindings:
          EbsVolumes: true
    Tags:
      - Key: Environment
        Value: !Ref Environment

# GuardDuty Threat Intel Set
ThreatIntelSet:
  Type: AWS::GuardDuty::ThreatIntelSet
  Properties:
    Activate: true
    DetectorId: !Ref GuardDutyDetector
    Format: TXT
    Location: !Sub 's3://${ThreatIntelBucket}/threat-intel.txt'
    Name: !Sub '${Environment}-threat-intel'

# Security Hub
SecurityHub:
  Type: AWS::SecurityHub::Hub
  Properties:
    Tags:
      Environment: !Ref Environment

# Config Configuration Recorder
ConfigurationRecorder:
  Type: AWS::Config::ConfigurationRecorder
  Properties:
    Name: !Sub '${Environment}-config-recorder'
    RoleARN: !GetAtt ConfigRole.Arn
    RecordingGroup:
      AllSupported: true
      IncludeGlobalResourceTypes: true
      ResourceTypes: []

# Config Delivery Channel
DeliveryChannel:
  Type: AWS::Config::DeliveryChannel
  Properties:
    Name: !Sub '${Environment}-delivery-channel'
    S3BucketName: !Ref ConfigBucket
    S3KeyPrefix: config
    ConfigSnapshotDeliveryProperties:
      DeliveryFrequency: Daily

# Config Rules
S3BucketPublicAccessProhibited:
  Type: AWS::Config::ConfigRule
  DependsOn: ConfigurationRecorder
  Properties:
    ConfigRuleName: s3-bucket-public-access-prohibited
    Source:
      Owner: AWS
      SourceIdentifier: S3_BUCKET_PUBLIC_ACCESS_PROHIBITED

RootAccessKeyCheck:
  Type: AWS::Config::ConfigRule
  DependsOn: ConfigurationRecorder
  Properties:
    ConfigRuleName: root-access-key-check
    Source:
      Owner: AWS
      SourceIdentifier: ROOT_ACCESS_KEY_CHECK

EncryptedVolumes:
  Type: AWS::Config::ConfigRule
  DependsOn: ConfigurationRecorder
  Properties:
    ConfigRuleName: encrypted-volumes
    Source:
      Owner: AWS
      SourceIdentifier: ENCRYPTED_VOLUMES
```

```python
# Security Automation Lambda
import boto3
import json
from datetime import datetime
from typing import Dict, List, Any

def lambda_handler(event, context):
    """Handle security events and automate responses"""
    
    event_source = event.get('source')
    
    if event_source == 'aws.guardduty':
        return handle_guardduty_finding(event)
    elif event_source == 'aws.securityhub':
        return handle_security_hub_finding(event)
    elif event_source == 'aws.config':
        return handle_config_compliance(event)
    elif event_source == 'aws.wafv2':
        return handle_waf_event(event)
    else:
        print(f"Unknown event source: {event_source}")
        return {'statusCode': 200}

def handle_guardduty_finding(event: Dict[str, Any]) -> Dict[str, Any]:
    """Handle GuardDuty security findings"""
    
    detail = event['detail']
    finding_type = detail['type']
    severity = detail['severity']
    
    response_actions = []
    
    # High severity findings require immediate action
    if severity >= 7.0:
        response_actions.extend(handle_high_severity_finding(detail))
    
    # Specific finding type responses
    if 'Backdoor' in finding_type:
        response_actions.extend(handle_backdoor_finding(detail))
    elif 'CryptoCurrency' in finding_type:
        response_actions.extend(handle_crypto_mining(detail))
    elif 'Malware' in finding_type:
        response_actions.extend(handle_malware_finding(detail))
    elif 'UnauthorizedAPICall' in finding_type:
        response_actions.extend(handle_unauthorized_api_call(detail))
    
    # Send notification
    send_security_notification({
        'type': 'GuardDuty Finding',
        'finding_type': finding_type,
        'severity': severity,
        'actions_taken': response_actions,
        'details': detail
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'actions_taken': len(response_actions),
            'response_actions': response_actions
        })
    }

def handle_high_severity_finding(detail: Dict[str, Any]) -> List[str]:
    """Handle high severity security findings"""
    actions = []
    
    # Get affected resource
    service = detail.get('service', {})
    resource_role = service.get('resourceRole')
    
    if resource_role == 'TARGET':
        # Instance is compromised
        instance_id = service.get('remoteIpDetails', {}).get('instanceId')
        if instance_id:
            actions.extend(isolate_instance(instance_id))
    
    # Create support case for high severity
    actions.append(create_support_case(detail))
    
    return actions

def handle_backdoor_finding(detail: Dict[str, Any]) -> List[str]:
    """Handle backdoor detection"""
    actions = []
    
    # Block malicious IPs
    remote_ip = detail.get('service', {}).get('remoteIpDetails', {}).get('ipAddressV4')
    if remote_ip:
        actions.append(block_ip_in_waf(remote_ip))
        actions.append(block_ip_in_nacl(remote_ip))
    
    # Isolate affected instance
    instance_id = detail.get('service', {}).get('resourceRole')
    if instance_id:
        actions.extend(isolate_instance(instance_id))
    
    return actions

def handle_crypto_mining(detail: Dict[str, Any]) -> List[str]:
    """Handle cryptocurrency mining detection"""
    actions = []
    
    # Block mining pool IPs
    remote_ip = detail.get('service', {}).get('remoteIpDetails', {}).get('ipAddressV4')
    if remote_ip:
        actions.append(block_ip_in_waf(remote_ip))
    
    # Check for unauthorized processes
    instance_id = detail.get('service', {}).get('resourceRole')
    if instance_id:
        actions.append(f"Initiated process scan on instance {instance_id}")
    
    return actions

def isolate_instance(instance_id: str) -> List[str]:
    """Isolate compromised EC2 instance"""
    ec2 = boto3.client('ec2')
    actions = []
    
    try:
        # Create isolation security group
        vpc_response = ec2.describe_instances(InstanceIds=[instance_id])
        vpc_id = vpc_response['Reservations'][0]['Instances'][0]['VpcId']
        
        isolation_sg = ec2.create_security_group(
            GroupName=f'isolation-{instance_id}-{int(datetime.utcnow().timestamp())}',
            Description=f'Isolation security group for compromised instance {instance_id}',
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'security-group',
                    'Tags': [
                        {'Key': 'Purpose', 'Value': 'SecurityIsolation'},
                        {'Key': 'InstanceId', 'Value': instance_id},
                        {'Key': 'CreatedBy', 'Value': 'SecurityAutomation'}
                    ]
                }
            ]
        )
        
        # Apply isolation security group
        ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[isolation_sg['GroupId']]
        )
        
        actions.append(f"Isolated instance {instance_id} with security group {isolation_sg['GroupId']}")
        
        # Create snapshot for forensics
        volumes_response = ec2.describe_volumes(
            Filters=[
                {'Name': 'attachment.instance-id', 'Values': [instance_id]}
            ]
        )
        
        for volume in volumes_response['Volumes']:
            snapshot_response = ec2.create_snapshot(
                VolumeId=volume['VolumeId'],
                Description=f'Forensic snapshot of {volume["VolumeId"]} from compromised instance {instance_id}',
                TagSpecifications=[
                    {
                        'ResourceType': 'snapshot',
                        'Tags': [
                            {'Key': 'Purpose', 'Value': 'ForensicAnalysis'},
                            {'Key': 'SourceInstance', 'Value': instance_id},
                            {'Key': 'CreatedBy', 'Value': 'SecurityAutomation'}
                        ]
                    }
                ]
            )
            actions.append(f"Created forensic snapshot {snapshot_response['SnapshotId']}")
        
    except Exception as e:
        actions.append(f"Failed to isolate instance {instance_id}: {str(e)}")
    
    return actions

def block_ip_in_waf(ip_address: str) -> str:
    """Block IP address in WAF"""
    wafv2 = boto3.client('wafv2')
    
    try:
        # Get existing blocked IPs set
        ip_set_name = 'blocked-ips'
        
        # Add IP to blocked set
        wafv2.update_ip_set(
            Scope='REGIONAL',
            Id=ip_set_name,
            Addresses=[ip_address],
            LockToken='update-token'
        )
        
        return f"Blocked IP {ip_address} in WAF"
        
    except Exception as e:
        return f"Failed to block IP {ip_address} in WAF: {str(e)}"

def block_ip_in_nacl(ip_address: str) -> str:
    """Block IP address in Network ACL"""
    ec2 = boto3.client('ec2')
    
    try:
        # Find default NACL
        nacls_response = ec2.describe_network_acls(
            Filters=[
                {'Name': 'default', 'Values': ['true']}
            ]
        )
        
        for nacl in nacls_response['NetworkAcls']:
            # Add deny rule
            ec2.create_network_acl_entry(
                NetworkAclId=nacl['NetworkAclId'],
                RuleNumber=1,
                Protocol='-1',
                RuleAction='deny',
                CidrBlock=f'{ip_address}/32'
            )
        
        return f"Blocked IP {ip_address} in Network ACL"
        
    except Exception as e:
        return f"Failed to block IP {ip_address} in NACL: {str(e)}"

def create_support_case(detail: Dict[str, Any]) -> str:
    """Create AWS Support case for security incident"""
    support = boto3.client('support')
    
    try:
        case_response = support.create_case(
            subject=f"Security Incident: {detail['type']}",
            serviceCode='security',
            severityCode='high',
            categoryCode='security',
            communicationBody=f"""Automated security incident report:
            
Finding Type: {detail['type']}
Severity: {detail['severity']}
Description: {detail['description']}
Time: {detail['updatedAt']}
            
This case was created automatically by our security automation system.
            Please investigate this security incident.
            """,
            ccEmailAddresses=[
                os.environ.get('SECURITY_EMAIL', 'security@company.com')
            ],
            language='en'
        )
        
        return f"Created support case {case_response['caseId']}"
        
    except Exception as e:
        return f"Failed to create support case: {str(e)}"

def send_security_notification(incident: Dict[str, Any]):
    """Send security incident notification"""
    sns = boto3.client('sns')
    
    severity_emoji = {
        'LOW': '🟡',
        'MEDIUM': '🟠', 
        'HIGH': '🔴',
        'CRITICAL': '🚨'
    }
    
    severity = 'HIGH' if incident.get('severity', 0) >= 7.0 else 'MEDIUM'
    emoji = severity_emoji.get(severity, '⚠️')
    
    message = f"""{emoji} SECURITY ALERT - {incident['type']}

Finding Type: {incident['finding_type']}
Severity: {incident['severity']}
Actions Taken: {len(incident['actions_taken'])}

Automated Response Actions:
"""
    
    for action in incident['actions_taken']:
        message += f"• {action}\n"
    
    message += f"\nTimestamp: {datetime.utcnow().isoformat()}"
    
    sns.publish(
        TopicArn=os.environ['SECURITY_ALERTS_TOPIC'],
        Subject=f"{emoji} Security Alert: {incident['finding_type']}",
        Message=message
    )
```


### Q20: How do you implement multi-account governance with AWS Organizations and Control Tower?
**Difficulty: Hard**

**Answer:**
Multi-account governance provides centralized management, security controls, and compliance across multiple AWS accounts.

```yaml
# AWS Organizations Setup
Organization:
  Type: AWS::Organizations::Organization
  Properties:
    FeatureSet: ALL
    EnabledPolicyTypes:
      - SERVICE_CONTROL_POLICY
      - TAG_POLICY
      - BACKUP_POLICY
      - AISERVICES_OPT_OUT_POLICY

# Organizational Units
SecurityOU:
  Type: AWS::Organizations::OrganizationalUnit
  Properties:
    Name: Security
    ParentId: !GetAtt Organization.RootId
    Tags:
      - Key: Purpose
        Value: SecurityAccounts

ProductionOU:
  Type: AWS::Organizations::OrganizationalUnit
  Properties:
    Name: Production
    ParentId: !GetAtt Organization.RootId
    Tags:
      - Key: Environment
        Value: Production

DevelopmentOU:
  Type: AWS::Organizations::OrganizationalUnit
  Properties:
    Name: Development
    ParentId: !GetAtt Organization.RootId
    Tags:
      - Key: Environment
        Value: Development

SandboxOU:
  Type: AWS::Organizations::OrganizationalUnit
  Properties:
    Name: Sandbox
    ParentId: !GetAtt Organization.RootId
    Tags:
      - Key: Environment
        Value: Sandbox

# Service Control Policies
DenyRootUserPolicy:
  Type: AWS::Organizations::Policy
  Properties:
    Name: DenyRootUserAccess
    Description: Deny root user access except for specific actions
    Type: SERVICE_CONTROL_POLICY
    Content: |
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "DenyRootUserAccess",
            "Effect": "Deny",
            "Principal": {
              "AWS": "*"
            },
            "Action": "*",
            "Resource": "*",
            "Condition": {
              "StringEquals": {
                "aws:PrincipalType": "Root"
              },
              "StringNotEquals": {
                "aws:RequestedRegion": [
                  "us-east-1",
                  "us-west-2"
                ]
              }
            }
          }
        ]
      }
    TargetIds:
      - !Ref ProductionOU
      - !Ref DevelopmentOU

DenyHighRiskServicesPolicy:
  Type: AWS::Organizations::Policy
  Properties:
    Name: DenyHighRiskServices
    Description: Deny access to high-risk services in development accounts
    Type: SERVICE_CONTROL_POLICY
    Content: |
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "DenyHighRiskServices",
            "Effect": "Deny",
            "Action": [
              "organizations:*",
              "account:*",
              "aws-portal:*",
              "trustedadvisor:*",
              "support:*",
              "directconnect:*",
              "route53domains:*",
              "route53resolver:*"
            ],
            "Resource": "*"
          },
          {
            "Sid": "DenyRegionRestriction",
            "Effect": "Deny",
            "NotAction": [
              "iam:*",
              "organizations:*",
              "route53:*",
              "cloudfront:*",
              "waf:*",
              "support:*",
              "trustedadvisor:*"
            ],
            "Resource": "*",
            "Condition": {
              "StringNotEquals": {
                "aws:RequestedRegion": [
                  "us-east-1",
                  "us-west-2",
                  "eu-west-1"
                ]
              }
            }
          }
        ]
      }
    TargetIds:
      - !Ref DevelopmentOU
      - !Ref SandboxOU

RequireEncryptionPolicy:
  Type: AWS::Organizations::Policy
  Properties:
    Name: RequireEncryption
    Description: Require encryption for S3 and EBS
    Type: SERVICE_CONTROL_POLICY
    Content: |
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "RequireS3Encryption",
            "Effect": "Deny",
            "Action": [
              "s3:PutObject"
            ],
            "Resource": "*",
            "Condition": {
              "StringNotEquals": {
                "s3:x-amz-server-side-encryption": [
                  "AES256",
                  "aws:kms"
                ]
              }
            }
          },
          {
            "Sid": "RequireEBSEncryption",
            "Effect": "Deny",
            "Action": [
              "ec2:CreateVolume"
            ],
            "Resource": "*",
            "Condition": {
              "Bool": {
                "ec2:Encrypted": "false"
              }
            }
          }
        ]
      }
    TargetIds:
      - !Ref ProductionOU
      - !Ref DevelopmentOU

# Tag Policies
RequiredTagsPolicy:
  Type: AWS::Organizations::Policy
  Properties:
    Name: RequiredTags
    Description: Require specific tags on resources
    Type: TAG_POLICY
    Content: |
      {
        "tags": {
          "Environment": {
            "tag_key": {
              "@@assign": "Environment"
            },
            "tag_value": {
              "@@assign": [
                "Production",
                "Development",
                "Staging",
                "Sandbox"
              ]
            },
            "enforced_for": {
              "@@assign": [
                "ec2:instance",
                "s3:bucket",
                "rds:db",
                "lambda:function"
              ]
            }
          },
          "Owner": {
            "tag_key": {
              "@@assign": "Owner"
            },
            "enforced_for": {
              "@@assign": [
                "ec2:instance",
                "s3:bucket",
                "rds:db"
              ]
            }
          },
          "CostCenter": {
            "tag_key": {
              "@@assign": "CostCenter"
            },
            "enforced_for": {
              "@@assign": [
                "ec2:instance",
                "rds:db",
                "lambda:function"
              ]
            }
          }
        }
      }
    TargetIds:
      - !Ref ProductionOU
      - !Ref DevelopmentOU

# Control Tower Landing Zone
ControlTowerLandingZone:
  Type: AWS::ControlTower::LandingZone
  Properties:
    Version: '3.0'
    Manifest:
      governedRegions:
        - us-east-1
        - us-west-2
        - eu-west-1
      organizationStructure:
        security:
          name: Security
        sandbox:
          name: Sandbox
      centralizedLogging:
        accountId: !Ref LogArchiveAccount
        configurations:
          loggingBucket:
            retentionConfiguration:
              retentionPeriodInDays: 365
          accessLoggingBucket:
            retentionConfiguration:
              retentionPeriodInDays: 3653
      securityRoles:
        accountId: !Ref AuditAccount
      accessManagement:
        enabled: true
    Tags:
      - Key: Purpose
        Value: LandingZone

# Account Factory for Control Tower
AccountFactory:
  Type: AWS::ServiceCatalog::CloudFormationProduct
  Properties:
    Name: AWS Control Tower Account Factory
    Description: Automated account provisioning with Control Tower
    Owner: Platform Team
    ProvisioningArtifactParameters:
      - Name: v1.0
        Description: Account Factory v1.0
        Info:
          LoadTemplateFromURL: !Sub 'https://${TemplatesBucket}.s3.amazonaws.com/account-factory.yaml'
    Tags:
      - Key: Purpose
        Value: AccountFactory

# Config Aggregator for multi-account compliance
ConfigAggregator:
  Type: AWS::Config::ConfigurationAggregator
  Properties:
    ConfigurationAggregatorName: OrganizationConfigAggregator
    OrganizationAggregationSource:
      AllAwsRegions: true
      RoleArn: !GetAtt ConfigAggregatorRole.Arn
    Tags:
      - Key: Purpose
        Value: ComplianceAggregation

# GuardDuty Organization Configuration
GuardDutyOrganizationConfiguration:
  Type: AWS::GuardDuty::OrganizationConfiguration
  Properties:
    DetectorId: !Ref GuardDutyDetector
    AutoEnable: true
    MemberFeatures:
      - Name: S3_DATA_EVENTS
        Status: ENABLED
        AdditionalConfiguration:
          - Name: EKS_AUDIT_LOGS
            Status: ENABLED
      - Name: EKS_AUDIT_LOGS
        Status: ENABLED
      - Name: EBS_MALWARE_PROTECTION
        Status: ENABLED
```

```python
# Multi-Account Governance Automation
import boto3
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

def lambda_handler(event, context):
    """Handle multi-account governance automation"""
    
    action = event.get('action')
    
    if action == 'create_account':
        return create_managed_account(event)
    elif action == 'apply_policies':
        return apply_organization_policies(event)
    elif action == 'compliance_check':
        return run_compliance_check(event)
    elif action == 'cost_analysis':
        return analyze_multi_account_costs(event)
    elif action == 'security_audit':
        return perform_security_audit(event)
    else:
        return {'statusCode': 400, 'body': f'Unknown action: {action}'}

def create_managed_account(event: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new managed account with Control Tower"""
    
    organizations = boto3.client('organizations')
    servicecatalog = boto3.client('servicecatalog')
    
    account_name = event['account_name']
    account_email = event['account_email']
    organizational_unit = event.get('organizational_unit', 'Sandbox')
    
    try:
        # Create account through Control Tower Account Factory
        response = servicecatalog.provision_product(
            ProductName='AWS Control Tower Account Factory',
            ProvisioningArtifactName='v1.0',
            ProvisionedProductName=f'Account-{account_name}-{int(datetime.utcnow().timestamp())}',
            ProvisioningParameters=[
                {
                    'Key': 'AccountName',
                    'Value': account_name
                },
                {
                    'Key': 'AccountEmail',
                    'Value': account_email
                },
                {
                    'Key': 'OrganizationalUnitName',
                    'Value': organizational_unit
                },
                {
                    'Key': 'ManagedOrganizationalUnit',
                    'Value': organizational_unit
                }
            ],
            Tags=[
                {
                    'Key': 'CreatedBy',
                    'Value': 'AccountFactory'
                },
                {
                    'Key': 'CreatedAt',
                    'Value': datetime.utcnow().isoformat()
                },
                {
                    'Key': 'Environment',
                    'Value': organizational_unit
                }
            ]
        )
        
        provisioned_product_id = response['RecordDetail']['ProvisionedProductId']
        
        # Wait for account creation to complete
        account_id = wait_for_account_creation(servicecatalog, provisioned_product_id)
        
        if account_id:
            # Apply additional configurations
            setup_account_baseline(account_id, organizational_unit)
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'account_id': account_id,
                    'account_name': account_name,
                    'organizational_unit': organizational_unit,
                    'status': 'CREATED'
                })
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Account creation failed'})
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def wait_for_account_creation(servicecatalog, provisioned_product_id: str, max_wait_time: int = 1800) -> Optional[str]:
    """Wait for account creation to complete"""
    
    start_time = datetime.utcnow()
    
    while (datetime.utcnow() - start_time).seconds < max_wait_time:
        try:
            response = servicecatalog.describe_provisioned_product(
                Id=provisioned_product_id
            )
            
            status = response['ProvisionedProductDetail']['Status']
            
            if status == 'AVAILABLE':
                # Extract account ID from outputs
                outputs = response['ProvisionedProductDetail'].get('Outputs', [])
                for output in outputs:
                    if output['OutputKey'] == 'AccountId':
                        return output['OutputValue']
            elif status in ['ERROR', 'TAINTED']:
                print(f"Account creation failed with status: {status}")
                return None
                
            time.sleep(30)
            
        except Exception as e:
            print(f"Error checking account creation status: {str(e)}")
            time.sleep(30)
    
    return None

def setup_account_baseline(account_id: str, environment: str):
    """Setup baseline configuration for new account"""
    
    # Assume role in the new account
    sts = boto3.client('sts')
    
    try:
        assumed_role = sts.assume_role(
            RoleArn=f'arn:aws:iam::{account_id}:role/AWSControlTowerExecution',
            RoleSessionName='AccountSetup'
        )
        
        credentials = assumed_role['Credentials']
        
        # Create session with assumed role
        session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )
        
        # Setup CloudTrail
        setup_cloudtrail(session, account_id, environment)
        
        # Setup Config
        setup_config_rules(session, environment)
        
        # Setup GuardDuty
        setup_guardduty(session)
        
        # Setup Security Hub
        setup_security_hub(session)
        
        # Setup cost allocation tags
        setup_cost_allocation_tags(session, environment)
        
    except Exception as e:
        print(f"Error setting up account baseline: {str(e)}")

def setup_cloudtrail(session, account_id: str, environment: str):
    """Setup CloudTrail for the account"""
    cloudtrail = session.client('cloudtrail')
    s3 = session.client('s3')
    
    bucket_name = f'cloudtrail-logs-{account_id}-{environment.lower()}'
    
    try:
        # Create S3 bucket for CloudTrail logs
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': session.region_name
            } if session.region_name != 'us-east-1' else {}
        )
        
        # Apply bucket policy
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AWSCloudTrailAclCheck",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "cloudtrail.amazonaws.com"
                    },
                    "Action": "s3:GetBucketAcl",
                    "Resource": f"arn:aws:s3:::{bucket_name}"
                },
                {
                    "Sid": "AWSCloudTrailWrite",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "cloudtrail.amazonaws.com"
                    },
                    "Action": "s3:PutObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                    "Condition": {
                        "StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control"
                        }
                    }
                }
            ]
        }
        
        s3.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(bucket_policy)
        )
        
        # Create CloudTrail
        cloudtrail.create_trail(
            Name=f'{environment}-cloudtrail',
            S3BucketName=bucket_name,
            IncludeGlobalServiceEvents=True,
            IsMultiRegionTrail=True,
            EnableLogFileValidation=True,
            EventSelectors=[
                {
                    'ReadWriteType': 'All',
                    'IncludeManagementEvents': True,
                    'DataResources': [
                        {
                            'Type': 'AWS::S3::Object',
                            'Values': ['arn:aws:s3:::*/*']
                        },
                        {
                            'Type': 'AWS::Lambda::Function',
                            'Values': ['arn:aws:lambda:*']
                        }
                    ]
                }
            ],
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': environment
                },
                {
                    'Key': 'Purpose',
                    'Value': 'Compliance'
                }
            ]
        )
        
        # Start logging
        cloudtrail.start_logging(
            Name=f'{environment}-cloudtrail'
        )
        
    except Exception as e:
        print(f"Error setting up CloudTrail: {str(e)}")

def apply_organization_policies(event: Dict[str, Any]) -> Dict[str, Any]:
    """Apply organization-wide policies"""
    
    organizations = boto3.client('organizations')
    
    policy_updates = []
    
    try:
        # Get all accounts in organization
        accounts_response = organizations.list_accounts()
        accounts = accounts_response['Accounts']
        
        # Get organizational units
        ous_response = organizations.list_organizational_units_for_parent(
            ParentId=organizations.list_roots()['Roots'][0]['Id']
        )
        
        for ou in ous_response['OrganizationalUnits']:
            ou_name = ou['Name']
            ou_id = ou['Id']
            
            # Apply environment-specific policies
            if ou_name == 'Production':
                policies = ['RequireEncryption', 'DenyRootUserAccess', 'RequiredTags']
            elif ou_name == 'Development':
                policies = ['DenyHighRiskServices', 'RequiredTags']
            elif ou_name == 'Sandbox':
                policies = ['DenyHighRiskServices']
            else:
                continue
            
            for policy_name in policies:
                try:
                    # Find policy by name
                    policies_response = organizations.list_policies(
                        Filter='SERVICE_CONTROL_POLICY'
                    )
                    
                    policy_id = None
                    for policy in policies_response['Policies']:
                        if policy['Name'] == policy_name:
                            policy_id = policy['Id']
                            break
                    
                    if policy_id:
                        # Attach policy to OU
                        organizations.attach_policy(
                            PolicyId=policy_id,
                            TargetId=ou_id
                        )
                        
                        policy_updates.append({
                            'policy_name': policy_name,
                            'target': ou_name,
                            'status': 'ATTACHED'
                        })
                    
                except Exception as e:
                    policy_updates.append({
                        'policy_name': policy_name,
                        'target': ou_name,
                        'status': 'FAILED',
                        'error': str(e)
                    })
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'policy_updates': policy_updates,
                'total_updates': len(policy_updates)
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def run_compliance_check(event: Dict[str, Any]) -> Dict[str, Any]:
    """Run compliance checks across all accounts"""
    
    config = boto3.client('config')
    organizations = boto3.client('organizations')
    
    compliance_results = []
    
    try:
        # Get compliance summary from Config aggregator
        response = config.get_aggregate_compliance_details_by_config_rule(
            ConfigurationAggregatorName='OrganizationConfigAggregator',
            ConfigRuleName='encrypted-volumes',
            ComplianceType='NON_COMPLIANT'
        )
        
        for result in response['AggregateEvaluationResults']:
            compliance_results.append({
                'account_id': result['AccountId'],
                'region': result['AwsRegion'],
                'resource_type': result['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceType'],
                'resource_id': result['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceId'],
                'compliance_type': result['ComplianceType'],
                'config_rule': 'encrypted-volumes'
            })
        
        # Check for untagged resources
        untagged_response = config.get_aggregate_compliance_details_by_config_rule(
            ConfigurationAggregatorName='OrganizationConfigAggregator',
            ConfigRuleName='required-tags',
            ComplianceType='NON_COMPLIANT'
        )
        
        for result in untagged_response['AggregateEvaluationResults']:
            compliance_results.append({
                'account_id': result['AccountId'],
                'region': result['AwsRegion'],
                'resource_type': result['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceType'],
                'resource_id': result['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceId'],
                'compliance_type': result['ComplianceType'],
                'config_rule': 'required-tags'
            })
        
        # Generate compliance report
        compliance_summary = generate_compliance_report(compliance_results)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'compliance_summary': compliance_summary,
                'non_compliant_resources': len(compliance_results),
                'details': compliance_results[:50]  # Limit for response size
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def generate_compliance_report(compliance_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate compliance summary report"""
    
    summary = {
        'total_non_compliant': len(compliance_results),
        'by_account': {},
        'by_rule': {},
        'by_resource_type': {}
    }
    
    for result in compliance_results:
        account_id = result['account_id']
        config_rule = result['config_rule']
        resource_type = result['resource_type']
        
        # Count by account
        if account_id not in summary['by_account']:
            summary['by_account'][account_id] = 0
        summary['by_account'][account_id] += 1
        
        # Count by rule
        if config_rule not in summary['by_rule']:
            summary['by_rule'][config_rule] = 0
        summary['by_rule'][config_rule] += 1
        
        # Count by resource type
        if resource_type not in summary['by_resource_type']:
            summary['by_resource_type'][resource_type] = 0
        summary['by_resource_type'][resource_type] += 1
    
    return summary

def analyze_multi_account_costs(event: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze costs across multiple accounts"""
    
    ce = boto3.client('ce')  # Cost Explorer
    organizations = boto3.client('organizations')
    
    try:
        # Get cost data for the last 30 days
        end_date = datetime.utcnow().date()
        start_date = end_date - timedelta(days=30)
        
        response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['BlendedCost'],
            GroupBy=[
                {
                    'Type': 'DIMENSION',
                    'Key': 'LINKED_ACCOUNT'
                },
                {
                    'Type': 'DIMENSION',
                    'Key': 'SERVICE'
                }
            ]
        )
        
        cost_analysis = {
            'total_cost': 0,
            'by_account': {},
            'by_service': {},
            'trends': []
        }
        
        for result in response['ResultsByTime']:
            date = result['TimePeriod']['Start']
            daily_total = 0
            
            for group in result['Groups']:
                account_id = group['Keys'][0]
                service = group['Keys'][1]
                amount = float(group['Metrics']['BlendedCost']['Amount'])
                
                daily_total += amount
                cost_analysis['total_cost'] += amount
                
                # Aggregate by account
                if account_id not in cost_analysis['by_account']:
                    cost_analysis['by_account'][account_id] = 0
                cost_analysis['by_account'][account_id] += amount
                
                # Aggregate by service
                if service not in cost_analysis['by_service']:
                    cost_analysis['by_service'][service] = 0
                cost_analysis['by_service'][service] += amount
            
            cost_analysis['trends'].append({
                'date': date,
                'cost': daily_total
            })
        
        # Get account names
        accounts_response = organizations.list_accounts()
        account_names = {acc['Id']: acc['Name'] for acc in accounts_response['Accounts']}
        
        # Add account names to results
        for account_id in cost_analysis['by_account']:
            if account_id in account_names:
                cost_analysis['by_account'][account_names[account_id]] = cost_analysis['by_account'].pop(account_id)
        
        return {
            'statusCode': 200,
            'body': json.dumps(cost_analysis, default=str)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

This comprehensive AWS questions collection now includes 20 detailed questions covering:

1. **AWS Fundamentals** - Global Infrastructure, Shared Responsibility Model
2. **Compute Services** - EC2, Lambda, Fargate, Auto Scaling
3. **Storage Services** - S3, EBS, storage classes, cross-region replication
4. **Database Services** - RDS, DynamoDB, Aurora comparisons
5. **Networking** - VPC, subnets, security groups
6. **Security** - IAM, WAF, GuardDuty, Security Hub
7. **Serverless** - Lambda, API Gateway, DynamoDB integration
8. **Containers** - ECS, Fargate, container orchestration
9. **CI/CD** - CodePipeline, CodeBuild, CodeDeploy
10. **Infrastructure as Code** - CloudFormation, CDK
11. **Monitoring** - CloudWatch, X-Ray, AWS Config
12. **Cost Optimization** - Cost analysis, recommendations
13. **Disaster Recovery** - Backup strategies, cross-region replication
14. **Advanced Security** - Multi-layered security, automated response
15. **Multi-Account Governance** - Organizations, Control Tower

Each question includes detailed explanations, comprehensive code examples in YAML/JSON/Python, and real-world implementation scenarios suitable for senior-level interviews.

Globals:
  Function:
    Timeout: 30
    Runtime: python3.9
    Environment:
      Variables:
        TABLE_NAME: !Ref UsersTable
        REGION: !Ref AWS::Region

Resources:
  # DynamoDB Table
  UsersTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub '${Environment}-users'
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: userId
          AttributeType: S
        - AttributeName: email
          AttributeType: S
      KeySchema:
        - AttributeName: userId
          KeyType: HASH
      GlobalSecondaryIndexes:
        - IndexName: EmailIndex
          KeySchema:
            - AttributeName: email
              KeyType: HASH
          Projection:
            ProjectionType: ALL
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
      SSESpecification:
        SSEEnabled: true

  # API Gateway
  ApiGateway:
    Type: AWS::Serverless::Api
    Properties:
      StageName: !Ref Environment
      Cors:
        AllowMethods: "'GET,POST,PUT,DELETE,OPTIONS'"
        AllowHeaders: "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
        AllowOrigin: "'*'"
      Auth:
        DefaultAuthorizer: CognitoAuthorizer
        Authorizers:
          CognitoAuthorizer:
            UserPoolArn: !GetAtt UserPool.Arn
      GatewayResponses:
        DEFAULT_4XX:
          ResponseParameters:
            Headers:
              Access-Control-Allow-Origin: "'*'"
              Access-Control-Allow-Headers: "'*'"
        DEFAULT_5XX:
          ResponseParameters:
            Headers:
              Access-Control-Allow-Origin: "'*'"
              Access-Control-Allow-Headers: "'*'"

  # Lambda Functions
  CreateUserFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-create-user'
      CodeUri: src/
      Handler: handlers.create_user
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref UsersTable
      Events:
        CreateUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /users
            Method: POST

  GetUserFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-get-user'
      CodeUri: src/
      Handler: handlers.get_user
      Policies:
        - DynamoDBReadPolicy:
            TableName: !Ref UsersTable
      Events:
        GetUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /users/{userId}
            Method: GET

  UpdateUserFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-update-user'
      CodeUri: src/
      Handler: handlers.update_user
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref UsersTable
      Events:
        UpdateUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /users/{userId}
            Method: PUT

  DeleteUserFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-delete-user'
      CodeUri: src/
      Handler: handlers.delete_user
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref UsersTable
      Events:
        DeleteUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /users/{userId}
            Method: DELETE

  # Stream Processing Function
  StreamProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-stream-processor'
      CodeUri: src/
      Handler: handlers.process_stream
      Events:
        DynamoDBStream:
          Type: DynamoDB
          Properties:
            Stream: !GetAtt UsersTable.StreamArn
            StartingPosition: LATEST
            BatchSize: 10
            MaximumBatchingWindowInSeconds: 5

  # Cognito User Pool
  UserPool:
    Type: AWS::Cognito::UserPool
    Properties:
      UserPoolName: !Sub '${Environment}-user-pool'
      AutoVerifiedAttributes:
        - email
      Policies:
        PasswordPolicy:
          MinimumLength: 8
          RequireUppercase: true
          RequireLowercase: true
          RequireNumbers: true
          RequireSymbols: true
      Schema:
        - Name: email
          AttributeDataType: String
          Required: true
          Mutable: true

  UserPoolClient:
    Type: AWS::Cognito::UserPoolClient
    Properties:
      UserPoolId: !Ref UserPool
      ClientName: !Sub '${Environment}-user-pool-client'
      GenerateSecret: false
      ExplicitAuthFlows:
        - ADMIN_NO_SRP_AUTH
        - USER_PASSWORD_AUTH
```

```python
# Lambda Handlers (src/handlers.py)
import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal
import os

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_response(status_code, body):
    """Create standardized Lambda response"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
        },
        'body': json.dumps(body, default=str)
    }

def create_user(event, context):
    """Create a new user"""
    try:
        # Parse request body
        body = json.loads(event['body'])
        
        # Validate required fields
        required_fields = ['name', 'email']
        for field in required_fields:
            if field not in body:
                return lambda_response(400, {
                    'error': f'Missing required field: {field}'
                })
        
        # Create user item
        user_id = str(uuid.uuid4())
        user_item = {
            'userId': user_id,
            'name': body['name'],
            'email': body['email'],
            'createdAt': datetime.utcnow().isoformat(),
            'updatedAt': datetime.utcnow().isoformat()
        }
        
        # Add optional fields
        optional_fields = ['phone', 'address', 'preferences']
        for field in optional_fields:
            if field in body:
                user_item[field] = body[field]
        
        # Save to DynamoDB
        table.put_item(
            Item=user_item,
            ConditionExpression='attribute_not_exists(userId)'
        )
        
        return lambda_response(201, {
            'message': 'User created successfully',
            'user': user_item
        })
        
    except Exception as e:
        print(f"Error creating user: {str(e)}")
        return lambda_response(500, {
            'error': 'Internal server error'
        })

def get_user(event, context):
    """Get user by ID"""
    try:
        user_id = event['pathParameters']['userId']
        
        # Get user from DynamoDB
        response = table.get_item(
            Key={'userId': user_id}
        )
        
        if 'Item' not in response:
            return lambda_response(404, {
                'error': 'User not found'
            })
        
        return lambda_response(200, {
            'user': response['Item']
        })
        
    except Exception as e:
        print(f"Error getting user: {str(e)}")
        return lambda_response(500, {
            'error': 'Internal server error'
        })

def update_user(event, context):
    """Update user"""
    try:
        user_id = event['pathParameters']['userId']
        body = json.loads(event['body'])
        
        # Build update expression
        update_expression = "SET updatedAt = :updatedAt"
        expression_values = {
            ':updatedAt': datetime.utcnow().isoformat()
        }
        
        # Add fields to update
        updatable_fields = ['name', 'email', 'phone', 'address', 'preferences']
        for field in updatable_fields:
            if field in body:
                update_expression += f", {field} = :{field}"
                expression_values[f":{field}"] = body[field]
        
        # Update item
        response = table.update_item(
            Key={'userId': user_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ConditionExpression='attribute_exists(userId)',
            ReturnValues='ALL_NEW'
        )
        
        return lambda_response(200, {
            'message': 'User updated successfully',
            'user': response['Attributes']
        })
        
    except Exception as e:
        print(f"Error updating user: {str(e)}")
        return lambda_response(500, {
            'error': 'Internal server error'
        })

def delete_user(event, context):
    """Delete user"""
    try:
        user_id = event['pathParameters']['userId']
        
        # Delete user
        table.delete_item(
            Key={'userId': user_id},
            ConditionExpression='attribute_exists(userId)'
        )
        
        return lambda_response(200, {
            'message': 'User deleted successfully'
        })
        
    except Exception as e:
        print(f"Error deleting user: {str(e)}")
        return lambda_response(500, {
            'error': 'Internal server error'
        })

def process_stream(event, context):
    """Process DynamoDB stream events"""
    try:
        for record in event['Records']:
            event_name = record['eventName']
            
            if event_name == 'INSERT':
                # Handle new user creation
                new_image = record['dynamodb']['NewImage']
                print(f"New user created: {new_image['userId']['S']}")
                
                # Send welcome email, update analytics, etc.
                
            elif event_name == 'MODIFY':
                # Handle user updates
                old_image = record['dynamodb']['OldImage']
                new_image = record['dynamodb']['NewImage']
                print(f"User updated: {new_image['userId']['S']}")
                
                # Update search index, send notifications, etc.
                
            elif event_name == 'REMOVE':
                # Handle user deletion
                old_image = record['dynamodb']['OldImage']
                print(f"User deleted: {old_image['userId']['S']}")
                
                # Clean up related data, send notifications, etc.
        
        return {'statusCode': 200}
        
    except Exception as e:
        print(f"Error processing stream: {str(e)}")
        raise e
```


### Q21: What is the difference between EBS and EFS?
**Difficulty: Medium**

**Answer:**

**Amazon EBS (Elastic Block Store)** and **Amazon EFS (Elastic File System)** are two different types of storage services offered by AWS, designed for different use cases.

| Feature | EBS (Elastic Block Store) | EFS (Elastic File System) |
| :--- | :--- | :--- |
| **Storage Type** | Block storage | File storage |
| **Access Model** | Accessible by a single EC2 instance in the same Availability Zone. | Accessible by multiple EC2 instances concurrently, across multiple Availability Zones. |
| **Use Case** | Boot volumes, databases, and applications that require low-latency access to a dedicated block device. | Content management systems, web serving, and shared file access for multiple servers. |
| **Performance** | High performance, with different volume types (gp2, io1, etc.) for different needs. | Performance scales with the amount of storage used. |
| **Scalability** | Manually scalable by resizing the volume. | Automatically scales up or down as you add or remove files. |

**EBS (Elastic Block Store)**

EBS provides persistent block-level storage volumes for use with EC2 instances. It's like a virtual hard drive that you can attach to a single EC2 instance.

**Use Cases:**
*   Boot volumes for EC2 instances.
*   Databases (e.g., MySQL, PostgreSQL).
*   Applications that require a single, dedicated block storage device.

**EFS (Elastic File System)**

EFS provides a simple, scalable, and fully managed elastic file system. It can be mounted on multiple EC2 instances simultaneously, making it ideal for shared file storage.

**Use Cases:**
*   Web serving and content management.
*   Shared code repositories.
*   Big data and analytics workloads.

**Code Example (Mounting EFS on an EC2 instance):**

```bash
# Install the EFS mount helper
sudo yum install -y amazon-efs-utils

# Create a directory to mount the file system
sudo mkdir /mnt/efs

# Mount the EFS file system
sudo mount -t efs fs-12345678:/ /mnt/efs
```

**Key Takeaways:**

*   Use **EBS** when you need high-performance, dedicated block storage for a single EC2 instance.
*   Use **EFS** when you need shared file storage that can be accessed by multiple EC2 instances.


### Q22: What is the difference between Security Groups and NACLs?
**Difficulty: Medium**

**Answer:**

**Security Groups** and **Network Access Control Lists (NACLs)** are both used to control traffic to and from your AWS resources, but they operate at different levels and have different characteristics.

| Feature | Security Groups | Network ACLs (NACLs) |
| :--- | :--- | :--- |
| **Level of Operation** | Instance level (act as a firewall for EC2 instances). | Subnet level (act as a firewall for a subnet). |
| **Statefulness** | Stateful: If you allow inbound traffic, the corresponding outbound traffic is automatically allowed. | Stateless: You must explicitly define rules for both inbound and outbound traffic. |
| **Rules** | Allow rules only. You cannot create deny rules. | Both allow and deny rules. |
| **Rule Evaluation** | All rules are evaluated before making a decision. | Rules are evaluated in order, from the lowest numbered rule to the highest. |
| **Default State** | Denies all inbound traffic and allows all outbound traffic. | Allows all inbound and outbound traffic. |

**Security Groups**

Security Groups act as a virtual firewall for your EC2 instances to control inbound and outbound traffic. They are stateful, which means that if you send a request from your instance, the response traffic is automatically allowed, regardless of inbound security group rules.

**Example (Allowing HTTP and SSH traffic):**

```json
{
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 80,
      "ToPort": 80,
      "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
    },
    {
      "IpProtocol": "tcp",
      "FromPort": 22,
      "ToPort": 22,
      "IpRanges": [{"CidrIp": "YOUR_IP/32"}]
    }
  ]
}
```

**Network ACLs (NACLs)**

NACLs are an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. They are stateless, which means that you must create rules for both inbound and outbound traffic.

**Example (Allowing HTTP traffic and denying all other traffic):**

```json
{
  "InboundRules": [
    {
      "RuleNumber": 100,
      "Protocol": "6", // TCP
      "RuleAction": "allow",
      "CidrBlock": "0.0.0.0/0",
      "PortRange": { "From": 80, "To": 80 }
    }
  ],
  "OutboundRules": [
    {
      "RuleNumber": 100,
      "Protocol": "6", // TCP
      "RuleAction": "allow",
      "CidrBlock": "0.0.0.0/0",
      "PortRange": { "From": 1024, "To": 65535 } // Ephemeral ports
    }
  ]
}
```

**Key Takeaways:**

*   **Security Groups** are the first line of defense and are applied at the instance level.
*   **NACLs** are an additional layer of defense and are applied at the subnet level.
*   It's a best practice to use both Security Groups and NACLs for a layered security approach.


### Q23: What is the difference between an IAM User and an IAM Role?
**Difficulty: Easy**

**Answer:**

**IAM Users** and **IAM Roles** are both IAM identities that you can use to manage access to your AWS resources, but they are designed for different use cases.

| Feature | IAM User | IAM Role |
| :--- | :--- | :--- |
| **Identity Type** | A person or application that needs long-term access to AWS. | An identity that can be assumed by trusted entities (users, applications, or services). |
| **Credentials** | Has permanent credentials (password and access keys). | Has temporary credentials that are generated when the role is assumed. |
| **Use Case** | For individuals who need to access the AWS Management Console or make API calls. | For granting temporary access to resources, delegating access to services, or providing access to users from a different AWS account. |

**IAM User**

An IAM user is an entity that you create in AWS to represent the person or application that uses it to interact with AWS. A user has permanent credentials, such as a password for console access and access keys for programmatic access.

**Use Cases:**
*   Creating individual accounts for developers, administrators, and other team members.
*   Creating service accounts for applications that need long-term access to AWS resources.

**IAM Role**

An IAM role is an identity that you can create in your account that has specific permissions. It is not associated with a specific user; instead, trusted entities, such as users, applications, or AWS services, can assume the role to obtain temporary security credentials.

**Use Cases:**
*   **Delegating access to AWS services:** Allowing an EC2 instance to access an S3 bucket.
*   **Cross-account access:** Allowing users from one AWS account to access resources in another account.
*   **Identity federation:** Granting access to users from a corporate directory (e.g., Active Directory) or a web identity provider (e.g., Google, Facebook).

**Example (Creating a role for an EC2 instance):**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "ec2.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

This trust policy allows EC2 instances to assume the role.

**Key Takeaways:**

*   Use **IAM Users** for entities that require permanent credentials.
*   Use **IAM Roles** for entities that require temporary credentials or for delegating access.
*   It's a best practice to use roles whenever possible to avoid using long-term credentials.


### Q24: What is the difference between SQS and SNS?
**Difficulty: Medium**

**Answer:**

**Amazon Simple Queue Service (SQS)** and **Amazon Simple Notification Service (SNS)** are both messaging services in AWS, but they serve different purposes and follow different messaging patterns.

| Feature | SQS (Simple Queue Service) | SNS (Simple Notification Service) |
| :--- | :--- | :--- |
| **Messaging Model** | **Pull-based (polling):** Consumers poll a queue to retrieve messages. | **Push-based (pub/sub):** A publisher sends a message to a topic, and the message is pushed to all subscribers. |
| **Use Case** | Decoupling microservices, distributing tasks, and buffering requests. | Fanning out messages to multiple recipients, sending notifications, and triggering parallel processing. |
| **Message Delivery** | A message is delivered to a single consumer and is deleted after being processed. | A message is delivered to all subscribers of a topic. |
| **Subscribers** | Consumers (e.g., EC2 instances, Lambda functions) that poll the queue. | Endpoints (e.g., SQS queues, Lambda functions, HTTP/S endpoints, email, SMS). |

**SQS (Simple Queue Service)**

SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It provides a message queue where messages are stored until they are processed and deleted by a consumer.

**Use Cases:**
*   **Decoupling:** A web server can send a request to an SQS queue, and a separate worker process can process the request asynchronously.
*   **Task distribution:** A single message can be sent to a queue, and multiple consumers can process different messages from the queue in parallel.

**SNS (Simple Notification Service)**

SNS is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It uses a publish/subscribe model, where a publisher sends a message to a topic, and all subscribers to that topic receive the message.

**Use Cases:**
*   **Fanout:** A single message can be sent to an SNS topic, and the message can be delivered to multiple SQS queues, Lambda functions, and HTTP endpoints.
*   **Notifications:** Sending email or SMS notifications to users.

**Example (Fanout pattern with SNS and SQS):**

1.  Create an SNS topic.
2.  Create multiple SQS queues.
3.  Subscribe the SQS queues to the SNS topic.
4.  When a message is published to the SNS topic, it will be sent to all the SQS queues.

**Key Takeaways:**

*   Use **SQS** when you need to decouple applications and ensure that a message is processed by a single consumer.
*   Use **SNS** when you need to send a message to multiple recipients (fanout) or send notifications.
*   You can use SQS and SNS together to build powerful and scalable applications.


### Q25: What is the difference between a launch template and a launch configuration?
**Difficulty: Medium**

**Answer:**

**Launch templates** and **launch configurations** are both used to specify the configuration of EC2 instances that are launched as part of an Auto Scaling group. However, launch templates are newer and provide more features and flexibility than launch configurations.

| Feature | Launch Configuration | Launch Template |
| :--- | :--- | :--- |
| **Versioning** | No | Yes (you can create multiple versions of a template) |
| **Flexibility** | Limited (you can't change a launch configuration after it's created) | High (you can create a new version of a template to change the configuration) |
| **Instance Types** | Single instance type | Multiple instance types (you can specify a mix of instance types and purchase options) |
| **Purchase Options** | On-Demand only | On-Demand and Spot Instances |
| **Tagging** | Limited (you can only tag instances) | Extensive (you can tag instances, volumes, and network interfaces) |

**Launch Configuration**

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances. It is an older feature and has been superseded by launch templates.

**Launch Template**

A launch template is similar to a launch configuration, but it provides more flexibility and features. With launch templates, you can create multiple versions of a template, use a mix of instance types and purchase options, and tag instances, volumes, and network interfaces.

**Key Takeaways:**

*   AWS recommends using **launch templates** instead of launch configurations.
*   Launch templates provide more flexibility and features than launch configurations.
*   You can't modify a launch configuration after you've created it, but you can create a new version of a launch template.


### Q26: What is AWS Shield and how does it work?
**Difficulty: Medium**

**Answer:**

**AWS Shield** is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. It provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection.

There are two tiers of AWS Shield: **Standard** and **Advanced**.

| Feature | AWS Shield Standard | AWS Shield Advanced |
| :--- | :--- | :--- |
| **Cost** | Free | Paid (monthly fee + data transfer fees) |
| **Protection Level** | Protects against most common, network and transport layer DDoS attacks. | Provides additional protection against larger and more sophisticated attacks. |
| **Visibility** | Basic attack visibility. | Detailed attack diagnostics and the ability to see the attack's source. |
| **Support** | AWS Support | 24x7 access to the AWS DDoS Response Team (DRT). |
| **Cost Protection** | No | Yes (protects against scaling charges resulting from a DDoS attack) |

**How it works:**

AWS Shield is integrated with other AWS services, such as Amazon CloudFront, Amazon Route 53, and Elastic Load Balancing. When you use these services, AWS Shield Standard is automatically enabled at no extra cost.

For a higher level of protection, you can subscribe to AWS Shield Advanced. Shield Advanced provides more sophisticated detection and mitigation techniques, as well as 24x7 access to the AWS DDoS Response Team (DRT).

**Key Takeaways:**

*   AWS Shield is a managed DDoS protection service.
*   There are two tiers: Standard (free) and Advanced (paid).
*   Shield Standard is automatically enabled for all AWS customers.
*   Shield Advanced provides a higher level of protection and access to the AWS DRT.


### Q27: What is the difference between Amazon RDS and Amazon Aurora?
**Difficulty: Medium**

**Answer:**

**Amazon RDS** and **Amazon Aurora** are both fully managed relational database services from AWS, but Aurora is a cloud-native database that offers higher performance and availability than standard RDS.

| Feature | Amazon RDS | Amazon Aurora |
| :--- | :--- | :--- |
| **Engine** | Standard MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server. | Custom-built, MySQL and PostgreSQL-compatible engine. |
| **Performance** | Standard performance. | Up to 5x faster than standard MySQL and 3x faster than standard PostgreSQL. |
| **Availability** | Multi-AZ deployments for high availability. | Replicates data across 3 Availability Zones for higher availability and durability. |
| **Storage** | Up to 64 TB, provisioned in advance. | Up to 128 TB, auto-scaling in 10 GB increments. |
| **Cost** | Generally less expensive than Aurora. | Generally more expensive than RDS, but can be more cost-effective for high-throughput workloads. |

**Amazon RDS**

Amazon Relational Database Service (RDS) is a managed service that makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

**Amazon Aurora**

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases.

**Key Takeaways:**

*   **Amazon RDS** is a good choice for a wide range of applications, from small projects to large enterprises.
*   **Amazon Aurora** is a good choice for applications that require high performance and availability, such as e-commerce sites, gaming applications, and financial systems.
*   If you are currently using MySQL or PostgreSQL, you can migrate to Aurora with little to no application changes.


### Q28: What is AWS Lambda and what are its benefits?
**Difficulty: Easy**

**Answer:**

**AWS Lambda** is a serverless compute service that lets you run code without provisioning or managing servers. You can run code for virtually any type of application or backend service - all with zero administration. Just upload your code and Lambda handles everything required to run and scale your code with high availability.

**Benefits of AWS Lambda:**

*   **No servers to manage:** AWS Lambda automatically runs your code without requiring you to provision or manage servers. This means you can focus on writing code and not have to worry about the underlying infrastructure.
*   **Continuous scaling:** AWS Lambda automatically scales your application by running code in response to each trigger. Your code runs in parallel and processes each trigger individually, scaling precisely with the size of the workload.
*   **Subsecond metering:** With AWS Lambda, you are charged for every 100ms your code executes and the number of times your code is triggered. You don't pay anything when your code isn't running.
*   **Flexibility:** You can use any programming language or framework that you want. Lambda supports Node.js, Python, Java, Go, Ruby, and .NET Core.

**How it works:**

1.  **Upload your code to AWS Lambda:** You can upload your code as a .zip file or container image.
2.  **Set up your code to trigger from other AWS services, HTTP endpoints, or in-app activity:** You can trigger your Lambda function from over 200 AWS services and SaaS applications.
3.  **Lambda runs your code only when triggered, and you only pay for the compute time you consume:** You are charged based on the number of requests for your functions and the duration, the time it takes for your code to execute.

**Example (A simple Node.js Lambda function):**

```javascript
exports.handler = async (event) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  return response;
};
```

This function can be triggered by an API Gateway endpoint to create a simple serverless API.


### Q29: What is the difference between an Application Load Balancer and a Network Load Balancer?
**Difficulty: Medium**

**Answer:**

**Application Load Balancers (ALB)** and **Network Load Balancers (NLB)** are both types of Elastic Load Balancers (ELB) in AWS, but they operate at different layers of the OSI model and are designed for different use cases.

| Feature | Application Load Balancer (ALB) | Network Load Balancer (NLB) |
| :--- | :--- | :--- |
| **OSI Layer** | Layer 7 (Application) | Layer 4 (Transport) |
| **Protocol** | HTTP, HTTPS, gRPC | TCP, UDP, TLS |
| **Routing** | Path-based, host-based, and query string-based routing. | Routes connections to targets based on IP protocol data. |
| **IP Address** | No static IP address. | Static IP address per Availability Zone. |
| **Use Case** | Microservices, container-based applications, and web applications. | Applications that require extreme performance, low latency, and TLS offloading. |

**Application Load Balancer (ALB)**

An ALB is best suited for load balancing of HTTP and HTTPS traffic and provides advanced routing capabilities. It operates at the application layer (Layer 7) and can inspect the content of the request to make routing decisions.

**Network Load Balancer (NLB)**

An NLB is best suited for load balancing of TCP, UDP, and TLS traffic where extreme performance is required. It operates at the transport layer (Layer 4) and can handle millions of requests per second while maintaining ultra-low latencies.

**Key Takeaways:**

*   Use an **ALB** when you need to route traffic based on the content of the request, such as the URL path or hostname.
*   Use an **NLB** when you need to handle a high volume of TCP/UDP traffic with low latency.
*   You can also use a **Classic Load Balancer**, which is the previous generation of ELB. However, AWS recommends using ALBs and NLBs for new applications.


### Q30: What is Amazon S3 Transfer Acceleration?
**Difficulty: Medium**

**Answer:**

**Amazon S3 Transfer Acceleration** is a feature of Amazon S3 that enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

**How it works:**

1.  **Enable Transfer Acceleration on your S3 bucket:** You can enable this feature in the S3 console.
2.  **Use the special S3 Transfer Acceleration endpoint:** Instead of the standard S3 endpoint (e.g., `my-bucket.s3.amazonaws.com`), you use the Transfer Acceleration endpoint (e.g., `my-bucket.s3-accelerate.amazonaws.com`).

When you use the Transfer Acceleration endpoint, your data is routed to the nearest CloudFront edge location. From there, it travels over AWS's private network to your S3 bucket, which is much faster than transferring data over the public internet.

**Benefits:**

*   **Faster data transfers:** Transfer Acceleration can be up to 50-500% faster than transferring data over the public internet.
*   **Secure:** Data is encrypted in transit using SSL/TLS.
*   **Easy to use:** You just need to enable the feature and use the special endpoint.

**Use Cases:**

*   Uploading large files to S3 from geographically dispersed locations.
*   Distributing content to users around the world.
*   Backing up data to S3 from on-premises data centers.


### Q31: What is AWS Global Accelerator?
**Difficulty: Medium**

**Answer:**

**AWS Global Accelerator** is a networking service that improves the availability and performance of your applications with local or global users. It provides you with two static IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers or Amazon EC2 instances.

**How it works:**

Global Accelerator uses the AWS global network to route user traffic to the optimal regional endpoint based on performance. If there's an application failure, Global Accelerator instantly fails over to the next best endpoint.

**Benefits:**

*   **Improved performance:** Global Accelerator directs traffic to the healthiest, closest endpoint to the user, which can reduce latency by up to 60%.
*   **Increased availability:** It automatically reroutes traffic to a healthy endpoint in case of an application failure.
*   **Simplified management:** You get a set of static IP addresses that you can use for all of your applications, which simplifies firewall rules and DNS configuration.

**Use Cases:**

*   **Gaming:** Reduce in-game latency and jitter.
*   **IoT:** Improve the performance and reliability of IoT device communication.
*   **Web applications:** Provide a faster and more reliable experience for your users.

**Difference between S3 Transfer Acceleration and Global Accelerator:**

*   **S3 Transfer Acceleration** is specifically for accelerating uploads and downloads to and from Amazon S3.
*   **Global Accelerator** is a more general-purpose service that can be used to accelerate any TCP or UDP application.


### Q32: What is Amazon CloudFront and how does it work?
**Difficulty: Easy**

**Answer:**

**Amazon CloudFront** is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.

**How it works:**

CloudFront works by caching your content in a worldwide network of edge locations. When a user requests your content, they are routed to the edge location that provides the lowest latency, so that content is delivered with the best possible performance.

1.  **You specify origin servers**, like an Amazon S3 bucket or your own HTTP server, from which CloudFront gets your files which will then be distributed from CloudFront edge locations all over the world.
2.  **You upload your files to your origin servers.** Your files, also known as *objects*, typically include web pages, images, and media files.
3.  **You create a CloudFront distribution**, which tells CloudFront which origin servers to get your files from when users request the files through your web site or application.
4.  **CloudFront assigns a domain name to your new distribution** that you can see in the CloudFront console.
5.  **CloudFront sends your distribution's configuration (but not your content) to all of its edge locations.**

**Benefits:**

*   **Fast and global:** CloudFront has a massive, global network of edge locations that ensures your content is delivered to users with low latency.
*   **Secure:** CloudFront provides a number of security features, such as SSL/TLS encryption, and integration with AWS Shield for DDoS mitigation.
*   **Cost-effective:** You pay only for the data you transfer, with no minimum fees.

**Use Cases:**

*   **Website delivery:** Deliver your entire website, including dynamic, static, streaming, and interactive content.
*   **Video streaming:** Deliver live and on-demand video to any device.
*   **Software distribution:** Distribute software, games, and other large files to users around the world.


### Q33: What is the difference between a stateful and a stateless application?
**Difficulty: Easy**

**Answer:**

**Stateful** and **stateless** are two different ways of designing applications. The main difference between them is how they handle user data (state).

| Feature | Stateful Application | Stateless Application |
| :--- | :--- | :--- |
| **State Management** | The application stores data about each client session. | The application does not store any client data. |
| **Scalability** | More difficult to scale, as you need to ensure that each request from a client is routed to the same server. | Easier to scale, as any server can handle any request. |
| **Reliability** | If a server fails, the user's session data is lost. | If a server fails, the user can be seamlessly redirected to another server without any loss of data. |
| **Examples** | Online banking, e-commerce shopping carts. | RESTful APIs, content delivery networks (CDNs). |

**Stateful Application**

A stateful application remembers information about each client session. This means that when a user interacts with the application, the application stores data about that interaction. For example, a shopping cart on an e-commerce website is a stateful application because it needs to remember which items the user has added to their cart.

**Stateless Application**

A stateless application, on the other hand, does not store any information about the client session. Each request is treated as an independent transaction. For example, a RESTful API is a stateless application because each API call is independent of the others.

**Key Takeaways:**

*   **Stateful applications** are more complex to design and scale, but they can provide a more personalized user experience.
*   **Stateless applications** are simpler to design and scale, and they are more resilient to server failures.
*   In a microservices architecture, it is a best practice to design services to be as stateless as possible.


### Q34: What is AWS Elastic Beanstalk?
**Difficulty: Easy**

**Answer:**

**AWS Elastic Beanstalk** is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.

You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

**Benefits:**

*   **Fast and simple to start:** You can deploy your application in minutes.
*   **Developer productivity:** Elastic Beanstalk handles the details of your hosting environment, so you can focus on writing code.
*   **Impossible to outgrow:** Elastic Beanstalk automatically scales your application up and down based on your application's specific needs using easily adjustable Auto Scaling settings.
*   **Complete resource control:** You have the flexibility to select the AWS resources, such as EC2 instance type, that are optimal for your application.

**How it works:**

1.  **Create an application:** An Elastic Beanstalk application is a logical collection of Elastic Beanstalk components, including environments, versions, and environment configurations.
2.  **Upload a version:** An application version refers to a specific, labeled iteration of deployable code for a web application.
3.  **Launch an environment:** An environment is a version that is deployed on AWS resources.

**Use Cases:**

*   **Web applications:** Deploy and scale web applications of all sizes.
*   **APIs:** Deploy and manage backend APIs.
*   **Microservices:** Deploy and manage individual microservices.


### Q35: What is the difference between horizontal and vertical scaling?
**Difficulty: Easy**

**Answer:**

**Horizontal scaling** and **vertical scaling** are two different ways to increase the capacity of your application.

| Feature | Horizontal Scaling (Scaling Out) | Vertical Scaling (Scaling Up) |
| :--- | :--- | :--- |
| **Method** | Add more machines to your pool of resources. | Add more power (CPU, RAM) to an existing machine. |
| **Scalability** | Highly scalable, as you can add as many machines as you need. | Limited by the capacity of a single machine. |
| **Reliability** | More reliable, as there is no single point of failure. | Less reliable, as the entire application will go down if the machine fails. |
| **Cost** | Can be more cost-effective, as you can use smaller, less expensive machines. | Can be more expensive, as you need to purchase more powerful machines. |
| **Example** | Adding more EC2 instances to an Auto Scaling group. | Increasing the instance size of an EC2 instance (e.g., from t2.micro to t2.large). |

**Horizontal Scaling (Scaling Out)**

Horizontal scaling means adding more machines to your pool of resources. For example, if you have a web application that is running on a single server, you can scale horizontally by adding more servers and using a load balancer to distribute the traffic between them.

**Vertical Scaling (Scaling Up)**

Vertical scaling means adding more power (CPU, RAM) to an existing machine. For example, if you have a database server that is running out of memory, you can scale vertically by adding more RAM to the server.

**Key Takeaways:**

*   **Horizontal scaling** is generally the preferred method for scaling web applications, as it is more scalable, reliable, and cost-effective.
*   **Vertical scaling** is a good option for applications that are difficult to scale horizontally, such as databases.
*   In many cases, a combination of both horizontal and vertical scaling is the best approach.


### Q36: What is Amazon ElastiCache?
**Difficulty: Medium**

**Answer:**

**Amazon ElastiCache** is a fully managed in-memory data store and cache service by AWS. It improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory caches, instead of relying entirely on slower disk-based databases.

ElastiCache supports two open-source in-memory caching engines:

*   **Redis:** A fast, open-source, in-memory data store and cache. Redis is a good choice for applications that require complex data types, such as sorted sets and hashes.
*   **Memcached:** A high-performance, distributed memory object caching system. Memcached is a good choice for applications that need to cache simple key-value data.

**Benefits:**

*   **Improved performance:** ElastiCache can significantly improve the performance of your application by reducing the latency of data retrieval.
*   **Reduced load on your database:** By caching frequently accessed data, ElastiCache can reduce the number of requests to your database, which can improve its performance and reduce costs.
*   **Fully managed:** ElastiCache is a fully managed service, so you don't have to worry about the operational overhead of managing a cache.

**Use Cases:**

*   **Caching:** Cache the results of database queries, API calls, and other expensive operations.
*   **Session storage:** Store user session data in a fast, scalable, and highly available cache.
*   **Real-time applications:** Power real-time applications, such as leaderboards, chat applications, and real-time analytics.


### Q37: What is AWS Snowball?
**Difficulty: Medium**

**Answer:**

**AWS Snowball** is a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of the AWS cloud. Using Snowball addresses common challenges with large-scale data transfers including high network costs, long transfer times, and security concerns.

There are two types of Snowball appliances:

*   **Snowball:** The standard Snowball appliance, which comes in 50TB and 80TB sizes.
*   **Snowball Edge:** A Snowball appliance with onboard storage and compute power. Snowball Edge can be used to run AWS Lambda functions and Amazon EC2 instances in remote or disconnected environments.

**How it works:**

1.  **Request a Snowball appliance:** You request a Snowball appliance from the AWS Management Console.
2.  **AWS ships the appliance to you:** AWS ships the appliance to your location.
3.  **Connect the appliance to your network and transfer your data:** You connect the appliance to your local network and use the Snowball client to transfer your data to the appliance.
4.  **Ship the appliance back to AWS:** You ship the appliance back to AWS.
5.  **AWS imports your data into S3:** AWS imports your data from the appliance into your S3 bucket.

**Benefits:**

*   **Fast:** Transferring data with Snowball can be up to 10 times faster than transferring data over the internet.
*   **Secure:** Snowball uses multiple layers of security, including tamper-resistant enclosures, 256-bit encryption, and an industry-standard Trusted Platform Module (TPM) designed to ensure both security and full chain-of-custody of your data.
*   **Cost-effective:** Snowball is a cost-effective way to transfer large amounts of data.

**Use Cases:**

*   **Data migration:** Migrate large amounts of data from on-premises data centers to AWS.
*   **Disaster recovery:** Back up large amounts of data to AWS for disaster recovery purposes.
*   **Content distribution:** Distribute large amounts of content to remote locations.


### Q38: What is AWS Storage Gateway?
**Difficulty: Medium**

**Answer:**

**AWS Storage Gateway** is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. Customers use Storage Gateway to simplify storage management and reduce costs for key hybrid cloud storage use cases. These include moving backups to the cloud, using on-premises file shares backed by cloud storage, and providing low latency access to data in AWS for on-premises applications.

There are three types of Storage Gateways:

*   **File Gateway:** Provides a file interface into Amazon S3, and is ideal for on-premises applications that need to store and retrieve objects in S3.
*   **Volume Gateway:** Provides a block storage interface for your on-premises applications, and is ideal for backing up your local applications and for disaster recovery.
*   **Tape Gateway:** Provides a virtual tape library (VTL) interface for your on-premises backup application, and is ideal for archiving your backup data in the AWS cloud.

**How it works:**

1.  **Deploy the Storage Gateway appliance:** You can deploy the Storage Gateway appliance as a virtual machine (VM) on your on-premises hypervisor or as a hardware appliance.
2.  **Connect the appliance to your network and AWS:** You connect the appliance to your local network and to your AWS account.
3.  **Configure the gateway:** You configure the gateway to work with your on-premises applications and your AWS storage.

**Benefits:**

*   **Simplified storage management:** Storage Gateway simplifies storage management by providing a single, unified view of your on-premises and cloud storage.
*   **Reduced costs:** Storage Gateway can help you reduce costs by moving your backups and archives to the cloud.
*   **Low latency access to data:** Storage Gateway provides low latency access to data in AWS for your on-premises applications.


### Q39: What is Amazon EKS?
**Difficulty: Medium**

**Answer:**

**Amazon Elastic Kubernetes Service (Amazon EKS)** is a managed service that makes it easy for you to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

**What is Kubernetes?**

Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

**Benefits of Amazon EKS:**

*   **Managed control plane:** Amazon EKS provisions and manages the Kubernetes control plane for you, which includes the Kubernetes API server, etcd, and other components.
*   **Managed worker nodes:** Amazon EKS allows you to create, manage, and scale your worker nodes using Amazon EC2 instances or AWS Fargate.
*   **Secure:** Amazon EKS is integrated with AWS Identity and Access Management (IAM), so you can use IAM to manage access to your Kubernetes cluster.
*   **Highly available:** Amazon EKS runs the Kubernetes control plane across multiple Availability Zones, so it is highly available.

**How it works:**

1.  **Create an Amazon EKS cluster:** You create an Amazon EKS cluster in the AWS Management Console.
2.  **Configure your worker nodes:** You configure your worker nodes to connect to the Amazon EKS cluster.
3.  **Deploy your applications:** You deploy your containerized applications to the Amazon EKS cluster.

**Use Cases:**

*   **Microservices:** Deploy and manage microservices-based applications.
*   **Web applications:** Deploy and scale web applications.
*   **Machine learning:** Train and deploy machine learning models.


### Q40: What is Amazon ECS?
**Difficulty: Medium**

**Answer:**

**Amazon Elastic Container Service (Amazon ECS)** is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications. It deeply integrates with the rest of the AWS platform to provide a secure and easy-to-use solution for running container workloads in the cloud.

**Key Concepts:**

*   **Task Definition:** A text file, in JSON format, that describes one or more containers that form your application.
*   **Task:** An instantiation of a task definition within a cluster.
*   **Cluster:** A logical grouping of tasks or services.
*   **Service:** Allows you to run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster.

**Launch Types:**

*   **Fargate:** A serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.
*   **EC2:** Allows you to run your containerized applications on a cluster of Amazon EC2 instances that you manage.

**Benefits:**

*   **Fully managed:** Amazon ECS is a fully managed service, so you don't have to worry about managing the underlying infrastructure.
*   **Scalable:** Amazon ECS is highly scalable, so you can easily scale your applications up or down as needed.
*   **Secure:** Amazon ECS is integrated with AWS Identity and Access Management (IAM), so you can use IAM to manage access to your containers.

**Use Cases:**

*   **Microservices:** Deploy and manage microservices-based applications.
*   **Batch processing:** Run batch processing workloads.
*   **Web applications:** Deploy and scale web applications.


### Q41: What is the difference between Amazon ECS and Amazon EKS?
**Difficulty: Hard**

**Answer:**

**Amazon ECS (Elastic Container Service)** and **Amazon EKS (Elastic Kubernetes Service)** are both powerful container orchestration services from AWS, but they cater to different needs and preferences.

Here’s a breakdown of their key differences:

| Feature | Amazon ECS | Amazon EKS |
| :--- | :--- | :--- |
| **Orchestration Engine** | AWS-proprietary | Kubernetes (Open-source) |
| **Control Plane** | Fully managed by AWS | Managed Kubernetes control plane, but requires more configuration. |
| **Ease of Use** | Simpler to set up and manage, deeply integrated with AWS services. | Steeper learning curve, but offers more flexibility and a larger open-source community. |
| **Networking** | Simpler networking model with AWS VPC. | More complex networking with CNI plugins (e.g., Calico, Weave Net). |
| **Ecosystem** | Tightly integrated with AWS services like IAM, CloudWatch, and ALB. | Benefits from the vast Kubernetes ecosystem, tools, and community support. |
| **Portability** | Workloads are specific to the AWS ecosystem. | Highly portable across any Kubernetes-conformant environment (on-premises, other clouds). |

**Key Takeaways:**

*   **Choose Amazon ECS if:**
    *   You are new to containers and want a simpler, more straightforward solution.
    *   Your architecture is heavily reliant on other AWS services.
    *   You prefer a fully managed, hands-off approach.

*   **Choose Amazon EKS if:**
    *   You want to leverage the power and flexibility of Kubernetes.
    *   You need a solution that is portable across multiple cloud providers or on-premises.
    *   You have an existing investment in the Kubernetes ecosystem and tooling.


### Q42: What is AWS Fargate?
**Difficulty: Medium**

**Answer:**

**AWS Fargate** is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

**How it works:**

With Fargate, you don’t need to provision, configure, or scale groups of virtual machines to run containers. You also don’t need to choose server types, decide when to scale your node groups, or optimize cluster packing. You can control scheduling of your containers and Fargate handles the rest.

**Benefits:**

*   **Serverless:** No servers to manage. Fargate removes the need to provision and manage servers.
*   **Scalable:** Fargate scales automatically to meet the demands of your applications.
*   **Secure:** Fargate provides strong security isolation between your containers.
*   **Cost-effective:** You only pay for the resources that your applications use.

**Use Cases:**

*   **Microservices:** Deploy and manage microservices-based applications.
*   **Web applications:** Deploy and scale web applications.
*   **Batch processing:** Run batch processing workloads.


### Q43: What is AWS CloudFormation?
**Difficulty: Medium**

**Answer:**

**AWS CloudFormation** is a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you.

**How it works:**

1.  **Create a template:** You create a template file (in YAML or JSON format) that defines the AWS resources you want to create.
2.  **Create a stack:** You upload the template to CloudFormation and create a stack. A stack is a collection of AWS resources that you can manage as a single unit.
3.  **CloudFormation provisions resources:** CloudFormation reads your template and provisions the resources in your AWS account.

**Benefits:**

*   **Infrastructure as Code (IaC):** Treat your infrastructure as code, which means you can version control it, review it, and share it with others.
*   **Automation:** Automate the process of setting up and managing your AWS resources.
*   **Consistency:** Ensure that your AWS resources are created in a consistent and repeatable way.
*   **Management:** Manage your AWS resources as a single unit (a stack).

**Example CloudFormation Template (YAML):**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A simple EC2 instance.
Resources:
  MyEC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c55b159cbfafe1f0 # Amazon Linux 2 AMI
      KeyName: my-key-pair
```


### Q44: What is AWS CDK and how does it differ from CloudFormation?
**Difficulty: Hard**

**Answer:**

**AWS Cloud Development Kit (CDK)** is an open-source software development framework to define your cloud application resources using familiar programming languages. AWS CDK provisions your resources in a safe, repeatable manner through AWS CloudFormation.

**How it differs from CloudFormation:**

| Feature | AWS CloudFormation | AWS CDK |
| :--- | :--- | :--- |
| **Language** | Declarative (YAML or JSON) | Imperative (TypeScript, Python, Java, .NET, Go) |
| **Abstraction** | Low-level, requires defining every resource property explicitly. | High-level, provides constructs that encapsulate boilerplate code and best practices. |
| **Logic** | Limited logic capabilities (e.g., conditions, parameters). | Full programming language capabilities (loops, conditionals, functions, objects). |
| **Reusability** | Reusability through modules and nested stacks. | Higher reusability through classes, libraries, and package managers. |
| **Development Experience** | Writing and debugging large templates can be cumbersome. | Familiar IDEs, code completion, and testing frameworks improve developer productivity. |

**Key Takeaways:**

*   **CloudFormation** is the underlying provisioning engine for both. It provides the foundation for IaC on AWS.
*   **AWS CDK** is a higher-level abstraction that makes it easier and faster to define cloud resources, especially for complex applications.
*   You can think of the CDK as a “compiler” that generates CloudFormation templates from your code.

**Example AWS CDK Code (TypeScript):**

```typescript
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';

const app = new cdk.App();
const stack = new cdk.Stack(app, 'MyStack');

new ec2.Instance(stack, 'MyInstance', {
  instanceType: new ec2.InstanceType('t2.micro'),
  machineImage: new ec2.AmazonLinuxImage(),
});
```

This CDK code will synthesize into a CloudFormation template similar to the one in the previous question.


### Q45: What is AWS SAM?
**Difficulty: Medium**

**Answer:**

**AWS Serverless Application Model (SAM)** is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster.

**Key Features:**

*   **Simplified Syntax:** SAM provides a simplified syntax for defining serverless resources, which makes it easier to write and manage your templates.
*   **Local Testing and Debugging:** The SAM CLI allows you to test and debug your serverless applications locally, before deploying them to the cloud.
*   **Built-in Best Practices:** SAM incorporates best practices for building serverless applications, such as creating IAM roles with the least privilege.
*   **Integration with Development Tools:** SAM integrates with popular development tools, such as the AWS Toolkit for VS Code, which provides a seamless development experience.

**Example SAM Template (YAML):**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'
Description: A simple serverless application.
Resources:
  MyFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: index.handler
      Runtime: nodejs16.x
      CodeUri: ./my-function
      Events:
        MyApi:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

This SAM template defines a simple serverless application with a single Lambda function and an API Gateway endpoint.


### Q46: What is AWS CodeCommit?
**Difficulty: Easy**

**Answer:**

**AWS CodeCommit** is a fully-managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.

**Benefits:**

*   **Fully Managed:** No hardware to provision and scale, and no software to install, configure, and operate.
*   **Secure:** CodeCommit automatically encrypts your files in transit and at rest.
*   **Highly Available:** CodeCommit is built on a highly available and durable architecture.
*   **Scalable:** CodeCommit is designed to scale to meet the needs of your projects.
*   **Integrated:** CodeCommit is integrated with other AWS services, such as AWS CodePipeline and AWS CodeBuild.

**How it works:**

1.  **Create a repository:** You create a CodeCommit repository in the AWS Management Console.
2.  **Configure your Git client:** You configure your Git client to connect to the CodeCommit repository.
3.  **Push your code:** You push your code to the CodeCommit repository.


### Q47: What is AWS CodeBuild?
**Difficulty: Easy**

**Answer:**

**AWS CodeBuild** is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue.

**Benefits:**

*   **Fully Managed:** No build servers to set up or manage.
*   **Pay-as-you-go:** You pay only for the build time you consume.
*   **Scalable and Concurrent:** Runs your builds in parallel and scales automatically.
*   **Extensible:** You can customize build environments with Docker images.

**How it works:**

1.  **Provide Source Code:** You point CodeBuild to your source code repository (e.g., AWS CodeCommit, GitHub, Bitbucket).
2.  **Define Build Spec:** You create a `buildspec.yml` file in the root of your source code that tells CodeBuild how to build and test your code.
3.  **Run Build:** CodeBuild uses the build spec to run your build in a clean, isolated container.
4.  **Produce Artifacts:** CodeBuild uploads the output of your build (e.g., a JAR file, a Docker image) to an S3 bucket.


### Q48: What is AWS CodeDeploy?
**Difficulty: Easy**

**Answer:**

**AWS CodeDeploy** is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers. CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications.

**Benefits:**

*   **Automated Deployments:** Automates the deployment of your applications, which reduces the risk of human error.
*   **Minimized Downtime:** Supports rolling deployments and blue/green deployments, which help to minimize downtime.
*   **Centralized Control:** Provides a centralized place to manage your deployments.
*   **Easy to Adopt:** Works with any application and is easy to get started with.

**How it works:**

1.  **Create a Deployment Group:** You create a deployment group, which is a set of instances where you want to deploy your application.
2.  **Specify the Application Revision:** You specify the application revision, which is the version of your application that you want to deploy.
3.  **Create a Deployment:** You create a deployment, which tells CodeDeploy to deploy the application revision to the deployment group.


### Q49: What is AWS CodePipeline?
**Difficulty: Easy**

**Answer:**

**AWS CodePipeline** is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.

**Benefits:**

*   **Automated Release Process:** Automates your software release process, allowing you to build, test, and deploy your applications quickly and reliably.
*   **Consistent Release Process:** Enforces a consistent release process, which helps to reduce the risk of errors.
*   **Fast Delivery:** Enables you to deliver new features to your users faster.
*   **Easy to Integrate:** Integrates with other AWS services and third-party tools.

**How it works:**

1.  **Create a Pipeline:** You create a pipeline in the AWS Management Console.
2.  **Define the Stages:** You define the stages of your pipeline, such as source, build, test, and deploy.
3.  **Configure the Actions:** You configure the actions for each stage, such as pulling code from a repository, building the code, running tests, and deploying the application.
4.  **Start the Pipeline:** You start the pipeline, and CodePipeline automates the release process.


### Q50: How do AWS CodeCommit, CodeBuild, CodeDeploy, and CodePipeline work together?
**Difficulty: Hard**

**Answer:**

AWS CodeCommit, CodeBuild, CodeDeploy, and CodePipeline are a suite of services designed to help you practice DevOps and automate your software release process. They are often used together to create a full CI/CD (Continuous Integration/Continuous Delivery) pipeline on AWS.

Here’s how they work together:

1.  **AWS CodeCommit (Source Stage):**
    *   **Role:** Source Code Storage.
    *   **Process:** A developer pushes code changes to a Git repository hosted on AWS CodeCommit. This action can trigger the start of the pipeline.

2.  **AWS CodePipeline (Orchestration):**
    *   **Role:** Workflow Orchestration.
    *   **Process:** CodePipeline detects the change in the CodeCommit repository and starts the release process you've defined. It orchestrates the entire workflow, moving the code from one stage to the next.

3.  **AWS CodeBuild (Build Stage):**
    *   **Role:** Build and Test.
    *   **Process:** CodePipeline sends the source code to AWS CodeBuild. CodeBuild compiles the code, runs unit tests, and produces deployment artifacts (e.g., a JAR file, a Docker image). The `buildspec.yml` file defines these build commands.

4.  **AWS CodeDeploy (Deploy Stage):**
    *   **Role:** Application Deployment.
    *   **Process:** If the build and tests are successful, CodePipeline takes the artifacts from CodeBuild and passes them to AWS CodeDeploy. CodeDeploy then automates the deployment of the application to your specified compute environment (EC2, Fargate, Lambda, or on-premises servers). It handles the complexities of deployments, such as blue/green deployments, to minimize downtime.

**Visualizing the Workflow:**

```
[Developer] -> git push -> [CodeCommit] -> triggers -> [CodePipeline]
                                                          |
                                                          v
                                                     [CodeBuild]
                                                          |
                                                          v
                                                     [CodeDeploy]
                                                          |
                                                          v
                                                  [EC2/Fargate/Lambda]
```

In summary, **CodePipeline** is the orchestrator that connects the other services. **CodeCommit** is the starting point where your code lives. **CodeBuild** compiles and tests your code. And **CodeDeploy** puts your application into production.


### Q51: How do you automate AWS infrastructure management using AWS CLI?
**Difficulty: Advanced**

**Answer:**
To automate AWS infrastructure management, we can use AWS CLI scripts combined with CloudFormation. Below is a comprehensive management script example.

**AWS CLI Management Scripts:**

```bash
#!/bin/bash
# AWS Infrastructure Management Script

# Set variables
ENVIRONMENT="production"
REGION="us-east-1"
STACK_NAME="${ENVIRONMENT}-infrastructure"
TEMPLATE_FILE="infrastructure.yaml"
PARAMETERS_FILE="parameters.json"

# === AWS CONFIGURATION ===

# Configure AWS CLI
echo "🔧 Configuring AWS CLI..."
aws configure set region $REGION
aws configure set output json

# Verify AWS credentials
echo "🔍 Verifying AWS credentials..."
aws sts get-caller-identity

if [ $? -ne 0 ]; then
    echo "❌ AWS credentials not configured properly"
    exit 1
fi

# === CLOUDFORMATION OPERATIONS ===

# Function to deploy CloudFormation stack
deploy_stack() {
    echo "🚀 Deploying CloudFormation stack: $STACK_NAME"
    
    # Validate template
    echo "✅ Validating CloudFormation template..."
    aws cloudformation validate-template \
        --template-body file://$TEMPLATE_FILE
    
    if [ $? -ne 0 ]; then
        echo "❌ Template validation failed"
        exit 1
    fi
    
    # Check if stack exists
    aws cloudformation describe-stacks \
        --stack-name $STACK_NAME \
        --region $REGION > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "📝 Updating existing stack..."
        aws cloudformation update-stack \
            --stack-name $STACK_NAME \
            --template-body file://$TEMPLATE_FILE \
            --parameters file://$PARAMETERS_FILE \
            --capabilities CAPABILITY_NAMED_IAM \
            --region $REGION
    else
        echo "🆕 Creating new stack..."
        aws cloudformation create-stack \
            --stack-name $STACK_NAME \
            --template-body file://$TEMPLATE_FILE \
            --parameters file://$PARAMETERS_FILE \
            --capabilities CAPABILITY_NAMED_IAM \
            --enable-termination-protection \
            --region $REGION
    fi
    
    # Wait for stack operation to complete
    echo "⏳ Waiting for stack operation to complete..."
    aws cloudformation wait stack-update-complete \
        --stack-name $STACK_NAME \
        --region $REGION
    
    if [ $? -eq 0 ]; then
        echo "✅ Stack operation completed successfully"
    else
        echo "❌ Stack operation failed"
        aws cloudformation describe-stack-events \
            --stack-name $STACK_NAME \
            --region $REGION \
            --query 'StackEvents[?ResourceStatus==`CREATE_FAILED` || ResourceStatus==`UPDATE_FAILED`]'
        exit 1
    fi
}

# Function to delete CloudFormation stack
delete_stack() {
    echo "🗑️  Deleting CloudFormation stack: $STACK_NAME"
    
    # Disable termination protection
    aws cloudformation update-termination-protection \
        --stack-name $STACK_NAME \
        --no-enable-termination-protection \
        --region $REGION
    
    # Delete stack
    aws cloudformation delete-stack \
        --stack-name $STACK_NAME \
        --region $REGION
    
    # Wait for deletion to complete
    echo "⏳ Waiting for stack deletion to complete..."
    aws cloudformation wait stack-delete-complete \
        --stack-name $STACK_NAME \
        --region $REGION
    
    echo "✅ Stack deleted successfully"
}

# Function to get stack outputs
get_outputs() {
    echo "📋 Getting stack outputs..."
    aws cloudformation describe-stacks \
        --stack-name $STACK_NAME \
        --region $REGION \
        --query 'Stacks[0].Outputs' \
        --output table
}

# Function to get stack resources
get_resources() {
    echo "📦 Getting stack resources..."
    aws cloudformation list-stack-resources \
        --stack-name $STACK_NAME \
        --region $REGION \
        --output table
}

# === EC2 OPERATIONS ===

# Function to list EC2 instances
list_instances() {
    echo "🖥️  Listing EC2 instances..."
    aws ec2 describe-instances \
        --filters "Name=tag:Environment,Values=$ENVIRONMENT" \
        --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PublicIpAddress,PrivateIpAddress,Tags[?Key==`Name`].Value|[0]]' \
        --output table \
        --region $REGION
}

# Function to get instance health
get_instance_health() {
    echo "🏥 Checking instance health..."
    
    # Get Auto Scaling Group instances
    ASG_NAME="${ENVIRONMENT}-web-asg"
    aws autoscaling describe-auto-scaling-groups \
        --auto-scaling-group-names $ASG_NAME \
        --query 'AutoScalingGroups[0].Instances[*].[InstanceId,HealthStatus,LifecycleState]' \
        --output table \
        --region $REGION
    
    # Get Load Balancer target health
    TARGET_GROUP_ARN=$(aws elbv2 describe-target-groups \
        --names "${ENVIRONMENT}-web-tg" \
        --query 'TargetGroups[0].TargetGroupArn' \
        --output text \
        --region $REGION)
    
    if [ "$TARGET_GROUP_ARN" != "None" ]; then
        echo "🎯 Target Group Health:"
        aws elbv2 describe-target-health \
            --target-group-arn $TARGET_GROUP_ARN \
            --query 'TargetHealthDescriptions[*].[Target.Id,TargetHealth.State,TargetHealth.Description]' \
            --output table \
            --region $REGION
    fi
}

# === RDS OPERATIONS ===

# Function to get RDS status
get_rds_status() {
    echo "🗄️  Getting RDS status..."
    aws rds describe-db-instances \
        --db-instance-identifier "${ENVIRONMENT}-database" \
        --query 'DBInstances[0].[DBInstanceIdentifier,DBInstanceStatus,Engine,EngineVersion,AllocatedStorage,DBInstanceClass,MultiAZ]' \
        --output table \
        --region $REGION
}

# Function to create RDS snapshot
create_rds_snapshot() {
    SNAPSHOT_ID="${ENVIRONMENT}-database-$(date +%Y%m%d%H%M%S)"
    echo "📸 Creating RDS snapshot: $SNAPSHOT_ID"
    
    aws rds create-db-snapshot \
        --db-instance-identifier "${ENVIRONMENT}-database" \
        --db-snapshot-identifier $SNAPSHOT_ID \
        --region $REGION
    
    echo "⏳ Waiting for snapshot to complete..."
    aws rds wait db-snapshot-completed \
        --db-snapshot-identifier $SNAPSHOT_ID \
        --region $REGION
    
    echo "✅ Snapshot created successfully: $SNAPSHOT_ID"
}

# === S3 OPERATIONS ===

# Function to sync files to S3
sync_to_s3() {
    BUCKET_NAME="${ENVIRONMENT}-app-assets-$(aws sts get-caller-identity --query Account --output text)-${REGION}"
    LOCAL_PATH="./assets/"
    
    echo "📤 Syncing files to S3 bucket: $BUCKET_NAME"
    
    if [ -d "$LOCAL_PATH" ]; then
        aws s3 sync $LOCAL_PATH s3://$BUCKET_NAME/ \
            --delete \
            --exclude "*.tmp" \
            --exclude ".DS_Store" \
            --region $REGION
        
        echo "✅ Files synced successfully"
    else
        echo "⚠️  Local assets directory not found: $LOCAL_PATH"
    fi
}

# === MONITORING ===

# Function to get CloudWatch metrics
get_metrics() {
    echo "📊 Getting CloudWatch metrics..."
    
    # CPU Utilization
    echo "CPU Utilization (last 1 hour):"
    aws cloudwatch get-metric-statistics \
        --namespace AWS/EC2 \
        --metric-name CPUUtilization \
        --dimensions Name=AutoScalingGroupName,Value="${ENVIRONMENT}-web-asg" \
        --statistics Average \
        --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
        --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
        --period 300 \
        --query 'Datapoints[*].[Timestamp,Average]' \
        --output table \
        --region $REGION
    
    # ALB Request Count
    ALB_ARN=$(aws elbv2 describe-load-balancers \
        --names "${ENVIRONMENT}-alb" \
        --query 'LoadBalancers[0].LoadBalancerArn' \
        --output text \
        --region $REGION)
    
    if [ "$ALB_ARN" != "None" ]; then
        echo "\nALB Request Count (last 1 hour):"
        aws cloudwatch get-metric-statistics \
            --namespace AWS/ApplicationELB \
            --metric-name RequestCount \
            --dimensions Name=LoadBalancer,Value=$(echo $ALB_ARN | cut -d'/' -f2-) \
            --statistics Sum \
            --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
            --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
            --period 300 \
            --query 'Datapoints[*].[Timestamp,Sum]' \
            --output table \
            --region $REGION
    fi
}

# Function to get recent CloudWatch alarms
get_alarms() {
    echo "🚨 Getting CloudWatch alarms..."
    aws cloudwatch describe-alarms \
        --alarm-name-prefix $ENVIRONMENT \
        --query 'MetricAlarms[*].[AlarmName,StateValue,StateReason]' \
        --output table \
        --region $REGION
}

# === COST ANALYSIS ===

# Function to get cost and usage
get_costs() {
    echo "💰 Getting cost information..."
    
    # Get current month costs
    START_DATE=$(date +%Y-%m-01)
    END_DATE=$(date +%Y-%m-%d)
    
    aws ce get-cost-and-usage \
        --time-period Start=$START_DATE,End=$END_DATE \
        --granularity MONTHLY \
        --metrics BlendedCost \
        --group-by Type=DIMENSION,Key=SERVICE \
        --query 'ResultsByTime[0].Groups[?Metrics.BlendedCost.Amount>`1`].[Keys[0],Metrics.BlendedCost.Amount,Metrics.BlendedCost.Unit]' \
        --output table
}

# === SECURITY ===

# Function to check security groups
check_security() {
    echo "🔒 Checking security configuration..."
    
    # List security groups with open access
    echo "Security groups with open access (0.0.0.0/0):"
    aws ec2 describe-security-groups \
        --filters "Name=tag:Environment,Values=$ENVIRONMENT" \
        --query 'SecurityGroups[?IpPermissions[?IpRanges[?CidrIp==`0.0.0.0/0`]]].[GroupId,GroupName,Description]' \
        --output table \
        --region $REGION
    
    # Check for unused security groups
    echo "\nUnused security groups:"
    aws ec2 describe-security-groups \
        --filters "Name=tag:Environment,Values=$ENVIRONMENT" \
        --query 'SecurityGroups[?length(IpPermissionsEgress)==`1` && IpPermissionsEgress[0].IpRanges[0].CidrIp==`0.0.0.0/0` && length(IpPermissions)==`0`].[GroupId,GroupName]' \
        --output table \
        --region $REGION
}

# === BACKUP AND DISASTER RECOVERY ===

# Function to create AMI backup
create_ami_backup() {
    echo "💾 Creating AMI backups..."
    
    # Get running instances
    INSTANCE_IDS=$(aws ec2 describe-instances \
        --filters "Name=tag:Environment,Values=$ENVIRONMENT" "Name=instance-state-name,Values=running" \
        --query 'Reservations[*].Instances[*].InstanceId' \
        --output text \
        --region $REGION)
    
    for INSTANCE_ID in $INSTANCE_IDS; do
        AMI_NAME="${ENVIRONMENT}-${INSTANCE_ID}-$(date +%Y%m%d%H%M%S)"
        echo "Creating AMI for instance $INSTANCE_ID: $AMI_NAME"
        
        aws ec2 create-image \
            --instance-id $INSTANCE_ID \
            --name $AMI_NAME \
            --description "Automated backup of $INSTANCE_ID" \
            --no-reboot \
            --region $REGION
    done
}

# === MAIN SCRIPT ===

case "$1" in
    deploy)
        deploy_stack
        ;;
    delete)
        delete_stack
        ;;
    outputs)
        get_outputs
        ;;
    resources)
        get_resources
        ;;
    instances)
        list_instances
        ;;
    health)
        get_instance_health
        ;;
    rds)
        get_rds_status
        ;;
    snapshot)
        create_rds_snapshot
        ;;
    sync)
        sync_to_s3
        ;;
    metrics)
        get_metrics
        ;;
    alarms)
        get_alarms
        ;;
    costs)
        get_costs
        ;;
    security)
        check_security
        ;;
    backup)
        create_ami_backup
        ;;
    status)
        echo "📊 Infrastructure Status Report"
        echo "================================"
        get_outputs
        echo "\n"
        list_instances
        echo "\n"
        get_instance_health
        echo "\n"
        get_rds_status
        echo "\n"
        get_alarms
        ;;
    *)
        echo "Usage: $0 {deploy|delete|outputs|resources|instances|health|rds|snapshot|sync|metrics|alarms|costs|security|backup|status}"
        echo ""
        echo "Commands:"
        echo "  deploy    - Deploy CloudFormation stack"
        echo "  delete    - Delete CloudFormation stack"
        echo "  outputs   - Show stack outputs"
        echo "  resources - Show stack resources"
        echo "  instances - List EC2 instances"
        echo "  health    - Check instance health"
        echo "  rds       - Show RDS status"
        echo "  snapshot  - Create RDS snapshot"
        echo "  sync      - Sync files to S3"
        echo "  metrics   - Show CloudWatch metrics"
        echo "  alarms    - Show CloudWatch alarms"
        echo "  costs     - Show cost information"
        echo "  security  - Check security configuration"
        echo "  backup    - Create AMI backups"
        echo "  status    - Show complete infrastructure status"
        exit 1
        ;;
esac

echo "\n✅ Operation completed successfully!"
```

**AWS Global Infrastructure Benefits:**

1. **High Availability**: Multiple AZs within regions
2. **Disaster Recovery**: Cross-region replication
3. **Low Latency**: Edge locations worldwide
4. **Scalability**: Auto-scaling capabilities
5. **Security**: Multiple layers of security
6. **Compliance**: Various compliance certifications
7. **Cost Optimization**: Pay-as-you-use model
8. **Global Reach**: Presence in multiple countries

**Key Components:**
- **Regions**: Geographic areas with multiple AZs
- **Availability Zones**: Isolated data centers
- **Edge Locations**: Content delivery network points
- **Regional Edge Caches**: Larger caching locations
- **Local Zones**: Ultra-low latency for specific metros
- **Wavelength**: 5G edge computing

---

This comprehensive AWS guide covers infrastructure design, automation, monitoring, and best practices for cloud-native applications.
### Q52: What is AWS Step Functions and when should you use it?
**Difficulty: Medium**

**Answer:**
AWS Step Functions is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build business-critical applications. It allows you to coordinate multiple AWS services into serverless workflows.

**Key Features:**
- **State Machines:** Define workflows as state machines using Amazon States Language (ASL).
- **Visual Workflows:** visually configure and monitor workflows.
- **Error Handling:** Built-in try/catch/retry logic.
- **Long-running processes:** Can run for up to 1 year (Standard Workflows).

**Use Cases:**
- Microservices orchestration
- Data processing pipelines
- IT automation
- Human-in-the-loop approval processes

```json
// Example: Step Functions State Machine Definition (ASL)
{
  "Comment": "Order Processing Workflow",
  "StartAt": "ValidateOrder",
  "States": {
    "ValidateOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ValidateOrder",
      "Next": "ProcessPayment",
      "Catch": [ {
        "ErrorEquals": ["OrderInvalid"],
        "Next": "NotifyFailure"
      } ]
    },
    "ProcessPayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ProcessPayment",
      "Next": "ShipItem",
      "Retry": [ {
        "ErrorEquals": ["PaymentServiceUnavailable"],
        "IntervalSeconds": 3,
        "MaxAttempts": 2
      } ]
    },
    "ShipItem": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ShipItem",
      "End": true
    },
    "NotifyFailure": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:NotifyFailure",
      "End": true
    }
  }
}
```

### Q53: What is Amazon EventBridge and how does it differ from CloudWatch Events?
**Difficulty: Medium**

**Answer:**
Amazon EventBridge is a serverless event bus service that makes it easy to connect applications together using data from your own applications, Integrated SaaS applications, and AWS services. It is the evolution of CloudWatch Events.

**Key Differences:**
- **SaaS Integration:** EventBridge can ingest events directly from partner SaaS applications (e.g., Datadog, Zendesk).
- **Schema Registry:** Discover, create, and manage schemas for events.
- **Custom Event Buses:** Create custom buses for application-specific events.

**Core Concepts:**
- **Event Bus:** Receives events. Default bus (AWS services), Custom bus, Partner bus.
- **Rules:** Match incoming events and route them to targets.
- **Targets:** AWS services (Lambda, SQS, SNS, Kinesis) that process events.

```yaml
# CloudFormation: EventBridge Rule
EventRule:
  Type: AWS::Events::Rule
  Properties:
    Name: OrderCreatedRule
    EventBusName: default
    EventPattern:
      source:
        - "com.mycompany.orders"
      detail-type:
        - "OrderCreated"
      detail:
        status:
          - "created"
    State: ENABLED
    Targets:
      - Arn: !GetAtt OrderProcessingLambda.Arn
        Id: OrderProcessingTarget
```

### Q54: Compare Amazon SQS, SNS, and Kinesis.
**Difficulty: Hard**

**Answer:**
| Feature | Amazon SQS (Simple Queue Service) | Amazon SNS (Simple Notification Service) | Amazon Kinesis Data Streams |
|---------|-----------------------------------|------------------------------------------|-----------------------------|
| **Pattern** | Queue (Point-to-Point) | Pub/Sub (Publish-Subscribe) | Streaming (Real-time data) |
| **Consumption** | Pull (Polling) | Push (to subscribers) | Pull (Polling by shards) |
| **Persistence** | Configurable (up to 14 days) | No persistence (unless delivery fails) | Configurable (up to 365 days) |
| **Ordering** | Standard: Best-effort; FIFO: Strict | Standard: No; FIFO: Strict | Strict ordering per shard |
| **Throughput** | Standard: Unlimited; FIFO: 300/3000 TPS | Standard: Unlimited; FIFO: 300/3000 TPS | Defined by number of shards |
| **Use Case** | Decoupling microservices, buffering | Broadcasting messages, fan-out | Real-time analytics, log ingestion |

### Q55: What are the different types of API Gateway endpoints?
**Difficulty: Medium**

**Answer:**
Amazon API Gateway supports three types of endpoint deployments:

1.  **Edge-Optimized:**
    -   Best for geographically distributed clients.
    -   Requests are routed to the nearest CloudFront Point of Presence (PoP).
    -   Default for REST APIs.

2.  **Regional:**
    -   Best for clients in the same region (e.g., EC2 instances).
    -   Reduces latency if client and API are in the same region.
    -   Can be used with your own CloudFront distribution for custom WAF/caching requirements.

3.  **Private:**
    -   Accessible only from within an Amazon VPC using Interface VPC Endpoints (PrivateLink).
    -   Secure communication for internal microservices.

### Q56: What are Lambda Layers and why should you use them?
**Difficulty: Easy**

**Answer:**
Lambda Layers are a distribution mechanism for libraries, custom runtimes, and other function dependencies. A layer is a ZIP archive that contains libraries or other dependencies.

**Benefits:**
- **Code Reusability:** Share code (e.g., SDKs, common utils) across multiple functions.
- **Smaller Deployment Packages:** Keep your function code small and focused on business logic.
- **Separation of Responsibilities:** Update dependencies independently of function code.

**Usage:**
- You can configure a Lambda function to use up to 5 layers.
- Layers are extracted to the `/opt` directory in the function execution environment.

### Q57: How do DynamoDB Global Tables work?
**Difficulty: Medium**

**Answer:**
DynamoDB Global Tables provide a fully managed, multi-region, and multi-active database. It automatically replicates data across your choice of AWS Regions.

**Key Characteristics:**
- **Multi-Active:** You can read and write to the table in any replica region.
- **Replication:** Uses DynamoDB Streams to replicate changes to other regions asynchronously.
- **Conflict Resolution:** Uses "Last Writer Wins" based on timestamps.
- **Setup:** Requires DynamoDB Streams to be enabled (New and Old Images).

**Use Case:**
- Global applications requiring low-latency local access.
- Disaster recovery with near-zero RTO/RPO.

### Q58: What are DynamoDB Streams?
**Difficulty: Medium**

**Answer:**
DynamoDB Streams captures a time-ordered sequence of item-level modifications in a DynamoDB table and stores this information in a log for up to 24 hours.

**Stream Records:**
- **KEYS_ONLY:** Only the key attributes of the modified item.
- **NEW_IMAGE:** The entire item as it appears after it was modified.
- **OLD_IMAGE:** The entire item as it appeared before it was modified.
- **NEW_AND_OLD_IMAGES:** Both the new and the old images of the item.

**Common Pattern:**
- Trigger a Lambda function to process changes (e.g., update a search index in OpenSearch, send a welcome email on new user creation, replicate data).

### Q59: Compare Amazon Cognito User Pools and Identity Pools.
**Difficulty: Medium**

**Answer:**
| Feature | Cognito User Pools | Cognito Identity Pools (Federated Identities) |
|---------|--------------------|-----------------------------------------------|
| **Primary Function** | Authentication (Sign-up/Sign-in) | Authorization (Access AWS Resources) |
| **Identity Source** | Directory of users managed by Cognito | Users from User Pools or external IdPs (Google, FB, SAML) |
| **Output** | JSON Web Tokens (JWT) | Temporary AWS Credentials (STS) |
| **Use Case** | specific app login, handling user profiles | Giving users access to S3 buckets, DynamoDB, etc. |

**Typical Flow:**
1. User authenticates with User Pool -> Receives JWT.
2. App exchanges JWT with Identity Pool -> Receives AWS Credentials.
3. App uses AWS Credentials to access AWS services directly.

### Q60: What is AWS AppSync?
**Difficulty: Medium**

**Answer:**
AWS AppSync is a managed service that uses GraphQL to make it easy for applications to get exactly the data they need. It simplifies building applications by letting you create a flexible API to securely access, manipulate, and combine data from one or more data sources.

**Key Features:**
- **GraphQL Support:** Schemas, Resolvers, Queries, Mutations, Subscriptions.
- **Real-time:** Built-in support for real-time data updates via WebSockets (Subscriptions).
- **Offline Support:** Data caching and synchronization for offline clients.
- **Data Sources:** Native integration with DynamoDB, Lambda, OpenSearch, Aurora, and HTTP endpoints.

```graphql
# Example GraphQL Schema
type Todo {
  id: ID!
  name: String!
  completed: Boolean!
}

type Query {
  getTodos: [Todo]
}

type Mutation {
  addTodo(name: String!): Todo
}

type Subscription {
  onAddTodo: Todo
    @aws_subscribe(mutations: ["addTodo"])
}
```

### Q61: What is Amazon Athena?
**Difficulty: Easy**

**Answer:**
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

**Key Features:**
- **Serverless:** No ETL or cluster management required.
- **Standard SQL:** Uses PrestoDB engine.
- **Integration:** Works directly with data stored in S3 (JSON, CSV, Parquet, ORC).
- **Glue Data Catalog:** Uses the Data Catalog to store table metadata.

**Performance Tip:**
- Use columnar data formats like Apache Parquet or ORC.
- Partition data in S3 (e.g., by year/month/day) to reduce the amount of data scanned.

### Q62: What is AWS Glue and its components?
**Difficulty: Medium**

**Answer:**
AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics.

**Components:**
1.  **Data Catalog:** A central metadata repository (Hive Metastore compatible).
2.  **Crawlers:** Automatically scan data sources (S3, RDS, DynamoDB) to infer schema and populate the Data Catalog.
3.  **Jobs:** Python or Scala scripts (Spark-based) that perform the ETL work.
4.  **Triggers:** Schedule or event-driven mechanisms to start jobs.

### Q63: What is Amazon Redshift Spectrum?
**Difficulty: Advanced**

**Answer:**
Amazon Redshift Spectrum is a feature of Amazon Redshift that allows you to run queries against exabytes of unstructured data in Amazon S3 without having to load the data into Redshift tables.

**How it works:**
- You define an external table in Redshift that points to data in S3.
- When you query the external table, the Redshift query optimizer delegates the processing to the Spectrum layer (thousands of nodes).
- Results are aggregated and sent back to the Redshift cluster.

**Use Case:**
- Offloading cold data to S3 while keeping hot data in Redshift SSDs.
- Querying data lake data alongside data warehouse data.

### Q64: Compare Kinesis Data Streams and Kinesis Data Firehose.
**Difficulty: Medium**

**Answer:**
| Feature | Kinesis Data Streams (KDS) | Kinesis Data Firehose (KDF) |
|---------|----------------------------|-----------------------------|
| **Purpose** | Real-time streaming storage & processing | Load streaming data into data stores |
| **Latency** | Sub-second (Real-time) | Near real-time (Buffer interval 60s+) |
| **Management** | Manual scaling (shards) | Fully managed (Auto-scaling) |
| **Consumption** | Custom consumers (KCL, Lambda) | Configure destinations (S3, Redshift, OpenSearch) |
| **Retention** | 24 hours to 365 days | No retention (Delivery focused) |

### Q65: What is AWS Lake Formation?
**Difficulty: Medium**

**Answer:**
AWS Lake Formation is a service that makes it easy to set up a secure data lake in days. It sits on top of AWS Glue and S3.

**Key Capabilities:**
- **Blueprints:** Templates to ingest data from databases and logs.
- **Security Management:** Define security policies at database, table, and column levels centrally.
- **Access Control:** Granular permissions (e.g., hide PII columns from certain users).
- **Audit:** Logs all access to data.

### Q66: What is Amazon EMR (Elastic MapReduce)?
**Difficulty: Medium**

**Answer:**
Amazon EMR is a cloud big data platform for running large-scale distributed data processing jobs, interactive SQL queries, and machine learning applications using open-source analytics frameworks.

**Supported Frameworks:**
- Apache Spark
- Apache Hadoop
- Apache Hive
- Apache HBase
- Presto
- Flink

**Deployment Options:**
- EMR on EC2 (Classic clusters)
- EMR on EKS (Containerized)
- EMR Serverless (On-demand scaling)

### Q67: What is Amazon OpenSearch Service?
**Difficulty: Medium**

**Answer:**
Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters.

**Use Cases:**
- **Log Analytics:** Aggregating logs (via Fluentd/Logstash) and visualizing in OpenSearch Dashboards (Kibana).
- **Full-Text Search:** Adding search capabilities to applications.
- **Application Monitoring:** Real-time metrics analysis.

**Architecture:**
- **Master Nodes:** Manage cluster state.
- **Data Nodes:** Store data and execute queries.
- **UltraWarm Nodes:** S3-backed storage for cheaper, long-term retention.

### Q68: What is AWS DMS (Database Migration Service)?
**Difficulty: Easy**

**Answer:**
AWS DMS helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime.

**Types of Migration:**
1.  **Homogeneous:** Same engine (e.g., Oracle to Oracle on RDS).
2.  **Heterogeneous:** Different engine (e.g., Oracle to Aurora PostgreSQL) using AWS Schema Conversion Tool (SCT).

**Capabilities:**
- **Full Load:** Migrates existing data.
- **CDC (Change Data Capture):** Replicates ongoing changes to keep source and target in sync.

### Q69: What is Amazon QuickSight?
**Difficulty: Easy**

**Answer:**
Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.

**Key Features:**
- **SPICE:** Super-fast, Parallel, In-memory Calculation Engine.
- **Auto-Graph:** Automatically suggests the best visualization.
- **ML Insights:** Anomaly detection, forecasting, and auto-narratives.
- **Embedded Analytics:** Embed dashboards into applications.

### Q70: What is Amazon MSK?
**Difficulty: Medium**

**Answer:**
Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that makes it easy for you to build and run applications that use Apache Kafka to process streaming data.

**Benefits over self-managed Kafka:**
- Automated provisioning and patching.
- Automated failure recovery of brokers.
- Integration with AWS IAM for security.
- Prometheus metrics integration.

### Q71: What is AWS Transit Gateway?
**Difficulty: Medium**

**Answer:**
AWS Transit Gateway connects VPCs and on-premises networks through a central hub. This simplifies your network and puts an end to complex peering relationships. It acts as a cloud router.

**Benefits:**
- **Simplified Management:** Hub-and-spoke topology.
- **Scalability:** Connect thousands of VPCs.
- **Inter-Region Peering:** Connect Transit Gateways across regions.
- **Multicast Support:** Supports IP multicast.

### Q72: What are VPC Endpoints and what types exist?
**Difficulty: Advanced**

**Answer:**
A VPC Endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

**Types:**
1.  **Interface Endpoints (PrivateLink):**
    -   Elastic Network Interface (ENI) with a private IP in your subnet.
    -   Supports most AWS services (EC2, SNS, Kinesis, etc.).
    -   Powered by AWS PrivateLink.
2.  **Gateway Endpoints:**
    -   A target for a specific route in your route table.
    -   Supports **S3** and **DynamoDB** only.
    -   Free of charge.

### Q73: Compare AWS Direct Connect and AWS VPN.
**Difficulty: Medium**

**Answer:**
| Feature | AWS Site-to-Site VPN | AWS Direct Connect |
|---------|----------------------|--------------------|
| **Connectivity** | Over the public Internet (IPsec encrypted tunnel) | Dedicated physical fiber connection |
| **Setup Time** | Minutes | Weeks/Months |
| **Reliability** | Dependent on Internet path | Consistent, low latency |
| **Throughput** | Up to 1.25 Gbps per tunnel (can aggregate) | 1 Gbps, 10 Gbps, or 100 Gbps ports |
| **Cost** | Lower | Higher (Port hours + Data transfer) |

### Q74: Explain Route 53 Routing Policies.
**Difficulty: Medium**

**Answer:**
Amazon Route 53 offers several routing policies to define how it responds to DNS queries:

1.  **Simple Routing:** Single resource mapping (e.g., one IP).
2.  **Weighted Routing:** Distribute traffic across multiple resources based on assigned weights (e.g., 80% to V1, 20% to V2).
3.  **Latency-based Routing:** Routes traffic to the region with the lowest latency for the user.
4.  **Failover Routing:** Active-Passive failover configuration (Primary/Secondary).
5.  **Geolocation Routing:** Routes based on the location of the user (e.g., EU users to EU servers).
6.  **Geoproximity Routing:** Routes based on geographic location of users and resources (requires Traffic Flow).
7.  **Multivalue Answer Routing:** Returns multiple IP addresses (simple load balancing).

### Q75: Compare VPC Peering and Transit Gateway.
**Difficulty: Medium**

**Answer:**
| Feature | VPC Peering | Transit Gateway |
|---------|-------------|-----------------|
| **Topology** | Mesh (Point-to-Point) | Hub-and-Spoke |
| **Transitive Routing** | No (A<->B<->C does not mean A<->C) | Yes (A<->TGW<->C works) |
| **Complexity** | High complexity at scale (N*(N-1)/2 connections) | Low complexity (Linear connections) |
| **Bandwidth** | Unrestricted (Wire speed) | Up to 50 Gbps per attachment |

### Q76: Compare Amazon EFS and Amazon FSx.
**Difficulty: Medium**

**Answer:**
| Feature | Amazon EFS | Amazon FSx for Windows File Server | Amazon FSx for Lustre |
|---------|------------|------------------------------------|-----------------------|
| **Protocol** | NFSv4 | SMB | Lustre |
| **OS Compatibility** | Linux | Windows (and Linux via SMB) | Linux |
| **Use Case** | General purpose, CMS, Home dirs | Windows-based apps, Active Directory integration | HPC, Machine Learning, Video Processing |
| **Performance** | Scalable throughput | High IOPS/Throughput | Sub-millisecond latencies, massive throughput |

### Q77: What are EC2 Placement Groups?
**Difficulty: Advanced**

**Answer:**
Placement groups determine how instances are placed on underlying hardware to optimize for performance or fault tolerance.

**Strategies:**
1.  **Cluster:**
    -   Packs instances close together inside a single AZ.
    -   **Goal:** Low latency, high network throughput (HPC).
2.  **Partition:**
    -   Spreads instances across logical partitions. Each partition has its own rack/power.
    -   **Goal:** Hadoop, Cassandra, Kafka (Distributed workloads).
3.  **Spread:**
    -   Places each instance on distinct hardware racks.
    -   **Goal:** High availability for critical applications (max 7 per AZ).

### Q78: What are EC2 Spot Instances and when should you use them?
**Difficulty: Easy**

**Answer:**
Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud. They are available at up to a 90% discount compared to On-Demand prices.

**Key Characteristic:** AWS can interrupt (terminate) a Spot Instance with a **2-minute warning** if it needs the capacity back.

**Use Cases:**
- Fault-tolerant, flexible applications.
- Big Data, containerized workloads, CI/CD, web servers behind a load balancer.
- **Not for:** Databases, critical stateful applications.

### Q79: How do S3 Lifecycle Policies work?
**Difficulty: Medium**

**Answer:**
Lifecycle configuration enables you to specify the lifecycle management of objects in a bucket. The configuration is a set of rules.

**Actions:**
1.  **Transition Actions:** Define when objects transition to another storage class.
    -   *Example:* Move to Standard-IA after 30 days, then to Glacier after 90 days.
2.  **Expiration Actions:** Define when objects expire and should be permanently deleted.
    -   *Example:* Delete logs after 365 days.

### Q80: What is AWS Outposts?
**Difficulty: Medium**

**Answer:**
AWS Outposts is a fully managed service that extends AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a truly consistent hybrid experience.

**Use Case:**
- Applications requiring single-digit millisecond latency to on-premises systems.
- Data residency requirements (data must remain on-premises).

### Q81: What is AWS Systems Manager (SSM) and its key capabilities?
**Difficulty: Medium**

**Answer:**
AWS Systems Manager is a secure, end-to-end management solution for hybrid cloud environments.

**Key Capabilities:**
- **Session Manager:** Secure shell access to instances without opening inbound ports (no SSH keys needed).
- **Run Command:** Execute commands across multiple instances at scale.
- **Patch Manager:** Automate patching of OS and applications.
- **Parameter Store:** Store configuration data and secrets (hierarchical storage).

### Q82: Compare AWS Secrets Manager and Systems Manager Parameter Store.
**Difficulty: Medium**

**Answer:**
| Feature | AWS Secrets Manager | SSM Parameter Store |
|---------|---------------------|---------------------|
| **Primary Use** | Managing secrets (DB passwords, API keys) | Managing config data (Strings, StringLists) |
| **Rotation** | Built-in automatic rotation (via Lambda) | No built-in rotation (requires custom setup) |
| **Cost** | Higher ($0.40 per secret/month) | Free (Standard) / Low cost (Advanced) |
| **Cross-Account** | Supported | Supported |
| **Encryption** | KMS (Default) | KMS (SecureString) |

### Q83: What is the difference between AWS KMS and CloudHSM?
**Difficulty: Advanced**

**Answer:**
| Feature | AWS KMS (Key Management Service) | AWS CloudHSM |
|---------|----------------------------------|--------------|
| **Tenancy** | Multi-tenant (Shared hardware) | Single-tenant (Dedicated hardware) |
| **Management** | Managed by AWS | Managed by Customer |
| **Compliance** | FIPS 140-2 Level 2 | FIPS 140-2 Level 3 |
| **Integration** | Integrated with most AWS services | Limited native integration |
| **Cost** | Low | High (Hourly fee per HSM) |

### Q84: Compare AWS CloudTrail and AWS Config.
**Difficulty: Medium**

**Answer:**
| Feature | AWS CloudTrail | AWS Config |
|---------|----------------|------------|
| **Question Answered** | "Who did what, where, and when?" | "What does my infrastructure look like?" |
| **Focus** | API Activity & Auditing | Configuration History & Compliance |
| **Data** | Logs of API calls (CreateBucket, TerminateInstance) | Snapshots of resource configuration |
| **Action** | Detect unauthorized access | Detect non-compliant resources |

### Q85: What is AWS Trusted Advisor?
**Difficulty: Easy**

**Answer:**
AWS Trusted Advisor is an online tool that provides real-time guidance to help you provision your resources following AWS best practices.

**Checks 5 Categories:**
1.  **Cost Optimization:** Idle instances, unattached EBS volumes.
2.  **Performance:** High utilization instances.
3.  **Security:** Open security groups, MFA on root.
4.  **Fault Tolerance:** Snapshots, AZ distribution.
5.  **Service Limits:** Approaching quotas.

### Q86: What are the pillars of the AWS Well-Architected Framework?
**Difficulty: Easy**

**Answer:**
The AWS Well-Architected Framework describes key concepts for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud.

**The 6 Pillars:**
1.  **Operational Excellence:** Running and monitoring systems to deliver business value.
2.  **Security:** Protecting information and systems.
3.  **Reliability:** Ability to recover from failures and meet demand.
4.  **Performance Efficiency:** Using computing resources efficiently.
5.  **Cost Optimization:** Avoiding unnecessary costs.
6.  **Sustainability:** Minimizing the environmental impacts of running cloud workloads.

### Q87: What is Amazon Macie?
**Difficulty: Medium**

**Answer:**
Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data in AWS.

**Function:**
- Automatically scans S3 buckets.
- Identifies PII (Personally Identifiable Information) like names, addresses, credit card numbers.
- Provides dashboards and alerts for data protection.

### Q88: What is Amazon Inspector?
**Difficulty: Medium**

**Answer:**
Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.

**Capabilities:**
- **Network Reachability:** Checks for unintended network accessibility.
- **Host Assessment:** Scans EC2 instances (via SSM Agent) for Common Vulnerabilities and Exposures (CVEs) and CIS Benchmarks.
- **Container Scanning:** Scans container images in ECR for vulnerabilities.

### Q89: What is AWS Service Catalog?
**Difficulty: Medium**

**Answer:**
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS.

**Benefits:**
- **Standardization:** Ensure products are deployed with standard configurations (compliance).
- **Self-Service:** Enable users to launch approved resources without needing full admin permissions.
- **Governance:** Control which users have access to which products.

### Q90: What is AWS Compute Optimizer?
**Difficulty: Easy**

**Answer:**
AWS Compute Optimizer recommends optimal AWS resources for your workloads to reduce costs and improve performance by using machine learning to analyze historical utilization metrics.

**Recommendations for:**
- EC2 instance types
- EBS volumes
- Lambda functions
- ECS services on Fargate

### Q91: Compare AWS Cost Explorer and Cost & Usage Report (CUR).
**Difficulty: Medium**

**Answer:**
| Feature | AWS Cost Explorer | Cost & Usage Report (CUR) |
|---------|-------------------|---------------------------|
| **Purpose** | Visualizing and analyzing costs interactively | Comprehensive raw data for deep analysis |
| **Granularity** | Daily/Monthly (Hourly requires extra cost) | Hourly (most granular) |
| **Format** | Dashboard/Charts | CSV/Parquet files in S3 |
| **Integration** | Native AWS Console | Athena, Redshift, QuickSight |
| **Use Case** | High-level trend analysis, quick checks | Chargeback, custom analytics, detailed auditing |

### Q92: What is AWS Budgets and Cost Anomaly Detection?
**Difficulty: Easy**

**Answer:**
- **AWS Budgets:** Allows you to set custom budgets to track your cost and usage. You can configure alerts (SNS, Email) when your cost or usage exceeds (or is forecasted to exceed) your budgeted amount.
- **Cost Anomaly Detection:** Uses machine learning to continuously monitor your cost and usage to detect unusual spends. It sends alerts with root-cause analysis when anomalies are detected.

### Q93: What is CloudWatch Logs Insights?
**Difficulty: Medium**

**Answer:**
CloudWatch Logs Insights enables you to interactively search and analyze your log data in Amazon CloudWatch Logs.

**Key Features:**
- **Query Language:** Specialized query syntax to filter, aggregate, and sort logs.
- **Speed:** fast queries over massive volumes of log data.
- **Visualization:** Generate charts directly from query results.

```sql
# Example Query: Find 20 most recent error logs
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

### Q94: What is the difference between AWS Shield Standard and Advanced?
**Difficulty: Medium**

**Answer:**
| Feature | AWS Shield Standard | AWS Shield Advanced |
|---------|---------------------|---------------------|
| **Cost** | Free (Automatic) | $3,000/month + Data transfer fees |
| **Protection** | Layer 3/4 (Network/Transport) | Layer 3/4 + Layer 7 (Application) |
| **Support** | Self-service | 24/7 access to AWS DRT (DDoS Response Team) |
| **Visibility** | None | Real-time metrics and reports |
| **Cost Protection** | No | Reimburses bill spikes due to DDoS |

### Q95: What is AWS Firewall Manager?
**Difficulty: Medium**

**Answer:**
AWS Firewall Manager is a security management service which allows you to centrally configure and manage firewall rules across your accounts and applications in AWS Organizations.

**Manages:**
- AWS WAF rules
- AWS Shield Advanced protections
- VPC Security Groups
- AWS Network Firewall

### Q96: What is S3 Object Lock and when would you use it?
**Difficulty: Medium**

**Answer:**
S3 Object Lock enables you to store objects using a "Write Once, Read Many" (WORM) model. It prevents an object from being deleted or overwritten for a fixed amount of time or indefinitely.

**Modes:**
1.  **Governance Mode:** Users need special permissions to overwrite/delete.
2.  **Compliance Mode:** No one (including root user) can overwrite/delete during the retention period.

**Use Case:**
- Regulatory compliance (SEC Rule 17a-4).
- Legal holds.
- Protection against ransomware deletion.

### Q97: Does DynamoDB support ACID transactions?
**Difficulty: Medium**

**Answer:**
Yes, Amazon DynamoDB supports fully ACID (Atomicity, Consistency, Isolation, Durability) transactions across one or more tables within a single AWS Region.

**API Operations:**
- `TransactWriteItems`: Batched write operation (Put, Update, Delete) that succeeds or fails as a unit.
- `TransactGetItems`: Batched read operation that returns a consistent snapshot.

**Use Case:**
- Financial transactions (debit one account, credit another).
- Inventory management (reserve item, update stock).

### Q98: What is AWS Backup?
**Difficulty: Easy**

**Answer:**
AWS Backup is a centralized backup service that makes it easy and cost-effective for you to backup your data across AWS services.

**Key Features:**
- **Centralized Management:** One place to configure backups for EBS, RDS, DynamoDB, EFS, S3, etc.
- **Policy-Based:** Define backup schedules and retention policies (Backup Plans).
- **Compliance:** Monitor backup compliance across accounts.
- **Cross-Region/Cross-Account:** Copy backups to other regions or accounts for DR.

### Q99: What is AWS App Runner?
**Difficulty: Easy**

**Answer:**
AWS App Runner is a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs, at scale and with no prior infrastructure experience.

**Workflow:**
- Connect to source code (GitHub) or container image (ECR).
- App Runner automatically builds and deploys the application.
- Handles load balancing, auto-scaling, and SSL certificates automatically.

**Difference from Fargate:**
- App Runner is more opinionated and easier (PaaS-like).
- Fargate provides more control over task definitions and networking.

### Q100: Scenario: You are experiencing high latency on your application hosted on EC2. How do you troubleshoot?
**Difficulty: Advanced**

**Answer:**
1.  **Check CloudWatch Metrics:**
    -   **CPUUtilization:** Is the instance overloaded?
    -   **StatusCheckFailed:** Are there hardware/software issues?
    -   **NetworkIn/Out:** Is there a bandwidth bottleneck?
2.  **Check Load Balancer (ALB/NLB):**
    -   **TargetResponseTime:** Is the backend slow?
    -   **RequestCount:** Is there a traffic spike?
    -   **5xxErrors:** Are requests failing?
3.  **Check Application Logs:**
    -   Look for application errors, slow database queries, or memory leaks.
4.  **Check Database (RDS/DynamoDB):**
    -   **CPU/Memory:** Is the DB overloaded?
    -   **Read/WriteLatency:** Is disk I/O the bottleneck?
    -   **ProvisionedThroughputExceeded:** Throttling?
5.  **Check Dependencies:**
    -   Are external API calls (e.g., 3rd party payment gateway) timing out?
    -   Use **AWS X-Ray** to trace the request path and identify the slow component.
