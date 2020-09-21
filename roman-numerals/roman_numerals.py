# finalix python challenge - roman numerals

import xlsxwriter


def get_roman_numeral(int_input: int):
    if not 1 <= int_input < 4000:
        raise ValueError("Invalid input provided, only numbers between 1 and 3999 are expected.")

    integers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numerals = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    result = []

    for i in range(len(integers)):
        count = int(int_input / integers[i])
        result.append(numerals[i] * count)
        int_input -= integers[i] * count
    return "".join(result)


workbook = xlsxwriter.Workbook("roman_numeral.xlsx")
worksheet = workbook.add_worksheet()

for i in range(1, 4000):
    numeral = get_roman_numeral(i)
    worksheet.write("A" + str(i), i)
    worksheet.write("B" + str(i), numeral)

workbook.close()
