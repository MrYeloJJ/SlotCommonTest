# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestReward(unittest.TestCase):
    """ 元素中奖奖金测试 """

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.full_line = self.common.full_line
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    def test_reward(self):
        if self.full_line:
            pass
        else:
            pass


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
