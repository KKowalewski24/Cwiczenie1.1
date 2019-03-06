import pandas
from scipy import stats
import statistics
import numpy


def printing(incomingData):
    inTotal = pandas.DataFrame(
        columns=['Szer Kielicha', 'Dlug Kielicha', 'Szer Platka', 'Dlug Platka'])

    inTotal.loc['Mininum'] = [i for i in incomingData.min(numeric_only=True)]
    inTotal.loc['Maximum'] = [i for i in incomingData.max(numeric_only=True)]
    inTotal.loc['Rozstep'] = [i for i in inTotal.loc['Maximum'] - inTotal.loc['Mininum']]

    inTotal.loc['Sred Arytm'] = [i for i in incomingData.mean()]
    inTotal.loc['Sred Geom'] = stats.gmean(incomingData.iloc[:, 0:4])
    inTotal.loc['Sred Harm'] = stats.hmean(incomingData.iloc[:, 0:4])
    inTotal.loc['Sred potegowa 2 rzedu '] = [i for i in (
            ((incomingData.iloc[:, 0:4] ** 2).sum() / incomingData.shape[0]) ** (1. / 2))]
    inTotal.loc['Sred potegowa 3 rzedu '] = [i for i in (
            ((incomingData.iloc[:, 0:4] ** 3).sum() / incomingData.shape[0]) ** (1. / 3))]

    inTotal.loc['Wariancja'] = [i for i in incomingData.var()]
    inTotal.loc['Odchylenie standardowe'] = [i for i in incomingData.std()]
    inTotal.loc['Kurtoza'] = stats.kurtosis(incomingData.iloc[:, 0:4], fisher=False)

    inTotal.loc['Pierszy Kwartyl'] = [numpy.quantile(incomingData.iloc[:, i], .25) for i in range(4)]
    inTotal.loc['Mediana'] = [statistics.median(incomingData.iloc[:, i]) for i in range(4)]
    inTotal.loc['Trzeci Kwartyl'] = [numpy.quantile(incomingData.iloc[:, i], .75) for i in range(4)]

    return inTotal
