data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../backend/package"
  output_path = "lambda_output.zip"
}

variable "credentials" {
    type        = string
}

variable "sheet_key" {
    type        = string
}

resource "aws_lambda_function" "get_highest_scorer" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getHighestScorer/getHighestScorer.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.lambda.output_path

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