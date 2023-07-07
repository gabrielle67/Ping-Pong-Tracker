data "archive_file" "opponent_scores_zip" {
  type        = "zip"
  source_dir  = "../package_dirs/getOpponentScores_pkg"
  output_path = "getOpponentScores_output.zip"
}

resource "aws_lambda_function" "get_opponent_scores" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getOpponentScores/getOpponentScores.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.opponent_scores_zip.output_path
  environment {
    variables = {
      "CREDENTIALS" = var.credentials
      "SHEET_KEY" = var.sheet_key
    }
  }
}

resource "aws_lambda_function_url" "get_opponent_scores_url" {
  function_name = aws_lambda_function.get_opponent_scores.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
  }
}