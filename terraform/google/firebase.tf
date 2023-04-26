resource "google_firebase_database_instance" "ping_pong_firebase_database" {
  provider = google-beta
  project  = google_firebase_project.default.project
  region   = "us-central1"
  instance_id = "ping_pong_firebase_database"
}