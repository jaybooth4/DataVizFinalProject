from google.cloud import bigquery

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