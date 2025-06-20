from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def convert_to_number(value) -> int:
    """Convert a string representation of a number with suffixes to an integer."""
    if isinstance(value, str):
        value = value.strip().lower()
        if value.endswith('b'):
            return int(float(value[:-1]) * 1_000_000_000)
        elif value.endswith('m'):
            return int(float(value[:-1]) * 1_000_000)
        elif value.endswith('k'):
            return int(float(value[:-1]) * 1_000)
        else:
            try:
                return int(float(value))
            except ValueError:
                return 0
    return value


def format_func(value, tick_number):
    """Format the y-axis ticks to display in millions."""
    return f'{int(value / 1000000)}M'


def aff_pop(country1: str, country2: str) -> None:
    """Display a graph that compare two country population"""
    data = load("../population_total.csv")
    if data is not None:
        data_clean = data.loc[:, '1801':'2050'].map(convert_to_number)
        columns = data_clean.columns.to_numpy().astype(np.int64)
        country1_data = data_clean.loc[country1].to_numpy()
        country2_data = data_clean.loc[country2].to_numpy()
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
        plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=8))
        plt.plot(columns, country1_data, label=country1)
        plt.plot(columns, country2_data, label=country2, color='Green')
        plt.legend(loc='lower right')
        plt.show()
    else:
        print("No data available.")
    return


def main():
    aff_pop("Belgium", "France")
    return


if __name__ == "__main__":
    main()
