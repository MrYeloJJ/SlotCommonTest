# coding=utf-8

import json
from app.automaticTest.slot.source.testcases.TestAutoGameView import TestAutoGameView
from app.automaticTest.slot.source.testcases.TestGameAttr import TestGameAttr
from app.automaticTest.slot.source.testcases.TestInfoBar import TestInfoBar
from app.automaticTest.slot.source.testcases.TestLoadingView import TestLoadingView
from app.automaticTest.slot.source.testcases.TestLoginMode import TestLoginMode
from app.automaticTest.slot.source.testcases.TestMainAndComView import TestMainAndComView
from app.automaticTest.slot.source.testcases.TestMainMenu import TestMainMenu
from app.automaticTest.slot.source.testcases.TestSettingView import TestSettingView
from app.automaticTest.slot.source.testcases.TestSpinBtn import TestSpinBtn
from app.automaticTest.slot.source.testcases.TestTurboView import TestTurboView


class SlotTestDoc(object):

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
        self.all_doc = []

    def get_doc(self):

        for i in self.test_class.keys():
            classes_doc = {}
            funcs_list = []
            obj = {}

            class_doc = self.test_class[i].__doc__
            classes_doc["key"] = i
            classes_doc["value"] = class_doc

            attr_list = dir(self.test_class[i])

            for y in attr_list:
                funcs_doc = {}
                if y.startswith("test"):
                    func = getattr(self.test_class[i], y)
                    funcs_doc["key"] = y
                    funcs_doc["value"] = func.__doc__
                    funcs_list.append(funcs_doc)

            obj["testClass"] = classes_doc
            obj["testCases"] = funcs_list
            self.all_doc.append(obj)

        doc_json = json.dumps(self.all_doc, ensure_ascii=False)
        # print(doc_json)
        return doc_json


if __name__ == "__main__":
    SlotTestDoc().get_doc()
