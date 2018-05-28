# coding=utf-8

""""" 运行source目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
from app.automaticTest.slot.lib import HTMLTestReportCN
from app.main.GameAttr import GameAttr
# from automaticTest.source.common.Config import Config


class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "./automaticTest/slot/source/testcases/"
        # self.tester = Config().get_message()["tester"]
        self.tester = GameAttr.get_attr("tester")

        # 将游戏名字放入报告里
        # self.game = Config().get_message()["game_name"]
        self.game = GameAttr.get_attr("game_name")
        self.title = "【" + self.game + "】公共模块测试报告"

        self.description = "Slot游戏公共模块测试报告"

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
