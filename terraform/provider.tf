
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.60.0"
    }
  }

  cloud {
    organization = "goob"

    workspaces {
      name = "Ping-Pong-Workspace"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}