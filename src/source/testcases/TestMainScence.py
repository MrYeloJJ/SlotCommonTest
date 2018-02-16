# coding=utf-8

""""" 载入场景测试用例 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.source.common.DirAndFiles import DirAndFiles


class TestLoading(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    # 测试是否正常显示主场景
    def test1_main_scence_visible(self):
        sleep(2)
        self.common.loading_bar()

        sleep(2)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()

        try:
            self.assertEqual(main_view, True, "正常显示主视图")
            self.assertEqual(common_view, True, "正常显示公共视图")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()