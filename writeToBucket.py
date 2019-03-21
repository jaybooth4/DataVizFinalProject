from google.cloud import bigquery

def extractTable(project, datasetID, tableID, bucket):
    """ Creates an export job from BigQuery to Cloud storage """

    client = bigquery.Client()

    destinationURI = 'gs://{}/{}'.format(bucket, tableID)
    dataset_ref = client.dataset(datasetID, project=project)
    table_ref = dataset_ref.table(tableID)

    extract_job = client.extract_table(
        table_ref,
        destinationURI,
        location='US') 

    # Waits for job to complete.
    extract_job.result()  

    print('Exported {}:{}.{} to {}'.format(
        project, datasetID, tableID, destinationURI))

extractTable("bigquery-public-data", "ncaa_basketball", "mascots", "datavizfinal")
