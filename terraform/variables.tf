variable "aws_region" {
  description = "AWS region for the DevSecOps infrastructure"
  type        = string
  default     = "us-east-2"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "devsecops"
}

variable "vpc_cidr" {
  description = "CIDR block for the EKS VPC"
  type        = string
  default     = "172.20.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones for the EKS VPC"
  type        = list(string)
  default     = ["us-east-2a", "us-east-2b"]
}