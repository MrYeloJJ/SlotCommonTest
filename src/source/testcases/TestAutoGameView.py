# coding=utf-8

""""" 自动游戏验证 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestAutoGameView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    # 验证横屏 显示自动游戏按钮
    def test_auto_game_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.auto_game_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏不会显示自动游戏按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 自动游戏按钮可点击否
    def test_auto_game_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.auto_game_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏自动游戏按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise





























if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
