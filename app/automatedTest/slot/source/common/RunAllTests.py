# coding=utf-8

""""" 运行source目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
from app.automatedTest.slot.lib import HTMLTestReportCN
from app.main.GameAttr import GameAttr


class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "./automatedTest/slot/source/testcases/"
        self.tester = GameAttr.get_attr("tester")

        # 将游戏id放入报告里
        self.game_id = str(GameAttr.get_attr("game_id"))
        self.title = "[" + self.game_id + "]CommonTestReport"

        # 将游戏名字放入报告描述
        self.game_name = GameAttr.get_attr("game_name")
        self.description = "Slot游戏【" + self.game_name + "】公共模块测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取最新文件夹的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=self.tester)
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()
