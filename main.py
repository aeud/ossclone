import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from google.cloud import storage
import os
import uuid
import click
import logging


# Setup logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TARGET_OSS_BUCKET_DOMAIN_NAME = os.environ.get("TARGET_OSS_BUCKET_DOMAIN_NAME")
TARGET_OSS_BUCKET_NAME = os.environ.get("TARGET_OSS_BUCKET_NAME")
SOURCE_GCS_PROJECT_NAME = os.environ.get("SOURCE_GCS_PROJECT_NAME")
GOOGLE_GCS_BUCKET_NAME = os.environ.get("GOOGLE_GCS_BUCKET_NAME")

@click.command()
@click.option(
    "--blob-name",
    required=True,
)
def main(blob_name):
    uid = uuid.uuid4()
    file_name = "/tmp/%s" % uid
    # Download the blob to a file
    download_blob_from_gcs(blob_name, file_name)
    # Upload the file to OSS bucket
    upload_blob_to_oss(file_name, blob_name)

def download_blob_from_gcs(blob_name, file_name):
    storage_client = storage.Client(project=SOURCE_GCS_PROJECT_NAME)
    bucket = storage_client.get_bucket(GOOGLE_GCS_BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(file_name)

def upload_blob_to_oss(file_name, blob_name):
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
    bucket = oss2.Bucket(auth, TARGET_OSS_BUCKET_DOMAIN_NAME, TARGET_OSS_BUCKET_NAME)
    bucket.put_object_from_file(blob_name, file_name)

if __name__ == "__main__":
    main()