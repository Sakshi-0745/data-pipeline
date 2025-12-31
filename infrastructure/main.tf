provider "aws" {
  region = "ap-south-1"
}

data "aws_s3_bucket" "raw_bucket" {
  bucket = "newevent-raw-data-pipeline"
}

data "aws_s3_bucket" "processed_bucket" {
  bucket = "newprocessed-event-data"
}
