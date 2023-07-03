variable "file_types" {
  type = map(string)

  default = {
    "html" = "text/html"
    "css"  = "text/css"
    "json" = "application/json"
    "js"   = "application/javascript"
    "png"  = "image/png"
    "jpg"  = "image/jpeg"
    "gif"  = "image/gif"
    "txt"  = "text/plain"
    "map"  = "binary/octet-stream"
  }
}

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

resource "aws_s3_object" "frontend_files" {
    for_each = fileset("../frontend/build/", "**/*")
    bucket   = aws_s3_bucket.ping_pong.id
    key      = each.value
    source   = "../frontend/build/${each.value}"

    content_type = coalesce(
                    lookup(var.file_types, 
                            split(".", each.value)[length(split(".", each.value))-1],
                             "application/octet-stream"))
}

resource "aws_s3_bucket_website_configuration" "ping_pong_site_config" {
    bucket = aws_s3_bucket.ping_pong.id

    index_document {
        suffix =  "index.html" 
        }
}
