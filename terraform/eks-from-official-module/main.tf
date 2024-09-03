provider "aws" {
  region = var.region
}

module "vpc" {
  source = "./modules/vpc"
}

module "iam" {
  source = "./modules/iam"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "18.0.0"
  cluster_name    = var.cluster_name
  cluster_version = "1.21"
  subnets         = concat(
    module.vpc.public_subnets,
    module.vpc.private_subnets
  )
  vpc_id          = module.vpc.vpc_id

  node_groups = {
    eks_nodes = {
      desired_capacity = var.desired_capacity
      max_capacity     = var.max_size
      min_capacity     = var.min_size

      instance_type = var.instance_type

      key_name = "your-key-pair-name"

      iam_role_arn = module.iam.eks_node_group_role_arn
    }
  }

  cluster_iam_role_name = module.iam.eks_cluster_role_name
  cluster_iam_role_arn  = module.iam.eks_cluster_role_arn
}
