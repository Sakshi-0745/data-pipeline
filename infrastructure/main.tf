provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "event-raw-data-pipeline"
}

resource "aws_s3_bucket" "processed_bucket" {
  bucket = "processed-event-data"
}
