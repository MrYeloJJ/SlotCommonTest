# coding=utf-8

""""" 线数、线注设置验证 """""

import unittest
import locale
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestSettingView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    # 初始化满线参数 True, False
    full_line = Common().full_line

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    # 验证横屏 显示线数线注设置按钮
    def test_setting_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.setting_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏没有显示线数线注设置按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 线数线注设置按钮可点击否
    def test_setting_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.setting_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏线数线注设置按钮无法点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 点击线数线注设置按钮，弹出设置面板
    def test_setting_btn_click_show_view(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
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

    # 验证横屏 弹出设置面板后，点击蒙板可以关闭蒙板
    def test_click_mask_setting_view_dispear(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
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

    # 验证横屏 设置面板显示关闭按钮
    def test_setting_view_close_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        visible = self.common.setting_view_close_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏线数线注设置面板不会显示关闭按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板关闭按钮可点击否
    def test_setting_view_close_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        touchable = self.common.setting_view_close_btn_visible()
        try:
            self.assertEqual(touchable, True, "横屏线数线注设置面板，关闭按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板点击关闭按钮，设置面板消失
    def test_setting_view_click_close_btn_view_dispear(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
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

    # 验证横屏 设置面板线数标题文字
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_text(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        text = self.common.setting_view_line_num_text()
        try:
            self.assertEqual(text, "线", "横屏线数线注设置面板，线数的标题错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板默认的线数数值
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_default_line_num(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        current_line_num = self.common.setting_view_line_num()
        target_line_num = str(self.common.line_num_max)
        info_bar_line_num = self.common.info_bar_view_line_num_label()
        try:
            self.assertEqual(current_line_num, target_line_num, "横屏线数线注设置面板，默认显示的线数不是最大值！")
            self.assertEqual(info_bar_line_num, current_line_num, "横屏线数线注设置面板，线数数值与下导航栏的不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线数 - 按钮显示
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_min_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        visible = self.common.setting_view_line_num_min_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏线数线注设置面板，不会显示线数 - 按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线数 - 按钮默认可点击否
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_min_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        touchable = self.common.setting_view_line_num_min_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏线数线注设置面板，线数 - 按钮默认不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置按钮线数 + 按钮显示
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_plus_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        visible = self.common.setting_view_line_num_plus_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏线数线注设置面板，不会显示线数 + 按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线数 + 按钮默认可点击否
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_plus_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        touchable = self.common.setting_view_line_num_plus_btn_touchable()
        try:
            self.assertEqual(touchable, False, "横屏线数线注设置面板，线数 + 按钮默认可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线数 - 按钮点击，显示正确
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_min_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        target_line_num = self.common.line_num_max
        for i in reversed(range(int(target_line_num), 1)):
            self.common.setting_view_line_num_min_btn_click()
            sleep(1)
            current_line_num = self.common.setting_view_line_num()
            info_bar_line_num = self.common.info_bar_view_line_num_label()
            line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
            line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
            if i > 1:
                try:
                    self.assertEqual(current_line_num, i, "横屏点击线数线注设置面板的 - 按钮，线数错误！")
                    self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                    self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最小值，- 按钮不可以点击！")
                    self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_num, i, "横屏点击线数线注设置面板的 - 按钮，线数错误！")
                    self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 - 按钮，面板线数与下导航栏的线数不一致！")
                    self.assertEqual(line_num_min_touchable, False, "横屏点击线数线注设置面板的 - 按钮，线数是最小值，- 按钮可以点击！")
                    self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 - 按钮，线数不是最大值，+ 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    # 验证横屏 设置面板线数 + 按钮点击，显示正确
    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_setting_view_line_num_plus_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)

        target_line_num = self.common.line_num_max

        for i in range(1, int(target_line_num)):
            self.common.setting_view_line_num_min_btn_click()

        sleep(1)

        for i in range(2, int(target_line_num)):
            self.common.setting_view_line_num_plus_btn_click()
            sleep(1)
            line_num = i
            current_line_num = self.common.setting_view_line_num()
            info_bar_line_num = self.common.info_bar_view_line_num_label()
            line_num_min_touchable = self.common.setting_view_line_num_min_btn_touchable()
            line_num_plus_touchable = self.common.setting_view_line_num_plus_btn_touchable()
            if line_num < int(target_line_num):
                try:
                    self.assertEqual(current_line_num, str(line_num), "横屏点击线数线注设置面板的 + 按钮，线数错误！")
                    self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                    self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                    self.assertEqual(line_num_plus_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最大值，+ 按钮不可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise
            else:
                try:
                    self.assertEqual(current_line_num, str(line_num), "横屏点击线数线注设置面板的 + 按钮，线数错误！")
                    self.assertEqual(info_bar_line_num, current_line_num, "横屏点击线数线注设置面板的 + 按钮，面板线数与下导航栏的线数不一致！")
                    self.assertEqual(line_num_min_touchable, True, "横屏点击线数线注设置面板的 + 按钮，线数不是最小值，- 按钮不可以点击！")
                    self.assertEqual(line_num_plus_touchable, False, "横屏点击线数线注设置面板的 + 按钮，线数是最大值，+ 按钮可以点击！")
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise

    # 验证横屏 设置面板线注标题文字
    def test_setting_view_line_cost_text(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        text = self.common.setting_view_line_cost_text()
        try:
            self.assertEqual(text, "线注", "横屏线数线注设置面板，线注的标题错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板默认的线注数值
    def test_setting_view_default_line_cost(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        current_line_cost = self.common.setting_view_line_cost()

        # 转化为货币格式
        locale.setlocale(locale.LC_ALL, "")
        target_line_cost = "¥" + locale.format("%.2f", self.common.line_cost[0]/100, 1)
        info_bar_line_cost = self.common.info_bar_view_line_cost_label()
        try:
            self.assertEqual(current_line_cost, target_line_cost, "横屏线数线注设置面板，默认显示的线注不是最小值！")
            self.assertEqual(info_bar_line_cost, current_line_cost, "横屏线数线注设置面板，线注数值与下导航栏的不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线注 - 按钮显示
    def test_setting_view_line_cost_min_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        visible = self.common.setting_view_line_cost_min_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏线数线注设置面板，不会显示线注 - 按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线注 - 按钮默认可点击否
    def test_setting_view_line_cost_min_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        touchable = self.common.setting_view_line_cost_min_btn_touchable()
        try:
            self.assertEqual(touchable, False, "横屏线数线注设置面板，线注 - 按钮默认可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置按钮线注 + 按钮显示
    def test_setting_view_line_cost_plus_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        visible = self.common.setting_view_line_cost_plus_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏线数线注设置面板，不会显示线注 + 按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线注 + 按钮默认可点击否
    def test_setting_view_line_cost_plus_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.setting_btn_click()
        sleep(1)
        touchable = self.common.setting_view_line_cost_plus_btn_touchable()
        try:
            self.assertEqual(touchable, False, "横屏线数线注设置面板，线注 + 按钮默认不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏 设置面板线注 + 按钮点击，显示正确
    def test_setting_view_line_cost_plus_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
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

    # 验证横屏 设置面板线注 - 按钮点击，显示正确
    def test_setting_view_line_cost_min_btn_click(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
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














































if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
