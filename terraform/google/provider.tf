terraform {
  required_providers {
    google-beta = {
        source = "hashicorp/google-beta"
        version = "4.63.1"
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
    region = "us-central1"
    project = "main-proj-385806"

}