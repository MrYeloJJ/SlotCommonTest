# coding=utf-8

import unittest
from time import sleep
from server.automaticTest.slot.source.common.Browser import Browser
from server.automaticTest.slot.source.common.Common import Common
from server.automaticTest.slot.lib.HTMLTestReportCN import DirAndFiles


class TestMainAndComView(unittest.TestCase):
    """ 主场景视图模块 """

    def setUp(self):
        self.browser = Browser().browser()
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    def test_main_scence_visible(self):
        """ 横屏显示主场景 """
        self.common.loading_pass()

        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "横屏没有显示主视图！")
            self.assertEqual(common_view, True, "横屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "横屏没有显示滚轴！")
            self.assertEqual(bg_view, True, "横屏没有显示背景图片！")
            self.assertEqual(bottom_bg_view, False, "横屏会显示竖屏背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_main_scence_in_portrait(self):
        """ 竖屏显示主场景 """
        self.common.portrait()
        self.common.loading_pass()

        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "竖屏没有显示主视图！")
            self.assertEqual(common_view, True, "竖屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "竖屏没有显示滚轴！")
            self.assertEqual(bg_view, False, "竖屏会显示横屏背景图片！")
            self.assertEqual(bottom_bg_view, True, "竖屏没有显示背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_main_scence_landscape_switch_screen(self):
        """ 横竖屏主场景显示正常 """
        self.common.loading_pass()

        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "横屏没有显示主视图！")
            self.assertEqual(common_view, True, "横屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "横屏没有显示滚轴！")
            self.assertEqual(bg_view, True, "横屏没有显示背景图片！")
            self.assertEqual(bottom_bg_view, False, "横屏会显示竖屏背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.portrait()
        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "竖屏没有显示主视图！")
            self.assertEqual(common_view, True, "竖屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "竖屏没有显示滚轴！")
            self.assertEqual(bg_view, False, "竖屏会显示横屏背景图片！")
            self.assertEqual(bottom_bg_view, True, "竖屏没有显示背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_main_scence_portrait_switch_screen(self):
        """ 横竖屏主场景显示正常 """
        self.common.portrait()
        self.common.loading_pass()

        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "竖屏没有显示主视图！")
            self.assertEqual(common_view, True, "竖屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "竖屏没有显示滚轴！")
            self.assertEqual(bg_view, False, "竖屏会显示横屏背景图片！")
            self.assertEqual(bottom_bg_view, True, "竖屏没有显示背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

        self.common.landscape()
        sleep(1)
        main_view = self.common.main_view_visible()
        common_view = self.common.common_view_visible()
        slot_machine_view = self.common.slot_machine_view_visible()
        bg_view = self.common.bg_view_visible()
        bottom_bg_view = self.common.bottom_bg_view_visible()

        try:
            self.assertEqual(main_view, True, "横屏没有显示主视图！")
            self.assertEqual(common_view, True, "横屏没有显示公共视图！")
            self.assertEqual(slot_machine_view, True, "横屏没有显示滚轴！")
            self.assertEqual(bg_view, True, "横屏没有显示背景图片！")
            self.assertEqual(bottom_bg_view, False, "横屏会显示竖屏背景图片！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
