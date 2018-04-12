# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestSpinBtn(unittest.TestCase):
    """ 旋转按钮模块 """

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

    def test_start_btn(self):
        """ 横屏旋转按钮默认显示 """
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.start_btn_visible()
        touchable = self.common.start_btn_touchable()
        status = self.common.start_btn_status()
        rolling = self.common.slot_machine_rolling()
        try:
            self.assertEqual(visible, True, "横屏进入游戏，旋转按钮默认不会显示！")
            self.assertEqual(touchable, True, "横屏进入游戏，旋转按钮默认不可点击！")
            self.assertEqual(status, "stopped", "横屏进入游戏，旋转按钮默认显示停止按钮！")
            self.assertEqual(rolling, False, "横屏进入游戏，滚轴默认处于滚动状态！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_start_btn_click(self):
        """ 横屏点击旋转按钮 """
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)

        slot_rolling = self.common.slot_machine_rolling()
        start_btn_status = self.common.start_btn_status()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()
        try:
            self.assertEqual(slot_rolling, True, "横屏点击旋转按钮，滚轴不会滚动！")
            self.assertEqual(start_btn_status, "playing", "横屏点击旋转按钮，旋转按钮不会变成停止按钮！")
            self.assertEqual(setting_btn, False, "横屏点击旋转按钮，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "横屏点击旋转按钮，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "横屏点击旋转按钮，左侧选项菜单可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.wait_for_rolling_stop(15)

        start_btn_status = self.common.start_btn_status()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()
        try:
            self.assertEqual(start_btn_status, "stopped", "横屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
            self.assertEqual(setting_btn, True, "横屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
            self.assertEqual(auto_game_btn, True, "横屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
            self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, True, "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_stop_btn_click(self):
        """ 横屏旋转过程点击停止按钮 """
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)
        sleep(0.5)
        self.common.start_btn_click()
        sleep(0.5)
        rolling = self.common.slot_machine_rolling()
        try:
            self.assertEqual(rolling, False, "横屏旋转过程，点击停止按钮，滚轴没有立刻停下！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_spin_btn_portrait(self):
        """ 竖屏旋转按钮默认显示 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.start_btn_visible()
        touchable = self.common.start_btn_touchable()
        status = self.common.start_btn_status()
        rolling = self.common.slot_machine_rolling()
        try:
            self.assertEqual(visible, True, "竖屏进入游戏，旋转按钮默认不会显示！")
            self.assertEqual(touchable, True, "竖屏进入游戏，旋转按钮默认不可点击！")
            self.assertEqual(status, "stopped", "竖屏进入游戏，旋转按钮默认显示停止按钮！")
            self.assertEqual(rolling, False, "竖屏进入游戏，滚轴默认处于滚动状态！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_start_btn_click_portrait(self):
        """ 竖屏点击旋转按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)

        slot_rolling = self.common.slot_machine_rolling()
        start_btn_status = self.common.start_btn_status()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()
        try:
            self.assertEqual(slot_rolling, True, "竖屏点击旋转按钮，滚轴不会滚动！")
            self.assertEqual(start_btn_status, "playing", "竖屏点击旋转按钮，旋转按钮不会变成停止按钮！")
            self.assertEqual(setting_btn, False, "竖屏点击旋转按钮，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "竖屏点击旋转按钮，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "竖屏点击旋转按钮，左侧选项菜单可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.wait_for_rolling_stop(15)

        start_btn_status = self.common.start_btn_status()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()
        try:
            self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
            self.assertEqual(setting_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
            self.assertEqual(auto_game_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
            self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, True, "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_stop_btn_click_portrait(self):
        """ 竖屏旋转过程点击停止按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)
        sleep(0.5)
        self.common.start_btn_click()
        sleep(0.5)
        rolling = self.common.slot_machine_rolling()
        try:
            self.assertEqual(rolling, False, "竖屏旋转过程，点击停止按钮，滚轴没有立刻停下！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
