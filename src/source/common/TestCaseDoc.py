# coding=utf-8

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


class TestCaseDoc(object):

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
        self.all_doc = {}

    def get_doc(self):
        classes_doc = {}
        for i in self.test_class.keys():
            class_doc = self.test_class[i].__doc__
            classes_doc[i] = class_doc

            attr_list = dir(self.test_class[i])

            funcs_doc = {}
            for y in attr_list:
                if y.startswith("test"):


if __name__ == "__main__":
    TestCaseDoc().get_doc()

