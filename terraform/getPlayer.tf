data "archive_file" "get_player_zip" {
  type        = "zip"
  source_dir  = "../package_dirs/getPlayer_pkg"
  output_path = "getPlayer_output.zip"
}

resource "aws_lambda_function" "get_player" {
  function_name = "getPlayer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getPlayer/getPlayer.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.get_player_zip.output_path
  environment {
    variables = {
      "CREDENTIALS" = var.credentials
      "SHEET_KEY" = var.sheet_key
    }
  }
}

resource "aws_lambda_function_url" "get_players_url" {
  function_name = aws_lambda_function.get_player.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
  }
}