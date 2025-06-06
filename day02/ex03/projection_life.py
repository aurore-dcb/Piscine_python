from load_csv import load
import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
import numpy as np
# import pandas as pd


def projection_life():
    """displays the projection of life expectancy in relation to \
        the gross national product of the year 1900 for each country."""
    to_load = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    data_income = load(to_load)
    data_life_exp = load("../life_expectancy_years.csv")
    if data_income is not None and data_life_exp is not None:
        print(data_income)
        print("----------------------")
        print(data_life_exp)


def main():
    projection_life()
    return


if __name__ == '__main__':
    main()
