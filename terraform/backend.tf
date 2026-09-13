terraform {
  backend "s3" {
    bucket = "devsecops-pipeline-407178839892"
    key    = "devsecops/terraform.tfstate"
    region = "us-east-2"
  }
}