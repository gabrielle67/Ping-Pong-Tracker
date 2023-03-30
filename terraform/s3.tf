resource "aws_s3_bucket" "ping_pong" {
    bucket = "Inception_ping_pong_tracker.com"
}

resource "aws_s3_bucket_acl" "ping_pong_acl" {
    bucket = aws_s3_bucket.ping_pong.id
    acl    = "public"
}

resource "aws_s3_bucket_policy" "ping_pong_policy"{
    bucket = aws_s3_bucket.ping_pong.id
    policy = data.ping_pong_policy_document.json
}

resource "aws_s3_bucket_website_configuration" "ping_pong" {
    bucket = aws_s3_bucket.ping_pong_bucket.id
    #TODO: add html
}
