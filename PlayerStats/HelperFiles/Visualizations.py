# This file accepts X_test,  y_test, and y_pred (predicted labels from classifier)  data for visualizations.
# also takes in y_score which is the probability from the classifier (log reg, svm) that the data point
# belongs to the positive class
#
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

def getROC(X_test, y_test, y_pred, y_score):
    #
    # ROC
    #
    # explanation
    # https://stackoverflow.com/questions/36681449/scikit-learn-return-value-of-logisticregression-predict-proba
    # https://stackoverflow.com/questions/31324218/scikit-learn-how-to-obtain-true-positive-true-negative-false-positive-and-fal
    logit_roc_auc = roc_auc_score(y_test, y_score)
    fpr, tpr, thresholds = roc_curve(y_test, y_score) # gets false pos rate, true pr, and thresh
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.savefig('Log_ROC')
    #plt.show()

def getHeatMap(X_test, y_test, y_pred, y_score):
    #
    #
    # Confusion Matrix
    from sklearn.metrics import confusion_matrix
    confusion_matrix = confusion_matrix(y_test, y_pred)
    print(confusion_matrix)
    df_cm = pd.DataFrame(confusion_matrix, index = ["Actually False", "Actually True"],
                    columns = ["Predicted False", "Predicted True"])
    #plt.figure(figsize = (10,7))
    sns_plot = sns.heatmap(df_cm, annot=True,fmt="d",cmap="YlGnBu")
    #sns_plot.savefig("HEATMAP")
    fig = sns_plot.get_figure()
    fig.savefig("HEATMAP") 

def getTSNE(X_test, y_test, y_pred, y_score):
    #
    #
    # Tsne
    #
    #
    from sklearn.manifold import TSNE
    tsne = TSNE(n_components=2, random_state=42,perplexity=10)
    X_reduced_tsne = tsne.fit_transform(X_test)
    plt.figure(2, figsize=(30, 20),)
    plt.scatter(X_reduced_tsne[:,0], X_reduced_tsne[:,1],s=100, c=y_test.values.ravel(), alpha=0.4)
    plt.savefig('TSNE')

if __name__ == '__main__':
    extractTable("concrete-fabric-234819", "player_data_table", "PlayerData", "playerquery")
