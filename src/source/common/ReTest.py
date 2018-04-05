# coding=utf-8

""""" 重新验证失败和错误的用例，引入不通过的测试类，修改对应的用例名字 """""

import unittest
from datetime import datetime
import sys
from src.source.testcases.TestAutoGameView import TestAutoGameView
from src.lib.HTMLTestReportCN import DirAndFiles


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()

    startTime = datetime.now()
    # 重复测试5遍
    for i in range(5):
        print("\n\033[36;0m第 " + str(i + 1) + " 次测试结果：\033[0m")

        suite = unittest.TestSuite()
        # 指定某测试类下的某个用例
        suite.addTest(TestAutoGameView("test_auto_spin_time_is_zero_portrait"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

        print("\n")

    stopTime = datetime.now()
    print("\n\033[36;0m--------------------- 测试结束 ---------------------\n"
          "------------- 合计耗时: %s -------------\033[0m" % (stopTime - startTime), file=sys.stderr)
