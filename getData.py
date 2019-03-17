from google.cloud import bigquery
import pickle 

# Credential file is stored locally and not included in version control
# Based on the GOOGLE_APPLICATION_CREDENTIALS path parameter

def query_ncaa():
    client = bigquery.Client()
    query_job = client.query("""
        SELECT *
        FROM `bigquery-public-data.ncaa_basketball.mascots`
        LIMIT 10""")

    results = query_job.result()  # Waits for job to complete.

    print(type(results))

    for row in results:
        print(row)

if __name__ == '__main__':
    query_ncaa()