from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    aff_life('France')


def aff_life(country: str):
    """Display a graph with information about a country."""
    data = load("../life_expectancy_years.csv")
    if data is not None:
        colonnes = data.columns.to_numpy().astype(np.int64)
        country_data = data.loc[country].to_numpy()
        plt.title(f"{country} Life expectancy Projections")
        plt.plot(colonnes, country_data)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.show()
    else:
        print("No data available.")
    return


if __name__ == "__main__":
    main()
