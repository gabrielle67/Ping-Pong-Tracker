data "aws_iam_policy_document" "ping_pong_policy_document" {
    statement {
        sid       = "PublicReadGetObject"
        effect    = "Allow"
        actions   = ["s3:GetObject", "s3:PutObject"]
        resources = ["${aws_s3_bucket.ping_pong.arn}/*"]

        principals {
            identifiers = ["*"]
            type        = "*"
        }
    }
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource aws_iam_role "lambda_iam" {
    name = "lambda_iam"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
}