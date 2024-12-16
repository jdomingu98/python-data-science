import matplotlib.pyplot as plt
from load_csv import load


def main():
    ds = load("life_expectancy_years.csv")
    years = list(map(int, ds.columns[1:]))
    row = ds[ds["country"] == "France"]
    plt.plot(years, row.iloc[0, 1:].values)
    plt.xticks(range(min(years), max(years)+1, 40))
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
