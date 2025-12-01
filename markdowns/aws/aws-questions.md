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
5. [How do you implement a disaster recovery strategy with RPO < 15 mins and RTO < 1 hour?](#q5-how-do-you-implement-a-disaster-recovery-strategy-with-rpo-<-15-mins-and-rto-<-1-hour) <span class="expert">Expert</span>
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
31. [How do you implement Rate Limiting using AWS WAF?](#q31-how-do-you-implement-rate-limiting-using-aws-waf) <span class="intermediate">Intermediate</span>
32. [How do you scale an Aurora database instantly for unpredictable workloads?](#q32-how-do-you-scale-an-aurora-database-instantly-for-unpredictable-workloads) <span class="intermediate">Intermediate</span>
33. [How do you orchestrate a multi-step workflow with error handling?](#q33-how-do-you-orchestrate-a-multi-step-workflow-with-error-handling) <span class="intermediate">Intermediate</span>
34. [How do you query CSV data stored in S3 without loading it into a database?](#q34-how-do-you-query-csv-data-stored-in-s3-without-loading-it-into-a-database) <span class="beginner">Beginner</span>
35. [How do you create an EKS Cluster using the command line?](#q35-how-do-you-create-an-eks-cluster-using-the-command-line) <span class="intermediate">Intermediate</span>
36. [How do you trigger a Lambda function on a schedule?](#q36-how-do-you-trigger-a-lambda-function-on-a-schedule) <span class="beginner">Beginner</span>
37. [How do you analyze CloudTrail logs for suspicious activity?](#q37-how-do-you-analyze-cloudtrail-logs-for-suspicious-activity) <span class="intermediate">Intermediate</span>
38. [How do you ensure all S3 buckets are encrypted using AWS Config?](#q38-how-do-you-ensure-all-s3-buckets-are-encrypted-using-aws-config) <span class="intermediate">Intermediate</span>
39. [How do you connect multiple VPCs together at scale?](#q39-how-do-you-connect-multiple-vpcs-together-at-scale) <span class="advanced">Advanced</span>
40. [How do you provide a static IP address for an application running in multiple regions?](#q40-how-do-you-provide-a-static-ip-address-for-an-application-running-in-multiple-regions) <span class="advanced">Advanced</span>
41. [How do you implement caching for a database to improve read performance?](#q41-how-do-you-implement-caching-for-a-database-to-improve-read-performance) <span class="intermediate">Intermediate</span>
42. [How do you limit the maximum permissions a user or role can have?](#q42-how-do-you-limit-the-maximum-permissions-a-user-or-role-can-have) <span class="advanced">Advanced</span>
43. [How do you allow users to upload files directly to S3 securely?](#q43-how-do-you-allow-users-to-upload-files-directly-to-s3-securely) <span class="intermediate">Intermediate</span>
44. [How do you handle user authentication for a mobile app?](#q44-how-do-you-handle-user-authentication-for-a-mobile-app) <span class="intermediate">Intermediate</span>
45. [How do you deploy a web application from source code without writing Dockerfiles?](#q45-how-do-you-deploy-a-web-application-from-source-code-without-writing-dockerfiles) <span class="beginner">Beginner</span>
46. [How do you securely access EC2 instances without opening port 22 (SSH)?](#q46-how-do-you-securely-access-ec2-instances-without-opening-port-22-ssh) <span class="intermediate">Intermediate</span>
47. [How do you run a serverless ETL job?](#q47-how-do-you-run-a-serverless-etl-job) <span class="intermediate">Intermediate</span>
48. [How do you serve private content via CloudFront?](#q48-how-do-you-serve-private-content-via-cloudfront) <span class="advanced">Advanced</span>
49. [How do you mount a shared file system to multiple EC2 instances?](#q49-how-do-you-mount-a-shared-file-system-to-multiple-ec2-instances) <span class="beginner">Beginner</span>
50. [How do you create a private connection between your on-premises data center and VPC?](#q50-how-do-you-create-a-private-connection-between-your-on-premises-data-center-and-vpc) <span class="intermediate">Intermediate</span>
51. [Difference between EC2 and Lambda?](#q51-difference-between-ec2-and-lambda) <span class="beginner">Beginner</span>
52. [What is VPC Peering?](#q52-what-is-vpc-peering) <span class="intermediate">Intermediate</span>
53. [How do you handle Lambda Cold Starts?](#q53-how-do-you-handle-lambda-cold-starts) <span class="intermediate">Intermediate</span>
54. [S3 Consistency Model?](#q54-s3-consistency-model) <span class="advanced">Advanced</span>
55. [DynamoDB GSI vs LSI?](#q55-dynamodb-gsi-vs-lsi) <span class="advanced">Advanced</span>
56. [IAM Roles vs Policies?](#q56-iam-roles-vs-policies) <span class="beginner">Beginner</span>
57. [How do you secure S3 buckets?](#q57-how-do-you-secure-s3-buckets) <span class="intermediate">Intermediate</span>
58. [What is CloudFront?](#q58-what-is-cloudfront) <span class="beginner">Beginner</span>
59. [ECS vs EKS?](#q59-ecs-vs-eks) <span class="intermediate">Intermediate</span>
60. [How do you monitor AWS resources?](#q60-how-do-you-monitor-aws-resources) <span class="beginner">Beginner</span>
61. [What is Auto Scaling?](#q61-what-is-auto-scaling) <span class="beginner">Beginner</span>
62. [How do you decouple services?](#q62-how-do-you-decouple-services) <span class="intermediate">Intermediate</span>
63. [What is Route 53?](#q63-what-is-route-53) <span class="beginner">Beginner</span>
64. [How do you manage infrastructure as code?](#q64-how-do-you-manage-infrastructure-as-code) <span class="intermediate">Intermediate</span>
65. [What is RDS Multi-AZ?](#q65-what-is-rds-multi-az) <span class="intermediate">Intermediate</span>
66. [Difference between SQS Standard and FIFO?](#q66-difference-between-sqs-standard-and-fifo) <span class="intermediate">Intermediate</span>
67. [What is API Gateway?](#q67-what-is-api-gateway) <span class="beginner">Beginner</span>
68. [How do you optimize AWS costs?](#q68-how-do-you-optimize-aws-costs) <span class="intermediate">Intermediate</span>
69. [What is Elastic Beanstalk?](#q69-what-is-elastic-beanstalk) <span class="beginner">Beginner</span>
70. [How do you implement Distributed Tracing?](#q70-how-do-you-implement-distributed-tracing) <span class="advanced">Advanced</span>
71. [What is Secrets Manager?](#q71-what-is-secrets-manager) <span class="intermediate">Intermediate</span>
72. [What is Transit Gateway?](#q72-what-is-transit-gateway) <span class="advanced">Advanced</span>
73. [How do you secure data at rest?](#q73-how-do-you-secure-data-at-rest) <span class="beginner">Beginner</span>
74. [What is Aurora?](#q74-what-is-aurora) <span class="intermediate">Intermediate</span>
75. [What is Cognito?](#q75-what-is-cognito) <span class="intermediate">Intermediate</span>
76. [How do you use Spot Instances?](#q76-how-do-you-use-spot-instances) <span class="intermediate">Intermediate</span>
77. [What is Glacier?](#q77-what-is-glacier) <span class="beginner">Beginner</span>
78. [What is WAF?](#q78-what-is-waf) <span class="intermediate">Intermediate</span>
79. [How do you connect on-prem to VPC?](#q79-how-do-you-connect-on-prem-to-vpc) <span class="intermediate">Intermediate</span>
80. [What is Kinesis?](#q80-what-is-kinesis) <span class="intermediate">Intermediate</span>
81. [Difference between NACL and Security Group?](#q81-difference-between-nacl-and-security-group) <span class="advanced">Advanced</span>
82. [What is CloudTrail?](#q82-what-is-cloudtrail) <span class="beginner">Beginner</span>
83. [How do you share AMI?](#q83-how-do-you-share-ami) <span class="beginner">Beginner</span>
84. [What is EFS?](#q84-what-is-efs) <span class="intermediate">Intermediate</span>
85. [How do you implement Blue/Green deployment?](#q85-how-do-you-implement-bluegreen-deployment) <span class="intermediate">Intermediate</span>
86. [What is Step Functions?](#q86-what-is-step-functions) <span class="intermediate">Intermediate</span>
87. [How do you host a static website?](#q87-how-do-you-host-a-static-website) <span class="beginner">Beginner</span>
88. [What is Global Accelerator?](#q88-what-is-global-accelerator) <span class="advanced">Advanced</span>
89. [How do you access private EC2?](#q89-how-do-you-access-private-ec2) <span class="intermediate">Intermediate</span>
90. [What is Organizations?](#q90-what-is-organizations) <span class="intermediate">Intermediate</span>
91. [How do you implement caching in API Gateway?](#q91-how-do-you-implement-caching-in-api-gateway) <span class="intermediate">Intermediate</span>
92. [What is Fargate?](#q92-what-is-fargate) <span class="intermediate">Intermediate</span>
93. [How do you validate CloudFormation?](#q93-how-do-you-validate-cloudformation) <span class="beginner">Beginner</span>
94. [What is Athena?](#q94-what-is-athena) <span class="intermediate">Intermediate</span>
95. [How do you restrict S3 access by IP?](#q95-how-do-you-restrict-s3-access-by-ip) <span class="intermediate">Intermediate</span>
96. [What is Transfer Family?](#q96-what-is-transfer-family) <span class="intermediate">Intermediate</span>
97. [How do you handle DDOS?](#q97-how-do-you-handle-ddos) <span class="intermediate">Intermediate</span>
98. [What is EventBridge?](#q98-what-is-eventbridge) <span class="intermediate">Intermediate</span>
99. [How do you copy S3 objects cross-region?](#q99-how-do-you-copy-s3-objects-cross-region) <span class="intermediate">Intermediate</span>
100. [What is AppSync?](#q100-what-is-appsync) <span class="intermediate">Intermediate</span>

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



---

### Q31: How do you implement Rate Limiting using AWS WAF?

**Difficulty**: Intermediate

**Strategy:**
Create a **Rate-based Rule** in your Web ACL. This tracks requests from each IP address over a 5-minute window. If the count exceeds the limit, WAF blocks the IP.

**Code Example:**
```bash
{
  "Name": "RateLimitRule",
  "Priority": 1,
  "Action": { "Block": {} },
  "VisibilityConfig": { ... },
  "Statement": {
    "RateBasedStatement": {
      "Limit": 2000,
      "AggregateKeyType": "IP"
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you scale an Aurora database instantly for unpredictable workloads?

**Difficulty**: Intermediate

**Strategy:**
Use **Aurora Serverless v2**. It scales capacity (ACUs) up and down in fractions of a second based on actual load, without dropping connections.

**Code Example:**
```bash
resource "aws_rds_cluster" "default" {
  cluster_identifier = "aurora-cluster-demo"
  engine             = "aurora-mysql"
  engine_mode        = "provisioned"
  serverless_v2_scaling_configuration {
    min_capacity = 0.5
    max_capacity = 128.0
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you orchestrate a multi-step workflow with error handling?

**Difficulty**: Intermediate

**Strategy:**
Use **AWS Step Functions**. Define a state machine in ASL (Amazon States Language) to coordinate Lambda functions, handle retries, and manage failures.

**Code Example:**
```bash
{
  "StartAt": "ProcessPayment",
  "States": {
    "ProcessPayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123:function:ProcessPayment",
      "Next": "ShipItem",
      "Catch": [ { "ErrorEquals": ["PaymentFailed"], "Next": "NotifyUser" } ]
    },
    "ShipItem": { "Type": "Task", "End": true },
    "NotifyUser": { "Type": "Task", "End": true }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you query CSV data stored in S3 without loading it into a database?

**Difficulty**: Beginner

**Strategy:**
Use **Amazon Athena**. Define a schema (table) pointing to the S3 location and run standard SQL queries. You pay only for the data scanned.

**Code Example:**
```bash
CREATE EXTERNAL TABLE IF NOT EXISTS orders (
  order_id string,
  amount double
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://my-data-bucket/orders/';

-- Query
SELECT * FROM orders WHERE amount > 100;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you create an EKS Cluster using the command line?

**Difficulty**: Intermediate

**Strategy:**
Use **eksctl**, the official CLI for EKS. It simplifies cluster creation by provisioning VPCs, Subnets, and Node Groups automatically.

**Code Example:**
```bash
eksctl create cluster \
  --name my-cluster \
  --region us-east-1 \
  --version 1.27 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 3 \
  --nodes-min 1 \
  --nodes-max 4 \
  --managed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you trigger a Lambda function on a schedule?

**Difficulty**: Beginner

**Strategy:**
Use **Amazon EventBridge** (formerly CloudWatch Events) with a Schedule Rule (Cron or Rate expression).

**Code Example:**
```bash
{
  "Name": "DailyReport",
  "ScheduleExpression": "cron(0 8 * * ? *)",
  "State": "ENABLED",
  "Targets": [
    {
      "Id": "MyLambda",
      "Arn": "arn:aws:lambda:us-east-1:123:function:GenerateReport"
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you analyze CloudTrail logs for suspicious activity?

**Difficulty**: Intermediate

**Strategy:**
Use **CloudTrail Lake** (SQL-based query) or **CloudTrail Insights** (anomaly detection). You can also stream logs to CloudWatch Logs and use Metric Filters.

**Code Example:**
```bash
-- CloudTrail Lake Query
SELECT eventTime, eventName, userIdentity.arn, sourceIPAddress
FROM $EDS_ID
WHERE eventName = 'ConsoleLogin'
AND errorMessage IS NOT NULL
ORDER BY eventTime DESC
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you ensure all S3 buckets are encrypted using AWS Config?

**Difficulty**: Intermediate

**Strategy:**
Enable **AWS Config** and add the managed rule `s3-bucket-server-side-encryption-enabled`. It flags non-compliant buckets.

**Code Example:**
```bash
aws configservice put-config-rule --config-rule '{
  "ConfigRuleName": "s3-encryption-enabled",
  "Source": {
    "Owner": "AWS",
    "SourceIdentifier": "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
  }
}'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you connect multiple VPCs together at scale?

**Difficulty**: Advanced

**Strategy:**
Use **AWS Transit Gateway**. It acts as a hub that connects VPCs and on-premises networks. It simplifies peering compared to a mesh of VPC Peering connections.

**Code Example:**
```bash
resource "aws_ec2_transit_gateway_vpc_attachment" "example" {
  subnet_ids         = [aws_subnet.private.id]
  transit_gateway_id = aws_ec2_transit_gateway.example.id
  vpc_id             = aws_vpc.main.id
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you provide a static IP address for an application running in multiple regions?

**Difficulty**: Advanced

**Strategy:**
Use **AWS Global Accelerator**. It provides two static Anycast IPs that route traffic to the nearest endpoint (ALB, EC2) over the AWS global network.

**Code Example:**
```bash
resource "aws_globalaccelerator_accelerator" "example" {
  name            = "example-accelerator"
  ip_address_type = "IPV4"
  enabled         = true
}
# Add listener and endpoint groups for regions...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you implement caching for a database to improve read performance?

**Difficulty**: Intermediate

**Strategy:**
Use **Amazon ElastiCache** (Redis or Memcached). Implement Lazy Loading (cache-aside) or Write-Through strategies in your application.

**Code Example:**
```bash
// Pseudo-code for Cache-Aside
val = cache.get(key);
if (val == null) {
    val = db.query(key);
    cache.set(key, val, ttl);
}
return val;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you limit the maximum permissions a user or role can have?

**Difficulty**: Advanced

**Strategy:**
Use an **IAM Permissions Boundary**. It sets the maximum intersection of permissions. Even if a policy allows `AdministratorAccess`, the boundary restricts it.

**Code Example:**
```bash
// Create User with Boundary
aws iam create-user     --user-name Alice     --permissions-boundary arn:aws:iam::123:policy/MaxPermissionsBoundary

// Boundary Policy Example
{
  "Effect": "Allow",
  "Action": ["s3:*", "ec2:*"],
  "Resource": "*"
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you allow users to upload files directly to S3 securely?

**Difficulty**: Intermediate

**Strategy:**
Generate an **S3 Presigned URL** using the AWS SDK. The URL grants temporary permission to upload a specific object without sharing AWS credentials.

**Code Example:**
```bash
s3 = boto3.client('s3')
url = s3.generate_presigned_url(
    'put_object',
    Params={'Bucket': 'my-bucket', 'Key': 'uploads/image.jpg'},
    ExpiresIn=3600
)
# Client uses PUT request to this URL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you handle user authentication for a mobile app?

**Difficulty**: Intermediate

**Strategy:**
Use **Amazon Cognito User Pools**. It handles sign-up, sign-in, MFA, and social identity providers (Google, Facebook). It returns JWT tokens.

**Code Example:**
```bash
// Amplify / JS SDK
import { Auth } from 'aws-amplify';

async function signUp() {
    try {
        const { user } = await Auth.signUp({
            username,
            password,
            attributes: { email }
        });
    } catch (error) {
        console.log('error signing up:', error);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you deploy a web application from source code without writing Dockerfiles?

**Difficulty**: Beginner

**Strategy:**
Use **AWS App Runner**. It connects to your GitHub repository, detects the language (Python, Node, Java), builds the image automatically, and deploys it.

**Code Example:**
```bash
# App Runner Configuration (apprunner.yaml)
version: 1.0
runtime: nodejs16
build:
  commands:
    build:
      - npm install
run:
  command: npm start
  network:
    port: 8080
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you securely access EC2 instances without opening port 22 (SSH)?

**Difficulty**: Intermediate

**Strategy:**
Use **AWS Systems Manager Session Manager**. It tunnels traffic through the SSM Agent, requires no inbound ports, and logs session activity to S3/CloudWatch.

**Code Example:**
```bash
# Start session via CLI
aws ssm start-session --target i-0123456789abcdef0

# Prerequisites:
# 1. SSM Agent installed
# 2. IAM Role with AmazonSSMManagedInstanceCore policy attached
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you run a serverless ETL job?

**Difficulty**: Intermediate

**Strategy:**
Use **AWS Glue**. Write PySpark or Scala scripts to transform data. Glue creates a serverless Spark environment to run the job.

**Code Example:**
```bash
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext

glueContext = GlueContext(SparkContext.getOrCreate())
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "db", table_name = "table")
# Transform...
glueContext.write_dynamic_frame.from_options(frame = datasource0, connection_type = "s3", connection_options = {"path": "s3://..."})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you serve private content via CloudFront?

**Difficulty**: Advanced

**Strategy:**
Use **Signed URLs** (for individual files) or **Signed Cookies** (for access to multiple files). The application generates the signature using a private key.

**Code Example:**
```bash
from botocore.signers import CloudFrontSigner

def rsa_signer(message):
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

signer = CloudFrontSigner(key_id, rsa_signer)
url = signer.generate_presigned_url(url, date_less_than=expire_date)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you mount a shared file system to multiple EC2 instances?

**Difficulty**: Beginner

**Strategy:**
Use **Amazon EFS (Elastic File System)**. It provides a scalable NFS file system that can be mounted by multiple Linux instances simultaneously.

**Code Example:**
```bash
# On EC2 Instance
sudo mount -t nfs4 -o nfsvers=4.1 fs-12345678.efs.us-east-1.amazonaws.com:/ /mnt/efs

# /etc/fstab entry for auto-mount
fs-12345678.efs.us-east-1.amazonaws.com:/ /mnt/efs nfs4 defaults,_netdev 0 0
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you create a private connection between your on-premises data center and VPC?

**Difficulty**: Intermediate

**Strategy:**
Use **AWS Direct Connect** for a dedicated fiber connection (consistent performance) or **AWS Site-to-Site VPN** for an encrypted tunnel over the public internet (cost-effective).

**Code Example:**
```bash
resource "aws_vpn_connection" "main" {
  vpn_gateway_id      = aws_vpn_gateway.vpn_gw.id
  customer_gateway_id = aws_customer_gateway.customer_gw.id
  type                = "ipsec.1"
  static_routes_only  = true
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q51: Difference between EC2 and Lambda?

**Difficulty**: Beginner

**Strategy**:
EC2: Virtual servers (manage OS). Lambda: Serverless (run code only).

**Code Example**:
```javascript
// Lambda handles scaling automatically
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is VPC Peering?

**Difficulty**: Intermediate

**Strategy**:
Connecting two VPCs to route traffic privately. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Enable communication between services in different VPCs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you handle Lambda Cold Starts?

**Difficulty**: Intermediate

**Strategy**:
Provisioned Concurrency or keep warm scripts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Provisioned Concurrency keeps instances initialized
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: S3 Consistency Model?

**Difficulty**: Advanced

**Strategy**:
Strong consistency for PUTs of new objects and overwrites.

**Code Example**:
```javascript
// Read after write is consistent
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: DynamoDB GSI vs LSI?

**Difficulty**: Advanced

**Strategy**:
LSI: Created at table creation, shares partition key. GSI: Created anytime, different keys.

**Code Example**:
```javascript
// GSI allows flexible query patterns
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: IAM Roles vs Policies?

**Difficulty**: Beginner

**Strategy**:
Policy: Permissions document. Role: Identity that can be assumed.

**Code Example**:
```javascript
// Attach Policy to Role, Role to EC2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you secure S3 buckets?

**Difficulty**: Intermediate

**Strategy**:
Block Public Access, Bucket Policies, KMS Encryption.

**Code Example**:
```javascript
"BlockPublicAcls": true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is CloudFront?

**Difficulty**: Beginner

**Strategy**:
CDN for low latency delivery. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Caches content at Edge Locations
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: ECS vs EKS?

**Difficulty**: Intermediate

**Strategy**:
ECS: AWS native container orchestration. EKS: Managed Kubernetes.

**Code Example**:
```javascript
// EKS allows standard K8s tooling
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you monitor AWS resources?

**Difficulty**: Beginner

**Strategy**:
CloudWatch (Logs, Metrics, Alarms). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Set alarm for high CPU
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What is Auto Scaling?

**Difficulty**: Beginner

**Strategy**:
Adjusting capacity based on load. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Scale out EC2 when CPU > 70%
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you decouple services?

**Difficulty**: Intermediate

**Strategy**:
Use SQS (Queue) or SNS (Pub/Sub). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Service A -> SQS -> Service B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: What is Route 53?

**Difficulty**: Beginner

**Strategy**:
DNS Web Service. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Routing policies: Simple, Weighted, Latency
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you manage infrastructure as code?

**Difficulty**: Intermediate

**Strategy**:
CloudFormation, Terraform, or CDK. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// CDK allows defining infra in TypeScript
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: What is RDS Multi-AZ?

**Difficulty**: Intermediate

**Strategy**:
Synchronous replication to standby for failover. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// High Availability
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: Difference between SQS Standard and FIFO?

**Difficulty**: Intermediate

**Strategy**:
Standard: At-least-once, best-effort order. FIFO: Exactly-once, strict order.

**Code Example**:
```javascript
// FIFO for banking transactions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: What is API Gateway?

**Difficulty**: Beginner

**Strategy**:
Entry point for APIs. Handles throttling, auth. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Triggers Lambda
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you optimize AWS costs?

**Difficulty**: Intermediate

**Strategy**:
Reserved Instances, Spot Instances, S3 Lifecycle policies.

**Code Example**:
```javascript
// Move old data to Glacier
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is Elastic Beanstalk?

**Difficulty**: Beginner

**Strategy**:
PaaS for deploying apps. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Handles deployment, scaling, balancing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Distributed Tracing?

**Difficulty**: Advanced

**Strategy**:
X-Ray. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Trace requests across microservices
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is Secrets Manager?

**Difficulty**: Intermediate

**Strategy**:
Rotates and manages secrets. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Fetch DB password at runtime
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: What is Transit Gateway?

**Difficulty**: Advanced

**Strategy**:
Hub to connect VPCs and on-prem networks. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Simplifies network topology
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you secure data at rest?

**Difficulty**: Beginner

**Strategy**:
KMS (Key Management Service). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Encrypt EBS volumes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is Aurora?

**Difficulty**: Intermediate

**Strategy**:
Cloud-native relational DB (MySQL/PG compatible). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// 3x faster than standard Postgres
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is Cognito?

**Difficulty**: Intermediate

**Strategy**:
User identity and authentication service. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// User Pools for sign-up/sign-in
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you use Spot Instances?

**Difficulty**: Intermediate

**Strategy**:
Bid for unused capacity. Handle interruptions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Stateless workloads
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: What is Glacier?

**Difficulty**: Beginner

**Strategy**:
Low-cost archive storage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Retrieval times: minutes to hours
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: What is WAF?

**Difficulty**: Intermediate

**Strategy**:
Web Application Firewall. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Protect against SQLi, XSS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you connect on-prem to VPC?

**Difficulty**: Intermediate

**Strategy**:
VPN or Direct Connect. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Direct Connect for dedicated line
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: What is Kinesis?

**Difficulty**: Intermediate

**Strategy**:
Real-time data streaming. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Ingest logs, clickstreams
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: Difference between NACL and Security Group?

**Difficulty**: Advanced

**Strategy**:
SG: Stateful, Instance level. NACL: Stateless, Subnet level.

**Code Example**:
```javascript
// SG allow return traffic automatically
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: What is CloudTrail?

**Difficulty**: Beginner

**Strategy**:
Auditing service. Logs API calls. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Who did what and when
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you share AMI?

**Difficulty**: Beginner

**Strategy**:
Modify permissions to share with account ID. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Cross-account deployment
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: What is EFS?

**Difficulty**: Intermediate

**Strategy**:
Elastic File System (NFS). Shared storage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Mount on multiple EC2s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Blue/Green deployment?

**Difficulty**: Intermediate

**Strategy**:
Route 53 weighted routing or CodeDeploy. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Zero downtime
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is Step Functions?

**Difficulty**: Intermediate

**Strategy**:
Serverless workflow orchestration. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Chain Lambdas together
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you host a static website?

**Difficulty**: Beginner

**Strategy**:
S3 Bucket + Static Website Hosting. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Index document: index.html
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: What is Global Accelerator?

**Difficulty**: Advanced

**Strategy**:
Static IP entry point, traffic over AWS backbone. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Improved performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you access private EC2?

**Difficulty**: Intermediate

**Strategy**:
Bastion Host or SSM Session Manager. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// SSM requires no open inbound ports
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: What is Organizations?

**Difficulty**: Intermediate

**Strategy**:
Manage multiple AWS accounts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Consolidated billing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you implement caching in API Gateway?

**Difficulty**: Intermediate

**Strategy**:
Enable Stage caching. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Reduce calls to backend
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: What is Fargate?

**Difficulty**: Intermediate

**Strategy**:
Serverless compute for containers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// No EC2 management
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you validate CloudFormation?

**Difficulty**: Beginner

**Strategy**:
validate-template command. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
$ aws cloudformation validate-template
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: What is Athena?

**Difficulty**: Intermediate

**Strategy**:
Query S3 data using SQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Serverless query
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you restrict S3 access by IP?

**Difficulty**: Intermediate

**Strategy**:
Bucket Policy with Condition IpAddress. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Deny if not corporate VPN
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: What is Transfer Family?

**Difficulty**: Intermediate

**Strategy**:
SFTP/FTPS support. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Migrate legacy workflows
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you handle DDOS?

**Difficulty**: Intermediate

**Strategy**:
Shield Standard/Advanced + CloudFront + WAF. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// AWS Shield
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: What is EventBridge?

**Difficulty**: Intermediate

**Strategy**:
Serverless event bus. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Decouple SaaS apps
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you copy S3 objects cross-region?

**Difficulty**: Intermediate

**Strategy**:
Cross-Region Replication (CRR). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Disaster recovery
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: What is AppSync?

**Difficulty**: Intermediate

**Strategy**:
Managed GraphQL service. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Real-time updates
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
