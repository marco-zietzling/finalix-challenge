# finalix python challenge - test data generator part 2

import pandas as pd
from pandas import DataFrame


def read_test_data():
    return pd.read_excel("test_data1.xlsx", header=0)


def manipulate_ids(data: DataFrame):
    for i in range(len(data)):
        data.at[i, "ID"] += 100000


def manipulate_lastnames(data: DataFrame):
    data.loc[data["Last name"] == "Müller", "Last name"] = "Müüüller"
    data.loc[data["Last name"] == "Schmid", "Last name"] = "Schmiiid"
    data.loc[data["Last name"] == "Bucher", "Last name"] = "Buuucher"


def manipulate_firstnames(data: DataFrame):
    return ""


def manipulate_birthdates(data: DataFrame):
    return ""


def manipulate_regions(data: DataFrame):
    return ""


test_data = read_test_data()
print(test_data.head())
print(test_data.tail())
manipulate_ids(test_data)
manipulate_lastnames(test_data)
print(test_data.head())
print(test_data.tail())
