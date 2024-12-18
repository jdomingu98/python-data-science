import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def to_int(number: str) -> float:
    """
    Converts a string representing a number with suffixes
    'M' (millions) or 'k' (thousands) into a float.

    Returns the number as a float if there is no suffix.
    """
    if number.endswith("M"):
        return float(number[:-1]) * 1_000_000
    if number.endswith("k"):
        return float(number[:-1]) * 1_000
    return float(number)


def main():
    """
    Plots a comparison of population projections for Spain and France
    using data from a CSV file.
    """
    ds = load("population_total.csv")

    parser = np.vectorize(to_int)

    years = np.array(ds.columns[1:].astype(int))
    spain_row = parser(ds[ds["country"] == "Spain"].values[0][1:])
    france_row = parser(ds[ds["country"] == "France"].values[0][1:])

    plt.figure(figsize=(10, 6))
    canvas = plt.gcf().canvas
    canvas.manager.set_window_title('Population Spain vs France')
    plt.title('Population Projections')

    plt.plot(years, spain_row, label="Spain", color="blue")
    plt.plot(years, france_row, label="France", color="green")

    plt.xlabel('Year')
    plt.xticks(range(1800, 2041, 40))
    plt.xlim(1790, 2050)

    plt.ylabel('Population')

    y_ticks = range(20_000_000, 80_000_000, 20_000_000)
    plt.yticks(
        y_ticks,
        ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks]
    )
    plt.ylim(0, 80_000_000, 20_000_000)
    plt.legend(loc='lower right')

    plt.show()


if __name__ == "__main__":
    main()
