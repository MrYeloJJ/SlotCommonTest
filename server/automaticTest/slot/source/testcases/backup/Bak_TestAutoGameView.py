# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestAutoGameView(unittest.TestCase):
    """ 自动游戏设置模块 """

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

    def test_auto_game_btn(self):
        """ 横屏自动游戏按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.auto_game_btn_visible()
        touchable = self.common.auto_game_btn_touchable()
        try:
            self.assertEqual(visible, True, "横屏不会显示自动游戏按钮！")
            self.assertEqual(touchable, True, "横屏自动游戏按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_game_btn_click(self):
        """ 横屏点击自动游戏按钮 """
        self.common.loading_pass()
        sleep(3)
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

    def test_click_mask_view_dispear(self):
        """ 横屏点击灰色蒙板，设置面板消失 """
        self.common.loading_pass()
        sleep(3)
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

    def test_close_btn_click(self):
        """ 横屏点击设置面板关闭按钮，面板消失 """
        self.common.loading_pass()
        sleep(3)
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

    def test_auto_game_view(self):
        """ 横屏设置面板按钮文字显示 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        icon = self.common.auto_game_view_icon_visible()
        slider_bar = self.common.auto_game_view_slider_bar_visible()
        slider_btn = self.common.auto_game_view_slider_btn_visible()

        current_auto_game_time = self.common.auto_game_view_auto_time_text()
        target_auto_game_time = self.common.auto_game_times[-1]
        current_value = self.common.auto_game_view_slider_value()

        start_btn = self.common.auto_game_view_start_btn_visible()
        start_btn_text = self.common.auto_game_view_start_btn_text()
        start_btn_touchable = self.common.auto_game_view_start_btn_touchable()

        close_btn = self.common.auto_game_view_close_btn_visible()
        close_btn_touchable = self.common.auto_game_view_close_btn_touchable()

        if target_auto_game_time == -1:
            target_auto_game_time = "直到环节"
        else:
            target_auto_game_time = str(target_auto_game_time) + "次旋转"
        try:
            self.assertEqual(icon, True, "横屏自动游戏设置面板，不会显示小图标！")
            self.assertEqual(slider_bar, True, "横屏自动游戏设置面板，没有显示拖动条！")
            self.assertEqual(slider_btn, True, "横屏自动游戏设置面板，不会显示拖动条按钮！")
            self.assertEqual(current_auto_game_time, target_auto_game_time, "横屏自动游戏设置面板，默认的自动次数不是最大值！")
            self.assertEqual(current_value, 100, "横屏自动游戏设置面板，默认的拖动条按钮没有在最右边！")
            self.assertEqual(start_btn, True, "横屏自动游戏设置面板，不会显示开始按钮！")
            self.assertEqual(start_btn_text, "开始旋转", "横屏自动游戏设置面板，开始按钮文字错误！")
            self.assertEqual(start_btn_touchable, True, "横屏自动游戏设置面板，开始按钮不能点击！")
            self.assertEqual(close_btn, True, "横屏自动游戏设置面板，没有显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "横屏自动游戏设置面板，关闭按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_change_auto_time(self):
        """ 横屏设置面板改变自动次数，次数显示正确 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        # 根据读取到的自动次数，分别改变自动次数
        for i in reversed(range(target_time_len)):
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            current_time = self.common.auto_game_view_auto_time_text()
            target_time = self.common.auto_game_times[i]

            if target_time == -1:
                target_time = "直到环节"
            else:
                target_time = str(target_time) + "次旋转"

            try:
                self.assertEqual(current_time, target_time, "横屏自动游戏设置面板，改变自动次数后与策划的不一致！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_start_btn_click(self):
        """ 横屏点击开始自动游戏按钮 """
        self.common.loading_pass()
        sleep(3)
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
            self.assertEqual(start_btn_status, "playing", "横屏启动自动游戏，旋转按钮不会变成停止按钮状态！")
            self.assertEqual(setting_btn, False, "横屏启动自动游戏，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "横屏启动自动游戏，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractL", "横屏启动自动游戏，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "横屏启动自动游戏，左侧选项菜单可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_spin_time(self):
        """ 横屏改变自动次数，点击开始旋转按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        # 根据配置数据分别设置自动次数，并启动自动游戏，验证次数是否依次减少
        for i in reversed(range(target_time_len)):
            self.common.auto_game_btn_click()
            sleep(1)
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            target_spin_btn_time = self.common.auto_game_times[i]

            self.common.auto_game_view_start_btn_click()
            sleep(1)

            game_status = None

            # 用这个循环来防止自动游戏过程触发特殊玩法，影响用例执行和验证
            while True:
                # 累计自动旋转次数
                y = 0
                # 自动游戏需要旋转的次数
                loop_time = 3
                for y in range(loop_time):

                    # 等待到滚轴旋转了再进入下一步
                    self.common.wait_for_rolling(30)

                    # 判断是否中了特殊玩法游戏，若中了则刷新游戏重来
                    game_status = self.common.get_game_current_status()
                    if game_status is not None:
                        self.browser.refresh()
                        self.common.loading_pass()
                        sleep(1)
                        self.common.sound_view_yes_btn_click()
                        sleep(1)
                        self.common.auto_game_btn_click()
                        sleep(1)
                        self.common.auto_game_view_change_auto_time(i)
                        sleep(1)

                        target_spin_btn_time = self.common.auto_game_times[i]

                        self.common.auto_game_view_start_btn_click()
                        sleep(1)
                        break

                    # 获取停止旋转按钮和下导航栏上的剩余次数
                    current_spin_time = self.common.in_auto_spin_btn_text()
                    current_info_bar_spin_time = self.common.info_bar_view_banner_tips_label()

                    if target_spin_btn_time == -1 or target_spin_btn_time == "直到":
                        target_spin_btn_time = "直到"
                        target_info_bar_spin_time = "直到环节自动旋转"
                    else:
                        target_spin_btn_time = target_spin_btn_time - 1
                        target_info_bar_spin_time = "剩余" + str(target_spin_btn_time) + "次自动旋转"

                    try:
                        self.assertEqual(current_spin_time, str(target_spin_btn_time), "横屏启动自动游戏，停止按钮上的剩余次数错误！")
                        self.assertEqual(current_info_bar_spin_time, target_info_bar_spin_time, "横屏启动自动游戏，下导航栏上的剩余次数错误！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    # 等待到滚轴停止了再进入下一步
                    self.common.wait_for_rolling_stop(30)

                if y == (loop_time - 1) and game_status is None:
                    self.common.start_btn_click()
                    sleep(1)
                    break

    def test_auto_spin_time_is_zero(self):
        """ 横屏自动次数为0时停止 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_change_auto_time(0)
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        # 用这个循环来防止自动游戏过程触发特殊玩法
        while True:

            self.common.wait_for_rolling(30)

            # 获取停止旋转按钮上的剩余次数
            current_spin_time = self.common.in_auto_spin_btn_text()

            # 判断自动游戏最后一局是否中了特殊玩法，若中了则刷新游戏重来
            if current_spin_time == "0":
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                        self.browser.refresh()
                        self.common.loading_pass()
                        sleep(1)
                        self.common.sound_view_yes_btn_click()
                        sleep(1)

                        self.common.auto_game_btn_click()
                        sleep(1)
                        self.common.auto_game_view_change_auto_time(0)
                        sleep(1)

                        self.common.auto_game_view_start_btn_click()
                        sleep(1)
                        continue
                else:
                    self.common.wait_for_rolling_stop(30)

                    for i in range(10):     # 循环10秒验证是否还会继续自动旋转
                        sleep(1)
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
                            self.assertEqual(slot_rolling, False, "横屏自动游戏次数为0后，滚轴不会停止滚动！")
                            self.assertEqual(start_btn_status, "stopped", "横屏自动游戏次数为0后，旋转按钮不会变成旋转按钮状态！")
                            self.assertEqual(setting_btn, True, "横屏自动游戏次数为0后，线数线注设置按钮不会重新显示！")
                            self.assertEqual(auto_game_btn, True, "横屏自动游戏次数为0后，自动游戏按钮不会重新显示！")
                            self.assertEqual(main_menu_expand, "retractL", "横屏自动游戏次数为0后，左侧选项菜单不会依然折叠！")
                            self.assertEqual(main_menu, True, "横屏自动游戏次数为0后，左侧选项菜单不可以点击！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break
            else:
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)
                    self.common.auto_game_view_change_auto_time(0)
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)

            self.common.wait_for_rolling_stop(30)

    def test_in_auto_game_click_start_btn(self):
        """ 横屏自动游戏过程，点击停止按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        while True:

            self.common.wait_for_rolling(30)

            # 自动游戏过程，点击停止按钮
            self.common.start_btn_click()

            slot_rolling = self.common.slot_machine_rolling()
            start_btn_text = self.common.in_auto_spin_btn_text()
            start_btn_status = self.common.start_btn_status()
            setting_btn = self.common.setting_btn_visible()
            auto_game_btn = self.common.auto_game_btn_visible()
            main_menu_expand = self.common.main_menu_expand()
            main_menu = self.common.main_menu_touchable()

            try:
                self.assertEqual(slot_rolling, True, "横屏自动游戏过程点击停止按钮，滚轴不会继续滚动！")
                self.assertEqual(start_btn_text, "", "横屏自动游戏过程点击停止按钮，按钮上依然显示自动次数！")
                self.assertEqual(start_btn_status, "playing", "横屏自动游戏过程点击停止按钮，旋转按钮不会保持显示停止按钮状态！")
                self.assertEqual(setting_btn, False, "横屏自动游戏过程点击停止按钮，线数线注设置按钮不会保持消失！")
                self.assertEqual(auto_game_btn, False, "横屏自动游戏过程点击停止按钮，自动游戏按钮不会保持消失！")
                self.assertEqual(main_menu_expand, "retractL", "横屏自动游戏过程点击停止按钮，左侧选项菜单不会保持折叠！")
                self.assertEqual(main_menu, False, "横屏自动游戏过程点击停止按钮，左侧选项菜单不会保持不可点击状态！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

            # 验证游戏是否触发特殊玩法，若触发了则刷新重来
            while True:
                self.common.wait_for_rolling_stop(30)

                sleep(1)
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)
                    break
                else:
                    start_btn_status = self.common.start_btn_status()
                    setting_btn = self.common.setting_btn_visible()
                    auto_game_btn = self.common.auto_game_btn_visible()
                    main_menu_expand = self.common.main_menu_expand()
                    main_menu = self.common.main_menu_touchable()

                    try:
                        self.assertEqual(start_btn_status, "stopped", "横屏自动游戏过程点击停止按钮，滚轴自动停下后，停止旋转按钮不会变成旋转按钮状态！")
                        self.assertEqual(setting_btn, True, "横屏自动游戏过程点击停止按钮，滚轴自动停下后，线数线注设置按钮不会重新显示！")
                        self.assertEqual(auto_game_btn, True, "横屏自动游戏过程点击停止按钮，滚轴自动停下后，自动游戏按钮不会重新显示！")
                        self.assertEqual(main_menu_expand, "retractL", "横屏自动游戏过程点击停止按钮，滚轴自动停下后，左侧选项菜单不会保持折叠！")
                        self.assertEqual(main_menu, True, "横屏自动游戏过程点击停止按钮，滚轴自动停下后，左侧选项菜单不会变成可点击状态！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    # 滚轴停止后，循环10秒验证是否还会自动旋转
                    for i in range(10):
                        sleep(1)
                        # 获取滚轴滚动状态
                        slot_rolling = self.common.slot_machine_rolling()

                        try:
                            self.assertEqual(slot_rolling, False, "横屏自动游戏过程点击停止按钮，滚轴自动停下后，还会继续自动旋转！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break

            if game_status is None:
                break

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_auto_game_btn_portrait(self):
        """ 竖屏自动游戏按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.auto_game_btn_visible()
        touchable = self.common.auto_game_btn_touchable()
        try:
            self.assertEqual(visible, True, "竖屏不会显示自动游戏按钮！")
            self.assertEqual(touchable, True, "竖屏自动游戏按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_game_btn_click_portrait(self):
        """ 竖屏点击自动游戏按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        visible = self.common.auto_game_view_visible()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(visible, True, "竖屏点击自动游戏按钮，不会显示自动游戏设置面板！")
            self.assertEqual(mask, True, "竖屏点击自动游戏按钮，不会显示灰色蒙板！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_click_mask_view_dispear_portrait(self):
        """ 竖屏点击灰色蒙板，设置面板消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        self.common.mask_view_click()
        sleep(1)
        dispear = self.common.auto_game_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "竖屏显示自动游戏设置面板时，点击灰色蒙板，设置面板不会消失！")
            self.assertEqual(mask, False, "竖屏显示自动游戏设置面板时，点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_close_btn_click_portrait(self):
        """ 竖屏点击设置面板关闭按钮，面板消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_close_btn_click()
        sleep(1)
        dispear = self.common.auto_game_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "竖屏显示自动游戏设置面板时，点击灰色蒙板，设置面板不会消失！")
            self.assertEqual(mask, False, "竖屏显示自动游戏设置面板时，点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_game_view_portrait(self):
        """ 竖屏设置面板按钮文字显示 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)
        icon = self.common.auto_game_view_icon_visible()
        slider_bar = self.common.auto_game_view_slider_bar_visible()
        slider_btn = self.common.auto_game_view_slider_btn_visible()

        current_auto_game_time = self.common.auto_game_view_auto_time_text()
        target_auto_game_time = self.common.auto_game_times[-1]
        current_value = self.common.auto_game_view_slider_value()

        start_btn = self.common.auto_game_view_start_btn_visible()
        start_btn_text = self.common.auto_game_view_start_btn_text()
        start_btn_touchable = self.common.auto_game_view_start_btn_touchable()

        close_btn = self.common.auto_game_view_close_btn_visible()
        close_btn_touchable = self.common.auto_game_view_close_btn_touchable()

        if target_auto_game_time == -1:
            target_auto_game_time = "直到环节"
        else:
            target_auto_game_time = str(target_auto_game_time) + "次旋转"
        try:
            self.assertEqual(icon, True, "竖屏自动游戏设置面板，不会显示小图标！")
            self.assertEqual(slider_bar, True, "竖屏自动游戏设置面板，没有显示拖动条！")
            self.assertEqual(slider_btn, True, "竖屏自动游戏设置面板，不会显示拖动条按钮！")
            self.assertEqual(current_auto_game_time, target_auto_game_time, "竖屏自动游戏设置面板，默认的自动次数不是最大值！")
            self.assertEqual(current_value, 100, "竖屏自动游戏设置面板，默认的拖动条按钮没有在最右边！")
            self.assertEqual(start_btn, True, "竖屏自动游戏设置面板，不会显示开始按钮！")
            self.assertEqual(start_btn_text, "开始旋转", "竖屏自动游戏设置面板，开始按钮文字错误！")
            self.assertEqual(start_btn_touchable, True, "竖屏自动游戏设置面板，开始按钮不能点击！")
            self.assertEqual(close_btn, True, "竖屏自动游戏设置面板，没有显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "竖屏自动游戏设置面板，关闭按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_change_auto_time_portrait(self):
        """ 竖屏设置面板改变自动次数，次数显示正确 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        # 根据读取到的自动次数，分别改变自动次数
        for i in reversed(range(target_time_len)):
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            current_time = self.common.auto_game_view_auto_time_text()
            target_time = self.common.auto_game_times[i]

            if target_time == -1:
                target_time = "直到环节"
            else:
                target_time = str(target_time) + "次旋转"

            try:
                self.assertEqual(current_time, target_time, "竖屏自动游戏设置面板，改变自动次数后与策划的不一致！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_start_btn_click_portrait(self):
        """ 竖屏点击开始自动游戏按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
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
            self.assertEqual(view_dispear, None, "竖屏启动自动游戏，自动游戏设置面板不会消失！")
            self.assertEqual(mask_dispear, False, "竖屏启动自动游戏，灰色蒙板不会消失！")
            self.assertEqual(slot_rolling, True, "竖屏启动自动游戏，滚轴不会滚动！")
            self.assertEqual(start_btn_status, "playing", "竖屏启动自动游戏，旋转按钮不会变成停止按钮状态！")
            self.assertEqual(setting_btn, False, "竖屏启动自动游戏，线数线注设置按钮不会消失！")
            self.assertEqual(auto_game_btn, False, "竖屏启动自动游戏，自动游戏按钮不会消失！")
            self.assertEqual(main_menu_expand, "retractP", "竖屏启动自动游戏，左侧选项菜单不会折叠！")
            self.assertEqual(main_menu, False, "竖屏启动自动游戏，左侧选项菜单可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_spin_time_portrait(self):
        """ 竖屏改变自动次数，点击开始旋转按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        # 根据配置数据分别设置自动次数，并启动自动游戏，验证次数是否依次减少
        for i in reversed(range(target_time_len)):
            self.common.auto_game_btn_click()
            sleep(1)
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)

            target_spin_btn_time = self.common.auto_game_times[i]

            self.common.auto_game_view_start_btn_click()
            sleep(1)

            game_status = None

            # 用这个循环来防止自动游戏过程触发特殊玩法，影响用例执行和验证
            while True:
                # 累计自动旋转次数
                y = 0
                # 自动游戏需要旋转的次数
                loop_time = 3
                for y in range(loop_time):

                    # 等待到滚轴旋转了再进入下一步
                    self.common.wait_for_rolling(30)

                    # 判断是否中了特殊玩法游戏，若中了则刷新游戏重来
                    game_status = self.common.get_game_current_status()
                    if game_status is not None:
                        self.browser.refresh()
                        self.common.loading_pass()
                        sleep(1)
                        self.common.sound_view_yes_btn_click()
                        sleep(1)
                        self.common.auto_game_btn_click()
                        sleep(1)
                        self.common.auto_game_view_change_auto_time(i)
                        sleep(1)

                        target_spin_btn_time = self.common.auto_game_times[i]

                        self.common.auto_game_view_start_btn_click()
                        sleep(1)
                        break

                    # 获取停止旋转按钮和下导航栏上的剩余次数
                    current_spin_time = self.common.in_auto_spin_btn_text()
                    current_info_bar_spin_time = self.common.info_bar_view_banner_tips_label()

                    if target_spin_btn_time == -1 or target_spin_btn_time == "直到":
                        target_spin_btn_time = "直到"
                        target_info_bar_spin_time = "直到环节自动旋转"
                    else:
                        target_spin_btn_time = target_spin_btn_time - 1
                        target_info_bar_spin_time = "剩余" + str(target_spin_btn_time) + "次自动旋转"

                    try:
                        self.assertEqual(current_spin_time, str(target_spin_btn_time), "竖屏启动自动游戏，停止按钮上的剩余次数错误！")
                        self.assertEqual(current_info_bar_spin_time, target_info_bar_spin_time, "竖屏启动自动游戏，下导航栏上的剩余次数错误！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    # 等待到滚轴停止了再进入下一步
                    self.common.wait_for_rolling_stop(30)

                if y == (loop_time - 1) and game_status is None:
                    self.common.start_btn_click()
                    sleep(1)
                    break

    def test_auto_spin_time_is_zero_portrait(self):
        """ 竖屏自动次数为0时停止 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_change_auto_time(0)
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        # 用这个循环来防止自动游戏过程触发特殊玩法
        while True:

            self.common.wait_for_rolling(30)

            # 获取停止旋转按钮上的剩余次数
            current_spin_time = self.common.in_auto_spin_btn_text()

            # 判断自动游戏最后一局是否中了特殊玩法，若中了则刷新游戏重来
            if current_spin_time == "0":
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                        self.browser.refresh()
                        self.common.loading_pass()
                        sleep(1)
                        self.common.sound_view_yes_btn_click()
                        sleep(1)

                        self.common.auto_game_btn_click()
                        sleep(1)
                        self.common.auto_game_view_change_auto_time(0)
                        sleep(1)

                        self.common.auto_game_view_start_btn_click()
                        sleep(1)
                        continue
                else:
                    self.common.wait_for_rolling_stop(30)

                    for i in range(10):     # 循环10秒验证是否还会继续自动旋转
                        sleep(1)
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
                            self.assertEqual(slot_rolling, False, "竖屏自动游戏次数为0后，滚轴不会停止滚动！")
                            self.assertEqual(start_btn_status, "stopped", "竖屏自动游戏次数为0后，旋转按钮不会变成旋转按钮状态！")
                            self.assertEqual(setting_btn, True, "竖屏自动游戏次数为0后，线数线注设置按钮不会重新显示！")
                            self.assertEqual(auto_game_btn, True, "竖屏自动游戏次数为0后，自动游戏按钮不会重新显示！")
                            self.assertEqual(main_menu_expand, "retractP", "竖屏自动游戏次数为0后，左侧选项菜单不会依然折叠！")
                            self.assertEqual(main_menu, True, "竖屏自动游戏次数为0后，左侧选项菜单不可以点击！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break
            else:
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)
                    self.common.auto_game_view_change_auto_time(0)
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)

            self.common.wait_for_rolling_stop(30)

    def test_in_auto_game_click_start_btn_portrait(self):
        """ 竖屏自动游戏过程，点击停止按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        while True:

            self.common.wait_for_rolling(30)

            # 自动游戏过程，点击停止按钮
            self.common.start_btn_click()

            slot_rolling = self.common.slot_machine_rolling()
            start_btn_text = self.common.in_auto_spin_btn_text()
            start_btn_status = self.common.start_btn_status()
            setting_btn = self.common.setting_btn_visible()
            auto_game_btn = self.common.auto_game_btn_visible()
            main_menu_expand = self.common.main_menu_expand()
            main_menu = self.common.main_menu_touchable()

            try:
                self.assertEqual(slot_rolling, True, "竖屏自动游戏过程点击停止按钮，滚轴不会继续滚动！")
                self.assertEqual(start_btn_text, "", "竖屏自动游戏过程点击停止按钮，按钮上依然显示自动次数！")
                self.assertEqual(start_btn_status, "playing", "竖屏自动游戏过程点击停止按钮，旋转按钮不会保持显示停止按钮状态！")
                self.assertEqual(setting_btn, False, "竖屏自动游戏过程点击停止按钮，线数线注设置按钮不会保持消失！")
                self.assertEqual(auto_game_btn, False, "竖屏自动游戏过程点击停止按钮，自动游戏按钮不会保持消失！")
                self.assertEqual(main_menu_expand, "retractP", "竖屏自动游戏过程点击停止按钮，左侧选项菜单不会保持折叠！")
                self.assertEqual(main_menu, False, "竖屏自动游戏过程点击停止按钮，左侧选项菜单不会保持不可点击状态！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

            # 验证游戏是否触发特殊玩法，若触发了则刷新重来
            while True:
                self.common.wait_for_rolling_stop(30)

                sleep(1)
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)
                    break
                else:
                    start_btn_status = self.common.start_btn_status()
                    setting_btn = self.common.setting_btn_visible()
                    auto_game_btn = self.common.auto_game_btn_visible()
                    main_menu_expand = self.common.main_menu_expand()
                    main_menu = self.common.main_menu_touchable()

                    try:
                        self.assertEqual(start_btn_status, "stopped", "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，停止旋转按钮不会变成旋转按钮状态！")
                        self.assertEqual(setting_btn, True, "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，线数线注设置按钮不会重新显示！")
                        self.assertEqual(auto_game_btn, True, "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，自动游戏按钮不会重新显示！")
                        self.assertEqual(main_menu_expand, "retractP", "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，左侧选项菜单不会保持折叠！")
                        self.assertEqual(main_menu, True, "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，左侧选项菜单不会变成可点击状态！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    # 滚轴停止后，循环10秒验证是否还会自动旋转
                    for i in range(10):
                        sleep(1)
                        # 获取滚轴滚动状态
                        slot_rolling = self.common.slot_machine_rolling()

                        try:
                            self.assertEqual(slot_rolling, False, "竖屏自动游戏过程点击停止按钮，滚轴自动停下后，还会继续自动旋转！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break

            if game_status is None:
                break

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_change_auto_time_switch_screen(self):
        """ 横竖屏设置面板改变自动次数，次数显示正确 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.auto_game_btn_click()
        sleep(1)

        target_time_len = len(self.common.auto_game_times)

        # 根据读取到的自动次数，分别改变自动次数
        for i in reversed(range(target_time_len)):
            self.common.auto_game_view_change_auto_time(i)
            sleep(1)
            auto_time1 = self.common.auto_game_view_auto_time_text()
            if i % 2 == 0:
                self.common.portrait()
            else:
                self.common.landscape()

            sleep(1)

            auto_time2 = self.common.auto_game_view_auto_time_text()

            try:
                self.assertEqual(auto_time1, auto_time2, "自动游戏设置面板，改变自动次数后切换横竖屏，自动次数不一致！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_auto_spin_time_switch_screen(self):
        """ 横竖屏改变自动次数，点击开始旋转按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_change_auto_time(0)
        sleep(1)

        target_spin_btn_time = self.common.auto_game_times[0]

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        # 用这个循环来防止自动游戏过程触发特殊玩法，影响用例执行和验证
        while True:
            i = 0

            for i in range(target_spin_btn_time):

                # 等待到滚轴旋转了再进入下一步
                self.common.wait_for_rolling(30)

                sleep(0.5)

                if i % 2 == 0:
                    self.common.landscape()
                else:
                    self.common.portrait()

                sleep(0.5)

                # 判断是否中了特殊玩法游戏，若中了则刷新游戏重来
                game_status = self.common.get_game_current_status()
                if i != 4 and game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)
                    self.common.auto_game_btn_click()
                    sleep(1)
                    self.common.auto_game_view_change_auto_time(0)
                    sleep(1)
                    target_spin_btn_time = self.common.auto_game_times[0]
                    self.common.auto_game_view_start_btn_click()
                    sleep(1)
                    break

                # 获取停止旋转按钮和下导航栏上的剩余次数
                current_spin_time = self.common.in_auto_spin_btn_text()
                current_info_bar_spin_time = self.common.info_bar_view_banner_tips_label()

                target_spin_btn_time -= 1
                target_info_bar_spin_time = "剩余" + str(target_spin_btn_time) + "次自动旋转"

                try:
                    self.assertEqual(current_spin_time, str(target_spin_btn_time), "启动自动游戏，切换横竖屏，停止按钮上的剩余次数错误！")
                    self.assertEqual(current_info_bar_spin_time, target_info_bar_spin_time, "启动自动游戏，切换横竖屏，下导航栏上的剩余次数错误！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

                # 等待到滚轴停止了再进入下一步
                self.common.wait_for_rolling_stop(30)

                # 验证5次即可
                if i == 4:
                    break

            if i == 4:
                break

    def test_auto_spin_click_btn_switch_screen(self):
        """ 横竖屏自动游戏过程点击停止按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        while True:

            self.common.wait_for_rolling(30)

            # 自动游戏过程，点击停止按钮
            self.common.start_btn_click()
            sleep(0.5)
            self.common.landscape()
            sleep(0.5)

            slot_rolling = self.common.slot_machine_rolling()
            start_btn_text = self.common.in_auto_spin_btn_text()
            start_btn_status = self.common.start_btn_status()
            setting_btn = self.common.setting_btn_visible()
            auto_game_btn = self.common.auto_game_btn_visible()
            main_menu_expand = self.common.main_menu_expand()
            main_menu = self.common.main_menu_touchable()

            try:
                self.assertEqual(slot_rolling, True, "自动游戏过程点击停止按钮，横竖屏切换，滚轴不会继续滚动！")
                self.assertEqual(start_btn_text, "", "自动游戏过程点击停止按钮，横竖屏切换，按钮上依然显示自动次数！")
                self.assertEqual(start_btn_status, "playing", "自动游戏过程点击停止按钮，横竖屏切换，旋转按钮不会保持显示停止按钮状态！")
                self.assertEqual(setting_btn, False, "自动游戏过程点击停止按钮，横竖屏切换，线数线注设置按钮不会保持消失！")
                self.assertEqual(auto_game_btn, False, "自动游戏过程点击停止按钮，横竖屏切换，自动游戏按钮不会保持消失！")
                self.assertEqual(main_menu_expand, "retractL", "自动游戏过程点击停止按钮，横竖屏切换，左侧选项菜单不会保持折叠！")
                self.assertEqual(main_menu, False, "自动游戏过程点击停止按钮，横竖屏切换，左侧选项菜单不会保持不可点击状态！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

            # 验证游戏是否触发特殊玩法，若触发了则刷新重来
            while True:
                self.common.wait_for_rolling_stop(30)

                sleep(1)
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_pass()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)
                    break
                else:
                    start_btn_status = self.common.start_btn_status()
                    setting_btn = self.common.setting_btn_visible()
                    auto_game_btn = self.common.auto_game_btn_visible()
                    main_menu_expand = self.common.main_menu_expand()
                    main_menu = self.common.main_menu_touchable()

                    try:
                        self.assertEqual(start_btn_status, "stopped", "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，停止旋转按钮不会变成旋转按钮状态！")
                        self.assertEqual(setting_btn, True, "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，线数线注设置按钮不会重新显示！")
                        self.assertEqual(auto_game_btn, True, "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，自动游戏按钮不会重新显示！")
                        self.assertEqual(main_menu_expand, "retractL", "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，左侧选项菜单不会保持折叠！")
                        self.assertEqual(main_menu, True, "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，左侧选项菜单不会变成可点击状态！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    # 滚轴停止后，循环10秒验证是否还会自动旋转
                    for i in range(10):
                        sleep(1)
                        # 获取滚轴滚动状态
                        slot_rolling = self.common.slot_machine_rolling()

                        try:
                            self.assertEqual(slot_rolling, False, "自动游戏过程点击停止按钮，横竖屏切换，滚轴自动停下后，还会继续自动旋转！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break

            if game_status is None:
                break


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
