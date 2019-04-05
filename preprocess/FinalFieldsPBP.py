import pandas as pd

IN_FILE_NAME = "../data/pbp_from_query_ordered.csv"
OUT_FILE_NAME = "../data/pbp_preprocessed.csv"
DROP_COLS = ['game_clock', 'turnover_type', 'rebound_type', 'timeout_duration', 'event_id', 'event_description', 'shot_type', 'shot_subtype', 'type', 'shot_made', 'three_point_shot']
CAT_VARS = ['team_basket', 'event_type']
FILL_NA = 'points_scored'


def dropCols(pbpDF, dropCols):
    # Drops unneeded columns
    return pbpDF.drop(dropCols, 1)

def fillNA(pbpDF, col, value):
    # Fill a column with a given value
    pbpDF[FILL_NA] = pbpDF[FILL_NA].fillna(value)
    return pbpDF

def encodeCategorical(df, catColumns):
    # Encodes categorical variables
    for var in catColumns:
        catDf = pd.get_dummies(df[var], prefix=var)
        df=df.join(catDf)
    df.drop(catColumns, 1, inplace=True)
    return df

def preprocessPBPData(fileName):
    # Preprocesses the dataset
    pbpDF = pd.read_csv(fileName)
    pbpDF = dropCols(pbpDF, DROP_COLS)
    pbpDF = fillNA(pbpDF, FILL_NA, 0.0)
    pbpDF = encodeCategorical(pbpDF, CAT_VARS)
    return pbpDF

def main():
    preprocessedData = preprocessPBPData(IN_FILE_NAME)
    preprocessedData.to_csv(OUT_FILE_NAME, index=False)

if __name__ == '__main__':
    main()