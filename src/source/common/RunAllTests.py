# coding=utf-8

""""

运行source目录下所有测试用例，并生成HTML测试报告文件

"""

import unittest
from src.lib import HTMLTestReportCN
import datetime

if __name__ == "__main__":
    test_suite = unittest.TestLoader().discover("../../source")

    now = str(datetime.datetime.now().strftime("%Y-%m-%d(%H-%M-%S)"))
    file_path = "..\\..\\assets\\report\\SlotCommonTest_report_" + now + ".html"

    fp = open(file_path, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="SlotCommonTest Report", description="Slot游戏公共模块测试报告", tester="Gelomen")
    runner.run(test_suite)
    fp.close()

    print("\033[36;0m--------------------- 测试结束 ---------------------\033[0m")
