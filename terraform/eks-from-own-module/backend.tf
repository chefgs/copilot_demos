terraform {
  backend "s3" {
    bucket         = "tf-backend-dev-c901f4d8481c0a19"
    key            = "dev/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "dynamodb-dev-e5707f670a8425a4"
  }
}
