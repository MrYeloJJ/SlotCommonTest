# coding=utf-8

import unittest
import json
from app.automatedTest.slot.lib import HTMLTestReportCN
from app.main.GameAttr import GameAttr
from app.automatedTest.slot.source.testcases.TestAutoGameView import TestAutoGameView
from app.automatedTest.slot.source.testcases.TestGameAttr import TestGameAttr
from app.automatedTest.slot.source.testcases.TestInfoBar import TestInfoBar
from app.automatedTest.slot.source.testcases.TestLoadingView import TestLoadingView
from app.automatedTest.slot.source.testcases.TestLoginMode import TestLoginMode
from app.automatedTest.slot.source.testcases.TestMainAndComView import TestMainAndComView
from app.automatedTest.slot.source.testcases.TestMainMenu import TestMainMenu
from app.automatedTest.slot.source.testcases.TestSettingView import TestSettingView
from app.automatedTest.slot.source.testcases.TestSpinBtn import TestSpinBtn
from app.automatedTest.slot.source.testcases.TestTurboView import TestTurboView


class CustomRun(object):

    def __init__(self):
        self.tester = GameAttr.get_attr("tester")

        # 将游戏id放入报告里
        self.game_id = str(GameAttr.get_attr("game_id"))
        self.title = "[" + self.game_id + "]CommonTestReport"

        # 将游戏名字放入报告描述
        self.game_name = GameAttr.get_attr("game_name")
        self.description = "Slot游戏【" + self.game_name + "】公共模块测试报告"
        self.test_class = {"TestAutoGameView": TestAutoGameView,
                           "TestGameAttr": TestGameAttr,
                           "TestInfoBar": TestInfoBar,
                           "TestLoadingView": TestLoadingView,
                           "TestLoginMode": TestLoginMode,
                           "TestMainAndComView": TestMainAndComView,
                           "TestMainMenu": TestMainMenu,
                           "TestSettingView": TestSettingView,
                           "TestSpinBtn": TestSpinBtn,
                           "TestTurboView": TestTurboView
                           }

    def run(self, test_list):
        suite = unittest.TestSuite()
        # 循环读取需要测试的用例，并添加到TestSuite里
        for i in test_list:
            test_class = self.test_class[i["key"]]
            test_case = i["value"]
            # 指定某测试类下的某个用例
            suite.addTest(test_class(test_case))

        # 启动测试时创建文件夹并获取最新文件夹的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=self.tester)
        runner.run(suite)
        fp.close()


if __name__ == "__main__":
    pass
