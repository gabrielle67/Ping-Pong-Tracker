data "archive_file" "all_player_names_zip" {
  type        = "zip"
  source_dir  = "../package_dirs/getAllPlayerNames_pkg"
  output_path = "getAllPlayerNames_output.zip"
}

resource "aws_lambda_function" "get_all_player_names" {
  function_name = "getAllPlayerNames"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getAllPlayerNames/getAllPlayerNames.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.all_player_names_zip.output_path

  environment {
    variables = {
      "CREDENTIALS" = var.credentials
      "SHEET_KEY" = var.sheet_key
    }
  }
}

resource "aws_lambda_function_url" "get_all_player_names_url" {
  function_name = aws_lambda_function.get_all_player_names.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
  }
}