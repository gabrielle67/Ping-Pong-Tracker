data "archive_file" "highest_scorer_zip" {
  type        = "zip"
  source_dir  = "$GITHUB_WORKSPACE/package_dirs/getHighestScorer_pkg"
  output_path = "lambda_package_output.zip"
}

resource "aws_lambda_function" "get_highest_scorer" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getHighestScorer/getHighestScorer.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.highest_scorer_zip.output_path

  environment {
    variables = {
      "CREDENTIALS" = var.credentials
      "SHEET_KEY" = var.sheet_key
    }
  }
}

resource "aws_lambda_function_url" "get_highest_scorer_url" {
  function_name = aws_lambda_function.get_highest_scorer.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
  }
}