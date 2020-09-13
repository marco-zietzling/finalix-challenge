# finalix python challenge - test data generator part 1
# Marco Zietzling, 2020

import xlsxwriter
import datetime
import random

phone_numbers = set()


def read_test_data():
    with open("vornamen.txt", "r") as file:
        first_names = [i.strip() for i in file.readlines()]

    with open("nachnamen.txt", "r") as file:
        last_names = [i.strip() for i in file.readlines()]

    with open("kantone.txt", "r") as file:
        regions = [i.strip() for i in file.readlines()]

    id = 11001
    result = list()

    for first_name in first_names:
        for last_name in last_names:
            for region in regions:
                data_item = [
                    id,
                    first_name,
                    last_name,
                    region,
                    generate_random_birthdate(),
                    generate_random_phonenumber()
                ]

                id += 1
                result.append(data_item)

    return result


def generate_random_birthdate():
    start_date = datetime.date(day=1, month=1, year=1920)
    end_date = datetime.date(day=31, month=12, year=2000)
    return (start_date + random.random() * (end_date - start_date)).strftime("%d.%m.%Y")


def generate_random_phonenumber():
    i = random.randint(10000000000, 99999999999)

    while i in phone_numbers:
        print("duplicate phone number hit, generating next one")
        i = random.randint(10000000000, 99999999999)

    phone_numbers.add(i)

    # print(f"{str(i)} -> {str(i)[0:2]}.{str(i)[2:4]}.{str(i)[4:7]}.{str(i)[7:11]}")
    return f"{str(i)[0:2]}.{str(i)[2:4]}.{str(i)[4:7]}.{str(i)[7:11]}"


def write_test_data(data: list):
    workbook = xlsxwriter.Workbook("test_data1.xlsx")
    worksheet = workbook.add_worksheet()

    # add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # write the header
    worksheet.write(0, 0, "ID", bold)
    worksheet.write(0, 1, "First name", bold)
    worksheet.write(0, 2, "Last name", bold)
    worksheet.write(0, 3, "Region", bold)
    worksheet.write(0, 4, "Birthdate", bold)
    worksheet.write(0, 5, "Phone", bold)

    # write data
    row = 1
    for [id, first_name, last_name, region, birthdate, phone] in data:
        worksheet.write(row, 0, id)
        worksheet.write(row, 1, first_name)
        worksheet.write(row, 2, last_name)
        worksheet.write(row, 3, region)
        worksheet.write(row, 4, birthdate)
        worksheet.write(row, 5, phone)

        row += 1

    workbook.close()


test_data = read_test_data()
write_test_data(test_data)
