# /////////////////////////////////////////////////////////////////// Imports #
from statistics import median

import pandas
from numpy import quantile
from scipy import stats


# /////////////////////////////////////////////////////////// Iris statistics #
def print_iris_statistics(data):
    # --------------------------------------------------- Create data frame < #
    df = pandas.DataFrame(
            columns = ["Dł. d. k.",
                       "Sz. d. k.",
                       "Dł. pł.",
                       "Sz. pł."])

    # ------------------------- Calculate different statistical information < #
    df.loc["Minimum [cm]", :] = [i for i in data.iloc[:, 0:4].min()]
    df.loc["Maksimum [cm]", :] = [i for i in data.iloc[:, 0:4].max()]
    df.loc["Rozstęp [cm]", :] = [i for i in df.loc["Maksimum [cm]"]
                                 - df.loc["Minimum [cm]"]]

    df.loc["Pierwszy kwartyl [cm]", :] = [
        quantile(data.iloc[:, i], 0.25) for i in range(4)]
    df.loc["Mediana [cm]", :] = [
        median(data.iloc[:, i]) for i in range(4)]
    df.loc["Trzeci kwartyl [cm]", :] = [
        quantile(data.iloc[:, i], 0.75) for i in range(4)]

    df.loc["Średnia harmoniczna [cm]", :] = stats.hmean(data.iloc[:, 0:4])
    df.loc["Średnia geometryczna [cm]", :] = stats.gmean(data.iloc[:, 0:4])
    df.loc["Średnia arytmetyczna [cm]", :] = [i for i in data.mean()]

    # Operator ** means power() method
    # The shape attribute for numpy arrays returns the dimensions of the array
    # If Y has n rows and m columns, then Y.shape is (n,m). So Y.shape[0] is n
    df.loc["Średnia potęgowa 2 rzędu [cm]", :] = [i for i in (
            ((data.iloc[:, 0:4] ** 2).sum() / data.shape[0]) ** (1 / 2))]
    df.loc["Średnia potęgowa 3 rzędu [cm]", :] = [i for i in (
            ((data.iloc[:, 0:4] ** 3).sum() / data.shape[0]) ** (1 / 3))]

    df.loc["Wariancja [cm^2]", :] = [i for i in data.var()]
    df.loc["Odchylenie standardowe [cm]", :] = [i for i in data.std()]

    # If True, Fisher’s definition is used (normal ==> 0.0)
    # If False, Pearson’s definition is used (normal ==> 3.0)
    df.loc["Kurtoza", :] = stats.kurtosis(data.iloc[:, 0:4], fisher = False)

    pandas.set_option('display.max_rows', 1000)
    pandas.set_option('display.max_columns', 1000)
    pandas.set_option('display.width', 1000)
    print(df.astype(float).round(1))

# /////////////////////////////////////////////////////////////////////////// #
