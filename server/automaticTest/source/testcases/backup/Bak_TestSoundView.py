# coding=utf-8

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestSoundView(unittest.TestCase):
    """ 声音提示窗口模块 """

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    def test_sound_view(self):
        """ 横屏声音窗口内容 """
        self.common.loading_pass()
        sleep(3)
        # 显示
        sound_view_showing = self.common.sound_view_showing()
        mask_view_showing = self.common.mask_view_showing()
        title = self.common.sound_view_text()
        toggle_btn_visible = self.common.sound_view_toggle_btn_visible()
        toggle_text = self.common.sound_view_toggle_text()
        yes_btn_showing = self.common.sound_view_yes_btn_showing()
        yes_btn_text = self.common.sound_view_yes_btn_text()
        no_btn_showing = self.common.sound_view_no_btn_showing()
        no_btn_text = self.common.sound_view_no_btn_text()
        toggle_btn_default_status = self.common.sound_view_toggle_status()
        # 能否点击
        toggle_btn_touchable = self.common.sound_view_toggle_btn_touchable()
        yes_btn_touchable = self.common.sound_view_yes_btn_touchable()
        no_btn_touchable = self.common.sound_view_no_btn_touchable()

        try:
            self.assertEqual(sound_view_showing, True, "横屏声音提示窗口没有显示！")
            self.assertEqual(mask_view_showing, True, "横屏弹出声音提示窗口，灰色蒙板没有显示！")
            self.assertEqual(title, "您想在游戏中打开声音吗？", "横屏声音提示窗口的提示文字错误！")
            self.assertEqual(toggle_btn_visible, True, "横屏声音提示窗口没有显示切换按钮！")
            self.assertEqual(toggle_text, "不再为我显示", "横屏声音提示窗口切换按钮的提示文字错误！")
            self.assertEqual(yes_btn_showing, True, "横屏声音提示窗口没有显示“是”按钮！")
            self.assertEqual(yes_btn_text, "是", "横屏声音提示窗口“是”按钮文字错误！")
            self.assertEqual(no_btn_showing, True, "横屏声音提示窗口没有显示“否”按钮！")
            self.assertEqual(no_btn_text, "否", "横屏声音提示窗口“否”按钮文字错误！")
            self.assertEqual(toggle_btn_default_status, "down", "横屏声音提示窗口切换按钮默认状态为开启！")
            self.assertEqual(toggle_btn_touchable, True, "横屏声音提示窗口切换按钮不能点击！")
            self.assertEqual(yes_btn_touchable, True, "横屏声音提示窗口“是”按钮不可以点击！")
            self.assertEqual(no_btn_touchable, True, "横屏声音提示窗口“否”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click(self):
        """ 横屏切换按钮点击 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "横屏声音提示窗口切换按钮点击后，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice(self):
        """ 横屏点击切换按钮两次 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "down", "横屏声音提示窗口切换按钮点击两次后，状态不会恢复！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh_imm(self):
        """ 横屏点击切换按钮后立刻刷新 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "横屏点击切换按钮，然后立刻刷新，声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "横屏点击切换按钮，然后立刻刷新，灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮，然后立刻刷新，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮，然后立刻刷新，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_refresh_imm(self):
        """ 横屏点击切换按钮两次后立刻刷新 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "横屏点击切换按钮两次，然后立刻刷新，声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "横屏点击切换按钮两次，然后立刻刷新，灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮两次，然后立刻刷新，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮两次，然后立刻刷新，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh(self):
        """ 横屏点击切换按钮，窗口自动消失刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "横屏点击切换按钮，然后等窗口自动消失，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "横屏点击切换按钮，然后等窗口自动消失，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮，然后等窗口自动消失，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮，然后等窗口自动消失，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_refresh(self):
        """ 横屏点击切换按钮两次，窗口自动消失刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.mask_view_showing()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "横屏点击切换按钮两次，然后等窗口自动消失，刷新后声音提示窗口没有弹出！")
            self.assertEqual(mask_view_showing, True, "横屏点击切换按钮两次，然后等窗口自动消失，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮两次，然后等窗口自动消失，刷新后声音状态余额刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮两次，然后等窗口自动消失，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_yes_refresh(self):
        """ 横屏点击切换按钮，点击是按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "横屏点击切换按钮，然后点击是按钮，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "横屏点击切换按钮，然后点击是按钮，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮，然后点击是按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮，然后点击是按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_yes_refresh(self):
        """ 横屏点击切换按钮两次，点击是按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "横屏点击切换按钮两次，然后点击是按钮，刷新后声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "横屏点击切换按钮两次，然后点击是按钮，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮两次，然后点击是按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮两次，然后点击是按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_no_refresh(self):
        """ 横屏点击切换按钮，点击否按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "横屏点击切换按钮，然后点击否按钮，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "横屏点击切换按钮，然后点击否按钮，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮，然后点击否按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮，然后点击否按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_no_refresh(self):
        """ 横屏点击切换按钮两次，点击否按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "横屏点击切换按钮两次，然后点击否按钮，刷新后声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "横屏点击切换按钮两次，然后点击否按钮，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "横屏点击切换按钮两次，然后点击否按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "横屏点击切换按钮两次，然后点击否按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_yes_btn_click(self):
        """ 横屏点击是按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "横屏点击“是”按钮，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "横屏点击“是”按钮，灰色蒙板不会消失！")
            self.assertEqual(sound_status, False, "横屏点击“是”按钮，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "横屏点击“是”按钮，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_no_btn_click(self):
        """ 横屏点击否按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "横屏点击“否”按钮，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "横屏点击“否”按钮，灰色蒙板不会消失！")
            self.assertEqual(sound_status, True, "横屏点击“否”按钮，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "横屏点击“否”按钮，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_on_sound_view_dispear(self):
        """ 横屏开启声音刷新，窗口8秒后自动消失 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "横屏8秒后声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "横屏8秒后灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "横屏声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "横屏声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_off_sound_view_dispear(self):
        """ 横屏关闭声音刷新，窗口8秒后自动消失 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "横屏8秒后声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "横屏8秒后灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "横屏声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "横屏声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    def test_sound_view_portrait(self):
        """ 竖屏声音窗口内容 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        # 显示
        sound_view_showing = self.common.sound_view_showing()
        mask_view_showing = self.common.mask_view_showing()
        title = self.common.sound_view_text()
        toggle_btn_visible = self.common.sound_view_toggle_btn_visible()
        toggle_text = self.common.sound_view_toggle_text()
        yes_btn_showing = self.common.sound_view_yes_btn_showing()
        yes_btn_text = self.common.sound_view_yes_btn_text()
        no_btn_showing = self.common.sound_view_no_btn_showing()
        no_btn_text = self.common.sound_view_no_btn_text()
        toggle_btn_default_status = self.common.sound_view_toggle_status()
        # 能否点击
        toggle_btn_touchable = self.common.sound_view_toggle_btn_touchable()
        yes_btn_touchable = self.common.sound_view_yes_btn_touchable()
        no_btn_touchable = self.common.sound_view_no_btn_touchable()

        try:
            self.assertEqual(sound_view_showing, True, "竖屏声音提示窗口没有显示！")
            self.assertEqual(mask_view_showing, True, "竖屏弹出声音提示窗口，灰色蒙板没有显示！")
            self.assertEqual(title, "您想在游戏中打开声音吗？", "竖屏声音提示窗口的提示文字错误！")
            self.assertEqual(toggle_btn_visible, True, "竖屏声音提示窗口没有显示切换按钮！")
            self.assertEqual(toggle_text, "不再为我显示", "竖屏声音提示窗口切换按钮的提示文字错误！")
            self.assertEqual(yes_btn_showing, True, "竖屏声音提示窗口没有显示“是”按钮！")
            self.assertEqual(yes_btn_text, "是", "竖屏声音提示窗口“是”按钮文字错误！")
            self.assertEqual(no_btn_showing, True, "竖屏声音提示窗口没有显示“否”按钮！")
            self.assertEqual(no_btn_text, "否", "竖屏声音提示窗口“否”按钮文字错误！")
            self.assertEqual(toggle_btn_default_status, "down", "竖屏声音提示窗口切换按钮默认状态为开启！")
            self.assertEqual(toggle_btn_touchable, True, "竖屏声音提示窗口切换按钮不能点击！")
            self.assertEqual(yes_btn_touchable, True, "竖屏声音提示窗口“是”按钮不可以点击！")
            self.assertEqual(no_btn_touchable, True, "竖屏声音提示窗口“否”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_portrait(self):
        """ 竖屏切换按钮点击 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "竖屏声音提示窗口切换按钮点击后，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_portrait(self):
        """ 竖屏点击切换按钮两次 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "down", "竖屏声音提示窗口切换按钮点击两次后，状态不会恢复！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh_imm_portrait(self):
        """ 竖屏点击切换按钮后立刻刷新 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏点击切换按钮，然后立刻刷新，声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "竖屏点击切换按钮，然后立刻刷新，灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮，然后立刻刷新，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮，然后立刻刷新，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_refresh_imm_portrait(self):
        """ 竖屏点击切换按钮两次后立刻刷新 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "竖屏点击切换按钮两次，然后立刻刷新，声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "竖屏点击切换按钮两次，然后立刻刷新，灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮两次，然后立刻刷新，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮两次，然后立刻刷新，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh_portrait(self):
        """ 竖屏点击切换按钮，窗口自动消失刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏点击切换按钮，然后等窗口自动消失，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "竖屏点击切换按钮，然后等窗口自动消失，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮，然后等窗口自动消失，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮，然后等窗口自动消失，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_refresh_portrait(self):
        """ 竖屏点击切换按钮两次，窗口自动消失刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.mask_view_showing()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "竖屏点击切换按钮两次，然后等窗口自动消失，刷新后声音提示窗口没有弹出！")
            self.assertEqual(mask_view_showing, True, "竖屏点击切换按钮两次，然后等窗口自动消失，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮两次，然后等窗口自动消失，刷新后声音状态余额刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮两次，然后等窗口自动消失，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_yes_refresh_portrait(self):
        """ 竖屏点击切换按钮，点击是按钮刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏点击切换按钮，然后点击是按钮，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "竖屏点击切换按钮，然后点击是按钮，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮，然后点击是按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮，然后点击是按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_yes_refresh_portrait(self):
        """ 竖屏点击切换按钮两次，点击是按钮刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "竖屏点击切换按钮两次，然后点击是按钮，刷新后声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "竖屏点击切换按钮两次，然后点击是按钮，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮两次，然后点击是按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮两次，然后点击是按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_no_refresh_portrait(self):
        """ 竖屏点击切换按钮，点击否按钮刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        dispear = self.common.sound_view_dispear()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏点击切换按钮，然后点击否按钮，刷新后声音提示窗口依然弹出！")
            self.assertEqual(mask_view, False, "竖屏点击切换按钮，然后点击否按钮，刷新后灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮，然后点击否按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮，然后点击否按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_twice_no_refresh_portrait(self):
        """ 竖屏点击切换按钮两次，点击否按钮刷新游戏 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sleep(0.5)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        showing = self.common.sound_view_showing()
        mask_view = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(showing, True, "竖屏点击切换按钮两次，然后点击否按钮，刷新后声音提示窗口不会弹出！")
            self.assertEqual(mask_view, True, "竖屏点击切换按钮两次，然后点击否按钮，刷新后灰色蒙板不会显示！")
            self.assertEqual(sound_status2, sound_status1, "竖屏点击切换按钮两次，然后点击否按钮，刷新后声音状态与刷新前不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏点击切换按钮两次，然后点击否按钮，刷新后声音按钮状态与刷新前不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_yes_btn_click_portrait(self):
        """ 竖屏点击是按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏点击“是”按钮，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "竖屏点击“是”按钮，灰色蒙板不会消失！")
            self.assertEqual(sound_status, False, "竖屏点击“是”按钮，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "竖屏点击“是”按钮，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_no_btn_click_portrait(self):
        """ 竖屏点击否按钮 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏点击“否”按钮，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "竖屏点击“否”按钮，灰色蒙板不会消失！")
            self.assertEqual(sound_status, True, "竖屏点击“否”按钮，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "竖屏点击“否”按钮，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_on_sound_portrait(self):
        """ 竖屏开启声音刷新，窗口8秒后自动消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏8秒后声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "竖屏8秒后灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "竖屏声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "竖屏声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_off_sound_portrait(self):
        """ 竖屏关闭声音刷新，窗口8秒后自动消失 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏8秒后声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "竖屏8秒后灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "竖屏声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "竖屏声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 横竖屏切换 ------------------------------------------------------------------------
    #
    #

    def test_sound_view_switch_screen(self):
        """ 横竖屏声音窗口内容 """
        self.common.portrait()
        self.common.loading_pass()
        sleep(3)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        # 显示
        sound_view_showing = self.common.sound_view_showing()
        mask_view_showing = self.common.mask_view_showing()
        title = self.common.sound_view_text()
        toggle_btn_visible = self.common.sound_view_toggle_btn_visible()
        toggle_text = self.common.sound_view_toggle_text()
        yes_btn_showing = self.common.sound_view_yes_btn_showing()
        yes_btn_text = self.common.sound_view_yes_btn_text()
        no_btn_showing = self.common.sound_view_no_btn_showing()
        no_btn_text = self.common.sound_view_no_btn_text()
        toggle_btn_default_status = self.common.sound_view_toggle_status()
        # 能否点击
        toggle_btn_touchable = self.common.sound_view_toggle_btn_touchable()
        yes_btn_touchable = self.common.sound_view_yes_btn_touchable()
        no_btn_touchable = self.common.sound_view_no_btn_touchable()

        try:
            self.assertEqual(sound_view_showing, True, "横竖屏切换，声音提示窗口没有显示！")
            self.assertEqual(mask_view_showing, True, "横竖屏切换，弹出声音提示窗口，灰色蒙板没有显示！")
            self.assertEqual(title, "您想在游戏中打开声音吗？", "横竖屏切换，声音提示窗口的提示文字错误！")
            self.assertEqual(toggle_btn_visible, True, "横竖屏切换，声音提示窗口没有显示切换按钮！")
            self.assertEqual(toggle_text, "不再为我显示", "横竖屏切换，声音提示窗口切换按钮的提示文字错误！")
            self.assertEqual(yes_btn_showing, True, "横竖屏切换，声音提示窗口没有显示“是”按钮！")
            self.assertEqual(yes_btn_text, "是", "横竖屏切换，声音提示窗口“是”按钮文字错误！")
            self.assertEqual(no_btn_showing, True, "横竖屏切换，声音提示窗口没有显示“否”按钮！")
            self.assertEqual(no_btn_text, "否", "横竖屏切换，声音提示窗口“否”按钮文字错误！")
            self.assertEqual(toggle_btn_default_status, "down", "横竖屏切换，声音提示窗口切换按钮默认状态为开启！")
            self.assertEqual(toggle_btn_touchable, True, "横竖屏切换，声音提示窗口切换按钮不能点击！")
            self.assertEqual(yes_btn_touchable, True, "横竖屏切换，声音提示窗口“是”按钮不可以点击！")
            self.assertEqual(no_btn_touchable, True, "横竖屏切换，声音提示窗口“否”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_switch_screen(self):
        """ 横竖屏点击切换按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "声音提示窗口切换按钮点击后，横竖屏切换，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh_imm_switch_screen(self):
        """ 横竖屏点击切换按钮后立刻刷新 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "点击切换按钮后立刻刷新，横竖屏切换，声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "点击切换按钮后立刻刷新，横竖屏切换，灰色蒙板会显示！")
            self.assertEqual(sound_status2, sound_status1, "点击切换按钮后立刻刷新，横竖屏切换，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "点击切换按钮后立刻刷新，横竖屏切换，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_refresh_switch_screen(self):
        """ 横竖屏点击切换按钮，窗口自动消失刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "点击切换按钮后等待窗口自动消失，刷新游戏然后横竖屏切换，声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "点击切换按钮后等待窗口自动消失，刷新游戏然后横竖屏切换，灰色蒙板依然显示！")
            self.assertEqual(sound_status2, sound_status1, "点击切换按钮后等待窗口自动消失，刷新游戏然后横竖屏切换，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "点击切换按钮后等待窗口自动消失，刷新游戏然后横竖屏切换，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_yes_refresh_switch_screen(self):
        """ 横竖屏点击切换按钮，点击是按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "点击切换按钮后点击是按钮，刷新游戏然后横竖屏切换，声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "点击切换按钮后点击是按钮，刷新游戏然后横竖屏切换，灰色蒙板会显示！")
            self.assertEqual(sound_status2, sound_status1, "点击切换按钮后点击是按钮，刷新游戏然后横竖屏切换，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "点击切换按钮后点击是按钮，刷新游戏然后横竖屏切换，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_toggle_click_no_refresh_switch_screen(self):
        """ 横竖屏点击切换按钮，点击否按钮刷新游戏 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(3)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "点击切换按钮后点击否按钮，刷新游戏然后横竖屏切换，声音提示窗口依然弹出！")
            self.assertEqual(mask_view_showing, False, "点击切换按钮后点击否按钮，刷新游戏然后横竖屏切换，灰色蒙板会显示！")
            self.assertEqual(sound_status2, sound_status1, "点击切换按钮后点击否按钮，刷新游戏然后横竖屏切换，声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "点击切换按钮后点击否按钮，刷新游戏然后横竖屏切换，声音按钮状态刷新前后不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_yes_btn_click_switch_screen(self):
        """ 横竖屏点击是按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击是按钮，横竖屏切换，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "点击是按钮，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(sound_status, False, "点击是按钮，横竖屏切换，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "点击是按钮，横竖屏切换，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_no_btn_click_switch_screen(self):
        """ 横竖屏点击否按钮 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击否按钮，横竖屏切换，声音提示窗口不会消失！")
            self.assertEqual(mask_view_showing, False, "点击否按钮，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(sound_status, True, "点击否按钮，横竖屏切换，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "点击否按钮，横竖屏切换，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_on_sound_switch_screen(self):
        """ 横竖屏开启声音刷新游戏，窗口8秒后自动消失 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "开启声音刷新游戏，等待窗口自动消失，横竖屏切换，声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "开启声音刷新游戏，等待窗口自动消失，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "开启声音刷新游戏，等待窗口自动消失，横竖屏切换，声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "开启声音刷新游戏，等待窗口自动消失，横竖屏切换，声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    def test_turn_off_sound_switch_screen(self):
        """ 横竖屏关闭声音刷新游戏，窗口8秒后自动消失 """
        self.common.loading_pass()
        sleep(3)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_pass()
        sleep(9)
        self.common.portrait()
        sleep(1)
        self.common.landscape()
        sleep(1)
        self.common.portrait()
        sleep(1)
        sound_view_dispear = self.common.sound_view_dispear()
        mask_view_showing = self.common.mask_view_showing()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_dispear, None, "关闭声音刷新游戏，等待窗口自动消失，横竖屏切换，声音提示窗口没有消失！")
            self.assertEqual(mask_view_showing, False, "关闭声音刷新游戏，等待窗口自动消失，横竖屏切换，灰色蒙板不会消失！")
            self.assertEqual(voice_btn_status, "normal", "关闭声音刷新游戏，等待窗口自动消失，横竖屏切换，声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "关闭声音刷新游戏，等待窗口自动消失，横竖屏切换，声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
