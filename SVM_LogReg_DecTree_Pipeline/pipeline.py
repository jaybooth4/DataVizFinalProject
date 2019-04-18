from HelperFiles.queryAndSaveResultToTable import createNewTableFromQuery
from HelperFiles.writeToBucket import extractTable
from HelperFiles.downloadData import downloadBlob
from HelperFiles.queryAndSaveResultToTable import playerQuery

from HelperFiles.PreProcess import preprocessPlayerData
from HelperFiles.PreProcess import preprocessGamesData
from HelperFiles.LogReg import runLogisticRegression
from HelperFiles.SVM import runSVM
from HelperFiles.DecTree import runDecTree
from HelperFiles.Visualizations import getHeatMap, getROC, getTSNE














def main():
    #createNewTableFromQuery(playerQuery, "concrete-fabric-234819", "player_data_table", "PlayerData")
    #extractTable("concrete-fabric-234819", "player_data_table", "PlayerData", "playerquery")
    #downloadBlob("playerquery", "PlayerData-000000000000", "PlayerData.csv")

    #X,y = preprocessPlayerData()
    #X,y = preprocessGamesData()
    #X_test, y_test, y_pred, y_score = runLogisticRegression(X,y)
    #X_test, y_test, y_pred, y_score = runSVM(X,y)
    #X_test, y_test, y_pred, y_score = runDecTree(X,y)

    #getROC(X_test, y_test, y_pred, y_score)
    #getHeatMap(X_test, y_test, y_pred, y_score)
    #getTSNE(X_test, y_test, y_pred, y_score)





if __name__ == '__main__':
    main()