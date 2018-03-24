# coding=utf-8

""""" 左侧选项菜单验证 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestMainMenu(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()

    def tearDown(self):
        self.browser.quit()

    # 验证横屏点击奖金表按钮后，显示奖金表场景
    def test_info_btn_click_info_view_showing(self):
        self.common.info_btn_click()
        showing = self.common.info_view_showing()
        try:
            self.assertEqual(showing, True, "横屏点击奖金表按钮后，不会显示奖金表场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
