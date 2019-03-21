from google.cloud import storage
from google.cloud import bigquery

def extractTable(project, datasetID, tableID, bucket):
    """ Creates an export job from BigQuery to Cloud storage """

    # project = 'bigquery-public-data'
    # dataset_id = 'samples'
    # table_id = 'shakespeare'
    client = bigquery.Client()

    destinationURI = 'gs://{}/{}'.format(bucket, tableID)
    dataset_ref = client.dataset(datasetID, project=project)
    table_ref = dataset_ref.table(tableID)

    extract_job = client.extract_table(
        table_ref,
        destinationURI,
        # Location must match that of the source table.
        location='US')  # API request
    extract_job.result()  # Waits for job to complete.

    print('Exported {}:{}.{} to {}'.format(
        project, datasetID, tableID, destinationURI))

def downloadBlob(bucketName, sourceBlobName, destinationFileName):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(sourceBlobName)

    blob.download_to_filename(destinationFileName)

    print('Blob {} downloaded to {}.'.format(
        sourceBlobName,
        destinationFileName))

extractTable("bigquery-public-data", "ncaa_basketball", "mascots", "datavizfinal")

# downloadBlob("datavizfinal", "test.txt", "test2.txt")
