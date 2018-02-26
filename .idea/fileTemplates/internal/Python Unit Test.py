# coding=utf-8

""""" XXXX测试用例 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestLoadingView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    # 验证是否进入载入场景
    def test1_loading_view_showing(self):
        sleep(1)
        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "没有进入载入场景！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()