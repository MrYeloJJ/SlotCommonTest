# coding=utf-8

import unittest
import json
from src.lib import HTMLTestReportCN
from src.source.common.Config import Config
from src.source.testcases.TestAutoGameView import TestAutoGameView
from src.source.testcases.TestGameAttr import TestGameAttr
from src.source.testcases.TestInfoBar import TestInfoBar
from src.source.testcases.TestLoadingView import TestLoadingView
from src.source.testcases.TestLoginMode import TestLoginMode
from src.source.testcases.TestMainAndComView import TestMainAndComView
from src.source.testcases.TestMainMenu import TestMainMenu
from src.source.testcases.TestSettingView import TestSettingView
from src.source.testcases.TestSpinBtn import TestSpinBtn
from src.source.testcases.TestTurboView import TestTurboView


class CustomRun(object):

    def __init__(self):
        self.tester = Config().get_message()["tester"]
        # 将游戏名字放入报告里
        self.game = Config().get_message()["game_name"]
        self.title = "【" + self.game + "】公共模块测试报告"
        self.description = "Slot游戏公共模块测试报告"
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

    def run(self, data_json):
        # 将json转为字典
        test_cases_data = json.loads(data_json)
        suite = unittest.TestSuite()
        # 循环读取需要测试的用例，并添加到TestSuite里
        for i in test_cases_data.keys():
            test_class = self.test_class[i]
            test_case = test_cases_data[i]
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
    data = {"TestLoadingView": "test_loading_view_showing_switch_screen",
            "TestGameAttr": "test_game_name"}
    # 将字典转为json
    my_json = json.dumps(data)
    CustomRun().run(my_json)