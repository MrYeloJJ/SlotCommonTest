# coding=utf-8

import unittest
from time import sleep
from app.automatedTest.slot.source.common.ReadExcel import ReadExcel
from app.automatedTest.slot.source.common.Browser import Browser
from app.automatedTest.slot.source.common.Common import Common
from app.automatedTest.slot.lib.HTMLTestReportCN import DirAndFiles


class TestReward(unittest.TestCase):
    """ 中奖奖金模块 """

    def setUp(self):
        self.browser = Browser().browser()
        self.common = Common(self.browser)
        self.common.start()
        self.full_line = self.common.full_line
        self.game_id = str(self.common.game_id)
        self.data_list = ReadExcel().read_data(self.game_id)
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    def test_reward(self):
        """ 元素中奖奖金测试 """
        self.common.loading_pass()
        sleep(1)

        for i in self.data_list:
            # 获取GM等信息
            card_id = i["card_id"]
            card_type = i["card_type"]
            same = i["same"]
            odds = i["odds"]
            gm = i["gm"]
            multiply_with = i["multiply_with"]

            self.common.show_gm_view()
            sleep(0.5)
            self.common.gm_input(gm)
            sleep(0.5)
            self.common.gm_confirm_btn_click()
            sleep(0.5)
            self.common.start_btn_click()
            self.common.wait_for_rolling(30)
            self.common.start_btn_click()
            self.common.wait_for_rolling_stop(30, just_rolling=True)

            # 获取游戏内线注、总赌注
            current_line_cost = eval(str(self.common.info_bar_view_line_cost_label())[1:])
            current_bet = eval(str(self.common.info_bar_view_bet_money_label())[1:])
            # 判断是否是满线项目
            if not self.full_line:
                # 获取游戏内某条线的奖金
                current_spin_coin = self.common.line_spin_coin(2) / 100
            else:
                # 获取游戏内某条线的奖金
                current_spin_coin = self.common.line_spin_coin(1) / 100

            if card_type == "simple":
                # 预期该线奖金
                if multiply_with == "lineCost":
                    target_spin_coin = current_line_cost * odds
                elif multiply_with == "bet":
                    target_spin_coin = current_bet * odds
                else:
                    target_spin_coin = None

                try:
                    self.assertEqual(target_spin_coin, current_spin_coin, "该旋转 " + same + "连id=" + card_id + "的卡牌，卡牌类型=" + card_type + "，"
                                     + "线注=" + str(current_line_cost) + "，赔率=" + str(odds) + "，GM指令=" + gm)
                except AssertionError:
                    self.daf.get_screenshot(self.browser)
                    raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main(warnings="ignore")
