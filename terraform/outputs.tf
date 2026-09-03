output "s3_bucket_arn" {
  value       = aws_s3_bucket.interview_guide_assets.arn
  description = "ARN of the S3 bucket"
}

output "cloudfront_domain_name" {
  value       = aws_cloudfront_distribution.cdn.domain_name
  description = "CloudFront distribution domain name"
}
