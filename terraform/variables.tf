variable "credentials" {
    type        = string
}

variable "sheet_key" {
    type        = string
}

variable "file_types" {
  type = map(string)

  default = {
    "html" = "text/html"
    "css"  = "text/css"
    "json" = "application/json"
    "js"   = "application/javascript"
    "png"  = "image/png"
    "jpg"  = "image/jpeg"
    "gif"  = "image/gif"
    "txt"  = "text/plain"
    "map"  = "binary/octet-stream"
  }
}
