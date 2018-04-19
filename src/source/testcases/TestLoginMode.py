# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestLoginMode(unittest.TestCase):
    """ 自动游戏设置模块 """

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.get_lobby()
        self.common.login()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    def test_has_money(self):
        """ 横屏登录余额 """
        lobby_chips = "¥" + self.browser.find_element_by_class_name("chips").text
        self.common.switch_page()
        self.common.find_game()
        self.common.switch_game_window()
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        title = self.common.info_bar_view_has_money_title()
        label = self.common.info_bar_view_has_money_label()

        try:
            self.assertEqual(title, "我的余额", "横屏登录下导航栏余额标题错误！")
            self.assertEqual(label, lobby_chips, "横屏登录下导航栏余额数值与大厅的不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
