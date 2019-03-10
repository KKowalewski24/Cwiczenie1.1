# /////////////////////////////////////////////////////////////////// Imports #
import matplotlib
import pandas
from matplotlib import pyplot

from functions import print_iris_statistics


# ////////////////////////////////////////////////////////////////////// Main #
def main():
    # ----------------------------------------------------------- Load data < #
    # Load data from file
    iris_data = pandas.read_csv("iris.data", header = None)

    # Divide data into proper types
    iris_setosa = iris_data.loc[iris_data.iloc[:, 4] == "Iris-setosa"]
    iris_versicolor = iris_data.loc[iris_data.iloc[:, 4] == "Iris-versicolor"]
    iris_virginica = iris_data.loc[iris_data.iloc[:, 4] == "Iris-virginica"]

    # --------------------------------------------------------- Plot graphs < #
    # Set main parameters
    matplotlib.rcParams["toolbar"] = "None"
    pyplot.get_current_fig_manager().full_screen_toggle()
    pyplot.suptitle("Ćwiczenie 1.1 - Wykresy")

    # Prepare the first graph (sepal length x sepal width)
    pyplot.subplot(1, 2, 1)
    pyplot.plot(iris_setosa.iloc[:, 0],
                iris_setosa.iloc[:, 1],
                "r+",
                label = "Iris setosa")
    pyplot.plot(iris_versicolor.iloc[:, 0],
                iris_versicolor.iloc[:, 1],
                "g+",
                label = "Iris versicolor")
    pyplot.plot(iris_virginica.iloc[:, 0],
                iris_virginica.iloc[:, 1],
                "b+",
                label = "Iris virginica")
    pyplot.title("Zależność szerokości od długości działki kielicha")
    pyplot.xlabel("Długość działki kielicha [cm]")
    pyplot.ylabel("Szerokość działki kielicha [cm]")
    pyplot.legend()

    # Prepare the second graph (petal length x petal width)
    pyplot.subplot(1, 2, 2)
    pyplot.plot(iris_setosa.iloc[:, 2],
                iris_setosa.iloc[:, 3],
                "r+",
                label = "Iris setosa")
    pyplot.plot(iris_versicolor.iloc[:, 2],
                iris_versicolor.iloc[:, 3],
                "g+",
                label = "Iris versicolor")
    pyplot.plot(iris_virginica.iloc[:, 2],
                iris_virginica.iloc[:, 3],
                "b+",
                label = "Iris virginica")
    pyplot.title("Zależność szerokości od długości płatka")
    pyplot.xlabel("Długość płatka [cm]")
    pyplot.ylabel("Szerokość płatka [cm]")
    pyplot.legend()

    # Plot final graph
    pyplot.show()

    # ---------------------------------------------------- Print statistics < #
    for i in [("Podsumowanie (ogólne)", iris_data),
              ("Podsumowanie (Iris setosa)", iris_setosa),
              ("Podsumowanie (Iris versicolor)", iris_versicolor),
              ("Podsumowanie (Iris virginica)", iris_virginica)]:
        print(i[0], '/' * (69 - len(i[0]) - 1))
        print_iris_statistics(i[1])
        print('/' * 69, '\n')


# /////////////////////////////////////////////////////////// Execute program #
if __name__ == "__main__":
    main()


# /////////////////////////////////////////////////////////////////////////// #
