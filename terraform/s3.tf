resource "aws_s3_bucket" "ping_pong" {
    bucket = "www.ping-pong-tracker.com"
}

resource "aws_s3_bucket_public_access_block" "ping_pong_public_access" {
    bucket = aws_s3_bucket.ping_pong.id

    block_public_acls       = false
    block_public_policy     = false
    ignore_public_acls      = false
    restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "ping_pong_policy"{
    bucket = aws_s3_bucket.ping_pong.id
    policy = data.aws_iam_policy_document.ping_pong_policy_document.json
}

resource "aws_s3_bucket_object" "frontend_files" {
  bucket = aws_s3_bucket.ping_pong.id
  key    = "ping_pong_frontend/"
  source = "../frontend"

}

/*
resource "aws_s3_bucket_website_configuration" "ping_pong_site_config" {
    bucket = aws_s3_bucket.ping_pong.id

    index_document {
        suffix =  "ping_pong_frontend/public/index.html" 
        }
}
*/