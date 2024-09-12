provider "aws" {
  region = var.region
}


module "vpc" {
  source = "./modules/vpc"
  vpc_cidr = var.vpc_cidr_block
  public_subnets = var.public_subnet_cidr_blocks
  private_subnets = var.private_subnet_cidr_blocks
}

data "aws_availability_zones" "available" {}

locals {
  availability_zones = data.aws_availability_zones.available.names
}

module "iam" {
  source = "./modules/iam"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version = "~> 18.0"

  cluster_name    = "gs-eks-cluster"
  cluster_version = "1.25"
  
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.public_subnets  # Add this line to provide subnet IDs
}
