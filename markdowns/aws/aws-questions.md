<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>AWS Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for Cloud Engineers</b></p>
</div>

---

## Table of Contents

1. [How do you secure an S3 bucket to ensure only a specific IAM role from another account can access it?](#q1-how-do-you-secure-an-s3-bucket-to-ensure-only-a-specific-iam-role-from-another-account-can-access-it) <span class="advanced">Advanced</span>
2. [How do you architect a serverless solution to process a stream of high-volume clickstream data?](#q2-how-do-you-architect-a-serverless-solution-to-process-a-stream-of-high-volume-clickstream-data) <span class="advanced">Advanced</span>
3. [How do you optimize DynamoDB costs for a workload with infrequent but high burst traffic?](#q3-how-do-you-optimize-dynamodb-costs-for-a-workload-with-infrequent-but-high-burst-traffic) <span class="intermediate">Intermediate</span>
4. [How do you securely access an RDS database in a private subnet from a Lambda function?](#q4-how-do-you-securely-access-an-rds-database-in-a-private-subnet-from-a-lambda-function) <span class="intermediate">Intermediate</span>
5. [How do you implement a disaster recovery strategy with RPO < 15 mins and RTO < 1 hour?](#q5-how-do-you-implement-a-disaster-recovery-strategy-with-rpo--15-mins-and-rto--1-hour) <span class="expert">Expert</span>
6. [How do you debug a Lambda function that is timing out?](#q6-how-do-you-debug-a-lambda-function-that-is-timing-out) <span class="intermediate">Intermediate</span>
7. [How do you deploy a Docker container to AWS without managing servers?](#q7-how-do-you-deploy-a-docker-container-to-aws-without-managing-servers) <span class="beginner">Beginner</span>
8. [How do you securely manage environment variables for an EC2 application?](#q8-how-do-you-securely-manage-environment-variables-for-an-ec2-application) <span class="intermediate">Intermediate</span>
9. [How do you prevent accidental deletion of an S3 bucket containing critical data?](#q9-how-do-you-prevent-accidental-deletion-of-an-s3-bucket-containing-critical-data) <span class="beginner">Beginner</span>
10. [How do you route traffic to the nearest server based on user location?](#q10-how-do-you-route-traffic-to-the-nearest-server-based-on-user-location) <span class="intermediate">Intermediate</span>
11. [How do you automate the patching of a fleet of EC2 instances?](#q11-how-do-you-automate-the-patching-of-a-fleet-of-ec2-instances) <span class="intermediate">Intermediate</span>
12. [How do you ensure data in transit is encrypted between a Load Balancer and EC2 instances?](#q12-how-do-you-ensure-data-in-transit-is-encrypted-between-a-load-balancer-and-ec2-instances) <span class="advanced">Advanced</span>
13. [How do you handle a situation where your Auto Scaling Group fails to launch new instances?](#q13-how-do-you-handle-a-situation-where-your-auto-scaling-group-fails-to-launch-new-instances) <span class="intermediate">Intermediate</span>
14. [How do you host a static website with global low latency?](#q14-how-do-you-host-a-static-website-with-global-low-latency) <span class="beginner">Beginner</span>
15. [How do you implement a cost-effective solution for processing large files uploaded to S3?](#q15-how-do-you-implement-a-cost-effective-solution-for-processing-large-files-uploaded-to-s3) <span class="intermediate">Intermediate</span>
16. [How do you allow an EC2 instance to access an S3 bucket without hardcoding credentials?](#q16-how-do-you-allow-an-ec2-instance-to-access-an-s3-bucket-without-hardcoding-credentials) <span class="intermediate">Intermediate</span>
17. [How do you create a DynamoDB table with a Global Secondary Index (GSI)?](#q17-how-do-you-create-a-dynamodb-table-with-a-global-secondary-index-gsi) <span class="intermediate">Intermediate</span>
18. [How do you implement an S3 Lifecycle Policy to move objects to Glacier?](#q18-how-do-you-implement-an-s3-lifecycle-policy-to-move-objects-to-glacier) <span class="intermediate">Intermediate</span>
19. [How do you configure a CloudFront distribution to serve a private S3 bucket?](#q19-how-do-you-configure-a-cloudfront-distribution-to-serve-a-private-s3-bucket) <span class="advanced">Advanced</span>
20. [How do you use SQS Visibility Timeout to handle processing failures?](#q20-how-do-you-use-sqs-visibility-timeout-to-handle-processing-failures) <span class="intermediate">Intermediate</span>
21. [How do you implement a Lambda Layer to share code across functions?](#q21-how-do-you-implement-a-lambda-layer-to-share-code-across-functions) <span class="intermediate">Intermediate</span>
22. [How do you protect an API Gateway endpoint with a Usage Plan and API Key?](#q22-how-do-you-protect-an-api-gateway-endpoint-with-a-usage-plan-and-api-key) <span class="intermediate">Intermediate</span>
23. [How do you use Route 53 Failover Routing for Disaster Recovery?](#q23-how-do-you-use-route-53-failover-routing-for-disaster-recovery) <span class="advanced">Advanced</span>
24. [How do you bootstrap an EC2 instance using User Data?](#q24-how-do-you-bootstrap-an-ec2-instance-using-user-data) <span class="beginner">Beginner</span>
25. [How do you use VPC Endpoints to access AWS services privately?](#q25-how-do-you-use-vpc-endpoints-to-access-aws-services-privately) <span class="advanced">Advanced</span>
26. [How do you rotate secrets automatically using AWS Secrets Manager?](#q26-how-do-you-rotate-secrets-automatically-using-aws-secrets-manager) <span class="intermediate">Intermediate</span>
27. [How do you use CloudWatch Alarms to trigger Auto Scaling actions?](#q27-how-do-you-use-cloudwatch-alarms-to-trigger-auto-scaling-actions) <span class="intermediate">Intermediate</span>
28. [How do you implement Cross-Region Replication (CRR) for an S3 bucket?](#q28-how-do-you-implement-cross-region-replication-crr-for-an-s3-bucket) <span class="advanced">Advanced</span>
29. [How do you use DynamoDB Streams to trigger a Lambda function?](#q29-how-do-you-use-dynamodb-streams-to-trigger-a-lambda-function) <span class="intermediate">Intermediate</span>
30. [How do you ensure your EBS volumes are encrypted?](#q30-how-do-you-ensure-your-ebs-volumes-are-encrypted) <span class="beginner">Beginner</span>

---

### Q1: How do you secure an S3 bucket to ensure only a specific IAM role from another account can access it?

**Difficulty**: Advanced

**Strategy:**
Use a Bucket Policy that explicitly allows the `Principal` (the ARN of the IAM role) and denies everyone else (implicit deny) or enforces conditions.

**Code Example:**
```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ExternalCrossAccountRole"
      },
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-secure-bucket/*"
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you architect a serverless solution to process a stream of high-volume clickstream data?

**Difficulty**: Advanced

**Strategy:**
Use Amazon Kinesis Data Streams to ingest the data, and trigger AWS Lambda functions to process it. Use Event Source Mapping with batching to handle high throughput efficiently.

**Architecture:**
1.  **Producer:** App sends data to Kinesis.
2.  **Buffer:** Kinesis Data Streams holds records.
3.  **Consumer:** Lambda (configured with `BatchSize` and `ParallelizationFactor`) processes records.
4.  **Destination:** Lambda writes processed data to DynamoDB or S3 (via Firehose).

**Code Example:**
```python
def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        # Process payload...
    return {"statusCode": 200}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you optimize DynamoDB costs for a workload with infrequent but high burst traffic?

**Difficulty**: Intermediate

**Strategy:**
Switch from **Provisioned Capacity** to **On-Demand Capacity**. On-Demand handles bursts automatically without throttling (assuming no hot partitions) and you pay per request, which is cheaper for idle periods.

**Code Example:**
```bash
aws dynamodb update-table     --table-name MyTable     --billing-mode PAY_PER_REQUEST
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you securely access an RDS database in a private subnet from a Lambda function?

**Difficulty**: Intermediate

**Strategy:**
1.  Deploy Lambda in the VPC (configure subnets and security groups).
2.  Ensure Lambda's Security Group allows outbound traffic to RDS.
3.  Ensure RDS Security Group allows inbound traffic from Lambda's SG.
4.  Use AWS Secrets Manager to rotate and retrieve database credentials.

**Code Example:**
```python
import boto3
import json

def get_secret():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='MyDBCreds')
    return json.loads(response['SecretString'])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you implement a disaster recovery strategy with RPO < 15 mins and RTO < 1 hour?

**Difficulty**: Expert

**Strategy:**
**Pilot Light** or **Warm Standby** approach.
1.  **Data:** Replicate databases (RDS Read Replicas, DynamoDB Global Tables) and S3 (Cross-Region Replication) to a secondary region.
2.  **Compute:** Have minimal infrastructure running (Pilot Light) or a scaled-down version (Warm Standby) in the DR region.
3.  **Failover:** Use Route 53 to switch traffic to the DR region.

**Code Example:**
```json
{
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "app.example.com",
        "Type": "A",
        "SetIdentifier": "Primary",
        "Failover": "PRIMARY",
        "TTL": 60,
        "ResourceRecords": [{"Value": "1.2.3.4"}]
      }
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you debug a Lambda function that is timing out?

**Difficulty**: Intermediate

**Strategy:**
1.  **CloudWatch Logs:** Check for "Task timed out" messages.
2.  **X-Ray:** Enable active tracing to see where time is spent (e.g., slow API call, DB wait).
3.  **Config:** Increase timeout setting (max 15 mins) or memory (which also increases CPU).

**Code Example:**
```bash
from aws_xray_sdk.core import patch_all
patch_all() # Patches boto3, requests, etc. to send traces
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you deploy a Docker container to AWS without managing servers?

**Difficulty**: Beginner

**Strategy:**
Use **AWS Fargate** with Amazon ECS or EKS. Fargate is the serverless compute engine for containers.

**Steps:**
1.  Push image to ECR.
2.  Create an ECS Task Definition (requires Fargate compatibility).
3.  Create an ECS Service using the Fargate launch type.

**Code Example:**
```bash
{
  "family": "my-task",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "my-app",
      "image": "my-repo/my-image:latest",
      "portMappings": [{"containerPort": 80}]
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512"
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you securely manage environment variables for an EC2 application?

**Difficulty**: Intermediate

**Strategy:**
Avoid `.env` files. Use **AWS Systems Manager Parameter Store** or **Secrets Manager**. Grant the EC2 instance an IAM Role to read these parameters.

**Code Example:**
```bash
# Retrieve parameter inside EC2 user data or app startup
aws ssm get-parameter --name "/myapp/prod/db_url" --with-decryption
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you prevent accidental deletion of an S3 bucket containing critical data?

**Difficulty**: Beginner

**Strategy:**
1.  Enable **Versioning**: Keeps history of objects.
2.  Enable **MFA Delete**: Requires MFA code to delete versions.
3.  Use a **Bucket Policy** with an explicit Deny on `s3:DeleteBucket`.
4.  Enable **Object Lock** (WORM model) for compliance.

**JSON (Bucket Policy Deny):**

**Code Example:**
```bash
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:DeleteBucket",
  "Resource": "arn:aws:s3:::my-critical-bucket"
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you route traffic to the nearest server based on user location?

**Difficulty**: Intermediate

**Strategy:**
Use **Amazon Route 53** with a **Geolocation Routing Policy** or **Latency Routing Policy**.

**Configuration:**
*   Create Record Sets for each region's load balancer IP/DNS.
*   Set Routing Policy to "Geolocation".
*   Map "North America" to the `us-east-1` resource, "Europe" to `eu-west-1`, etc.

**Code Example:**
```json
{
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "example.com",
        "Type": "A",
        "SetIdentifier": "NorthAmerica",
        "GeoLocation": { "ContinentCode": "NA" },
        "TTL": 60,
        "ResourceRecords": [{"Value": "1.2.3.4"}]
      }
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you automate the patching of a fleet of EC2 instances?

**Difficulty**: Intermediate

**Strategy:**
Use **AWS Systems Manager (SSM) Patch Manager**.
1.  Install SSM Agent on instances.
2.  Define a Patch Baseline (what patches to approve).
3.  Create a Maintenance Window.
4.  Register targets (instances via tags).
5.  Run the "AWS-RunPatchBaseline" document.

**Code Example:**
```bash
aws ssm create-association \
    --name "AWS-RunPatchBaseline" \
    --targets "Key=tag:PatchGroup,Values=Production" \
    --schedule-expression "cron(0 2 ? * SUN *)" 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you ensure data in transit is encrypted between a Load Balancer and EC2 instances?

**Difficulty**: Advanced

**Strategy:**
Implement End-to-End Encryption.
1.  **Client -> ALB:** Terminate HTTPS at ALB (ACM Certificate).
2.  **ALB -> EC2:** Re-encrypt traffic. Install a self-signed cert or private CA cert on EC2. Configure ALB Target Group to use HTTPS/443.

**Note:** This adds CPU overhead to EC2 for SSL termination.

**Code Example:**
```hcl
resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.front_end.arn
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"
  certificate_arn   = "arn:aws:acm:us-east-1:123456789012:certificate/..."

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.front_end.arn
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you handle a situation where your Auto Scaling Group fails to launch new instances?

**Difficulty**: Intermediate

**Strategy:**
Check **Activity History** in the ASG console for "Failed" status messages. Common causes:
1.  **Service Limits:** Reached max EC2 instances limit.
2.  **Subnet IP Exhaustion:** No available IPs in the subnet.
3.  **IAM Role:** The Launch Template uses a role that doesn't exist or lacks permissions.
4.  **AMI:** The AMI ID in the template is invalid or deleted.

**Code Example:**
```bash
aws autoscaling describe-scaling-activities \
    --auto-scaling-group-name my-asg \
    --query 'Activities[?StatusCode==`Failed`].[Description,Cause]'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you host a static website with global low latency?

**Difficulty**: Beginner

**Strategy:**
Use **Amazon S3** (static hosting) + **Amazon CloudFront** (CDN).
1.  Upload HTML/JS/CSS to S3.
2.  Create a CloudFront Distribution with S3 as origin.
3.  Restrict S3 access to only CloudFront (Origin Access Control).
4.  Point Route 53 domain to CloudFront.

**Code Example:**
```bash
aws s3 website s3://my-bucket/ --index-document index.html --error-document error.html
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you implement a cost-effective solution for processing large files uploaded to S3?

**Difficulty**: Intermediate

**Strategy:**
Use **S3 Event Notifications** to trigger a **Lambda** function.
For very large files or long processing, Lambda might time out. Instead:
S3 Event -> SQS Queue -> Lambda (or EC2/Fargate worker).
This decouples the upload from processing and handles retries.

**Code Example:**
```bash
{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:us-east-1:123:function:ProcessUpload",
      "Events": ["s3:ObjectCreated:*"]
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you allow an EC2 instance to access an S3 bucket without hardcoding credentials?

**Difficulty**: Intermediate

**Strategy:**
Attach an IAM Role to the EC2 instance. The SDK on the instance will automatically retrieve temporary credentials from the instance metadata service.

**Code Example:**
```bash
// IAM Role Trust Policy (Trusting EC2)
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

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you create a DynamoDB table with a Global Secondary Index (GSI)?

**Difficulty**: Intermediate

**Strategy:**
Define the `GlobalSecondaryIndexes` property in your CloudFormation template or Terraform. GSIs allow you to query data using non-key attributes.

**Code Example:**
```json
{
  "Type": "AWS::DynamoDB::Table",
  "Properties": {
    "TableName": "Orders",
    "AttributeDefinitions": [
      { "AttributeName": "OrderId", "AttributeType": "S" },
      { "AttributeName": "CustomerId", "AttributeType": "S" }
    ],
    "KeySchema": [{ "AttributeName": "OrderId", "KeyType": "HASH" }],
    "GlobalSecondaryIndexes": [
      {
        "IndexName": "CustomerIndex",
        "KeySchema": [{ "AttributeName": "CustomerId", "KeyType": "HASH" }],
        "Projection": { "ProjectionType": "ALL" }
      }
    ]
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you implement an S3 Lifecycle Policy to move objects to Glacier?

**Difficulty**: Intermediate

**Strategy:**
Use a Lifecycle Configuration on the bucket to transition objects to cheaper storage classes (Standard-IA, Glacier) after a set number of days.

**Code Example:**
```json
{
  "Rules": [
    {
      "ID": "MoveToGlacier",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you configure a CloudFront distribution to serve a private S3 bucket?

**Difficulty**: Advanced

**Strategy:**
Use Origin Access Control (OAC) or Origin Access Identity (OAI). Update the S3 Bucket Policy to allow read access only to the OAC/OAI principal.

**Code Example:**
```bash
// S3 Bucket Policy for OAC
{
  "Version": "2012-10-17",
  "Statement": {
    "Sid": "AllowCloudFrontServicePrincipalReadOnly",
    "Effect": "Allow",
    "Principal": { "Service": "cloudfront.amazonaws.com" },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket/*",
    "Condition": {
      "StringEquals": {
        "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/EDFDVBD632BHDS5"
      }
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use SQS Visibility Timeout to handle processing failures?

**Difficulty**: Intermediate

**Strategy:**
Visibility Timeout hides a message from other consumers while it's being processed. If processing fails (no delete request sent), the message becomes visible again after the timeout for retrying.

**Code Example:**
```bash
// CLI command to set visibility timeout
aws sqs receive-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123/my-queue \
  --visibility-timeout 60
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you implement a Lambda Layer to share code across functions?

**Difficulty**: Intermediate

**Strategy:**
Package your shared libraries (e.g., node_modules, python packages) into a zip file and create a Layer. Attach this layer to multiple Lambda functions.

**Code Example:**
```json
# AWS SAM template definition
Resources:
  MyLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      LayerName: common-utils
      ContentUri: layers/common-utils/
      CompatibleRuntimes:
        - nodejs18.x

  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Layers:
        - !Ref MyLayer
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you protect an API Gateway endpoint with a Usage Plan and API Key?

**Difficulty**: Intermediate

**Strategy:**
Create an API Key, a Usage Plan (with throttle/quota limits), and associate the API Key with the Usage Plan and the API Stage.

**Code Example:**
```json
// CloudFormation Snippet
UsagePlan:
  Type: AWS::ApiGateway::UsagePlan
  Properties:
    ApiStages:
      - ApiId: !Ref MyApi
        Stage: prod
    Quota:
      Limit: 5000
      Period: MONTH
    Throttle:
      BurstLimit: 200
      RateLimit: 100
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you use Route 53 Failover Routing for Disaster Recovery?

**Difficulty**: Advanced

**Strategy:**
Configure a Primary and Secondary record set. Associate a Health Check with the Primary record. If the Health Check fails, Route 53 routes traffic to the Secondary record (e.g., a static site in S3 or a standby region).

**Code Example:**
```json
{
  "Comment": "Failover configuration",
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "app.example.com",
        "Type": "A",
        "SetIdentifier": "Primary",
        "Failover": "PRIMARY",
        "HealthCheckId": "hc-12345",
        "AliasTarget": { ... }
      }
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you bootstrap an EC2 instance using User Data?

**Difficulty**: Beginner

**Strategy:**
Provide a shell script (or cloud-init directive) in the `UserData` field when launching the instance. This script runs once at launch to install software.

**Code Example:**
```json
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you use VPC Endpoints to access AWS services privately?

**Difficulty**: Advanced

**Strategy:**
Create a Gateway Endpoint (for S3/DynamoDB) or an Interface Endpoint (PrivateLink for others) to access services from a private subnet without a NAT Gateway or Internet Gateway.

**Code Example:**
```hcl
// Terraform: VPC Endpoint for S3
resource "aws_vpc_endpoint" "s3" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.us-east-1.s3"
  vpc_endpoint_type = "Gateway"
  route_table_ids = [aws_route_table.private.id]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you rotate secrets automatically using AWS Secrets Manager?

**Difficulty**: Intermediate

**Strategy:**
Enable automatic rotation in Secrets Manager. It uses a Lambda function to rotate credentials for supported databases (RDS, Redshift, DocumentDB) automatically.

**Code Example:**
```json
// CloudFormation: Secret Rotation
MySecretRotationSchedule:
  Type: AWS::SecretsManager::RotationSchedule
  Properties:
    SecretId: !Ref MySecret
    RotationLambdaARN: !Ref MyRotationLambda
    RotationRules:
      AutomaticallyAfterDays: 30
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you use CloudWatch Alarms to trigger Auto Scaling actions?

**Difficulty**: Intermediate

**Strategy:**
Create a CloudWatch Alarm based on a metric (e.g., CPUUtilization > 70%). Configure the Auto Scaling Policy to execute when the alarm state is ALARM.

**Code Example:**
```bash
{
  "AlarmName": "HighCPU",
  "MetricName": "CPUUtilization",
  "Namespace": "AWS/EC2",
  "Statistic": "Average",
  "Threshold": 70,
  "ComparisonOperator": "GreaterThanThreshold",
  "EvaluationPeriods": 2,
  "AlarmActions": [ "arn:aws:autoscaling:us-east-1:123:scalingPolicy:..." ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you implement Cross-Region Replication (CRR) for an S3 bucket?

**Difficulty**: Advanced

**Strategy:**
Enable Versioning on both source and destination buckets. Create a replication rule on the source bucket specifying the destination bucket and an IAM role.

**Code Example:**
```bash
{
  "Role": "arn:aws:iam::123:role/replication-role",
  "Rules": [
    {
      "Status": "Enabled",
      "Priority": 1,
      "DeleteMarkerReplication": { "Status": "Disabled" },
      "Destination": {
        "Bucket": "arn:aws:s3:::destination-bucket"
      }
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you use DynamoDB Streams to trigger a Lambda function?

**Difficulty**: Intermediate

**Strategy:**
Enable DynamoDB Streams on the table. Create an Event Source Mapping in Lambda to poll the stream and invoke the function on changes (INSERT, MODIFY, REMOVE).

**Code Example:**
```bash
// AWS CLI
aws lambda create-event-source-mapping \
  --function-name ProcessOrder \
  --batch-size 100 \
  --starting-position TRIM_HORIZON \
  --event-source-arn arn:aws:dynamodb:us-east-1:123:table/Orders/stream/2023...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you ensure your EBS volumes are encrypted?

**Difficulty**: Beginner

**Strategy:**
Enable EBS Encryption by Default in the region. Alternatively, specify `Encrypted: true` and a KMS Key ID when creating individual volumes or launching instances.

**Code Example:**
```hcl
// Terraform
resource "aws_ebs_volume" "example" {
  availability_zone = "us-east-1a"
  size              = 40
  encrypted         = true
  kms_key_id        = aws_kms_key.my_key.arn
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

