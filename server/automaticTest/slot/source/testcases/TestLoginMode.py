# coding=utf-8

import unittest
from time import sleep
from server.automaticTest.slot.source.common.Browser import Browser
from server.automaticTest.slot.source.common.Common import Common
from server.automaticTest.slot.lib.HTMLTestReportCN import DirAndFiles


class TestLoginMode(unittest.TestCase):
    """ 登录状态模块 """

    def setUp(self):
        self.browser = Browser().browser()
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

    def test_login(self):
        """ 横屏登录状态 """
        sleep(1)
        lobby_chips = self.common.lobby_chips()["lobby_chips"]
        self.common.switch_page()
        self.common.find_game()
        self.common.switch_game_window()
        self.common.loading_pass()
        sleep(1)

        has_money_title = self.common.info_bar_view_has_money_title()
        has_money_label = self.common.info_bar_view_has_money_label()
        game_record = self.common.game_record_btn_enable()
        game_record_touchable = self.common.game_record_btn_touchable()

        try:
            self.assertEqual(has_money_title, "我的余额", "横屏登录下导航栏余额标题错误！")
            self.assertEqual(has_money_label, lobby_chips, "横屏登录下导航栏余额数值与大厅的不一致！")
            self.assertEqual(game_record, True, "横屏登录选项菜单不会显示游戏记录按钮！")
            self.assertEqual(game_record_touchable, True, "横屏登录游戏记录按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        sleep(1)
        self.common.set_chips_to_zero()
        self.browser.refresh()
        self.common.loading_pass()
        sleep(1)
        self.common.start_btn_click()
        sleep(1)

        slot_status = self.common.slot_machine_rolling()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        start_btn = self.common.start_btn_status()
        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()
        lack_of_money_title = self.common.lack_of_money_title()
        lack_of_money_ok_btn = self.common.lack_of_money_ok_btn_visible()
        lack_of_money_ok_btn_title = self.common.lack_of_money_ok_btn_title()
        lack_of_money_ok_btn_touchable = self.common.lack_of_money_ok_btn_touchable()

        try:
            self.assertEqual(slot_status, False, "横屏余额为0时点击旋转按钮，滚轴会滚动！")
            self.assertEqual(setting_btn, True, "横屏余额为0时点击旋转按钮，线数线注设置按钮消失！")
            self.assertEqual(auto_game_btn, True, "横屏余额为0时点击旋转按钮，自动游戏按钮消失！")
            self.assertEqual(start_btn, "stopped", "横屏余额为0时点击旋转按钮，旋转按钮不是停止状态！")
            self.assertEqual(lack_of_money_view, True, "横屏余额为0时点击旋转按钮，不会弹出余额不足窗口！")
            self.assertEqual(mask_view, True, "横屏余额为0时点击旋转按钮，不会显示灰色蒙板！")
            self.assertEqual(lack_of_money_title, "您的额度不足，无法完成您所请求的下注", "横屏弹出余额不足窗口，提示文字错误！")
            self.assertEqual(lack_of_money_ok_btn, True, "横屏弹出余额不足窗口，不会显示确定按钮！")
            self.assertEqual(lack_of_money_ok_btn_title, "确定", "横屏弹出余额不足窗口，确定按钮文字错误！")
            self.assertEqual(lack_of_money_ok_btn_touchable, True, "横屏弹出余额不足窗口，确定按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.mask_view_click()
        sleep(1)

        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, True, "横屏弹出余额不足窗口时，点击灰色蒙板，窗口会消失！")
            self.assertEqual(mask_view, True, "横屏弹出余额不足窗口时，点击灰色蒙板，灰色蒙板会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.lack_of_money_ok_btn_click()
        sleep(1)

        lack_of_money_view = self.common.lack_of_money_view_dispear()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, None, "横屏弹出余额不足窗口时，点击确定按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "横屏弹出余额不足窗口时，点击确定按钮，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_login_portrait(self):
        """ 竖屏登录状态 """
        sleep(1)
        lobby_chips = self.common.lobby_chips()["lobby_chips"]
        self.common.switch_page()
        self.common.find_game()
        self.common.switch_game_window()
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)

        has_money_title = self.common.info_bar_view_has_money_title()
        has_money_label = self.common.info_bar_view_has_money_label()
        game_record = self.common.game_record_btn_enable()
        game_record_touchable = self.common.game_record_btn_touchable()

        try:
            self.assertEqual(has_money_title, "我的余额", "竖屏登录下导航栏余额标题错误！")
            self.assertEqual(has_money_label, lobby_chips, "竖屏登录下导航栏余额数值与大厅的不一致！")
            self.assertEqual(game_record, True, "竖屏登录选项菜单不会显示游戏记录按钮！")
            self.assertEqual(game_record_touchable, True, "竖屏登录游戏记录按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        sleep(1)
        self.common.set_chips_to_zero()
        self.browser.refresh()
        self.common.loading_pass()
        sleep(1)
        self.common.start_btn_click()
        sleep(1)

        slot_status = self.common.slot_machine_rolling()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        start_btn = self.common.start_btn_status()
        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()
        lack_of_money_title = self.common.lack_of_money_title()
        lack_of_money_ok_btn = self.common.lack_of_money_ok_btn_visible()
        lack_of_money_ok_btn_title = self.common.lack_of_money_ok_btn_title()
        lack_of_money_ok_btn_touchable = self.common.lack_of_money_ok_btn_touchable()

        try:
            self.assertEqual(slot_status, False, "竖屏余额为0时点击旋转按钮，滚轴会滚动！")
            self.assertEqual(setting_btn, True, "竖屏余额为0时点击旋转按钮，线数线注设置按钮消失！")
            self.assertEqual(auto_game_btn, True, "竖屏余额为0时点击旋转按钮，自动游戏按钮消失！")
            self.assertEqual(start_btn, "stopped", "竖屏余额为0时点击旋转按钮，旋转按钮不是停止状态！")
            self.assertEqual(lack_of_money_view, True, "竖屏余额为0时点击旋转按钮，不会弹出余额不足窗口！")
            self.assertEqual(mask_view, True, "竖屏余额为0时点击旋转按钮，不会显示灰色蒙板！")
            self.assertEqual(lack_of_money_title, "您的额度不足，无法完成您所请求的下注", "竖屏弹出余额不足窗口，提示文字错误！")
            self.assertEqual(lack_of_money_ok_btn, True, "竖屏弹出余额不足窗口，不会显示确定按钮！")
            self.assertEqual(lack_of_money_ok_btn_title, "确定", "竖屏弹出余额不足窗口，确定按钮文字错误！")
            self.assertEqual(lack_of_money_ok_btn_touchable, True, "竖屏弹出余额不足窗口，确定按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.mask_view_click()
        sleep(1)

        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, True, "竖屏弹出余额不足窗口时，点击灰色蒙板，窗口会消失！")
            self.assertEqual(mask_view, True, "竖屏弹出余额不足窗口时，点击灰色蒙板，灰色蒙板会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.lack_of_money_ok_btn_click()
        sleep(1)

        lack_of_money_view = self.common.lack_of_money_view_dispear()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, None, "竖屏弹出余额不足窗口时，点击确定按钮，窗口不会消失！")
            self.assertEqual(mask_view, False, "竖屏弹出余额不足窗口时，点击确定按钮，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_login_switch_screen(self):
        """ 横竖屏登录状态 """
        sleep(1)
        lobby_chips = self.common.lobby_chips()["lobby_chips"]
        self.common.switch_page()
        self.common.find_game()
        self.common.switch_game_window()
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)

        has_money_title = self.common.info_bar_view_has_money_title()
        has_money_label = self.common.info_bar_view_has_money_label()
        game_record = self.common.game_record_btn_enable()
        game_record_touchable = self.common.game_record_btn_touchable()

        try:
            self.assertEqual(has_money_title, "我的余额", "登录后横竖屏切换，下导航栏余额标题错误！")
            self.assertEqual(has_money_label, lobby_chips, "登录后横竖屏切换，下导航栏余额数值与大厅的不一致！")
            self.assertEqual(game_record, True, "登录后横竖屏切换，选项菜单不会显示游戏记录按钮！")
            self.assertEqual(game_record_touchable, True, "登录后横竖屏切换，游戏记录按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        sleep(1)
        self.common.set_chips_to_zero()
        self.browser.refresh()
        self.common.loading_pass()
        sleep(1)
        self.common.start_btn_click()
        sleep(1)

        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)

        slot_status = self.common.slot_machine_rolling()
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        start_btn = self.common.start_btn_status()
        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()
        lack_of_money_title = self.common.lack_of_money_title()
        lack_of_money_ok_btn = self.common.lack_of_money_ok_btn_visible()
        lack_of_money_ok_btn_title = self.common.lack_of_money_ok_btn_title()
        lack_of_money_ok_btn_touchable = self.common.lack_of_money_ok_btn_touchable()

        try:
            self.assertEqual(slot_status, False, "登录后余额为0时点击旋转按钮，横竖屏切换，滚轴会滚动！")
            self.assertEqual(setting_btn, True, "登录后余额为0时点击旋转按钮，横竖屏切换，线数线注设置按钮消失！")
            self.assertEqual(auto_game_btn, True, "登录后余额为0时点击旋转按钮，横竖屏切换，自动游戏按钮消失！")
            self.assertEqual(start_btn, "stopped", "登录后余额为0时点击旋转按钮，横竖屏切换，旋转按钮不是停止状态！")
            self.assertEqual(lack_of_money_view, True, "登录后余额为0时点击旋转按钮，横竖屏切换，不会弹出余额不足窗口！")
            self.assertEqual(mask_view, True, "登录后余额为0时点击旋转按钮，横竖屏切换，不会显示灰色蒙板！")
            self.assertEqual(lack_of_money_title, "您的额度不足，无法完成您所请求的下注", "登录后弹出余额不足窗口，横竖屏切换，提示文字错误！")
            self.assertEqual(lack_of_money_ok_btn, True, "登录后弹出余额不足窗口，横竖屏切换，不会显示确定按钮！")
            self.assertEqual(lack_of_money_ok_btn_title, "确定", "登录后弹出余额不足窗口，横竖屏切换，确定按钮文字错误！")
            self.assertEqual(lack_of_money_ok_btn_touchable, True, "登录后弹出余额不足窗口，横竖屏切换，确定按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.mask_view_click()
        sleep(1)
        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)

        lack_of_money_view = self.common.lack_of_money_view_showing()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, True, "登录后弹出余额不足窗口时，点击灰色蒙板，横竖屏切换，窗口会消失！")
            self.assertEqual(mask_view, True, "登录后弹出余额不足窗口时，点击灰色蒙板，横竖屏切换，灰色蒙板会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.lack_of_money_ok_btn_click()
        sleep(1)
        self.common.landscape()
        sleep(0.5)
        self.common.portrait()
        sleep(0.5)

        lack_of_money_view = self.common.lack_of_money_view_dispear()
        mask_view = self.common.mask_view_showing()

        try:
            self.assertEqual(lack_of_money_view, None, "录后弹出余额不足窗口时，点击确定按钮，横竖屏切换，窗口不会消失！")
            self.assertEqual(mask_view, False, "录后弹出余额不足窗口时，点击确定按钮，横竖屏切换，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
