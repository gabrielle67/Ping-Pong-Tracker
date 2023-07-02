data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/backend/lambda_functions"
  output_path = "lambda_output.zip"
}

resource "aws_lambda_function" "get_highest_scorer" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getHighestScorer.lambda_handler"
  runtime       = "python3.9"
  filename      = "lambda_output/lambda_functions/getHighestScorer/getHighestScorer.py"
}