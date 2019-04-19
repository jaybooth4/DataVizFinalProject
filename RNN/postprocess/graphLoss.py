# -*- coding: utf-8 -*-
import re
import matplotlib.pyplot as plt
import matplotlib
# from LogisticRegression import readBeta

# gradNormReg = u"\|\|∇L\(β_k\)\|\|_2\s*=\s*([0-9]*\.[0-9]*)\s"
# timeReg = u"t\s*=\s*([0-9]*\.[0-9]*)\s"
# accReg = u"ACC\s*=\s*([0-9]*\.[0-9]*)\s"
# precReg = u"PRE\s*=\s*([0-9]*\.[0-9]*)\s"
# recReg = u"REC\s*=\s*([0-9]*\.[0-9]*)\s"
# RMSE = u"5-fold cross validation error is:\s([0-9]*\.[0-9]*)\s"
LOSSReg = 'tensor\(([0-9|e|\.|+]*)'
GameReg = 'Game number: ([0-9]*)'

def parseRegsFromFile(fileName, regex):
    values = []
    with open(fileName, 'r') as fh:
        for line in fh:
            found = re.search(regex, line)#unicode(line, "utf-8"))
            if found:
                match = found.group(1)
                values.append(float(match))
            else:
                continue
    return values

def parseValueFromFile(fileName, regex):
    with open(fileName, 'r') as fh:
        for line in fh:
            found = re.search(regex, unicode(line, "utf-8"))
            if found:
                match = found.group(1)
                return float(match)

def graphResults(x, y, xAxisLabel, yAxisLabel, title):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x, y, label="RNN Loss")
    ax1.set_xlabel(xAxisLabel)
    ax1.set_ylabel(yAxisLabel)
    ax1.set_title(title)
    ax1.legend(loc=0)
    plt.ylim(0, 1000000000)

    plt.savefig(title + '.png')

# indices = list(range(1, 11))
# rmses = [parseValueFromFile("output-d-" + str(i) + ".txt", RMSE) for i in indices]
# graphResults(indices, rmses, "D", "RMSE", "D vs RMSE for Small Dataset")
losses = parseRegsFromFile('../output/trainProgression.txt', LOSSReg)
games = list(range(len(losses)))
graphResults(games, losses, "Games", "Loss", "Loss vs Number of games")