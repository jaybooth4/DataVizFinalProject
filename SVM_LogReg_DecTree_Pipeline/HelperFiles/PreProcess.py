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
	X = removeCorrelation(X, THRESHOLD)
	y = players_numeric.loc[:, players_numeric.columns == 'NBA']
	# Our final return variables will be X and y
	return X,y


def preprocessGamesData():
	#this file requires a CSV file already in the directory
	#games2.CSV
	#This file will output the cleaned CSV file in a dataframe X with a corresponding label df y
	#Columns are the columns we want dropped from the dataset RemCor is boolean representing if we want to remove correlated vars
	cols2Drop=0
	remCor=True
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
		colsDropping = ['season','periods','two_points_att','two_points_made','points','points_game','field_goals_att','field_goals_made','three_points_made','three_points_att','free_throws_made','free_throws_att','opp_points','opp_points_game','opp_two_points_att','opp_two_points_made','opp_field_goals_att','opp_field_goals_made','opp_three_points_made','opp_three_points_att','opp_free_throws_made','opp_free_throws_att']
	games = games.drop(colsDropping,1)

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
		games = removeCorrelation(games, .8)

	#Finally split into data and labels 
	X = games.loc[:, games.columns != 'WIN']
	y = games.loc[:, games.columns == 'WIN']

	#Return data and labels!
	return X,y	
	
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























