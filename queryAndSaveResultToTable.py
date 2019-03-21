import time
from google.cloud.bigquery.dataset import Dataset
from google.cloud.bigquery.table import Table
from google.cloud import bigquery
import pickle

def createNewTableFromQuery(destProject, destDataset, destTableName):

    client = bigquery.Client()

    query = ("""SELECT *
        FROM `bigquery-public-data.ncaa_basketball.mascots`
        LIMIT 10""")

    jobConfig = bigquery.QueryJobConfig()

    # Set configuration.query.destinationTable
    destination_dataset = client.dataset(destDataset, project=destProject)
    destination_table = destination_dataset.table(destTableName)
    jobConfig.destination = destination_table

    # Set configuration.query.createDisposition
    jobConfig.create_disposition = 'CREATE_IF_NEEDED'

    # Set configuration.query.writeDisposition
    jobConfig.write_disposition = 'WRITE_APPEND'

    # Start the query
    job = client.query(query, job_config=jobConfig)

    # Wait for the query to finish
    job.result()

    print("success")

if __name__ == '__main__':
    createNewTableFromQuery("datavizfinal", "datavizfinal", "mascots")
