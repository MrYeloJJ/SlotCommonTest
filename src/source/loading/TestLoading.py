# coding=utf-8

""""

载入场景测试用例

"""

import unittest
from selenium import webdriver
from src.source.common.Common import Common
from time import sleep


class TestLoading(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.driver)
        self.common.start()

    def tearDown(self):
        self.driver.quit()

    # 验证是否进入载入场景
    def test1_loading_view_showing(self):
        sleep(1)
        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "没有进入载入场景！")
        except AssertionError:
            raise

    # 验证载入场景进度条
    def test2_loading_bar(self):
        sleep(1)
        tip = self.common.loading_bar()
        try:
            self.assertEqual(tip, "100%", "进度条走满后，百分比不是100%！")
        except AssertionError:
            raise

    # 验证载入场景进度条100%后是否消失
    def test3_loading_view_dispear(self):
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "载入完成后载入场景不会消失！")
        except AssertionError:
            raise


if __name__ == "__main__":
    unittest.main()
