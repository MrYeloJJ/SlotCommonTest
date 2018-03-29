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

    # 验证横屏 自动游戏按钮点击后，弹出自动游戏设置面板
    def test_auto_game_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_visible()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(visible, True, "横屏点击自动游戏按钮，不会显示自动游戏设置面板！")
            self.assertEqual(mask, True, "横屏点击自动游戏按钮，不会显示灰色蒙板！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 点击灰色蒙板，设置面板消失
    def test_click_mask_view_dispear(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        self.common.mask_view_click()
        sleep(1)
        dispear = self.common.auto_game_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "横屏显示自动游戏设置面板时，点击灰色蒙板，设置面板不会消失！")
            self.assertEqual(mask, False, "横屏显示自动游戏设置面板时，点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板显示关闭按钮
    def test_close_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_close_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏自动游戏设置面板，没有显示关闭按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板关闭按钮可点击否
    def test_close_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        touchable = self.common.auto_game_view_close_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏自动游戏设置面板，关闭按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #  验证横屏 点击设置面板关闭按钮，面板消失
    def test_close_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_close_btn_click()
        sleep(1)
        dispear = self.common.auto_game_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "横屏显示自动游戏设置面板时，点击灰色蒙板，设置面板不会消失！")
            self.assertEqual(mask, False, "横屏显示自动游戏设置面板时，点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板显示自动游戏小图标
    def test_auto_game_icon_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_icon_visible()
        try:
            self.assertEqual(visible, True, "横屏自动游戏设置面板，不会显示小图标！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板显示拖动条
    def test_slider_bar_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_slider_bar_visible()
        try:
            self.assertEqual(visible, True, "横屏自动游戏设置面板，没有显示拖动条！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板显示拖动条按钮
    def test_slider_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_slider_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏自动游戏设置面板，不会显示拖动条按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板默认设置的自动次数为最大值，拖动条拉到最右边
    def test_default_auto_game_time(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        current_auto_game_time = self.common.auto_game_view_auto_time_text()
        target_auto_game_time = self.common.auto_game_times[-1]

        current_value = self.common.auto_game_view_slider_value()

        if target_auto_game_time is -1:
            target_auto_game_time = "直到环节"
        else:
            target_auto_game_time = str(target_auto_game_time) + "次旋转"

        try:
            self.assertEqual(current_auto_game_time, target_auto_game_time, "横屏自动游戏设置面板，默认的自动次数不是最大值！")
            self.assertEqual(current_value, 100, "横屏自动游戏设置面板，默认的拖动条按钮没有在最右边！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板改变自动次数，次数显示正确
    def test_change_auto_game_time(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        for i in reversed(range(target_time_len)):
            sleep(1)
            target_time = self.common.auto_game_times[i]
            if target_time is -1:
                target_time = "直到环节"
            else:
                target_time = str(target_time) + "次旋转"

            current_time = self.common.auto_game_view_change_auto_time(i)

            try:
                self.assertEqual(current_time, target_time, "横屏自动游戏设置面板，改变自动次数后与策划的不一致！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                range





























if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()