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
  source          = "./modules/eks"
  cluster_name    = var.cluster_name
  vpc_id          = module.vpc.vpc_id
  public_subnets  = module.vpc.public_subnets
  private_subnets = module.vpc.private_subnets
  desired_capacity = var.desired_capacity
  max_size        = var.max_size
  min_size        = var.min_size
  instance_type   = var.instance_type
  cluster_iam_role_arn = module.iam.eks_cluster_role_arn
  node_group_iam_role_arn = module.iam.eks_node_group_role_arn
}
