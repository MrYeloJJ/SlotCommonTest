# coding=utf-8

import unittest
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


class RunSingleTest(object):

    def __init__(self):
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

    def run(self, test_class, test_case):
        target_class = self.test_class[test_class]
        suite = unittest.TestSuite()
        # 指定某测试类下的某个用例
        suite.addTest(target_class(test_case))
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    RunSingleTest().run("TestLoadingView", "test_loading_view_showing_switch_screen")
