data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../backend/package"
  output_path = "lambda_output.zip"
}

resource "aws_lambda_function" "get_highest_scorer" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getHighestScorer/getHighestScorer.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.lambda.output_path
}

resource "aws_lambda_function_url" "get_highest_scorer_url" {
  function_name = aws_lambda_function.get_highest_scorer.function_name
  authorization_type = "NONE"
}