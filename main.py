import matplotlib.pyplot as drawPlot
import pandas
import functions

# LOADING DATA FROM FILE
irisData = pandas.read_csv('Irys.data', header=None)

# SEGREGATION OF SPECIFIC TYPES TO PROPER VARIABLE
irisSetosa = irisData.loc[irisData.iloc[:, 4] == 'Iris-setosa']
irisVersicolor = irisData.loc[irisData.iloc[:, 4] == 'Iris-versicolor']
irisVirginica = irisData.loc[irisData.iloc[:, 4] == 'Iris-virginica']

# DRAWING FIRST GRAPH - SEPAL
drawPlot.figure(1)
drawPlot.plot(irisSetosa.iloc[:, 0], irisSetosa.iloc[:, 1], 'm+', label='Iris-setosa')
drawPlot.plot(irisVersicolor.iloc[:, 0], irisVersicolor.iloc[:, 1], 'c+', label='Iris-versicolor')
drawPlot.plot(irisVirginica.iloc[:, 0], irisVirginica.iloc[:, 1], 'k+', label='Iris-virginica')
drawPlot.xlabel('Szerokosc Dzialki Kielicha')
drawPlot.ylabel('Dlugosc Dzialki Kielicha')
drawPlot.legend()
drawPlot.show()

# DRAWING SECOND GRAPH - PETAL
drawPlot.figure(2)
drawPlot.plot(irisSetosa.iloc[:, 2], irisSetosa.iloc[:, 3], 'm+', label='Iris-setosa')
drawPlot.plot(irisVersicolor.iloc[:, 2], irisVersicolor.iloc[:, 3], 'c+', label='Iris-versicolor')
drawPlot.plot(irisVirginica.iloc[:, 2], irisVirginica.iloc[:, 3], 'k+', label='Iris-virginica')
drawPlot.xlabel('Szerokosc Platka')
drawPlot.ylabel('Dlugosc Platka')
drawPlot.legend()
drawPlot.show()



#############################################################################################################

def printSeperator():
    print('=================================================================================================')


#############################################################################################################

print('\nPodsumowanie Ogolne')
print(functions.printing(irisData))
printSeperator()

print('\nPodsumowanie Iris Setosa')
print(functions.printing(irisSetosa))
printSeperator()

print('\nPodsumowanie Iris Versicolor')
print(functions.printing(irisVersicolor))
printSeperator()

print('\nPodsumowanie Iris Virginica')
print(functions.printing(irisVirginica))
printSeperator()
