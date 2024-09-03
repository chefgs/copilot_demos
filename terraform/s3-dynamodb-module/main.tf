provider "aws" {
  region = var.region
}

module "s3" {
  source          = "./modules/s3"
  s3_bucket_name  = var.s3_bucket_name
  environment     = var.environment
}

module "dynamodb" {
  source              = "./modules/dynamodb"
  dynamodb_table_name = var.dynamodb_table_name
  environment         = var.environment
}
