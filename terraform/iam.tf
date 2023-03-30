data "aws_iam_policy_document" "ping_pong_policy_document" {
    statement {
        sid       = "PublicReadGetObject"
        effect    = "Allow"
        actions   = ["s3:GetObject"]
        resources = [aws_s3_bucket.ping_pong.arn + "/*"]

        principals {
            identifiers = ["*"]
            type        = "*"
        }
    }
}