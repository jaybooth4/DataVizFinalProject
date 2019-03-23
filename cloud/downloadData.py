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

downloadBlob("datavizfinal", "pbp-000000000000", "pbp-0.csv")
downloadBlob("datavizfinal", "pbp-000000000001", "pbp-1.csv")
downloadBlob("datavizfinal", "pbp-000000000002", "pbp-2.csv")
downloadBlob("datavizfinal", "pbp-000000000003", "pbp-3.csv")
downloadBlob("datavizfinal", "pbp-000000000004", "pbp-4.csv")
downloadBlob("datavizfinal", "pbp-000000000005", "pbp-5.csv")
downloadBlob("datavizfinal", "pbp-000000000006", "pbp-6.csv")