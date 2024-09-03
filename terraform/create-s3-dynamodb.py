import os

# Define the directory structure and files
structure = {
    "main.tf": """
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
""",
    "variables.tf": """
variable "region" {
  description = "AWS region"
  default     = "us-west-2"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket for Terraform state"
  default     = "your-s3-bucket-name"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for Terraform state locking"
  default     = "your-dynamodb-table-name"
}

variable "environment" {
  description = "Environment tag"
  default     = "dev"
}
""",
    "outputs.tf": """
output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = module.s3.s3_bucket_name
}

output "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  value       = module.dynamodb.dynamodb_table_name
}
""",
    "backend.tf": """
terraform {
  backend "s3" {
    bucket         = "your-s3-bucket-name"
    key            = "path/to/your/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "your-dynamodb-table-name"
  }
}
""",
    "modules": {
        "s3": {
            "main.tf": """
resource "aws_s3_bucket" "terraform_state_bucket" {
  bucket = var.s3_bucket_name

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  lifecycle_rule {
    id      = "log"
    enabled = true

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    expiration {
      days = 365
    }
  }

  tags = {
    Name        = "terraform-state-bucket"
    Environment = var.environment
  }
}
""",
            "variables.tf": """
variable "s3_bucket_name" {
  description = "Name of the S3 bucket for Terraform state"
  type        = string
}

variable "environment" {
  description = "Environment tag"
  type        = string
  default     = "dev"
}
""",
            "outputs.tf": """
output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.terraform_state_bucket.id
}
"""
        },
        "dynamodb": {
            "main.tf": """
resource "aws_dynamodb_table" "terraform_state_lock_table" {
  name         = var.dynamodb_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name        = "terraform-state-lock-table"
    Environment = var.environment
  }
}
""",
            "variables.tf": """
variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for Terraform state locking"
  type        = string
}

variable "environment" {
  description = "Environment tag"
  type        = string
  default     = "dev"
}
""",
            "outputs.tf": """
output "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  value       = aws_dynamodb_table.terraform_state_lock_table.name
}
"""
        }
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content.strip() + "\n")

# Define the directory structure
directories = ["s3-dynamodb-module"]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    
# Create the directory structure and files
create_structure("./s3-dynamodb-module", structure)