import time
from google.cloud.bigquery.dataset import Dataset
from google.cloud.bigquery.table import Table
from google.cloud import bigquery
import pickle

pbp = """SELECT * FROM `bigquery-public-data.ncaa_basketball.mbb_pbp_sr` WHERE event_coord_x IS NOT NULL AND event_coord_y IS NOT NULL;"""

def createNewTableFromQuery(queryString, destProject, destDataset, destTableName):

    client = bigquery.Client()

    query = (queryString)

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
    createNewTableFromQuery(pbp, "datavizfinal", "datavizfinal", "pbp")
