terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
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

provider "google" {
    region = "us-central1"
    project = "main-proj-385806"
    credentials = var.GOOGLE_APPLICATIONS_CREDENTIALS
}