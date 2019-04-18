# Support Vector Machines
# The kernel function can be any of the following:

# linear: .
# polynomial: .  is specified by keyword degree,  by coef0.
# rbf: .  is specified by keyword gamma, must be greater than 0.


# When training an SVM with the Radial Basis Function (RBF) kernel, two parameters must be considered: 
#     C and gamma. The parameter C, common to all SVM kernels, trades off misclassification of training 
#     examples against simplicity of the decision surface. A low C makes the decision surface smooth, 
#     while a high C aims at classifying all training examples correctly. gamma defines how much influence 
#     a single training example has. The larger gamma is, the closer other examples must be to be affected.

# Proper choice of C and gamma is critical to the SVM's performance. 
# One is advised to use sklearn.model_selection.GridSearchCV with C and 
# gamma spaced exponentially far apart to choose good values.

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import svm
import warnings
warnings.filterwarnings('always')


def runSVM(X,y,weight='balanced'):
        # Split the dataset in two equal parts
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        svc = svm.SVC(gamma="scale",class_weight=weight)

        # Set the parameters by cross-validation
        # tuned_parameters = [{'kernel': ['rbf'], 'gamma': [10, 1, 0.1],
        #                 'C': [0.001, 0.01,0.1]},]
        tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1],
                         'C': [0.01]},]
                        #{'kernel': ['linear'], 'C': [0.01, 0.1, 1, 10, 100, 1000]}

        scores = ['precision', 'recall']

        for score in scores:
                #print("# Tuning hyper-parameters for %s" % score)
                #print()

                clf = GridSearchCV(svc, tuned_parameters, cv=5,
                                scoring='%s_macro' % score)
                clf.fit(X_train, y_train.values.ravel())

                #print("Best parameters set found on development set:")
                #print()
                #print(clf.best_params_)
                #print()
                #print("Grid scores on development set:")
                #print()
                means = clf.cv_results_['mean_test_score']
                stds = clf.cv_results_['std_test_score']
                #for mean, std, params in zip(means, stds, clf.cv_results_['params']):
                        #print("%0.3f (+/-%0.03f) for %r"
                        #% (mean, std * 2, params))
                #print()
                #print("Detailed classification report:")
                #print()
                #print("The model is trained on the full development set.")
                #print("The scores are computed on the full evaluation set.")
                #print()
                y_pred = clf.predict(X_test)
                #print(classification_report(y_test, y_pred))
                #print()

        gamma_ = clf.best_params_['gamma']
        C_ = clf.best_params_['C']

        clf2 = svm.SVC(gamma=gamma_, C=C_,probability=True)
        clf2.fit(X_train, y_train.values.ravel())

        y_pred = clf2.predict(X_test)
        y_score = clf2.predict_proba(X_test)[:,1]

        print("\n\n\n")
        print(clf2.score(X,y.values.ravel()))
        return X_test, y_test, y_pred, y_score






