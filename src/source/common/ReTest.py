# coding=utf-8

""""" 重新验证失败和错误的用例，引入不通过的测试类，修改对应的用例名字 """""

import unittest
from datetime import datetime
import sys
from src.source.testcases.TestLoadingView import TestLoadingView
from src.lib.HTMLTestReportCN import DirAndFiles


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()

    startTime = datetime.now()

    # 重复测试n遍
    n = 1
    for i in range(n):

        suite = unittest.TestSuite()
        # 指定某测试类下的某个用例
        suite.addTest(TestLoadingView("test_loading_view_dispear"))
        runner = unittest.TextTestRunner()

        print("\n\033[36;0m第 " + str(i + 1) + " 次测试结果：\033[0m")
        runner.run(suite)

        print("\n")

    stopTime = datetime.now()
    print("\n\033[36;0m--------------------- 测试结束 ---------------------\n"
          "------------- 合计耗时: %s -------------\033[0m" % (stopTime - startTime), file=sys.stderr)
