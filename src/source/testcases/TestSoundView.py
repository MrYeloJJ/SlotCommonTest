# coding=utf-8

""""" 声音提示窗口验证 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestSoundView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()
        self.common.loading_bar()

    def tearDown(self):
        self.browser.quit()

    #
    #
    # ------------------------------------------------------------------------ 横屏模式 ------------------------------------------------------------------------
    #
    #

    # 验证窗口显示
    def test_sound_view_showing(self):
        sleep(1)
        showing = self.common.sound_view_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口提示文字
    def test_sound_view_title(self):
        sleep(1)
        title = self.common.sound_view_text()
        try:
            self.assertEqual(title, "您想在游戏中打开声音吗？", "声音提示窗口的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口切换按钮显示
    def test_toggle_btn_visible(self):
        sleep(1)
        visible = self.common.sound_view_toggle_btn_visible()
        try:
            self.assertEqual(visible, True, "声音提示窗口没有显示切换按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口切换按钮提示文字
    def test_toggle_text(self):
        sleep(1)
        text = self.common.sound_view_toggle_text()
        try:
            self.assertEqual(text, "不再为我显示", "声音提示窗口切换按钮的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 是 按钮显示
    def test_yes_btn_showing(self):
        sleep(1)
        showing = self.common.sound_view_yes_btn_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示“是”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 是 按钮文字
    def test_yes_btn_text(self):
        sleep(1)
        text = self.common.sound_view_yes_btn_text()
        try:
            self.assertEqual(text, "是", "声音提示窗口“是”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 否 按钮显示
    def test_no_btn_showing(self):
        sleep(1)
        showing = self.common.sound_view_no_btn_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示“否”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 否 按钮文字
    def test_no_btn_text(self):
        sleep(1)
        text = self.common.sound_view_no_btn_text()
        try:
            self.assertEqual(text, "否", "声音提示窗口“否”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 切换按钮 默认状态是否为关闭
    def test_toggle_btn_default_status(self):
        sleep(1)
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "down", "声音提示窗口切换按钮默认状态为开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 切换按钮 可否点击
    def test_toggle_btn_touchable(self):
        sleep(1)
        touchable = self.common.sound_view_toggle_btn_touchable()
        try:
            self.assertEqual(touchable, True, "声音提示窗口切换按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 切换按钮 点击后状态是否改变
    def test_toggle_click_status(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "声音提示窗口切换按钮点击后，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 切换按钮 点击后立刻刷新，是否还弹出窗口
    def test_toggle_click_refresh_imm(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 切换按钮 点击后，窗口自动消失，刷新游戏后是否还弹出
    def test_toggle_click_view_dispear_refresh(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证点击切换按钮，然后点击是按钮，刷新游戏是否不再弹出
    def test_toggle_click_yes_refresh(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证点击切换按钮，然后点击否按钮，刷新游戏是否不再弹出
    def test_toggle_click_no_refresh(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 是 按钮可点击否
    def test_yes_btn_touchable(self):
        sleep(1)
        touchable = self.common.sound_view_yes_btn_touchable()
        try:
            self.assertEqual(touchable, True, "声音提示窗口“是”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证点击 是 按钮后，声音播放，声音开关按钮状态为打开
    def test_yes_btn_click(self):
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击“是”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, False, "点击“是”按钮，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "点击“是”按钮，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证窗口 否 按钮可点击否
    def test_no_btn_touchable(self):
        sleep(1)
        touchable = self.common.sound_view_no_btn_touchable()
        try:
            self.assertEqual(touchable, True, "声音提示窗口“否”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证点击 否 按钮后，声音播放，声音开关按钮状态为关闭
    def test_no_btn_click(self):
        sleep(1)
        self.common.sound_view_no_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击“否”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, True, "点击“否”按钮，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "点击“否”按钮，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证开启声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_on_sound_view_auto_dispear(self):
        sleep(1)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "8秒后声音提示窗口没有消失")
            self.assertEqual(voice_btn_status, "normal", "声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证关闭声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_off_sound_view_auto_dispear(self):
        sleep(1)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "8秒后声音提示窗口没有消失")
            self.assertEqual(voice_btn_status, "normal", "声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    # 验证竖屏窗口显示
    def test_sound_view_showing_portrait(self):
        self.common.portrait()
        sleep(1)
        showing = self.common.sound_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏声音提示窗口没有显示！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口提示文字
    def test_sound_view_title_portrait(self):
        self.common.portrait()
        sleep(1)
        title = self.common.sound_view_text()
        try:
            self.assertEqual(title, "您想在游戏中打开声音吗？", "竖屏声音提示窗口的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口切换按钮显示
    def test_toggle_btn_visible_portrait(self):
        self.common.portrait()
        sleep(1)
        visible = self.common.sound_view_toggle_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏声音提示窗口没有显示切换按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口切换按钮提示文字
    def test_toggle_text_portrait(self):
        self.common.portrait()
        sleep(1)
        text = self.common.sound_view_toggle_text()
        try:
            self.assertEqual(text, "不再为我显示", "竖屏声音提示窗口切换按钮的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 是 按钮显示
    def test_yes_btn_showing_portrait(self):
        self.common.portrait()
        sleep(1)
        showing = self.common.sound_view_yes_btn_showing()
        try:
            self.assertEqual(showing, True, "竖屏声音提示窗口没有显示“是”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 是 按钮文字
    def test_yes_btn_text_portrait(self):
        self.common.portrait()
        sleep(1)
        text = self.common.sound_view_yes_btn_text()
        try:
            self.assertEqual(text, "是", "竖屏声音提示窗口“是”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 否 按钮显示
    def test_no_btn_showing_portrait(self):
        self.common.portrait()
        sleep(1)
        showing = self.common.sound_view_no_btn_showing()
        try:
            self.assertEqual(showing, True, "竖屏声音提示窗口没有显示“否”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 否 按钮文字
    def test_no_btn_text_portrait(self):
        self.common.portrait()
        sleep(1)
        text = self.common.sound_view_no_btn_text()
        try:
            self.assertEqual(text, "否", "竖屏声音提示窗口“否”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 切换按钮 默认状态是否为关闭
    def test_toggle_btn_default_status_portrait(self):
        self.common.portrait()
        sleep(1)
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "down", "竖屏声音提示窗口切换按钮默认状态为开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 切换按钮 可否点击
    def test_toggle_btn_touchable_portrait(self):
        self.common.portrait()
        sleep(1)
        touchable = self.common.sound_view_toggle_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏声音提示窗口切换按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 切换按钮 点击后状态是否改变
    def test_toggle_click_status_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_toggle_click()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "竖屏声音提示窗口切换按钮点击后，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 切换按钮 点击后立刻刷新，是否还弹出窗口
    def test_toggle_click_refresh_imm_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "竖屏声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 切换按钮 点击后，窗口自动消失，刷新游戏后是否还弹出
    def test_toggle_click_view_dispear_refresh_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "竖屏声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击切换按钮，然后点击是按钮，刷新游戏是否不再弹出
    def test_toggle_click_yes_refresh_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "竖屏声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击切换按钮，然后点击否按钮，刷新游戏是否不再弹出
    def test_toggle_click_no_refresh_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "竖屏声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "竖屏声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "竖屏声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 是 按钮可点击否
    def test_yes_btn_touchable_portrait(self):
        self.common.portrait()
        sleep(1)
        touchable = self.common.sound_view_yes_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏声音提示窗口“是”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击 是 按钮后，声音播放，声音开关按钮状态为打开
    def test_yes_btn_click_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏点击“是”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, False, "竖屏点击“是”按钮，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "竖屏点击“是”按钮，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏窗口 否 按钮可点击否
    def test_no_btn_touchable_portrait(self):
        self.common.portrait()
        sleep(1)
        touchable = self.common.sound_view_no_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏声音提示窗口“否”按钮不可以点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击 否 按钮后，声音播放，声音开关按钮状态为关闭
    def test_no_btn_click_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_no_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "竖屏点击“否”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, True, "竖屏点击“否”按钮，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "竖屏点击“否”按钮，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏开启声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_on_sound_view_auto_dispear_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "竖屏声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "竖屏8秒后声音提示窗口没有消失")
            self.assertEqual(voice_btn_status, "normal", "竖屏声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "竖屏声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏关闭声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_off_sound_view_auto_dispear_portrait(self):
        self.common.portrait()
        sleep(1)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(9)
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "竖屏声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "竖屏8秒后声音提示窗口没有消失")
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

    # 验证横竖屏 窗口显示
    def test_sound_view_showing_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        showing = self.common.sound_view_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口提示文字
    def test_sound_view_title_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        title = self.common.sound_view_text()
        try:
            self.assertEqual(title, "您想在游戏中打开声音吗？", "声音提示窗口的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口切换按钮显示
    def test_toggle_btn_visible_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        visible = self.common.sound_view_toggle_btn_visible()
        try:
            self.assertEqual(visible, True, "声音提示窗口没有显示切换按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口切换按钮提示文字
    def test_toggle_text_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        text = self.common.sound_view_toggle_text()
        try:
            self.assertEqual(text, "不再为我显示", "声音提示窗口切换按钮的提示文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 是 按钮显示
    def test_yes_btn_showing_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        showing = self.common.sound_view_yes_btn_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示“是”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 是 按钮文字
    def test_yes_btn_text_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        text = self.common.sound_view_yes_btn_text()
        try:
            self.assertEqual(text, "是", "声音提示窗口“是”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 否 按钮显示
    def test_no_btn_showing_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        showing = self.common.sound_view_no_btn_showing()
        try:
            self.assertEqual(showing, True, "声音提示窗口没有显示“否”按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 否 按钮文字
    def test_no_btn_text_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        text = self.common.sound_view_no_btn_text()
        try:
            self.assertEqual(text, "否", "声音提示窗口“否”按钮文字错误！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 切换按钮 默认状态是否为关闭
    def test_toggle_btn_default_status_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "down", "声音提示窗口切换按钮默认状态为开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 切换按钮 可否点击
    def test_toggle_btn_touchable_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        touchable = self.common.sound_view_toggle_btn_touchable()
        try:
            self.assertEqual(touchable, True, "声音提示窗口切换按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 切换按钮 点击后状态是否改变
    def test_toggle_click_status_switch_screen(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        status = self.common.sound_view_toggle_status()
        try:
            self.assertEqual(status, "up", "声音提示窗口切换按钮点击后，状态不会改变！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 切换按钮 点击后立刻刷新，是否还弹出窗口
    def test_toggle_click_refresh_imm_switch_screen(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 窗口 切换按钮 点击后，窗口自动消失，刷新游戏后是否还弹出
    def test_toggle_click_view_dispear_refresh_switch_screen(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        sleep(9)
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 点击切换按钮，然后点击是按钮，刷新游戏是否不再弹出
    def test_toggle_click_yes_refresh_switch_screen(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_yes_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 点击切换按钮，然后点击否按钮，刷新游戏是否不再弹出
    def test_toggle_click_no_refresh_switch_screen(self):
        sleep(1)
        self.common.sound_view_toggle_click()
        self.common.sound_view_no_btn_click()
        sound_status1 = self.common.sound_status()
        voice_btn_status1 = self.common.voice_btn_status()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        dispear = self.common.sound_view_dispear()
        sound_status2 = self.common.sound_status()
        voice_btn_status2 = self.common.voice_btn_status()
        try:
            self.assertEqual(dispear, None, "声音提示窗口依然弹出！")
            self.assertEqual(sound_status2, sound_status1, "声音状态刷新前后不一致！")
            self.assertEqual(voice_btn_status2, voice_btn_status1, "声音按钮状态刷新切换不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 点击 是 按钮后，声音播放，声音开关按钮状态为打开
    def test_yes_btn_click_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        self.common.sound_view_yes_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击“是”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, False, "点击“是”按钮，声音不会播放！")
            self.assertEqual(voice_btn_status, "normal", "点击“是”按钮，声音开关按钮显示关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 点击 否 按钮后，声音播放，声音开关按钮状态为关闭
    def test_no_btn_click_switch_screen(self):
        sleep(1)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        self.common.sound_view_no_btn_click()
        sound_view_dispear = self.common.sound_view_dispear()
        sound_status = self.common.sound_status()
        voice_btn_status = self.common.voice_btn_status()

        try:
            self.assertEqual(sound_view_dispear, None, "点击“否”按钮，声音提示窗口不会消失！")
            self.assertEqual(sound_status, True, "点击“否”按钮，声音会播放！")
            self.assertEqual(voice_btn_status, "silience", "点击“否”按钮，声音开关按钮显示开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 开启声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_on_sound_view_auto_dispear_switch_screen(self):
        sleep(1)
        self.common.sound_view_yes_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(8)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "8秒后声音提示窗口没有消失")
            self.assertEqual(voice_btn_status, "normal", "声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横竖屏 关闭声音，窗口8秒后是否自动消失，声音自动设置开启
    def test_turn_off_sound_view_auto_dispear_switch_screen(self):
        sleep(1)
        self.common.sound_view_no_btn_click()
        self.browser.refresh()
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        sound_view_showing = self.common.sound_view_showing()
        sleep(9)
        self.common.portrait()
        self.common.landscape()
        self.common.portrait()
        sound_view_dispear = self.common.sound_view_dispear()
        voice_btn_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()

        try:
            self.assertEqual(sound_view_showing, True, "声音提示窗口没有显示！")
            self.assertEqual(sound_view_dispear, None, "8秒后声音提示窗口没有消失")
            self.assertEqual(voice_btn_status, "normal", "声音按钮状态是关闭！")
            self.assertEqual(sound_status, False, "声音没有播放！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
