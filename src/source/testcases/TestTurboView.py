# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestTurboView(unittest.TestCase):
    """ 快速模式窗口模块 """

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

    def test_turbo_view(self):
        """ 横屏快速模式窗口显示 """
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        turbo_view = self.common.turbo_mode_view_showing()
        mask_view = self.common.mask_view_showing()
        close_btn = self.common.turbo_mode_view_close_btn_visible()
        close_btn_touchable = self.common.turbo_mode_view_close_btn_touchable()
        title_long = self.common.turbo_mode_view_title_long()
        title_short = self.common.turbo_mode_view_title_short()
        enable_btn = self.common.turbo_mode_view_enable_btn_visible()
        enable_btn_text = self.common.turbo_mode_view_enable_btn_text()
        enable_btn_touchable = self.common.turbo_mode_view_enable_btn_touchable()

        try:
            self.assertEqual(turbo_view, True, "横屏快速旋转停止两次，不会弹出快速模式窗口！")
            self.assertEqual(mask_view, True, "横屏弹出快速模式窗口，不会显示灰色蒙板！")
            self.assertEqual(close_btn, True, "横屏弹出快速模式窗口，不会显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "横屏弹出快速模式窗口，关闭按钮不可点击！")
            self.assertEqual(title_long, "看来您喜欢更快速的玩游戏。\n你想启用快速模式吗?", "横屏弹出快速模式窗口，长的提示文字错误！")
            self.assertEqual(title_short, "您可以随时在菜单中将其禁用", "横屏弹出快速模式窗口，短的提示文字错误！")
            self.assertEqual(enable_btn, True, "横屏弹出快速模式窗口，不会显示启动快速按钮！")
            self.assertEqual(enable_btn_text, "启用快速模式", "横屏弹出快速模式窗口，启动快速模式按钮上的文字错误！")
            self.assertEqual(enable_btn_touchable, True, "横屏弹出快速模式窗口，启动快速模式按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_close_btn_click(self):
        """ 横屏点击关闭按钮 """
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_close_btn_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "横屏点击快速模式窗口关闭按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "横屏点击快速模式窗口关闭按钮，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "横屏点击快速模式窗口关闭按钮，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "横屏点击快速模式窗口关闭按钮，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_mask_click(self):
        """ 横屏点击灰色蒙板 """
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.mask_view_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "横屏点击灰色蒙板，快速模式窗口不会消失！")
            self.assertEqual(mask_view, False, "横屏点击灰色蒙板，蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "横屏点击灰色蒙板，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "横屏点击灰色蒙板，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_dispear(self):
        """ 横屏窗口自动消失 """
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(7)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "横屏等待6秒，快速模式窗口不会消失！")
            self.assertEqual(mask_view, False, "横屏等待6秒，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "横屏快速模式窗口自动消失后，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "横屏快速模式窗口自动消失后，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_enable_btn_click(self):
        """ 横屏点击启用快速模式按钮 """
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_enable_btn_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "横屏点击快速模式窗口启用按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "横屏点击快速模式窗口启用按钮，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "2x", "横屏点击快速模式窗口启用按钮，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "横屏点击快速模式窗口启用按钮，滚轴滚动方式不是快速速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_enable_btn_click_refresh(self):
        """ 横屏点击启用快速模式按钮后刷新页面 """
        self.common.loading_pass()
        sleep(1)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_enable_btn_click()
        sleep(1)
        self.browser.refresh()
        self.common.loading_pass()
        sleep(1)

        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "2x", "横屏点击启用快速模式按钮后刷新，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "横屏点击启用快速模式按钮后刷新，滚轴滚动方式不是快速速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_turbo_view_portrait(self):
        """ 竖屏快速模式窗口显示 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        turbo_view = self.common.turbo_mode_view_showing()
        mask_view = self.common.mask_view_showing()
        close_btn = self.common.turbo_mode_view_close_btn_visible()
        close_btn_touchable = self.common.turbo_mode_view_close_btn_touchable()
        title_long = self.common.turbo_mode_view_title_long()
        title_short = self.common.turbo_mode_view_title_short()
        enable_btn = self.common.turbo_mode_view_enable_btn_visible()
        enable_btn_text = self.common.turbo_mode_view_enable_btn_text()
        enable_btn_touchable = self.common.turbo_mode_view_enable_btn_touchable()

        try:
            self.assertEqual(turbo_view, True, "竖屏快速旋转停止两次，不会弹出快速模式窗口！")
            self.assertEqual(mask_view, True, "竖屏弹出快速模式窗口，不会显示灰色蒙板！")
            self.assertEqual(close_btn, True, "竖屏弹出快速模式窗口，不会显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "竖屏弹出快速模式窗口，关闭按钮不可点击！")
            self.assertEqual(title_long, "看来您喜欢更快速的玩游戏。\n你想启用快速模式吗?", "竖屏弹出快速模式窗口，长的提示文字错误！")
            self.assertEqual(title_short, "您可以随时在菜单中将其禁用", "竖屏弹出快速模式窗口，短的提示文字错误！")
            self.assertEqual(enable_btn, True, "竖屏弹出快速模式窗口，不会显示启动快速按钮！")
            self.assertEqual(enable_btn_text, "启用快速模式", "竖屏弹出快速模式窗口，启动快速模式按钮上的文字错误！")
            self.assertEqual(enable_btn_touchable, True, "竖屏弹出快速模式窗口，启动快速模式按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_close_btn_click_portrait(self):
        """ 竖屏点击关闭按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_close_btn_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏点击快速模式窗口关闭按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏点击快速模式窗口关闭按钮，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "竖屏点击快速模式窗口关闭按钮，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "竖屏点击快速模式窗口关闭按钮，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_mask_click_portrait(self):
        """ 竖屏点击灰色蒙板 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.mask_view_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏点击灰色蒙板，快速模式窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏点击灰色蒙板，蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "竖屏点击灰色蒙板，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "竖屏点击灰色蒙板，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_dispear_portrait(self):
        """ 竖屏窗口自动消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(7)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏等待6秒，快速模式窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏等待6秒，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "竖屏快速模式窗口自动消失后，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "竖屏快速模式窗口自动消失后，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_enable_btn_click_portrait(self):
        """ 竖屏点击启用快速模式按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_enable_btn_click()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏点击快速模式窗口启用按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏点击快速模式窗口启用按钮，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "2x", "竖屏点击快速模式窗口启用按钮，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "竖屏点击快速模式窗口启用按钮，滚轴滚动方式不是快速速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_enable_btn_click_refresh_portrait(self):
        """ 竖屏点击启用快速模式按钮后刷新页面 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_enable_btn_click()
        sleep(1)
        self.browser.refresh()
        self.common.loading_pass()
        sleep(1)

        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "2x", "竖屏点击启用快速模式按钮后刷新，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "竖屏点击启用快速模式按钮后刷新，滚轴滚动方式不是快速速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_turbo_view_switch_screen(self):
        """ 横竖屏快速模式窗口显示 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)

        turbo_view = self.common.turbo_mode_view_showing()
        mask_view = self.common.mask_view_showing()
        close_btn = self.common.turbo_mode_view_close_btn_visible()
        close_btn_touchable = self.common.turbo_mode_view_close_btn_touchable()
        title_long = self.common.turbo_mode_view_title_long()
        title_short = self.common.turbo_mode_view_title_short()
        enable_btn = self.common.turbo_mode_view_enable_btn_visible()
        enable_btn_text = self.common.turbo_mode_view_enable_btn_text()
        enable_btn_touchable = self.common.turbo_mode_view_enable_btn_touchable()

        try:
            self.assertEqual(turbo_view, True, "竖屏快速旋转停止两次，横竖屏切换，不会弹出快速模式窗口！")
            self.assertEqual(mask_view, True, "竖屏弹出快速模式窗口，横竖屏切换，不会显示灰色蒙板！")
            self.assertEqual(close_btn, True, "竖屏弹出快速模式窗口，横竖屏切换，不会显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "竖屏弹出快速模式窗口，横竖屏切换，关闭按钮不可点击！")
            self.assertEqual(title_long, "看来您喜欢更快速的玩游戏。\n你想启用快速模式吗?", "竖屏弹出快速模式窗口，横竖屏切换，长的提示文字错误！")
            self.assertEqual(title_short, "您可以随时在菜单中将其禁用", "竖屏弹出快速模式窗口，横竖屏切换，短的提示文字错误！")
            self.assertEqual(enable_btn, True, "竖屏弹出快速模式窗口，横竖屏切换，不会显示启动快速按钮！")
            self.assertEqual(enable_btn_text, "启用快速模式", "竖屏弹出快速模式窗口，横竖屏切换，启动快速模式按钮上的文字错误！")
            self.assertEqual(enable_btn_touchable, True, "竖屏弹出快速模式窗口，横竖屏切换，启动快速模式按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_close_btn_click_switch_screen(self):
        """ 横竖屏点击关闭按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_close_btn_click()
        sleep(0.5)
        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏点击快速模式窗口关闭按钮，横竖屏切换，窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏点击快速模式窗口关闭按钮，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "竖屏点击快速模式窗口关闭按钮，横竖屏切换，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "竖屏点击快速模式窗口关闭按钮，横竖屏切换，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_dispear_switch_screen(self):
        """ 横竖屏窗口自动消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(6.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏等待6秒，横竖屏切换，快速模式窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏等待6秒，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "1x", "竖屏快速模式窗口自动消失后，横竖屏切换，快速模式按钮状态不是1x！")
            self.assertEqual(spin_status, False, "竖屏快速模式窗口自动消失后，横竖屏切换，滚轴滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_enable_btn_click_switch_screen(self):
        """ 横竖屏点击启用快速模式按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        while True:
            i = 0
            game_status = None
            total_win = 0
            for i in range(2):
                self.common.start_btn_click()
                self.common.wait_for_rolling(30)
                sleep(0.5)
                self.common.start_btn_click()
                sleep(0.5)
                game_status = self.common.get_game_current_status()
                total_win = self.common.total_win()

                if game_status is not None or total_win != 0:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(3)
                    break

            if i == 1 and game_status is None and total_win == 0:
                break

        sleep(1)
        self.common.turbo_mode_view_enable_btn_click()
        sleep(0.5)
        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)
        turbo_view = self.common.turbo_mode_view_dispear()
        mask_view = self.common.mask_view_showing()
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_view, None, "竖屏点击快速模式窗口启用按钮，横竖屏切换，窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏点击快速模式窗口启用按钮，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(turbo_btn_status, "2x", "竖屏点击快速模式窗口启用按钮，横竖屏切换，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "竖屏点击快速模式窗口启用按钮，横竖屏切换，滚轴滚动方式不是快速速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
