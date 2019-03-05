import matplotlib.pyplot as drawPlot
import pandas

#LOADING DATA FROM FILE
irisData = pandas.read_csv('Irys.data', header=None)

#SEGREGATION OF SPECIFIC TYPES TO PROPER VARIABLE
irisSetosa = irisData.loc[irisData.iloc[:, 4] == 'Iris-setosa']
irisVersicolor = irisData.loc[irisData.iloc[:, 4] == 'Iris-versicolor']
irisVirginica = irisData.loc[irisData.iloc[:, 4] == 'Iris-virginica']

#DRAWING FIRST GRAPH - SEPAL
drawPlot.figure(1)
drawPlot.plot(irisSetosa.iloc[:, 0], irisSetosa.iloc[:, 1], 'm+', label='Iris-setosa')
drawPlot.plot(irisVersicolor.iloc[:, 0], irisVersicolor.iloc[:, 1], 'c+', label='Iris-versicolor')
drawPlot.plot(irisVirginica.iloc[:, 0], irisVirginica.iloc[:, 1], 'k+', label='Iris-virginica')
drawPlot.xlabel('sepalWidth')
drawPlot.ylabel('sepalLength')
drawPlot.legend()
drawPlot.show()

#DRAWING SECOND GRAPH - PETAL
drawPlot.figure(2)
drawPlot.plot(irisSetosa.iloc[:, 2], irisSetosa.iloc[:, 3], 'm+', label='Iris-setosa')
drawPlot.plot(irisVersicolor.iloc[:, 2], irisVersicolor.iloc[:, 3], 'c+', label='Iris-versicolor')
drawPlot.plot(irisVirginica.iloc[:, 2], irisVirginica.iloc[:, 3], 'k+', label='Iris-virginica')
drawPlot.xlabel('petalWidth')
drawPlot.ylabel('petalLength')
drawPlot.legend()
drawPlot.show()
