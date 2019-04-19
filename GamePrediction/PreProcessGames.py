# this file requires a CSV file already in the directory

#games2.CSV
#This file will output the cleaned CSV file in a dataframe X with a corresponding label df y

import pandas as pd
import numpy as np
import os

#Columns are the columns we want dropped from the dataset RemCor is boolean representing if we want to remove correlated vars
def preprocessGamesData(cols2Drop, remCor):

    #All game data before dropping of non-numeric columns occur
    gamesPre = pd.read_csv("games2.csv", encoding = "ISO-8859-1", index_col=0)
    #drop all duplicate columns
    gamesPre.drop_duplicates()

    # CreategamesPreill row with 1 if points_game > opp_points_game , 0 otherwise
    gamesPre['WIN'] = np.where(gamesPre['points_game']>gamesPre['opp_points_game'],1,0)
    
    #Remove all non Numeric columns
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    games = gamesPre.select_dtypes(include=numerics)

    #Drop columns specified by 'Columns'
    colsDropping = []
    if cols2Drop == 0:
        colsDropping = ['season','periods','two_points_att','two_points_made','win','points','points_game','field_goals_att','field_goals_made','three_points_made','three_points_att','free_throws_made','free_throws_att','opp_points','opp_points_game','opp_two_points_att','opp_two_points_made','opp_field_goals_att','opp_field_goals_made','opp_three_points_made','opp_three_points_att','opp_free_throws_made','opp_free_throws_att']
    games = gamesPre.drop(colsDropping,1)

    #Make all percentages uniform between 0-1 instead of some being full numbers (e.g. fifty percent from 50 -> .5)
    games.loc[games['field_goals_pct'] > 1, 'field_goals_pct'] *= .01
    games.loc[games['three_points_pct'] > 1, 'three_points_pct'] *= .01
    games.loc[games['two_points_pct'] > 1, 'two_points_pct'] *= .01
    games.loc[games['free_throws_pct'] > 1, 'free_throws_pct'] *= .01
    games.loc[games['opp_field_goals_pct'] > 1, 'opp_field_goals_pct'] *= .01
    games.loc[games['opp_three_points_pct'] > 1, 'opp_three_points_pct'] *= .01
    games.loc[games['opp_two_points_pct'] > 1, 'opp_two_points_pct'] *= .01
    games.loc[games['opp_free_throws_pct'] > 1, 'opp_free_throws_pct'] *= .01

    #Get row and column count
    count_row = games.shape[0]
    count_col = games.shape[1]

    #Drop columns that have more than 5% of NA's in them before dropping all rows with any NA's
    #so as to try to keep as many columns and games of data as possible
    #Indices of columns that qualify and a list to hold them all
    indexC = 0
    listofbadcols=[]
    #Check if the sum of the NA's in each column is larger than acceptable and if so add to list 
    for cols in games:
        if games[cols].isna().sum() > .05*count_row:
            print (cols)      
            listofbadcols.extend([indexC])
        indexC = indexC+1
    #Drop unacceptable columns        
    games.drop(games.columns[listofbadcols],axis=1,inplace=True)

    #Now drop rows with any NA's in them
    games.dropna(inplace=True)

    #Normalize the data
    games=(games-games.min())/(games.max()-games.min())

    #Remove correlated columns if remCor is true
    if remCor:
        games = removeCorrelation(games)

    #Finally split into data and labels 
    X = games.loc[:, games.columns != 'WIN']
    y = games.loc[:, games.columns == 'WIN']

    #Return data and labels!
    return X,y

#A method for removing all correlated columns in a dataset with a threshold of .8
def removeCorrelation(dataset):
    #Set of all the names of deleted columns
    col_corr = set() 
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j] >= .8) and (corr_matrix.columns[j] not in col_corr):
                print('Column ',corr_matrix.columns[i],' is being removed because this cell has a value of ',corr_matrix.iloc[i, j])
                #Getting the name of column
                colname = corr_matrix.columns[i] 
                col_corr.add(colname)
                if colname in dataset.columns:
                    #Deleting the column from the dataset
                    del dataset[colname] 
    return dataset
