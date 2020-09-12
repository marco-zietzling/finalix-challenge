# finalix python challenge - test data generator part 1

import xlsxwriter


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
                data_item = {
                    "id": id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "region": region,
                    "birthdate": generate_birthdate(),
                    "phone": generate_phone()
                }

                id += 1
                result.append(data_item)

    return result


def generate_birthdate():
    return ""


def generate_phone():
    return ""


def write_test_data(data: list):
    workbook = xlsxwriter.Workbook("test_data1.xlsx")
    worksheet = workbook.add_worksheet()

    for i in data:
        worksheet.write_row(i)

    workbook.close()


test_data = read_test_data()
write_test_data(test_data)
