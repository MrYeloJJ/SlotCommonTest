# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestGameAttr(unittest.TestCase):
    """ 游戏基本属性模块 """

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()
        self.common.loading_pass()

    def tearDown(self):
        self.browser.quit()

    # 初始化满线参数 True, False
    full_line = Common().full_line

    def test_game_id(self):
        """ 游戏id """
        sleep(1)
        current_game_id = self.common.get_game_id()
        target_game_id = self.common.game_id
        try:
            self.assertEqual(current_game_id, target_game_id, "游戏ID错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_game_name(self):
        """ 游戏名字 """
        sleep(1)
        current_game_name = self.common.get_game_name()
        target_game_name = self.common.game_name
        try:
            self.assertEqual(current_game_name, target_game_name, "游戏名字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_min_line_num(self):
        """ 最小线数 """
        sleep(1)
        current_min_line_num = self.common.get_min_line_num()
        target_min_line_num = self.common.line_num_min
        try:
            self.assertEqual(current_min_line_num, target_min_line_num, "最小线数配置错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    @unittest.skipIf(full_line is True, "满线项目不测试线数设置")
    def test_max_line_num(self):
        """ 最大线数 """
        sleep(1)
        current_max_line_num = self.common.get_max_line_num()
        target_max_line_num = self.common.line_num_max
        try:
            self.assertEqual(current_max_line_num, target_max_line_num, "最大线数配置错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_line_cost(self):
        """ 线注 """
        sleep(1)
        current_line_cost = self.common.get_line_cost_list()
        target_line_cost = self.common.line_cost
        try:
            self.assertEqual(current_line_cost, target_line_cost, "线注不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_game_times(self):
        """ 自动次数 """
        sleep(1)
        current_auto_game_times = self.common.get_auto_game_times_list()
        target_auto_game_times = self.common.auto_game_times
        try:
            self.assertEqual(current_auto_game_times, target_auto_game_times, "自动次数不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
