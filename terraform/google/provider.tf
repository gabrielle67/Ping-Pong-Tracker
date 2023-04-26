terraform {
  required_providers {
    google-beta = {
        source = "hashicorp/google-beta"
        version = "~> 4.0"
    }
  }

  cloud {
    organization = "goob"

    workspaces {
      name = "Ping-Pong-Workspace"
    }
  }
}

provider "google-beta" {
    project = "pingpong-384918"
    region = "us-east1"
}