from google.cloud import storage


def downloadBlob(bucketName, sourceBlobName, destinationFileName):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(sourceBlobName)

    blob.download_to_filename(destinationFileName)

    print('Blob {} downloaded to {}.'.format(
        sourceBlobName,
        destinationFileName))

# downloadBlob("datavizfinal", "test.txt", "test2.txt")