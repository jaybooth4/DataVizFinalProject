import time
from google.cloud.bigquery.dataset import Dataset
from google.cloud.bigquery.table import Table
from google.cloud import bigquery
import pickle
import os

playerQuery = """SELECT
  MAX(first_name) AS first_name,
  MAX(last_name) AS last_name,
  MAX(jersey_number) AS jersey_num,
  MAX(height) AS height,
  MAX(weight) AS weight,
  MAX(birthplace_state) AS birth_state,
  MAX(Teams.market) AS TeamName,
  AVG(points) AS avg_points,
  AVG(minutes_int64) AS avg_mins,
  MAX(position) AS position,
  AVG(field_goals_made) AS avg_fg_made,
  AVG(field_goals_att) AS avg_fg_att,
  AVG(field_goals_pct) AS avg_fg_pct,
  AVG(three_points_made) AS avg_thrp_made,
  AVG(three_points_att) AS avg_thrp_att,
  AVG(three_points_pct) AS avg_thrp_pct,
  AVG(two_points_made) AS avg_twop_made,
  AVG(two_points_pct) AS avg_twop_pct,
  AVG(blocked_att) AS avg_blocked_att,
  AVG(free_throws_made) AS avg_free_thr_made,
  AVG(free_throws_att) AS avg_free_thr_att,
  AVG(free_throws_pct) AS avg_free_thr_pct,
  AVG(offensive_rebounds) AS avg_off_rebnd,
  AVG(defensive_rebounds) AS avg_def_rebnd,
  AVG(rebounds) AS avg_rebnd,
  AVG(assists) AS avg_assists,
  AVG(turnovers) AS avg_turnovers,
  AVG(steals) AS avg_steals,
  AVG(blocks) AS avg_blocks,
  AVG(assists_turnover_ratio)  AS avg_ATR,
  AVG(personal_fouls)  AS avg_personal_fouls,
  MAX(tech_fouls) AS avg_tech_fouls,
  MAX(flagrant_fouls) AS avg_flagrant_fouls
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` AS Players
# USE INNER JOIN to gather alphabetical team names for each player as well.
INNER JOIN `bigquery-public-data.ncaa_basketball.mbb_teams` AS Teams 
ON Players.team_id = Teams.id
#concat all results so every player is in this list only once.
GROUP BY player_id;"""

def createNewTableFromQuery(queryString, destProject, destDataset, destTableName):

    print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

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
    createNewTableFromQuery(playerQuery, "concrete-fabric-234819", "player_data_table", "PlayerData")
# Yes I know I messed up the "destDataset" name. 