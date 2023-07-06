data "archive_file" "wins_and_losses_zip" {
  type        = "zip"
  source_dir  = "../package_dirs/getAllWinsandLosses_pkg"
  output_path = "lambda_package2_output.zip"
}

resource "aws_lambda_function" "get_wins_and_losses" {
  function_name = "getAllWinsandLosses"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getAllWinsandLosses/getAllWinsandLosses.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.wins_and_losses_zip.output_path

  environment {
    variables = {
      "CREDENTIALS" = var.credentials
      "SHEET_KEY" = var.sheet_key
    }
  }
}

resource "aws_lambda_function_url" "get_wins_and_losses_url" {
  function_name = aws_lambda_function.get_wins_and_losses.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
  }
}