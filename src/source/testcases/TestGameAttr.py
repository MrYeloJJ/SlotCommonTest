# coding=utf-8

""""" 游戏基本属性验证 """""

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
        self.common.loading_bar()

    def tearDown(self):
        self.browser.quit()

    # 验证游戏id
    def test_game_id(self):
        sleep(1)
        current_game_id = self.common.get_game_id()
        target_game_id = self.common.game_id
        try:
            self.assertEqual(current_game_id, target_game_id, "游戏ID错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_game_name(self):
        """ 验证游戏名字 """
        sleep(1)
        current_game_name = self.common.get_game_name()
        target_game_name = self.common.game_name
        try:
            self.assertEqual(current_game_name, target_game_name, "游戏名字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_min_line_num(self):
        """ 验证最小线数 """
        sleep(1)
        current_min_line_num = self.common.get_min_line_num()
        target_min_line_num = self.common.line_num_min
        try:
            self.assertEqual(current_min_line_num, target_min_line_num, "最小线数配置错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_max_line_num(self):
        """ 验证最大线数 """
        sleep(1)
        current_max_line_num = self.common.get_max_line_num()
        target_max_line_num = self.common.line_num_max
        try:
            self.assertEqual(current_max_line_num, target_max_line_num, "最大线数配置错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_line_cost(self):
        """ 验证线注 """
        sleep(1)
        current_line_cost = self.common.get_line_cost_list()
        target_line_cost = self.common.line_cost
        try:
            self.assertEqual(current_line_cost, target_line_cost, "线注不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_auto_game_times(self):
        """ 验证自动次数 """
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
