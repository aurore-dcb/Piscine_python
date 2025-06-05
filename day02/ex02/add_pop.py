from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def convert_to_number(value) -> int :
    if isinstance(value, str):
        value = value.strip().lower()
        if value.endswith('m'):
            return int(float(value[:-1]) * 1_000_000)
        elif value.endswith('k'):
            return int(float(value[:-1]) * 1_000)
        else:
            try:
                return int(float(value))
            except ValueError:
                return np.nan
    return value


def aff_pop(country1: str, country2:str):
    """Display a graph that compare two country population"""
    data = load("../population_total.csv")
    if data is not None:
        data_clean = data.loc[:, '1801':'2050']
        data_clean = data_clean.map(convert_to_number)
        print(data_clean)
        columns = data_clean.columns.to_numpy().astype(np.int64)
        country1_data = data_clean.loc[country1].to_numpy()
        country2_data = data_clean.loc[country2].to_numpy()
        # Bon format de l'axe Population
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.plot(columns, country1_data)
        plt.plot(columns, country2_data)
        plt.legend([country1, country2])
        plt.show()

    else:
        print("No data available.")
    return

def main():
    aff_pop("France", "Belgium")
    return


if __name__ == "__main__":
    main()