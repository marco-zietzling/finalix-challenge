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
    data.loc[data["Birthdate"] == "11.02.1982", "Birthdate"] = "12.02.1982"


def manipulate_regions(data: DataFrame):
    data.loc[data["Region"] == "Zürich", "Region"] = "ZH"
    data.loc[data["Region"] == "Bern", "Region"] = "BE"
    data.loc[data["Region"] == "Luzern", "Region"] = "LU"
    data.loc[data["Region"] == "Uri", "Region"] = "UR"
    data.loc[data["Region"] == "Schwyz", "Region"] = "SZ"
    data.loc[data["Region"] == "Obwalden", "Region"] = "OW"
    data.loc[data["Region"] == "Nidwalden", "Region"] = "NW"
    data.loc[data["Region"] == "Glarus", "Region"] = "GL"
    data.loc[data["Region"] == "Zug", "Region"] = "ZG"
    data.loc[data["Region"] == "Freiburg", "Region"] = "FR"
    data.loc[data["Region"] == "Solothurn", "Region"] = "SO"
    data.loc[data["Region"] == "Basel - Stadt", "Region"] = "BS"
    data.loc[data["Region"] == "Basel - Landschaft", "Region"] = "BL"
    data.loc[data["Region"] == "Schaffhausen", "Region"] = "SH"
    data.loc[data["Region"] == "Appenzell Ausserrhoden", "Region"] = "AR"
    data.loc[data["Region"] == "Appenzell Innerrhoden", "Region"] = "AI"
    data.loc[data["Region"] == "St.Gallen", "Region"] = "SG"
    data.loc[data["Region"] == "Graubünden", "Region"] = "GR"
    data.loc[data["Region"] == "Aargau", "Region"] = "AG"
    data.loc[data["Region"] == "Thurgau", "Region"] = "TG"
    data.loc[data["Region"] == "Tessin", "Region"] = "TI"
    data.loc[data["Region"] == "Waadt", "Region"] = "VD"
    data.loc[data["Region"] == "Wallis", "Region"] = "VS"
    data.loc[data["Region"] == "Neuenburg", "Region"] = "NE"
    data.loc[data["Region"] == "Genf", "Region"] = "GE"
    data.loc[data["Region"] == "Jura", "Region"] = "JU"


def generate_email_address(data: DataFrame):
    return ""


def export_to_csv(data: DataFrame):
    data.to_csv("test_data2.csv", sep="|", encoding="utf8", quotechar='"', quoting=2, index=False,
                columns=["ID", "Last name", "First name", "Birthdate", "Region", "Phone"])
    # columns = ["ID", "Last name", "First name", "Birthdate", "Region", "Email", "Phone"])


test_data = read_test_data()
print(test_data.head())
print(test_data.tail())

print(test_data.dtypes)

manipulate_ids(test_data)
manipulate_lastnames(test_data)
manipulate_firstnames(test_data)
manipulate_birthdates(test_data)
manipulate_regions(test_data)
generate_email_address(test_data)

print(test_data.head())
print(test_data.tail())

export_to_csv(test_data)
