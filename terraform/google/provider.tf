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
    project = google_project.default.project_id
    region = "us-central1"
}