# coding=utf-8

import unittest
import locale
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
        sleep(3)
        visible = self.common.start_btn_visible()
        touchable = self.common.start_btn_touchable()
        status = self.common.start_btn_status()
        rolling = self.common.slot_machine_rolling()
        banner = self.common.info_bar_view_banner_tips_label()
        try:
            self.assertEqual(visible, True, "横屏进入游戏，旋转按钮默认不会显示！")
            self.assertEqual(touchable, True, "横屏进入游戏，旋转按钮默认不可点击！")
            self.assertEqual(status, "stopped", "横屏进入游戏，旋转按钮默认显示停止按钮！")
            self.assertEqual(rolling, False, "横屏进入游戏，滚轴默认处于滚动状态！")
            self.assertEqual(banner, "滑动转轴或按旋转", "横屏进入游戏，下导航栏默认的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_start_btn_click(self):
        """ 横屏点击旋转按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)

        slot_rolling = self.common.slot_machine_rolling()
        start_btn_status = self.common.start_btn_status()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()
        banner = self.common.info_bar_view_banner_tips_label()
        try:
            self.assertEqual(slot_rolling, True, "横屏点击旋转按钮，滚轴不会滚动！")
            self.assertEqual(start_btn_status, "playing", "横屏点击旋转按钮，旋转按钮不会变成停止按钮！")
            self.assertEqual(setting_btn, False, "横屏点击旋转按钮，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "横屏点击旋转按钮，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "横屏点击旋转按钮，左侧选项菜单可以点击！")
            self.assertEqual(banner, "触摸转轴来提前停止", "横屏点击旋转按钮，下导航栏的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.wait_for_rolling_stop(15)
        game_status = self.common.get_game_current_status()

        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "横屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "横屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "横屏点击旋转按钮，等待滚轴停下后，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "横屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "横屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "横屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "横屏点击旋转按钮，等待滚轴停下后，下导航栏提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "横屏点击旋转按钮，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_stop_btn_click(self):
        """ 横屏旋转过程点击停止按钮 """
        self.common.loading_pass()
        sleep(3)
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

        self.common.wait_for_rolling_stop(15)
        game_status = self.common.get_game_current_status()

        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏旋转过程，点击停止按钮，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "横屏旋转过程，点击停止按钮，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "横屏旋转过程，点击停止按钮，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏旋转过程，点击停止按钮，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "横屏旋转过程，点击停止按钮，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "横屏旋转过程，点击停止按钮，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏旋转过程，点击停止按钮，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "横屏旋转过程，点击停止按钮，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "横屏旋转过程，点击停止按钮，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏旋转过程，点击停止按钮，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "横屏旋转过程，点击停止按钮，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "横屏旋转过程，点击停止按钮，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏旋转过程，点击停止按钮后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "横屏旋转过程，点击停止按钮后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "横屏旋转过程，点击停止按钮后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏旋转过程，点击停止按钮后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "横屏旋转过程，点击停止按钮后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "横屏旋转过程，点击停止按钮后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "横屏旋转过程，点击停止按钮后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "横屏旋转过程，点击停止按钮后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "横屏旋转过程，点击停止按钮后了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractL", "横屏旋转过程，点击停止按钮后了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "横屏旋转过程，点击停止按钮后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "横屏旋转过程，点击停止按钮后中了特殊玩法，下导航栏的提示文字错误！")
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
        sleep(3)
        visible = self.common.start_btn_visible()
        touchable = self.common.start_btn_touchable()
        status = self.common.start_btn_status()
        rolling = self.common.slot_machine_rolling()
        banner = self.common.info_bar_view_banner_tips_label()
        try:
            self.assertEqual(visible, True, "竖屏进入游戏，旋转按钮默认不会显示！")
            self.assertEqual(touchable, True, "竖屏进入游戏，旋转按钮默认不可点击！")
            self.assertEqual(status, "stopped", "竖屏进入游戏，旋转按钮默认显示停止按钮！")
            self.assertEqual(rolling, False, "竖屏进入游戏，滚轴默认处于滚动状态！")
            self.assertEqual(banner, "滑动转轴或按旋转", "横屏进入游戏，下导航栏默认的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_start_btn_click_portrait(self):
        """ 竖屏点击旋转按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
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
        game_status = self.common.get_game_current_status()

        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "竖屏点击旋转按钮，等待滚轴停下后，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "竖屏点击旋转按钮，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "竖屏点击旋转按钮，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "竖屏点击旋转按钮，等待滚轴停下后，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "竖屏点击旋转按钮，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_stop_btn_click_portrait(self):
        """ 竖屏旋转过程点击停止按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
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

        self.common.wait_for_rolling_stop(15)
        game_status = self.common.get_game_current_status()

        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，点击停止按钮，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "竖屏点击旋转按钮，点击停止按钮，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "竖屏点击旋转按钮，点击停止按钮，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，点击停止按钮，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "竖屏点击旋转按钮，点击停止按钮，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "竖屏点击旋转按钮，点击停止按钮，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，点击停止按钮，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "竖屏点击旋转按钮，点击停止按钮，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "竖屏点击旋转按钮，点击停止按钮，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，点击停止按钮，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "竖屏点击旋转按钮，点击停止按钮，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "竖屏点击旋转按钮，点击停止按钮，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "竖屏点击旋转按钮，点击停止按钮后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_start_btn_click_switch_screen(self):
        """ 横竖屏点击旋转按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.start_btn_click()
        sleep(0.5)
        self.common.landscape()
        sleep(0.5)
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
        self.common.portrait()
        sleep(0.5)

        game_status = self.common.get_game_current_status()
        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "点击旋转按钮，切换横竖屏，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "点击旋转按钮，切换横竖屏，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "点击旋转按钮，切换横竖屏，等待滚轴停下后，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "点击旋转按钮，切换横竖屏，等待滚轴停下后，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "点击旋转按钮，切换横竖屏，等待滚轴停下后，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "点击旋转按钮，切换横竖屏，等待滚轴停下后，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "点击旋转按钮，切换横竖屏，等待滚轴停下后，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "点击旋转按钮，切换横竖屏，等待滚轴停下后中了特殊玩法，下导航栏的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_stop_btn_click_switch_screen(self):
        """ 横竖屏旋转过程点击停止按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.start_btn_click()
        self.common.wait_for_rolling(15)
        sleep(0.5)
        self.common.landscape()
        sleep(0.5)
        self.common.start_btn_click()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)
        rolling = self.common.slot_machine_rolling()
        try:
            self.assertEqual(rolling, False, "旋转过程，点击停止按钮，横竖屏切换，滚轴没有立刻停下！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.wait_for_rolling_stop(15)
        game_status = self.common.get_game_current_status()

        coin = self.common.total_win()

        if game_status is None:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "旋转过程，点击停止按钮，横竖屏切换，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "旋转过程，点击停止按钮，横竖屏切换，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "旋转过程，点击停止按钮，横竖屏切换，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "旋转过程，点击停止按钮，横竖屏切换，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "旋转过程，点击停止按钮，横竖屏切换，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "旋转过程，点击停止按钮，横竖屏切换，下导航栏默认的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "旋转过程，点击停止按钮，横竖屏切换，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, True, "旋转过程，点击停止按钮，横竖屏切换，线数线注设置按钮不会恢复显示！")
                    self.assertEqual(auto_game_btn, True, "旋转过程，点击停止按钮，横竖屏切换，自动游戏按钮不会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "旋转过程，点击停止按钮，横竖屏切换，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, True, "旋转过程，点击停止按钮，横竖屏切换，左侧选项菜单不会恢复可点击状态！")
                    self.assertEqual(banner, coin, "旋转过程，点击停止按钮，横竖屏切换，下导航栏提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
        else:
            if coin == 0:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()
                try:
                    self.assertEqual(start_btn_status, "stopped", "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "旋转过程，点击停止按钮，横竖屏切换后中了特殊玩法，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, "滑动转轴或按旋转", "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，下导航栏默认的提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                start_btn_status = self.common.start_btn_status()
                setting_btn = self.common.setting_btn_visible()
                auto_game_btn = self.common.auto_game_btn_visible()
                main_menu_expand = self.common.main_menu_expand()
                main_menu = self.common.main_menu_touchable()
                banner = self.common.info_bar_view_banner_tips_label()

                locale.setlocale(locale.LC_ALL, "")
                coin = "奖金 ¥" + locale.format("%.2f", coin / 100, 1)
                try:
                    self.assertEqual(start_btn_status, "stopped", "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，停止按钮不会恢复成旋转按钮！")
                    self.assertEqual(setting_btn, False, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，线数线注设置按钮会恢复显示！")
                    self.assertEqual(auto_game_btn, False, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，自动游戏按钮会恢复显示！")
                    self.assertEqual(main_menu_expand, "retractP", "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，左侧选项菜单不会折叠！")
                    self.assertEqual(main_menu, False, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，左侧选项菜单会恢复可点击状态！")
                    self.assertEqual(banner, coin, "旋转过程，点击停止按钮后中了特殊玩法，横竖屏切换，下导航栏提示文字错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
