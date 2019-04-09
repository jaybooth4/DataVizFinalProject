# This file requires you already have 2 csvs in the directory

# PlayerData.csv
# NBAonlyNames.csv

# This file relies on another process to bring these files in
# The end goal of this file will be numeric data for further use.
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

#removes columns with this amount (or higher) of co-correlation with any other column
#THRESHOLD = 0.7

def preprocessPlayerData(THRESHOLD=0.7):
    players = pd.read_csv("PlayerData.csv",encoding = "ISO-8859-1")
    players.drop_duplicates()
    #now remove any rows with N/A
    players=players.dropna(how="any")
    #add full name column
    players['full_name'] = players['first_name'] + ' ' + players['last_name']

    #Load NBA names from CSV
    NBA = pd.read_csv("NBAonlyNames.csv")
    NBA.drop_duplicates()
    print('')

    #Upper case all names
    players['full_name'] = players['full_name'].str.upper()
    NBA['NBA_Player'] = NBA['NBA_Player'].str.upper()

    # Create new column called NBA. fill row with 1 if name found in NBA, 0 otherwise
    players['NBA'] = np.where(players.full_name.isin(NBA.NBA_Player),1,0)

    # extract only numeric columns. Make algorithmic later? Keep in mind we can't have too many variables because we need enough data to support them
    players_numeric = players[['jersey_num','height','weight','avg_points','avg_mins', 'avg_fg_made','avg_fg_att','avg_fg_pct','avg_thrp_made','avg_thrp_att','avg_thrp_pct','avg_twop_made','avg_twop_pct','avg_blocked_att','avg_free_thr_made','avg_free_thr_att','avg_free_thr_pct','avg_off_rebnd','avg_def_rebnd','avg_rebnd','avg_assists','avg_turnovers','avg_steals','avg_blocks','avg_ATR','avg_personal_fouls','avg_tech_fouls','avg_flagrant_fouls','NBA']]

    #normailize data from 0-1
    players_numeric=(players_numeric-players_numeric.min())/(players_numeric.max()-players_numeric.min())

    #Now separate data into data where players made it to the NBA, and data where they did not
    # Capital X will be all data except whether or not they made the NBA
    # y is the labels for the X data
    X = players_numeric.loc[:, players_numeric.columns != 'NBA']

    y = players_numeric.loc[:, players_numeric.columns == 'NBA']
    # Our final return variables will be X and y

    #Now check for correlated features and remove them
    def removeCorrelation(dataset, threshold):
        col_corr = set() # Set of all the names of deleted columns
        corr_matrix = dataset.corr()
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if (corr_matrix.iloc[i, j] >= threshold) and (corr_matrix.columns[j] not in col_corr):
                    #print('Column ',corr_matrix.columns[i],' is being removed because this cell has a value of ',corr_matrix.iloc[i, j])
                    colname = corr_matrix.columns[i] # getting the name of column
                    col_corr.add(colname)
                    if colname in dataset.columns:
                        del dataset[colname] # deleting the column from the dataset
        return dataset

    X = removeCorrelation(X, THRESHOLD)
    return X,y





















