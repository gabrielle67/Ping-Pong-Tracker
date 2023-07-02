data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../backend/lambda_functions"
  output_path = "/tmp/lambda_output.zip"
}

resource "aws_lambda_function" "get_highest_scorer" {
  function_name = "getHighestScorer"
  role          = aws_iam_role.lambda_iam.arn
  handler       = "getHighestScorer/getHighestScorer.lambda_handler"
  runtime       = "python3.9"
  filename      = data.archive_file.lambda.output_path
}
