# coding=utf-8

""""

读取大厅、游戏名字等数据

"""

import xlrd


class Data(object):

    # 打开excel文档
    @staticmethod
    def open_excel(excel):

        try:
            data = xlrd.open_workbook(excel)
            return data
        except Exception as e:
            print(e)

    # 读取excel信息
    def get_excel_message(self):

        # 初始化excel文档路径，路径为测试用例的相对路径，而不是当前.py文件的相对路径
        excel = "../../assets/data.xlsx"
        data = self.open_excel(excel)
        # 读取第一个工作表
        sheet1 = data.sheet_by_index(0)

        # 大厅地址 A2
        lobby = sheet1.cell(1, 0).value
        # 游戏名字 B2
        game = sheet1.cell(1, 1).value

        return lobby, game
