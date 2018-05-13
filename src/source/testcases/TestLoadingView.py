# coding=utf-8

import unittest
from time import sleep
from datetime import datetime
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestLoadingView(unittest.TestCase):
    """ 载入场景模块 """

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

    def test_loading_view_showing(self):
        """ 横屏进入载入场景 """
        self.common.wait_for_loading_view_showing()
        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "横屏没有进入载入场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_view_ui_showing(self):
        """ 横屏显示logo、进度条、版本号 """
        self.common.wait_for_loading_view_showing()
        bg = self.common.loading_view_background_visible()
        # G2E loading 图没有logo
        # logo = self.common.loading_view_logo_visible()
        progress_title = self.common.loading_view_progress_title_visible()
        progress_bar = self.common.loading_view_progress_bar_visible()
        version = self.common.loading_view_version_visible()
        try:
            self.assertEqual(bg, True, "横屏载入场景没有显示背景图片！")
            # self.assertEqual(logo, True, "横屏载入场景没有显示logo！")
            self.assertEqual(progress_title, True, "横屏载入场景没有显示当前进度百分比！")
            self.assertEqual(progress_bar, True, "横屏载入场景没有显示进度条！")
            self.assertEqual(version, True, "横屏载入场景没有显示版本号！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_progress_bar_is_loading(self):
        """ 横屏进度条会走动 """
        self.common.wait_for_loading_view_showing()

        title_value1 = self.common.loading_view_progress_title_value()
        bar_value1 = self.common.loading_view_progress_bar_value()

        self.common.wait_for_loading_bar_completed()

        title_value2 = self.common.loading_view_progress_title_value()
        bar_value2 = self.common.loading_view_progress_bar_value()

        try:
            self.assertNotEqual(title_value1, title_value2, "横屏载入场景百分比数值不会变！")
            self.assertNotEqual(bar_value1, bar_value2, "横屏载入场景进度条不会动！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_bar_complete(self):
        """ 横屏进度条走完是100% """
        self.common.wait_for_loading_view_showing()
        start_time = datetime.now()
        while True:
            bar_value = self.common.loading_view_progress_bar_value()
            title_value = self.common.loading_view_progress_title_value()

            end_time = datetime.now()
            cost_time = (end_time - start_time).seconds
            if bar_value == 100:
                cost_time = True
                break
            else:
                if cost_time >= 15:
                    cost_time = False
                    break

        try:
            self.assertEqual(cost_time, True, "横屏等待15秒，进度条不会走满！")
            self.assertEqual(title_value, "100%", "横屏进度条走满后，百分比不是100%！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_view_dispear(self):
        """ 横屏在进度条100%后载入消失 """
        self.common.loading_pass()
        sleep(3)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "横屏载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_loading_view_showing_portrait(self):
        """ 竖屏进入载入场景 """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()
        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏没有进入载入场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_view_ui_showing_portrait(self):
        """ 竖屏显示logo、进度条、版本号 """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()
        bg = self.common.loading_view_background_visible()
        # G2E loading 图没有logo
        # logo = self.common.loading_view_logo_visible()
        progress_title = self.common.loading_view_progress_title_visible()
        progress_bar = self.common.loading_view_progress_bar_visible()
        version = self.common.loading_view_version_visible()
        try:
            self.assertEqual(bg, True, "竖屏载入场景没有显示背景图片！")
            # self.assertEqual(logo, True, "竖屏载入场景没有显示logo！")
            self.assertEqual(progress_title, True, "竖屏载入场景没有显示当前进度百分比！")
            self.assertEqual(progress_bar, True, "竖屏载入场景没有显示进度条！")
            self.assertEqual(version, True, "竖屏载入场景没有显示版本号！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_progress_bar_is_loading_portrait(self):
        """ 竖屏进度条会走动 """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()

        title_value1 = self.common.loading_view_progress_title_value()
        bar_value1 = self.common.loading_view_progress_bar_value()

        self.common.wait_for_loading_bar_completed()

        title_value2 = self.common.loading_view_progress_title_value()
        bar_value2 = self.common.loading_view_progress_bar_value()

        try:
            self.assertNotEqual(title_value1, title_value2, "竖屏载入场景百分比数值不会变！")
            self.assertNotEqual(bar_value1, bar_value2, "竖屏载入场景进度条不会动！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_bar_complete_portrait(self):
        """ 竖屏载入场景进度条走完是100% """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()
        start_time = datetime.now()
        while True:
            bar_value = self.common.loading_view_progress_bar_value()
            title_value = self.common.loading_view_progress_title_value()

            end_time = datetime.now()
            cost_time = (end_time - start_time).seconds
            if bar_value == 100:
                cost_time = True
                break
            else:
                if cost_time >= 15:
                    cost_time = False
                    break

        try:
            self.assertEqual(cost_time, True, "竖屏等待15秒，进度条不会走满！")
            self.assertEqual(title_value, "100%", "竖屏进度条走满后，百分比不是100%！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_view_dispear_portrait(self):
        """ 竖屏进度条100%后载入消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "竖屏载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_loading_view_showing_switch_screen(self):
        """ 横竖屏显示logo、进度条、版本号 """
        self.common.portrait()
        self.common.landscape()
        self.common.wait_for_loading_view_showing()
        bg = self.common.loading_view_background_visible()
        # G2E loading 图没有logo
        # logo = self.common.loading_view_logo_visible()
        progress_title = self.common.loading_view_progress_title_visible()
        progress_bar = self.common.loading_view_progress_bar_visible()
        version = self.common.loading_view_version_visible()
        try:
            self.assertEqual(bg, True, "横竖屏切换，载入场景没有显示背景图片！")
            # self.assertEqual(logo, True, "横竖屏切换，载入场景没有显示logo！")
            self.assertEqual(progress_title, True, "横竖屏切换，载入场景没有显示当前进度百分比！")
            self.assertEqual(progress_bar, True, "横竖屏切换，载入场景没有显示进度条！")
            self.assertEqual(version, True, "横竖屏切换，载入场景没有显示版本号！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_progress_bar_is_loading_switch_screen(self):
        """ 横竖屏进度条会走动 """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()

        title_value1 = self.common.loading_view_progress_title_value()
        bar_value1 = self.common.loading_view_progress_bar_value()

        self.common.landscape()
        self.common.wait_for_loading_bar_completed()

        title_value2 = self.common.loading_view_progress_title_value()
        bar_value2 = self.common.loading_view_progress_bar_value()

        try:
            self.assertNotEqual(title_value1, title_value2, "横竖屏切换，载入场景百分比数值不会变！")
            self.assertNotEqual(bar_value1, bar_value2, "横竖屏切换，载入场景进度条不会动！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_loading_view_dispear_switch_screen(self):
        """ 横竖屏载入场景进度条100%后消失 """
        self.common.portrait()
        self.common.wait_for_loading_view_showing()
        sleep(1)
        self.common.landscape()
        self.common.wait_for_loading_view_dispear()
        sleep(1)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "横竖屏切换，载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
