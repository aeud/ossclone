# Cloud Storage Migration Tool

This tool allows you to migrate files from a Google Cloud Storage (GCS) bucket to an Alibaba Cloud Object Storage Service (OSS) bucket. The migration process involves downloading a specified blob from GCS and uploading it to OSS.

## Requirements

- Python 3.6 or higher
- Google Cloud SDK
- Alibaba Cloud OSS SDK
- `click` package for command-line interface
- Environment variables for configuration

## Installation

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**

   ```sh
   pip install oss2 google-cloud-storage click
   ```

3. **Set up environment variables:**

   The following environment variables must be set:

   - `TARGET_OSS_BUCKET_DOMAIN_NAME`: Domain name of the target OSS bucket
   - `TARGET_OSS_BUCKET_NAME`: Name of the target OSS bucket
   - `SOURCE_GCS_PROJECT_NAME`: Google Cloud project name containing the source GCS bucket
   - `GOOGLE_GCS_BUCKET_NAME`: Name of the source GCS bucket

   You can set these variables in your shell or in a `.env` file.

   Example:

   ```sh
   export TARGET_OSS_BUCKET_DOMAIN_NAME="your-oss-bucket-domain"
   export TARGET_OSS_BUCKET_NAME="your-oss-bucket-name"
   export SOURCE_GCS_PROJECT_NAME="your-gcs-project-name"
   export GOOGLE_GCS_BUCKET_NAME="your-gcs-bucket-name"
   ```

## Usage

To run the migration tool, use the following command:

```sh
python migrate.py --blob-name <blob-name>
```

Replace `<blob-name>` with the name of the blob you want to migrate from the GCS bucket.

### Example

```sh
python migrate.py --blob-name example-blob.txt
```

This will:

1. Generate a unique filename and download `example-blob.txt` from the GCS bucket to the `/tmp/` directory.
2. Upload the downloaded file to the specified OSS bucket.

## Code Overview

- **Logging Configuration:** Sets up logging to provide informative messages about the migration process.
- **Environment Variables:** Retrieves necessary configuration values from the environment.
- **Main Function:** Parses command-line arguments and initiates the migration process.
- **Download Function:** Downloads a specified blob from the GCS bucket to a local file.
- **Upload Function:** Uploads a local file to the OSS bucket.

### Functions

- `main(blob_name)`: Entry point for the command-line interface. Downloads and uploads the specified blob.
- `download_blob_from_gcs(blob_name, file_name)`: Downloads a blob from the GCS bucket and saves it to a local file.
- `upload_blob_to_oss(file_name, blob_name)`: Uploads a local file to the OSS bucket.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.

---

By following these instructions, you should be able to successfully migrate blobs from Google Cloud Storage to Alibaba Cloud OSS. If you encounter any issues or have questions, please open an issue in the repository.