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
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            current_time = self.common.auto_game_view_auto_time_text()
            target_time = self.common.auto_game_times[i]

            if target_time is -1:
                target_time = "直到环节"
            else:
                target_time = str(target_time) + "次旋转"

            try:
                self.assertEqual(current_time, target_time, "横屏自动游戏设置面板，改变自动次数后与策划的不一致！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    # 验证横屏 显示开始旋转按钮
    def test_start_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_start_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏自动游戏设置面板，不会显示开始按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 开始旋转按钮文字
    def test_start_btn_text(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        text = self.common.auto_game_view_start_btn_text()
        try:
            self.assertEqual(text, "开始旋转", "横屏自动游戏设置面板，开始按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 开始旋转按钮可点击否
    def test_start_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        touchable = self.common.auto_game_view_start_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏自动游戏设置面板，开始按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 点击开始自动游戏按钮，自动游戏设置面板消失，蒙板消失，滚轴滚动，按钮状态改变
    def test_start_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_start_btn_click()
        sleep(1)

        # 获取自动游戏设置面板和蒙板状态
        view_dispear = self.common.auto_game_view_dispear()
        mask_dispear = self.common.mask_view_showing()
        # 获取滚轴滚动状态
        slot_rolling = self.common.slot_machine_rolling()
        # 获取旋转按钮状态
        start_btn_status = self.common.start_btn_status()
        # 获取线数线注按钮、自动游戏按钮、选项菜单状态
        setting_btn = self.common.setting_btn_visible()
        auto_game_btn = self.common.auto_game_btn_visible()
        main_menu_expand = self.common.main_menu_expand()
        main_menu = self.common.main_menu_touchable()

        try:
            self.assertEqual(view_dispear, None, "横屏启动自动游戏，自动游戏设置面板不会消失！")
            self.assertEqual(mask_dispear, False, "横屏启动自动游戏，灰色蒙板不会消失！")
            self.assertEqual(slot_rolling, True, "横屏启动自动游戏，滚轴不会滚动！")
            self.assertEqual(start_btn_status, "playing", "横屏启动自动游戏，旋转按钮不会变成停止状态！")
            self.assertEqual(setting_btn, False, "横屏启动自动游戏，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "横屏启动自动游戏，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractL", "横屏启动自动游戏，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "横屏启动自动游戏，左侧选项菜单可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 改变自动次数，点击开始旋转按钮
    def test_auto_spin_time(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        for i in reversed(range(target_time_len)):
            self.common.auto_game_btn_click()
            sleep(1)
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            target_spin_btn_time = self.common.auto_game_times[i]

            self.common.auto_game_view_start_btn_click()
            sleep(1)

            for y in range(2):

                # 获取停止旋转按钮上的剩余次数
                current_spin_time = self.common.in_auto_spin_btn_text()
                current_info_bar_spin_time = self.common.info_bar_view_banner_tips_label()

                if target_spin_btn_time is -1:
                    target_spin_btn_time = "直到"
                    # 获取下导航栏提示文字
                    target_info_bar_spin_time = "直到环节自动游戏"
                else:
                    target_spin_btn_time = target_spin_btn_time - 1
                    target_info_bar_spin_time = "剩余" + str(target_spin_btn_time) + "次自动旋转"

                try:
                    self.assertEqual(current_spin_time, target_spin_btn_time, "横屏启动自动游戏，停止按钮上的剩余次数错误！")
                    self.assertEqual(current_info_bar_spin_time, target_info_bar_spin_time, "横屏启动自动游戏，下导航栏上的剩余次数错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

                while True:
                    slot_status = self.common.slot_machine_rolling()
                    if slot_status is False:
                        break
































if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
