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
51. [How do you implement Blue/Green deployment with ECS CodeDeploy?](#q51-how-do-you-implement-bluegreen-deployment-with-ecs-codedeploy) <span class="advanced">Advanced</span>
52. [How do you use AWS Backup to automate cross-region backups?](#q52-how-do-you-use-aws-backup-to-automate-cross-region-backups) <span class="intermediate">Intermediate</span>
53. [How do you use AWS X-Ray for distributed tracing?](#q53-how-do-you-use-aws-x-ray-for-distributed-tracing) <span class="intermediate">Intermediate</span>
54. [How do you use AWS Organizations to manage multiple accounts?](#q54-how-do-you-use-aws-organizations-to-manage-multiple-accounts) <span class="intermediate">Intermediate</span>
55. [How do you use S3 Object Lambda to modify data on retrieval?](#q55-how-do-you-use-s3-object-lambda-to-modify-data-on-retrieval) <span class="advanced">Advanced</span>
56. [How do you use Athena to analyze VPC Flow Logs?](#q56-how-do-you-use-athena-to-analyze-vpc-flow-logs) <span class="intermediate">Intermediate</span>
57. [How do you use Kinesis Data Firehose to transform and load data?](#q57-how-do-you-use-kinesis-data-firehose-to-transform-and-load-data) <span class="intermediate">Intermediate</span>
58. [How do you use Amazon Macie to discover sensitive data?](#q58-how-do-you-use-amazon-macie-to-discover-sensitive-data) <span class="beginner">Beginner</span>
59. [How do you use SSM Parameter Store Hierarchy?](#q59-how-do-you-use-ssm-parameter-store-hierarchy) <span class="intermediate">Intermediate</span>
60. [How do you use AWS WAF to block SQL Injection attacks?](#q60-how-do-you-use-aws-waf-to-block-sql-injection-attacks) <span class="intermediate">Intermediate</span>
61. [What are the security implications of AWS in large scale applications?](#q61-what-are-the-security-implications-of-aws-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug AWS memory leaks in microservices?](#q62-how-do-you-debug-aws-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for AWS code organization in mobile devices?](#q63-best-practices-for-aws-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement AWS error handling for legacy systems?](#q64-how-do-you-implement-aws-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test AWS functionality in cloud infrastructure?](#q65-how-do-you-test-aws-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle AWS state management in real-time systems?](#q66-how-do-you-handle-aws-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform AWS data validation in distributed systems?](#q67-how-do-you-perform-aws-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate AWS deployment for high-traffic sites?](#q68-how-do-you-automate-aws-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle AWS concurrency issues in embedded systems?](#q69-how-do-you-handle-aws-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement AWS caching in production environments?](#q70-how-do-you-implement-aws-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage AWS configuration for large scale applications?](#q71-how-do-you-manage-aws-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle AWS internationalization (i18n) in microservices?](#q72-how-do-you-handle-aws-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure AWS accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-aws-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize AWS network requests in legacy systems?](#q74-how-do-you-optimize-aws-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle AWS performance optimization for cloud infrastructure?](#q75-how-do-you-handle-aws-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of AWS in real-time systems?](#q76-what-are-the-security-implications-of-aws-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug AWS memory leaks in distributed systems?](#q77-how-do-you-debug-aws-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for AWS code organization in high-traffic sites?](#q78-best-practices-for-aws-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement AWS error handling for embedded systems?](#q79-how-do-you-implement-aws-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test AWS functionality in production environments?](#q80-how-do-you-test-aws-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle AWS state management in large scale applications?](#q81-how-do-you-handle-aws-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform AWS data validation in microservices?](#q82-how-do-you-perform-aws-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate AWS deployment for mobile devices?](#q83-how-do-you-automate-aws-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle AWS concurrency issues in legacy systems?](#q84-how-do-you-handle-aws-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement AWS caching in cloud infrastructure?](#q85-how-do-you-implement-aws-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage AWS configuration for real-time systems?](#q86-how-do-you-manage-aws-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle AWS internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-aws-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure AWS accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-aws-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize AWS network requests in embedded systems?](#q89-how-do-you-optimize-aws-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle AWS performance optimization for production environments?](#q90-how-do-you-handle-aws-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of AWS in large scale applications?](#q91-what-are-the-security-implications-of-aws-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug AWS memory leaks in microservices?](#q92-how-do-you-debug-aws-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for AWS code organization in mobile devices?](#q93-best-practices-for-aws-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement AWS error handling for legacy systems?](#q94-how-do-you-implement-aws-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test AWS functionality in cloud infrastructure?](#q95-how-do-you-test-aws-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle AWS state management in real-time systems?](#q96-how-do-you-handle-aws-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform AWS data validation in distributed systems?](#q97-how-do-you-perform-aws-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate AWS deployment for high-traffic sites?](#q98-how-do-you-automate-aws-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle AWS concurrency issues in embedded systems?](#q99-how-do-you-handle-aws-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement AWS caching in production environments?](#q100-how-do-you-implement-aws-caching-in-production-environments) <span class="intermediate">Intermediate</span>

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

### Q51: How do you implement Blue/Green deployment with ECS CodeDeploy?

**Difficulty**: Advanced

**Strategy:**
Use CodeDeploy with ECS. Define a `TaskSet` and a Load Balancer. CodeDeploy shifts traffic from the Blue target group to the Green target group gradually.

**Code Example:**
```yaml
# appspec.yaml
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:..."
        LoadBalancerInfo:
          ContainerName: "my-app"
          ContainerPort: 80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you use AWS Backup to automate cross-region backups?

**Difficulty**: Intermediate

**Strategy:**
Create a Backup Plan in AWS Backup. Add a rule to copy recovery points to a destination vault in another region for DR compliance.

**Code Example:**
```bash
# Terraform
resource "aws_backup_plan" "example" {
  name = "cross-region-backup"
  rule {
    rule_name = "daily"
    target_vault_name = aws_backup_vault.primary.name
    schedule = "cron(0 12 * * ? *)"
    copy_action {
      destination_vault_arn = aws_backup_vault.secondary.arn
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you use AWS X-Ray for distributed tracing?

**Difficulty**: Intermediate

**Strategy:**
Instrument your application using the X-Ray SDK. Enable X-Ray tracing on Lambda or ECS. It visualizes the service map and latency bottlenecks.

**Code Example:**
```bash
from aws_xray_sdk.core import xray_recorder

@xray_recorder.capture('process_record')
def process_record(record):
    # ... logic
    pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you use AWS Organizations to manage multiple accounts?

**Difficulty**: Intermediate

**Strategy:**
Use AWS Organizations to consolidate billing, apply Service Control Policies (SCPs) to restrict actions across accounts, and automate account creation.

**Code Example:**
```bash
# SCP to deny leaving the organization
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": ["organizations:LeaveOrganization"],
      "Resource": "*"
    }
  ]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you use S3 Object Lambda to modify data on retrieval?

**Difficulty**: Advanced

**Strategy:**
S3 Object Lambda allows you to add your own code to S3 GET requests. Use it to redact PII, resize images, or convert data formats on the fly.

**Code Example:**
```bash
def lambda_handler(event, context):
    # Get original object
    response = requests.get(event['inputS3Url'])
    original_data = response.text
    
    # Modify
    transformed_data = original_data.upper()
    
    # Write back
    s3.write_get_object_response(
        RequestRoute=event['outputRoute'],
        RequestToken=event['outputToken'],
        Body=transformed_data
    )
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you use Athena to analyze VPC Flow Logs?

**Difficulty**: Intermediate

**Strategy:**
Publish VPC Flow Logs to S3. Create an Athena table mapped to the S3 path. Run SQL queries to troubleshoot connectivity or detect threats.

**Code Example:**
```bash
SELECT interface_id, srcaddr, dstaddr, action, count(*) as count
FROM vpc_flow_logs
WHERE action = 'REJECT'
GROUP BY interface_id, srcaddr, dstaddr, action
ORDER BY count DESC
LIMIT 10;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you use Kinesis Data Firehose to transform and load data?

**Difficulty**: Intermediate

**Strategy:**
Firehose delivers streaming data to destinations like S3, Redshift, or OpenSearch. It can transform data using Lambda (e.g., JSON to Parquet) before delivery.

**Code Example:**
```bash
# Terraform
resource "aws_kinesis_firehose_delivery_stream" "extended_s3_stream" {
  name        = "terraform-kinesis-firehose-extended-s3-test-stream"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_role.arn
    bucket_arn = aws_s3_bucket.bucket.arn
    processing_configuration {
      enabled = "true"
      processors {
        type = "Lambda"
        parameters {
          parameter_name  = "LambdaArn"
          parameter_value = aws_lambda_function.lambda_processor.arn
        }
      }
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you use Amazon Macie to discover sensitive data?

**Difficulty**: Beginner

**Strategy:**
Enable Macie on your S3 buckets. It uses ML to automatically classify and discover sensitive data (PII, keys) and generates findings.

**Code Example:**
```bash
aws macie2 create-classification-job     --job-type ONE_TIME     --name "FindPII"     --s3-job-definition BucketDefinitions=[{AccountId=123456789012,Buckets=[my-bucket]}]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use SSM Parameter Store Hierarchy?

**Difficulty**: Intermediate

**Strategy:**
Organize parameters using paths (e.g., `/dev/db/password`, `/prod/db/password`). You can then retrieve all parameters under a path recursively.

**Code Example:**
```bash
aws ssm get-parameters-by-path     --path "/prod/service-a/"     --recursive     --with-decryption
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you use AWS WAF to block SQL Injection attacks?

**Difficulty**: Intermediate

**Strategy:**
Use the AWS Managed Ruleset `AWSManagedRulesSQLiRuleSet` in your Web ACL. It contains pre-configured rules to detect common SQL injection patterns.

**Code Example:**
```bash
{
  "Name": "AWS-AWSManagedRulesSQLiRuleSet",
  "Priority": 0,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesSQLiRuleSet"
    }
  },
  "OverrideAction": { "None": {} },
  "VisibilityConfig": { ... }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
### Q61: What are the security implications of AWS in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```bash
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you debug AWS memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```bash
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for AWS code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```bash
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement AWS error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```bash
try {
  await AWSOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test AWS functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```bash
test('AWS works', () => {
  expect(AWS()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle AWS state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```bash
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform AWS data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```bash
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate AWS deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```bash
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle AWS concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```bash
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement AWS caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```bash
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage AWS configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```bash
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle AWS internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```bash
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure AWS accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```bash
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize AWS network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```bash
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle AWS performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```bash
const start = performance.now();
// AWS logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of AWS in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```bash
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug AWS memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```bash
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for AWS code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```bash
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement AWS error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```bash
try {
  await AWSOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test AWS functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```bash
test('AWS works', () => {
  expect(AWS()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle AWS state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```bash
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform AWS data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```bash
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate AWS deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```bash
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle AWS concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```bash
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement AWS caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```bash
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage AWS configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```bash
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle AWS internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```bash
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure AWS accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```bash
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize AWS network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```bash
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle AWS performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```bash
const start = performance.now();
// AWS logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of AWS in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```bash
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug AWS memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```bash
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for AWS code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```bash
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement AWS error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```bash
try {
  await AWSOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test AWS functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```bash
test('AWS works', () => {
  expect(AWS()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle AWS state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```bash
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform AWS data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```bash
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate AWS deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```bash
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle AWS concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```bash
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement AWS caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```bash
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
