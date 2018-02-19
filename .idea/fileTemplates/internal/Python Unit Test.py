# coding=utf-8

""""" XXX测试用例 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.source.common.DirAndFiles import DirAndFiles


class TestMainAndCommonView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()
        
    # 测试XXXXXXX
    def test1_XXXX_XXXX(self):
        a = 1
        b = 2
    
        try:
            self.assertEqual(a, b, "XXX错误!")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
