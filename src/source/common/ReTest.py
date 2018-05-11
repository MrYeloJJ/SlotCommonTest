# coding=utf-8

""""" 重新验证失败和错误的用例，引入不通过的测试类，修改对应的用例名字 """""

import unittest
import sys
from src.source.testcases.TestAutoGameView import TestAutoGameView
from src.lib.HTMLTestReportCN import DirAndFiles


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()

    # 重复测试n遍
    n = 1
    for i in range(n):

        suite = unittest.TestSuite()
        # 指定某测试类下的某个用例
        suite.addTest(TestAutoGameView("test_auto_game_btn"))
        runner = unittest.TextTestRunner()

        print("\n\033[36;0m第 " + str(i + 1) + " 次测试结果：\033[0m")
        runner.run(suite)

        print("\n")

    print("\n\033[36;0m--------------------- 测试结束 ---------------------\n", file=sys.stderr)
