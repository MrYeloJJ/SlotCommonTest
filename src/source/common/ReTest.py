# coding=utf-8

""""" 重新验证失败和错误的用例，将不通过的用例拷贝到这里循环运行，setUp内容记得保持一致 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class ReTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    # 验证竖屏 自动次数为0时停止
    def test_auto_spin_time_is_zero_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)

        self.common.auto_game_btn_click()
        sleep(1)
        self.common.auto_game_view_change_auto_time(0)
        sleep(1)

        self.common.auto_game_view_start_btn_click()
        sleep(1)

        # 用这个循环来防止自动游戏过程触发特殊玩法
        while True:

            time = 15
            slot_status = self.common.wait_for_rolling(time)
            try:
                self.assertEqual(slot_status, True, "竖屏等待" + str(time) + "秒滚轴依然不会旋转！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise

            # 获取停止旋转按钮上的剩余次数
            current_spin_time = self.common.in_auto_spin_btn_text()

            # 判断自动游戏最后一局是否中了特殊玩法，若中了则刷新游戏重来
            if current_spin_time == "0":
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                        self.browser.refresh()
                        self.common.loading_bar()
                        sleep(1)
                        self.common.sound_view_yes_btn_click()
                        sleep(1)

                        self.common.auto_game_btn_click()
                        sleep(1)
                        self.common.auto_game_view_change_auto_time(0)
                        sleep(1)

                        self.common.auto_game_view_start_btn_click()
                        sleep(1)
                        continue
                else:
                    time = 15
                    slot_status = self.common.wait_for_stop(time)
                    try:
                        self.assertEqual(slot_status, True, "竖屏等待" + str(time) + "秒滚轴依然不会停止！")
                    except AssertionError:
                        self.daf.get_screenshot(self.browser)
                        raise

                    for i in range(10):     # 循环10秒验证是否还会继续自动旋转
                        sleep(1)
                        # 获取滚轴滚动状态
                        slot_rolling = self.common.slot_machine_rolling()
                        # 获取旋转按钮状态
                        start_btn_status = self.common.start_btn_status()
                        # 获取线数线注按钮、自动游戏按钮、选项菜单状态
                        setting_btn = self.common.setting_btn_visible()
                        auto_game_btn = self.common.auto_game_btn_visible()
                        main_menu_expand = self.common.main_menu_expand()
                        main_menu = self.common.main_menu_touchable()

                        try:
                            self.assertEqual(slot_rolling, False, "竖屏自动游戏次数为0后，滚轴不会停止滚动！")
                            self.assertEqual(start_btn_status, "stopped", "竖屏自动游戏次数为0后，旋转按钮不会变成旋转按钮状态！")
                            self.assertEqual(setting_btn, True, "竖屏自动游戏次数为0后，线数线注设置按钮不会重新显示！")
                            self.assertEqual(auto_game_btn, True, "竖屏自动游戏次数为0后，自动游戏按钮不会重新显示！")
                            self.assertEqual(main_menu_expand, "retractP", "竖屏自动游戏次数为0后，左侧选项菜单不会依然折叠！")
                            self.assertEqual(main_menu, True, "竖屏自动游戏次数为0后，左侧选项菜单不可以点击！")
                        except AssertionError:
                            self.daf.get_screenshot(self.browser)
                            raise
                    break
            else:
                game_status = self.common.get_game_current_status()
                if game_status is not None:
                    self.browser.refresh()
                    self.common.loading_bar()
                    sleep(1)
                    self.common.sound_view_yes_btn_click()
                    sleep(1)

                    self.common.auto_game_btn_click()
                    sleep(1)
                    self.common.auto_game_view_change_auto_time(0)
                    sleep(1)

                    self.common.auto_game_view_start_btn_click()
                    sleep(1)

            time = 15
            slot_status = self.common.wait_for_stop(time)
            try:
                self.assertEqual(slot_status, True, "竖屏等待" + str(time) + "秒滚轴依然不会停止！")
            except AssertionError:
                self.daf.get_screenshot(self.browser)
                raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    for test_time in range(5):
        unittest.main()
