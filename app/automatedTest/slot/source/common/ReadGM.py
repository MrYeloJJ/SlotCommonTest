# coding=utf-8

import xlrd


class ReadGM(object):

    def __init__(self):
        self.file_path = "./automatedTest/slot/assets/GMAndOdds.xlsx"

    def read_data(self, game_id):

        excel_file = xlrd.open_workbook(self.file_path)
        table = excel_file.sheet_by_name(game_id)
        rows = table.nrows
        data_list = []

        for i in range(1, rows):
            row = {}

            card_id = str(int(table.cell_value(i, 0)))
            card_type = str(table.cell_value(i, 1))
            same = str(int(table.cell_value(i, 2)))
            odds = int(table.cell_value(i, 3))
            gm = "\"" + str(table.cell_value(i, 4)) + "\""
            multiply_with = str(table.cell_value(i, 5))
            multiply = int(table.cell_value(i, 6))

            row["card_id"] = card_id
            row["card_type"] = card_type
            row["same"] = same
            row["odds"] = odds
            row["gm"] = gm
            row["multiply_with"] = multiply_with
            row["multiply"] = multiply
            data_list.append(row)

        return data_list


if __name__ == "__main__":
    ReadGM().read_data('3303')
