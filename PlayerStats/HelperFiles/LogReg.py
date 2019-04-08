# This file will take in data from PreProcess.py (X=all player data, y=labels (NBA or not))
# and create a logistic regression modelfrom it.

# outputs X_test, y_test, y_pred, y_score

# # Properties to tweak:
#     Class weighting!
#     unless specified to nothing, make the classifier use balanced mode which 
#     uses the values of y to automatically adjust weights inversely proportional 
#     to class frequencies in the input data 
weight = 'balanced'

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#import seaborn as sns
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import metrics
import statsmodels.api as sm

def runLogisticRegression(X,y,weight='balanced'):
    #do logistic regression so we can see p values of column variables
    logit_model=sm.Logit(y,X)
    result=logit_model.fit()
    print(result.summary2())

    #remove variables with a p value greater than 0.05
    droplist = []
    for idx,pval in enumerate(result.pvalues):
        if pval >= 0.05:
                print(X.columns[idx], idx, pval )
                droplist.append(X.columns[idx])
    print(droplist)
    X=X.drop(columns=droplist)
    
    #print(X.columns)
    #class_weight=weight
    # Actually train the classifier now that we have the good data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression(class_weight=weight)
    logreg.fit(X_train, y_train.values.ravel())

    y_pred = logreg.predict(X_test)
    #print('Accuracy of logistic regression classifier on test set: {:.5f}'.format(logreg.score(X_test, y_test)))
    #y_score = logreg.predict_proba(X_test) # returns probs that data points belong to neg and pos classes
    #only keep pos probs actually
    y_score = logreg.predict_proba(X_test)[:,1]

    return X_test, y_test, y_pred, y_score






