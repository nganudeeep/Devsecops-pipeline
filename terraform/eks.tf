resource "aws_eks_cluster" "main" {
  name     = "${var.project_name}-eks"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = "1.32"

  vpc_config {
    subnet_ids = aws_subnet.public[*].id

    endpoint_public_access  = true
    endpoint_private_access = false
  }

  tags = {
    Name    = "${var.project_name}-eks"
    Project = var.project_name
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluster_policy
  ]
}