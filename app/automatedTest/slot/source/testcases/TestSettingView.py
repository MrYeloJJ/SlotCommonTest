# coding=utf-8

import unittest
import locale
from time import sleep
from app.automatedTest.slot.source.common.Browser import Browser
from app.automatedTest.slot.source.common.Common import Common
from app.automatedTest.slot.lib.HTMLTestReportCN import DirAndFiles


class TestSettingView(unittest.TestCase):
    """ 线数线注设置模块 """

    def setUp(self):
        self.browser = Browser().browser()
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()
        self.full_line = self.common.full_line

    def tearDown(self):
        self.browser.quit()

    # 初始化满线参数 True, False
    full_line = Common().full_line

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    def test_setting_btn_visible(self):
        """ 横屏显示线数线注设置按钮 """
        self.common.loading_pass()
        sleep(1)
        # 显示
        setting_btn = self.common.setting_btn_visible()
        # 能否点击
        setting_btn_touchable = self.common.setting_btn_touchable()
        try:
            self.assertEqual(setting_btn, True, "横屏没有显示线数线注设置按钮！")
            self.assertEqual(setting_btn_touchable, True, "横屏线数线注设置按钮无法点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_setting_btn_click_show_view(self):
        """ 横屏点击线数线注设置按钮 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        showing = self.common.setting_view_showing()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(showing, True, "横屏点击线数线注设置按钮，不会弹出对应的面板！")
            self.assertEqual(mask, True, "横屏点击线数线注设置按钮，不会显示灰色蒙板！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_click_mask_setting_view_dispear(self):
        """ 横屏点击蒙板可以关闭面板 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.mask_view_click()
        sleep(1)
        dispear = self.common.setting_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "横屏点击灰色蒙板，线数线注设置面板不会消失！")
            self.assertEqual(mask, False, "横屏点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_click_close_btn_view_dispear(self):
        """ 横屏点击关闭按钮面板消失 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.setting_view_close_btn_click()
        sleep(1)
        dispear = self.common.setting_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "横屏点击线数线注设置面板的关闭按钮，面板不会消失！")
            self.assertEqual(mask, False, "横屏点击线数线注设置面板的关闭按钮，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num(self):
        """ 横屏面板线数标题文字按钮 """
        if self.full_line is False:
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)
            # 文本
            line_num_text = self.common.setting_view_line_num_text()
            current_line_num = self.common.setting_view_line_num()
            target_line_num = str(self.common.line_num_max)
            info_bar_line_num = self.common.info_bar_view_line_num_label()
            # 显示
            line_num_min_btn = self.common.setting_view_line_num_min_btn_visible()
            line_num_plus_btn = self.common.setting_view_line_num_plus_btn_visible()
            # 能否点击
            line_num_min_btn_touchable = self.common.setting_view_line_num_min_btn_touchable()
            line_num_plus_btn_touchable = self.common.setting_view_line_num_plus_btn_touchable()
            try:
                self.assertEqual(line_num_text, "线", "横屏线数线注设置面板，线数的标题错误！")
                self.assertEqual(current_line_num, target_line_num, "横屏线数线注设置面板，默认显示的线数不是最大值！")
                self.assertEqual(info_bar_line_num, current_line_num, "横屏线数线注设置面板，线数数值与下导航栏的不一致！")
                self.assertEqual(line_num_min_btn, True, "横屏线数线注设置面板，不会显示线数 - 按钮！")
                self.assertEqual(line_num_min_btn_touchable, True, "横屏线数线注设置面板，线数 - 按钮默认不能点击！")
                self.assertEqual(line_num_plus_btn, True, "横屏线数线注设置面板，不会显示线数 + 按钮！")
                self.assertEqual(line_num_plus_btn_touchable, False, "横屏线数线注设置面板，线数 + 按钮默认可以点击！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_min_btn_click(self):
        """ 横屏面板线数 - 按钮点击 """
        if self.full_line is False:
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max
            for i in reversed(range(1, int(target_line_num))):
                self.common.setting_view_line_num_min_btn_click()
                sleep(1)
                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i > 1:
                    try:
                        self.assertEqual(current_line_num, str(i), "横屏点击线数线注设置面板的 - 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "横屏点击线数线注设置面板的 - 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, False, "横屏点击线数线注设置面板的 - 按钮，线数是最小值，- 按钮可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_plus_btn_click(self):
        """ 横屏面板线数 + 按钮点击 """
        if self.full_line is False:
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max

            for i in range(1, int(target_line_num)):
                self.common.setting_view_line_num_min_btn_click()

            sleep(1)

            for i in range(2, int(target_line_num)+1):
                self.common.setting_view_line_num_plus_btn_click()
                sleep(1)
                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i < int(target_line_num):
                    try:
                        self.assertEqual(current_line_num, str(i), "横屏点击线数线注设置面板的 + 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "横屏点击线数线注设置面板的 + 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, False, "横屏点击线数线注设置面板的 + 按钮，线数是最大值，+ 按钮可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    def test_setting_view_btn_status(self):
        """ 横屏面板按钮状态 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        # 文本
        line_cost_text = self.common.setting_view_line_cost_text()

        current_line_cost = self.common.setting_view_line_cost()
        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[0]/100, 1)
        info_bar_line_cost = self.common.info_bar_view_line_cost_label()

        # 显示
        close_btn = self.common.setting_view_close_btn_visible()
        line_cost_min_btn = self.common.setting_view_line_cost_min_btn_visible()
        line_cost_plus_btn = self.common.setting_view_line_cost_plus_btn_visible()

        # 能否点击
        close_btn_touchable = self.common.setting_view_close_btn_touchable()
        line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
        line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()
        try:
            self.assertEqual(close_btn, True, "横屏线数线注设置面板不会显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "横屏线数线注设置面板，关闭按钮不能点击！")
            self.assertEqual(line_cost_text, "线注", "横屏线数线注设置面板，线注的标题错误！")
            self.assertEqual(current_line_cost, target_line_cost, "横屏线数线注设置面板，默认显示的线注不是最小值！")
            self.assertEqual(info_bar_line_cost, current_line_cost, "横屏线数线注设置面板，线注数值与下导航栏的不一致！")
            self.assertEqual(line_cost_min_btn, True, "横屏线数线注设置面板，不会显示线注 - 按钮！")
            self.assertEqual(line_cost_min_btn_touchable, False, "横屏线数线注设置面板，线注 - 按钮默认可以点击！")
            self.assertEqual(line_cost_plus_btn, True, "横屏线数线注设置面板，不会显示线注 + 按钮！")
            self.assertEqual(line_cost_plus_btn_touchable, True, "横屏线数线注设置面板，线注 + 按钮默认不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_line_cost_plus_btn_click(self):
        """ 横屏面板线注 + 按钮点击 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)
        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)
            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i < (cost_len - 1):
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "横屏点击线数线注设置面板的 + 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "横屏点击线数线注设置面板的 + 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "横屏点击线数线注设置面板的 + 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "横屏点击线数线注设置面板的 + 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, False, "横屏点击线数线注设置面板的 + 按钮，线注是最大值，线注 + 按钮可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_line_cost_min_btn_click(self):
        """ 横屏面板线注 - 按钮点击 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)

        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()

        sleep(1)

        for i in reversed(range(cost_len - 1)):
            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)
            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i > 0:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "横屏点击线数线注设置面板的 - 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "横屏点击线数线注设置面板的 - 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "横屏点击线数线注设置面板的 - 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "横屏点击线数线注设置面板的 - 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, False, "横屏点击线数线注设置面板的 - 按钮，线注是最小值，线注 - 按钮可以点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线注是最小值，线注 + 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_setting_btn_visible_portrait(self):
        """ 竖屏显示线数线注设置按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        # 显示
        setting_btn = self.common.setting_btn_visible()
        # 能否点击
        setting_btn_touchable = self.common.setting_btn_touchable()
        try:
            self.assertEqual(setting_btn, True, "竖屏没有显示线数线注设置按钮！")
            self.assertEqual(setting_btn_touchable, True, "竖屏线数线注设置按钮无法点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_setting_btn_click_show_view_portrait(self):
        """ 竖屏点击线数线注设置按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        showing = self.common.setting_view_showing()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏点击线数线注设置按钮，不会弹出对应的面板！")
            self.assertEqual(mask, True, "竖屏点击线数线注设置按钮，不会显示灰色蒙板！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_click_mask_setting_view_dispear_portrait(self):
        """ 竖屏点击蒙板可以关闭面板 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.mask_view_click()
        sleep(1)
        dispear = self.common.setting_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "竖屏点击灰色蒙板，线数线注设置面板不会消失！")
            self.assertEqual(mask, False, "竖屏点击灰色蒙板，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_click_close_btn_view_dispear_portrait(self):
        """ 竖屏点击关闭按钮面板消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.setting_view_close_btn_click()
        sleep(1)
        dispear = self.common.setting_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "竖屏点击线数线注设置面板的关闭按钮，面板不会消失！")
            self.assertEqual(mask, False, "竖屏点击线数线注设置面板的关闭按钮，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_portrait(self):
        """ 竖屏面板线数标题文字按钮 """
        if self.full_line is False:
            self.common.portrait()
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)
            # 文本
            line_num_text = self.common.setting_view_line_num_text()
            current_line_num = self.common.setting_view_line_num()
            target_line_num = str(self.common.line_num_max)
            info_bar_line_num = self.common.info_bar_view_line_num_label()
            # 显示
            line_num_min_btn = self.common.setting_view_line_num_min_btn_visible()
            line_num_plus_btn = self.common.setting_view_line_num_plus_btn_visible()
            # 能否点击
            line_num_min_btn_touchable = self.common.setting_view_line_num_min_btn_touchable()
            line_num_plus_btn_touchable = self.common.setting_view_line_num_plus_btn_touchable()
            try:
                self.assertEqual(line_num_text, "线", "竖屏线数线注设置面板，线数的标题错误！")
                self.assertEqual(current_line_num, target_line_num, "竖屏线数线注设置面板，默认显示的线数不是最大值！")
                self.assertEqual(info_bar_line_num, current_line_num, "竖屏线数线注设置面板，线数数值与下导航栏的不一致！")
                self.assertEqual(line_num_min_btn, True, "竖屏线数线注设置面板，不会显示线数 - 按钮！")
                self.assertEqual(line_num_min_btn_touchable, True, "竖屏线数线注设置面板，线数 - 按钮默认不能点击！")
                self.assertEqual(line_num_plus_btn, True, "竖屏线数线注设置面板，不会显示线数 + 按钮！")
                self.assertEqual(line_num_plus_btn_touchable, False, "竖屏线数线注设置面板，线数 + 按钮默认可以点击！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_min_btn_click_portrait(self):
        """ 竖屏面板线数 - 按钮点击 """
        if self.full_line is False:
            self.common.portrait()
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max
            for i in reversed(range(1, int(target_line_num))):
                self.common.setting_view_line_num_min_btn_click()
                sleep(1)
                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i > 1:
                    try:
                        self.assertEqual(current_line_num, str(i), "竖屏点击线数线注设置面板的 - 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "竖屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "竖屏点击线数线注设置面板的 - 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "竖屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, False, "竖屏点击线数线注设置面板的 - 按钮，线数是最小值，- 按钮可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_plus_btn_click_portrait(self):
        """ 竖屏面板线数 + 按钮点击 """
        if self.full_line is False:
            self.common.portrait()
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max

            for i in range(1, int(target_line_num)):
                self.common.setting_view_line_num_min_btn_click()

            sleep(1)

            for i in range(2, int(target_line_num)+1):
                self.common.setting_view_line_num_plus_btn_click()
                sleep(1)
                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i < int(target_line_num):
                    try:
                        self.assertEqual(current_line_num, str(i), "竖屏点击线数线注设置面板的 + 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "竖屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "竖屏点击线数线注设置面板的 + 按钮，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "竖屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, False, "竖屏点击线数线注设置面板的 + 按钮，线数是最大值，+ 按钮可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    def test_setting_view_btn_status_portrait(self):
        """ 竖屏面板按钮状态 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        # 文本
        line_cost_text = self.common.setting_view_line_cost_text()

        current_line_cost = self.common.setting_view_line_cost()
        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[0]/100, 1)
        info_bar_line_cost = self.common.info_bar_view_line_cost_label()

        # 显示
        close_btn = self.common.setting_view_close_btn_visible()
        line_cost_min_btn = self.common.setting_view_line_cost_min_btn_visible()
        line_cost_plus_btn = self.common.setting_view_line_cost_plus_btn_visible()

        # 能否点击
        close_btn_touchable = self.common.setting_view_close_btn_touchable()
        line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
        line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()
        try:
            self.assertEqual(close_btn, True, "竖屏线数线注设置面板不会显示关闭按钮！")
            self.assertEqual(close_btn_touchable, True, "竖屏线数线注设置面板，关闭按钮不能点击！")
            self.assertEqual(line_cost_text, "线注", "竖屏线数线注设置面板，线注的标题错误！")
            self.assertEqual(current_line_cost, target_line_cost, "竖屏线数线注设置面板，默认显示的线注不是最小值！")
            self.assertEqual(info_bar_line_cost, current_line_cost, "竖屏线数线注设置面板，线注数值与下导航栏的不一致！")
            self.assertEqual(line_cost_min_btn, True, "竖屏线数线注设置面板，不会显示线注 - 按钮！")
            self.assertEqual(line_cost_min_btn_touchable, False, "竖屏线数线注设置面板，线注 - 按钮默认可以点击！")
            self.assertEqual(line_cost_plus_btn, True, "竖屏线数线注设置面板，不会显示线注 + 按钮！")
            self.assertEqual(line_cost_plus_btn_touchable, True, "竖屏线数线注设置面板，线注 + 按钮默认不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_line_cost_plus_btn_click_portrait(self):
        """ 竖屏面板线注 + 按钮点击 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)
        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)
            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i < (cost_len - 1):
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "竖屏点击线数线注设置面板的 + 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "竖屏点击线数线注设置面板的 + 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "竖屏点击线数线注设置面板的 + 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "竖屏点击线数线注设置面板的 + 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "竖屏点击线数线注设置面板的 + 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, False, "竖屏点击线数线注设置面板的 + 按钮，线注是最大值，线注 + 按钮可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_line_cost_min_btn_click_portrait(self):
        """ 竖屏面板线注 - 按钮点击 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)

        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()

        sleep(1)

        for i in reversed(range(cost_len - 1)):
            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)
            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i > 0:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "竖屏点击线数线注设置面板的 - 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "竖屏点击线数线注设置面板的 - 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "竖屏点击线数线注设置面板的 - 按钮，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "竖屏点击线数线注设置面板的 - 按钮，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, False, "竖屏点击线数线注设置面板的 - 按钮，线注是最小值，线注 - 按钮可以点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "竖屏点击线数线注设置面板的 - 按钮，线注是最小值，线注 + 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_setting_btn_visible_switch_screen(self):
        """ 横竖屏线数线注按钮显示 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        visible = self.common.setting_btn_visible()
        try:
            self.assertEqual(visible, True, "横竖屏切换，没有显示线数线注设置按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_show_view_switch_screen(self):
        """ 横竖屏弹出设置面板 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        showing = self.common.setting_view_showing()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(showing, True, "横竖屏切换，线数线注设置面板显示不正常！")
            self.assertEqual(mask, True, "横竖屏切换，灰色蒙板显示不正常！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_setting_view_dispear_switch_screen(self):
        """ 横竖屏点击蒙板可以关闭面板 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.mask_view_click()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        dispear = self.common.setting_view_dispear()
        mask = self.common.mask_view_showing()
        try:
            self.assertEqual(dispear, None, "点击蒙板关闭线数线注设置面板后，横竖屏切换，面板不会消失！")
            self.assertEqual(mask, False, "点击蒙板关闭线数线注设置面板后，横竖屏切换，灰色蒙板不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_switch_screen(self):
        """ 横竖屏面板线数标题文字按钮 """
        if self.full_line is False:
            self.common.portrait()
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)
            self.common.landscape()
            sleep(1)
            self.common.portrait()
            sleep(1)
            line_num_text = self.common.setting_view_line_num_text()
            current_line_num = self.common.setting_view_line_num()
            target_line_num = str(self.common.line_num_max)
            info_bar_line_num = self.common.info_bar_view_line_num_label()
            line_num_min_btn = self.common.setting_view_line_num_min_btn_visible()
            line_num_plus_btn = self.common.setting_view_line_num_plus_btn_visible()
            try:
                self.assertEqual(line_num_text, "线", "横竖屏切换，设置面板线数的标题错误！")
                self.assertEqual(current_line_num, target_line_num, "横竖屏切换，默认显示的线数不是最大值！")
                self.assertEqual(info_bar_line_num, current_line_num, "横竖屏切换，线数数值与下导航栏的不一致！")
                self.assertEqual(line_num_min_btn, True, "横竖屏切换，不会显示线数 - 按钮！")
                self.assertEqual(line_num_plus_btn, True, "横竖屏切换，不会显示线数 + 按钮！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_min_btn_click_switch_screen(self):
        """ 横竖屏面板线数 - 按钮点击 """
        if self.full_line is False:
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max
            for i in reversed(range(1, int(target_line_num))):
                self.common.setting_view_line_num_min_btn_click()
                sleep(1)

                if i % 2 == 0:
                    self.common.portrait()
                else:
                    self.common.landscape()

                sleep(1)

                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i > 1:
                    try:
                        self.assertEqual(current_line_num, str(i), "点击线数线注设置面板的 - 按钮，横竖屏切换，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "点击线数线注设置面板的 - 按钮，横竖屏切换，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "点击线数线注设置面板的 - 按钮，横竖屏切换，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "点击线数线注设置面板的 - 按钮，横竖屏切换，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, False, "点击线数线注设置面板的 - 按钮，横竖屏切换，线数是最小值，- 按钮可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_plus_btn_click_switch_screen(self):
        """ 横竖屏面板线数 + 按钮点击 """
        if self.full_line is False:
            self.common.loading_pass()
            sleep(1)
            self.common.setting_btn_click()
            sleep(1)

            target_line_num = self.common.line_num_max

            for i in range(1, int(target_line_num)):
                self.common.setting_view_line_num_min_btn_click()

            sleep(1)

            for i in range(2, int(target_line_num)+1):
                self.common.setting_view_line_num_plus_btn_click()
                sleep(1)

                if i % 2 == 0:
                    self.common.portrait()
                else:
                    self.common.landscape()

                sleep(1)

                current_line_num = self.common.setting_view_line_num()
                info_bar_line_num = self.common.info_bar_view_line_num_label()
                line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
                line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
                if i < int(target_line_num):
                    try:
                        self.assertEqual(current_line_num, str(i), "点击线数线注设置面板的 + 按钮，横竖屏切换，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "点击线数线注设置面板的 + 按钮，横竖屏切换，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线数不是最大值，+ 按钮不可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise
                else:
                    try:
                        self.assertEqual(current_line_num, str(i), "点击线数线注设置面板的 + 按钮，横竖屏切换，线数错误！")
                        self.assertEqual(info_bar_line_num, current_line_num, "点击线数线注设置面板的 + 按钮，横竖屏切换，面板线数与下导航栏的线数不一致！")
                        self.assertEqual(line_num_min_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线数不是最小值，- 按钮不可以点击！")
                        self.assertEqual(line_num_plus_touchable, False, "点击线数线注设置面板的 + 按钮，横竖屏切换，线数是最大值，+ 按钮可以点击！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

    def test_setting_view_btn_switch_screen(self):
        """ 横竖屏面板线注标题文字 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        view_line_cost_text = self.common.setting_view_line_cost_text()

        current_line_cost = self.common.setting_view_line_cost()
        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[0]/100, 1)
        info_bar_line_cost = self.common.info_bar_view_line_cost_label()

        line_cost_min_btn = self.common.setting_view_line_cost_min_btn_visible()
        line_cost_plus_btn = self.common.setting_view_line_cost_plus_btn_visible()
        try:
            self.assertEqual(view_line_cost_text, "线注", "横竖屏切换，线注的标题错误！")
            self.assertEqual(current_line_cost, target_line_cost, "横竖屏切换，默认显示的线注不是最小值！")
            self.assertEqual(info_bar_line_cost, current_line_cost, "横竖屏切换，线注数值与下导航栏的不一致！")
            self.assertEqual(line_cost_min_btn, True, "横竖屏切换，不会显示线注 - 按钮！")
            self.assertEqual(line_cost_plus_btn, True, "横竖屏切换，不会显示线注 + 按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_line_cost_plus_btn_click_switch_screen(self):
        """ 横竖屏面板线注 + 按钮点击 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)
        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)

            if i % 2 == 0:
                self.common.landscape()
            else:
                self.common.portrait()

            sleep(1)

            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i < (cost_len - 1):
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "点击线数线注设置面板的 + 按钮，横竖屏切换，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "点击线数线注设置面板的 + 按钮，横竖屏切换，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, False, "点击线数线注设置面板的 + 按钮，横竖屏切换，线注是最大值，线注 + 按钮可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    def test_line_cost_min_btn_click_switch_screen(self):
        """ 横竖屏面板线注 - 按钮点击 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        cost_len = len(self.common.line_cost)

        for i in range(1, cost_len):
            self.common.setting_view_line_cost_plus_btn_click()

        sleep(1)

        for i in reversed(range(cost_len - 1)):
            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)

            if i % 2 == 0:
                self.common.landscape()
            else:
                self.common.portrait()

            sleep(1)

            current_line_cost = self.common.setting_view_line_cost()
            target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[i]/100, 1)
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            line_cost_min_btn_touchable = self.common.setting_view_line_cost_min_btn_touchable()
            line_cost_plus_btn_touchable = self.common.setting_view_line_cost_plus_btn_touchable()

            if i > 0:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "点击线数线注设置面板的 - 按钮，横竖屏切换，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注不是最小值，线注 - 按钮不能点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注不是最大值，线注 + 按钮不能点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_cost, target_line_cost, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注错误！")
                    self.assertEqual(info_bar_line_cost, current_line_cost, "点击线数线注设置面板的 - 按钮，横竖屏切换，面板线注与下导航栏的不一致！")
                    self.assertEqual(line_cost_min_btn_touchable, False, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注是最小值，线注 - 按钮可以点击！")
                    self.assertEqual(line_cost_plus_btn_touchable, True, "点击线数线注设置面板的 - 按钮，横竖屏切换，线注是最小值，线注 + 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
