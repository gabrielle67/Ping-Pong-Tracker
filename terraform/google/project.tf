resource "google_project" "ping_pong_project" {
  provider = google-beta
  project_id = "ping-pong"
  name       = "Ping-Pong-Project"
  labels     = {
    "firebase" = "enabled"
  }
}

resource "google_firebase_project" "ping_pong_firebase_project" {
  provider = google-beta
  project  = google_project.default.project_id
}