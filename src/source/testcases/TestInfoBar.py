# coding=utf-8

import unittest
import locale
from time import sleep
from src.source.common.Browser import Browser
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestInfoBar(unittest.TestCase):
    """ 下导航栏模块 """

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

    def test_info_bar_default(self):
        """ 横屏下导航栏内容 """
        self.common.loading_pass()
        sleep(3)
        locale.setlocale(locale.LC_ALL, "")

        # 目标线注
        line_cost = self.common.line_cost[0] / 100
        target_line_cost = "¥" + locale.format("%.2f", line_cost, 1)

        banner_tips = self.common.info_bar_view_banner_tips_label()
        has_money_title = self.common.info_bar_view_has_money_title()
        has_money = self.common.info_bar_view_has_money_label()
        line_num_title = self.common.info_bar_view_line_num_title()
        line_num = self.common.info_bar_view_line_num_label()
        line_cost_title = self.common.info_bar_view_line_cost_title()
        line_cost = self.common.info_bar_view_line_cost_label()
        bet_money_title = self.common.info_bar_view_bet_money_title()
        bet_money = self.common.info_bar_view_bet_money_label()

        if self.full_line is False:
            # 目标线数
            target_line_num = self.common.line_num_max
            bet = target_line_num * eval(line_cost[1:])
            try:
                self.assertEqual(line_num_title, "线", "横屏试玩下导航栏线数标题文字错误！")
                self.assertEqual(line_num, str(target_line_num), "横屏试玩下导航栏默认线数数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise
        else:
            bet = self.common.full_line_mulitiplier * eval(line_cost[1:])

        # 目标总赌注
        target_bet_money = "¥" + locale.format("%.2f", bet, 1)

        try:
            self.assertEqual(banner_tips, "滑动转轴或按旋转", "横屏下导航栏默认提示文字错误！")
            self.assertEqual(has_money_title, "试玩余额", "横屏试玩下导航栏余额标题文字错误！")
            self.assertEqual(has_money, "¥2,000.00", "横屏试玩下导航栏余额数值错误！")
            self.assertEqual(line_cost_title, "线注", "横屏试玩下导航栏线注标题错误！")
            self.assertEqual(line_cost, target_line_cost, "横屏试玩下导航栏线注数值错误！")
            self.assertEqual(bet_money_title, "总赌注", "横屏试玩下导航栏总赌注标题文字错误！")
            self.assertEqual(bet_money, target_bet_money, "横屏试玩下导航栏总赌注数值错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_effect_bet_money(self):
        """ 横屏点击线数按钮后计算总赌注 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线数 - 按钮
        for i in range(3):
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "横屏点击线数 - 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "横屏点击线数 - 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横屏点击线数 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线数 + 按钮
        for i in range(3):
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "横屏点击线数 + 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "横屏点击线数 + 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横屏点击线数 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_line_cost_effect_bet_money(self):
        """ 横屏点击线注按钮后计算总赌注 """
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线注 + 按钮
        for i in range(3):
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])

            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "横屏点击线注 + 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "横屏点击线注 + 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横屏点击线注 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线注 - 按钮
        for i in range(3):
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "横屏点击线注 - 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "横屏点击线注 - 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横屏点击线注 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_info_bar_default_portrait(self):
        """ 竖屏下导航栏内容 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        locale.setlocale(locale.LC_ALL, "")

        # 目标线注
        line_cost = self.common.line_cost[0] / 100
        target_line_cost = "¥" + locale.format("%.2f", line_cost, 1)

        banner_tips = self.common.info_bar_view_banner_tips_label()
        has_money_title = self.common.info_bar_view_has_money_title()
        has_money = self.common.info_bar_view_has_money_label()
        line_num_title = self.common.info_bar_view_line_num_title()
        line_num = self.common.info_bar_view_line_num_label()
        line_cost_title = self.common.info_bar_view_line_cost_title()
        line_cost = self.common.info_bar_view_line_cost_label()
        bet_money_title = self.common.info_bar_view_bet_money_title()
        bet_money = self.common.info_bar_view_bet_money_label()

        if self.full_line is False:
            # 目标线数
            target_line_num = self.common.line_num_max
            bet = target_line_num * eval(line_cost[1:])
            try:
                self.assertEqual(line_num_title, "线", "竖屏试玩下导航栏线数标题文字错误！")
                self.assertEqual(line_num, str(target_line_num), "竖屏试玩下导航栏默认线数数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise
        else:
            bet = self.common.full_line_mulitiplier * eval(line_cost[1:])

        # 目标总赌注
        target_bet_money = "¥" + locale.format("%.2f", bet, 1)

        try:
            self.assertEqual(banner_tips, "滑动转轴或按旋转", "竖屏下导航栏默认提示文字错误！")
            self.assertEqual(has_money_title, "试玩余额", "竖屏试玩下导航栏余额标题文字错误！")
            self.assertEqual(has_money, "¥2,000.00", "竖屏试玩下导航栏余额数值错误！")
            self.assertEqual(line_cost_title, "线注", "竖屏试玩下导航栏线注标题错误！")
            self.assertEqual(line_cost, target_line_cost, "竖屏试玩下导航栏线注数值错误！")
            self.assertEqual(bet_money_title, "总赌注", "竖屏试玩下导航栏总赌注标题文字错误！")
            self.assertEqual(bet_money, target_bet_money, "竖屏试玩下导航栏总赌注数值错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_effect_bet_money_portrait(self):
        """ 竖屏点击线数按钮后计算总赌注 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线数 - 按钮
        for i in range(3):
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "竖屏点击线数 - 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "竖屏点击线数 - 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "竖屏点击线数 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线数 + 按钮
        for i in range(3):
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "竖屏点击线数 + 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "竖屏点击线数 + 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "竖屏点击线数 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_line_cost_effect_bet_money_portrait(self):
        """ 竖屏点击线注按钮后计算总赌注 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线注 + 按钮
        for i in range(3):
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])

            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "竖屏点击线注 + 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "竖屏点击线注 + 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "竖屏点击线注 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线注 - 按钮
        for i in range(3):
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])

            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "竖屏点击线注 - 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "竖屏点击线注 - 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "竖屏点击线注 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_info_bar_default_switch_screen(self):
        """ 横竖屏下导航栏内容 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 目标线注
        line_cost = self.common.line_cost[0] / 100
        target_line_cost = "¥" + locale.format("%.2f", line_cost, 1)

        banner_tips = self.common.info_bar_view_banner_tips_label()
        has_money_title = self.common.info_bar_view_has_money_title()
        has_money = self.common.info_bar_view_has_money_label()
        line_num_title = self.common.info_bar_view_line_num_title()
        line_num = self.common.info_bar_view_line_num_label()
        line_cost_title = self.common.info_bar_view_line_cost_title()
        line_cost = self.common.info_bar_view_line_cost_label()
        bet_money_title = self.common.info_bar_view_bet_money_title()
        bet_money = self.common.info_bar_view_bet_money_label()

        if self.full_line is False:
            # 目标线数
            target_line_num = self.common.line_num_max
            bet = target_line_num * eval(line_cost[1:])
            try:
                self.assertEqual(line_num_title, "线", "横竖屏切换，试玩下导航栏线数标题文字错误！")
                self.assertEqual(line_num, str(target_line_num), "横竖屏切换，试玩下导航栏默认线数数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise
        else:
            bet = self.common.full_line_mulitiplier * eval(line_cost[1:])

        # 目标总赌注
        target_bet_money = "¥" + locale.format("%.2f", bet, 1)

        try:
            self.assertEqual(banner_tips, "滑动转轴或按旋转", "横竖屏切换，下导航栏默认提示文字错误！")
            self.assertEqual(has_money_title, "试玩余额", "横竖屏切换，试玩下导航栏余额标题文字错误！")
            self.assertEqual(has_money, "¥2,000.00", "横竖屏切换，试玩下导航栏余额数值错误！")
            self.assertEqual(line_cost_title, "线注", "横竖屏切换，试玩下导航栏线注标题错误！")
            self.assertEqual(line_cost, target_line_cost, "横竖屏切换，试玩下导航栏线注数值错误！")
            self.assertEqual(bet_money_title, "总赌注", "横竖屏切换，试玩下导航栏总赌注标题文字错误！")
            self.assertEqual(bet_money, target_bet_money, "横竖屏切换，试玩下导航栏总赌注数值错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_line_num_effect_bet_money_switch_screen(self):
        """ 横竖屏点击线数按钮后计算总赌注 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线数 - 按钮
        for i in range(3):
            if i % 2 == 0:
                self.common.landscape()
            else:
                self.common.portrait()
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "横竖屏切换，点击线数 - 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "横竖屏切换，点击线数 - 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横竖屏切换，点击线数 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线数 + 按钮
        for i in range(3):
            if i % 2 == 0:
                self.common.portrait()
            else:
                self.common.landscape()
            target_line_cost = self.common.setting_view_line_cost()

            self.common.setting_view_line_num_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])
            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_num = self.common.setting_view_line_num()

            try:
                self.assertEqual(info_bar_line_cost, target_line_cost, "横竖屏切换，点击线数 + 按钮，线注会改变！")
                self.assertEqual(info_bar_line_num, target_line_num, "横竖屏切换，点击线数 + 按钮，设置窗口的线数与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横竖屏切换，点击线数 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

    def test_line_cost_effect_bet_money_switch_screen(self):
        """ 横竖屏点击线注按钮后计算总赌注 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        locale.setlocale(locale.LC_ALL, "")

        # 点击线注 + 按钮
        for i in range(3):
            if i % 2 == 0:
                self.common.landscape()
            else:
                self.common.portrait()
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_plus_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])

            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "横竖屏切换，点击线注 + 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "横竖屏切换，点击线注 + 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横竖屏切换，点击线注 + 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

        sleep(1)

        # 点击线注 - 按钮
        for i in range(3):
            if i % 2 == 0:
                self.common.portrait()
            else:
                self.common.landscape()
            target_line_num = self.common.setting_view_line_num()

            self.common.setting_view_line_cost_min_btn_click()
            sleep(1)

            info_bar_line_num = self.common.info_bar_view_line_num_label()
            info_bar_line_cost = self.common.info_bar_view_line_cost_label()
            info_bar_bet_money = self.common.info_bar_view_bet_money_label()

            if self.full_line:
                bet_money = self.common.full_line_mulitiplier * eval(info_bar_line_cost[1:])
            else:
                bet_money = eval(info_bar_line_num) * eval(info_bar_line_cost[1:])

            target_bet_money = "¥" + locale.format("%.2f", bet_money, 1)
            target_line_cost = self.common.setting_view_line_cost()

            try:
                self.assertEqual(info_bar_line_num, target_line_num, "横竖屏切换，点击线注 - 按钮，线数会改变！")
                self.assertEqual(info_bar_line_cost, target_line_cost, "横竖屏切换，点击线注 - 按钮，设置窗口的线注与下导航栏的不一致！")
                self.assertEqual(info_bar_bet_money, target_bet_money, "横竖屏切换，点击线注 - 按钮，总赌注数值错误！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
