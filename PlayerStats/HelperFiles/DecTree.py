# This file will take in data from PreProcess.py (X=all player data, y=labels (NBA or not))
# and create a random forest tree modelfrom it.

# Vary the class_weight to be not 'balanced' for better accuracy, but fewer NBA guesses correct 
#
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def runDecTree(X,y,weight='balanced'):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0,class_weight = weight)

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        y_score = clf.predict_proba(X_test)[:,1]
        
        return X_test, y_test, y_pred, y_score






