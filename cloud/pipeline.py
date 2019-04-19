from queryAndSaveResultToTable import createNewTableFromQuery
from writeToBucket import extractTable
from downloadData import downloadBlob

queryPbpSub = "SELECT game_id, elapsed_time_sec, team_basket, event_id, event_description, event_coord_x, event_coord_y, event_type, type, shot_made, shot_type, shot_subtype, three_point_shot, points_scored, turnover_type, rebound_type, timeout_duration FROM `bigquery-public-data.ncaa_basketball.mbb_pbp_sr` WHERE (event_coord_x IS NOT NULL OR event_coord_y IS NOT NULL) OR (event_coord_x != 0 AND event_coord_y != 0) ORDER BY game_id, elapsed_time_sec;"


def main():
    # createNewTableFromQuery(queryPbpSub, "datavizfinal", "datavizfinal", "pbp_subset_ordered_no_0")
    # extractTable("datavizfinal", "datavizfinal", "pbp_subset_ordered_no_0", "datavizfinal")
    # downloadBlob("datavizfinal", "pbp_subset_ordered_no_0-000000000000", "pbp_subset_ordered_no_0.csv")

if __name__ == '__main__':
    main()