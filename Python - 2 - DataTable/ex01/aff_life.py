import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def main():
    """
    Plots the life expectancy projections for Spain using data from a CSV file.
    """
    ds = load("life_expectancy_years.csv")
    years = np.array(ds.columns[1:])
    row = ds[ds["country"] == "Spain"]
    life_expectancy = np.array(row.values[0][1:])

    plt.plot(years, life_expectancy)
    plt.title('Spain Life Expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 100, 10))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
