import os
import boto3
from dotenv import load_dotenv

#Loading the seceret keys from the .env file
load_dotenv()

# Telling boto3 to grab those keys and connect to S3
s3_client = boto3.client('s3', region_name=os.getenv('AWS_REGION'))
BUCKET_NAME = "kunal-portfolio-rag-data"
def upload_document(local_file_path, s3_file_name):
    """Uploads a file from your computer to your S3 bucket."""
    try:
        print(f"Attempting to upload {local_file_path}...")
        # The actual upload command
        s3_client.upload_file(local_file_path, BUCKET_NAME, s3_file_name)
        print(f"Success! {s3_file_name} is now safely in the cloud.")
    except Exception as e:
        print(f"Upload failed: {e}")

def download_document(s3_file_name, local_file_path):
    """Downloads a file from your S3 bucket to your computer."""
    try:
        print(f"Attempting to pull down {s3_file_name}...")
        s3_client.download_file(BUCKET_NAME, s3_file_name, local_file_path)
        print(f"Success! File downloaded and saved as {local_file_path}.")
    except Exception as e:
        print(f"Download failed: {e}")