resource "aws_s3_bucket" "terraform_state" {
  bucket = "devsecops-pipeline-407178839892"

  tags = {
    Name    = "devsecops-terraform-state"
    Project = "devsecops"
  }
}