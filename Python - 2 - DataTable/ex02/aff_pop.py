import matplotlib.pyplot as plt
from load_csv import load


def convert_to_numeric(value):
    """Convierte valores con sufijos 'k' (mil) o 'M' (millones) a números."""
    if isinstance(value, str):
        if 'k' in value:
            return float(value.replace('k', '')) * 1_000
        elif 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
    return value


def main():
    ds = load("population_total.csv")
    years = list(map(int, ds.columns[1:]))
    years = [year for year in years if year >= 1800 and year <= 2050]

    # Convertir las columnas con valores de población de string a numérico
    for column in ds.columns[1:]:  # Asumimos que la primera columna es el país
        ds[column] = ds[column].apply(convert_to_numeric)

    france_data = ds[ds["country"] == "France"].iloc[0, 1:].values
    spain_data = ds[ds["country"] == "Spain"].iloc[0, 1:].values
    france_values = france_data[
                        years.index(min(years)):years.index(max(years))+1
                    ]
    spain_values = spain_data[
                        years.index(min(years)):years.index(max(years))+1
                    ]

    plt.plot(years, france_values, label="France", color="green")
    plt.plot(years, spain_values, label="Spain", color="blue")
    plt.xticks(range(min(years), max(years)+1, 40))
    y_max = max(max(france_values), max(spain_values))
    yticks_range = range(0, int(y_max) + 20_000_000, 20_000_000)
    plt.yticks(yticks_range, [f"{tick//1_000_000}M" for tick if yticks_range])
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
