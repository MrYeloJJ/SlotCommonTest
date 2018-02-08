# coding=utf-8

""""

载入场景测试用例

"""

import unittest
from selenium import webdriver
from src.source.common.Common import Common
from time import sleep


class TestLoading(unittest.TestCase, Common):

    def setUp(self):
        self.driver = webdriver.Chrome()
        Common.start(self, self.driver)

    def tearDown(self):
        self.driver.quit()

    # 验证是否进入载入场景
    def test1_loading_showing(self):
        sleep(0.5)
        showing = Common.loading_showing(self.driver)
        try:
            self.assertEqual(showing, True, "没有进入载入场景！")
        except AssertionError as e:
            print(e)
            raise

    # 验证载入场景进度条
    def test2_loading_bar(self):
        sleep(0.5)
        tip = Common.loading_bar(self.driver)
        try:
            self.assertEqual(tip, "100%", "进度条走满后，百分比不是100%")
        except AssertionError as e:
            print(e)
            raise

    # 验证载入场景进度条100%后是否进入主场景
    def test3_enter_main_scence(self):
        Common.loading_bar(self.driver)
        sleep(0.5)
        showing = Common.enter_main_scence(self.driver)
        try:
            self.assertEqual(showing, None, "载入完成后不会进入主场景")
        except AssertionError as e:
            print(e)
            raise


if __name__ == "__main__":
    unittest.main()
