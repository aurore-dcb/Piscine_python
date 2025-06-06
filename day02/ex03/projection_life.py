from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def projection_life(data_dom_prod: pd.DataFrame, data_life_exp: pd.DataFrame):
    """displays the projection of life expectancy in relation to \
        the gross national product of the year 1900 for each country."""
    clean_dom_exp = data_dom_prod.loc[:, '1900']
    clean_life_exp = data_life_exp.loc[:, '1900']
    plt.xscale('log')
    plt.gca().xaxis.set_major_formatter(ticker.EngFormatter(unit=''))
    plt.xticks([300, 1000, 10000])
    plt.xlim(left=300, right=10000)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.scatter(clean_dom_exp, clean_life_exp)
    plt.show()


def main():
    to_load = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    data_dom_prod = load(to_load)
    data_life_exp = load("../life_expectancy_years.csv")
    if data_dom_prod is not None and data_life_exp is not None:
        projection_life(data_dom_prod, data_life_exp)
    else:
        print("No data available.")
    return


if __name__ == '__main__':
    main()
