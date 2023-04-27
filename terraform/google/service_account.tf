resource "google_service_account" "ping_pong_service_account" {
  account_id   = "ping-pong-svc-acct"
  display_name = "Ping Pong Service Account"
}

resource "google_service_account_key" "ping_pong_service_account_key" {
  service_account_id = google_service_account.ping_pong_service_account.id
  key_algorithm      = "KEY_ALG_RSA_2048"
}
