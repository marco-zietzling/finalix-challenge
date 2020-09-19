# finalix python challenge - aggregation of test data and output to Excel

import pandas as pd
from pandas import DataFrame
import numpy as np


def read_test_data():
    return pd.read_csv("../test-data-generator/test_data2.csv", sep="|", encoding="utf8", quotechar='"', quoting=2)


def create_report(test_data: DataFrame):
    return pd.pivot_table(test_data, index="Region", columns="Last name", values="ID", aggfunc=np.count_nonzero)


def save_report(test_data: DataFrame):
    test_data.to_excel("test_data_report.xlsx")


data = read_test_data()
# print(data.head())
pivot = create_report(data)
# print(pivot)
save_report(pivot)
