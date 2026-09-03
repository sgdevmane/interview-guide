variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "AWS deployment region"
}

variable "environment" {
  type        = string
  default     = "production"
  description = "Deployment environment (staging/production)"
}

variable "s3_bucket_name" {
  type        = string
  default     = "interview-guide-production-assets"
  description = "S3 bucket name for hosting static assets"
}
