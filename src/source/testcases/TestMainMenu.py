# coding=utf-8

""""" 左侧选项菜单验证 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestMainMenu(unittest.TestCase):

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

    # 验证横屏显示左侧主菜单按钮
    def test_main_menu_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.main_menu_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏不会显示主菜单按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏左侧主菜单默认为展开状态
    def test_main_menu_default_expand(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        expand = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(expand, "expandLPC", "横屏左侧主菜单默认不是展开状态！")
            self.assertEqual(info_btn, True, "横屏左侧主菜单展开时不会显示奖金表按钮！")
            self.assertEqual(help_btn, True, "横屏左侧主菜单展开时不会显示帮助按钮！")
            self.assertEqual(voice_btn, True, "横屏左侧主菜单展开时不会显示声音按钮！")
            self.assertEqual(turbo_btn, True, "横屏左侧主菜单展开时不会显示快速按钮！")
            self.assertEqual(home_btn, False, "横屏PC端左侧主菜单展开时，会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "横屏试玩左侧主菜单展开时，会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏整个左侧主菜单可点击否
    def test_main_menu_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.main_menu_touchable()
        try:
            self.assertEqual(touchable, True, "横屏整个左侧主菜单不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击左侧主菜单按钮后是否折叠
    def test_main_menu_btn_click_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        status = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(status, "retractL", "横屏点击左侧主菜单按钮后不会折叠！")
            self.assertEqual(info_btn, False, "横屏左侧主菜单折叠时会显示奖金表按钮！")
            self.assertEqual(help_btn, False, "横屏左侧主菜单折叠时会显示帮助按钮！")
            self.assertEqual(voice_btn, False, "横屏左侧主菜单折叠时会显示声音按钮！")
            self.assertEqual(turbo_btn, False, "横屏左侧主菜单折叠时会显示快速按钮！")
            self.assertEqual(home_btn, False, "横屏PC端左侧主菜单折叠时会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "横屏试玩左侧主菜单折叠时会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击左侧主菜单按钮两次后恢复展开状态
    def test_main_menu_btn_click_twice_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        status = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(status, "expandLPC", "横屏点击左侧主菜单按钮两次后不会恢复展开状态！")
            self.assertEqual(info_btn, True, "横屏点击左侧主菜单按钮两次后不会显示奖金表按钮！")
            self.assertEqual(help_btn, True, "横屏点击左侧主菜单按钮两次后不会显示帮助按钮！")
            self.assertEqual(voice_btn, True, "横屏点击左侧主菜单按钮两次后不会显示声音按钮！")
            self.assertEqual(turbo_btn, True, "横屏点击左侧主菜单按钮两次后不会显示快速按钮！")
            self.assertEqual(home_btn, False, "横屏PC端点击左侧主菜单按钮两次后，会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "横屏试玩点击左侧主菜单按钮两次后，会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏显示奖金表按钮
    def test_info_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.info_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏奖金表按钮默认不会显示！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏奖金表按钮可点击否
    def test_info_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.info_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏奖金表按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击奖金表按钮后，显示奖金表场景
    def test_info_btn_click_info_view_showing(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        showing = self.common.info_view_showing()
        try:
            self.assertEqual(showing, True, "横屏点击奖金表按钮后，不会显示奖金表场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏奖金表场景显示返回按钮
    def test_info_view_return_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        visible = self.common.info_view_return_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏奖金表场景，不会显示返回按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏奖金表场景返回按钮可点击否
    def test_info_view_return_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        touchable = self.common.info_view_return_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏奖金表场景返回按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击奖金表返回按钮，奖金表场景消失
    def test_return_btn_click_info_view_dispear(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        self.common.info_view_return_btn_click()
        sleep(1)
        dispear = self.common.info_view_dispear()
        try:
            self.assertEqual(dispear, None, "横屏点击奖金表返回按钮，奖金表场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏显示帮助按钮
    def test_help_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.help_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏不会显示帮助按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏帮助按钮可点击否
    def test_help_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.help_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏帮助按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击帮助按钮后，显示帮助场景
    def test_help_btn_click_help_view_showing(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        showing = self.common.help_view_showing()
        try:
            self.assertEqual(showing, True, "横屏点击帮助按钮后，不会显示帮助场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏帮助场景显示返回按钮
    def test_help_view_return_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        visible = self.common.help_view_return_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏帮助场景不会显示返回按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏帮助场景返回按钮可点击否
    def test_help_view_return_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        touchable = self.common.help_view_return_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏帮助场景返回按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏点击帮助场景返回按钮，帮助场景消失
    def test_return_btn_click_help_view_dispear(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        self.common.help_view_return_btn_click()
        sleep(1)
        dispear = self.common.help_view_dispear()
        try:
            self.assertEqual(dispear, None, "横屏点击帮助场景返回按钮，帮助场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏显示声音开关按钮
    def test_voice_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.voice_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏不会显示声音开关按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏声音开关按钮可点击否
    def test_voice_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.voice_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏声音开关按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏声音开关按钮点击后，按钮状态改变，声音关闭
    def test_voice_btn_click_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        voice_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()
        try:
            self.assertEqual(voice_status, "silience", "横屏声音开关按钮点击后，按钮状态不会改变！")
            self.assertEqual(sound_status, True, "横屏声音开关按钮点击后，声音不会关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏声音开关按钮点击两次后，按钮状态恢复打开，声音开启
    def test_voice_btn_click_twice_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        voice_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()
        try:
            self.assertEqual(voice_status, "normal", "横屏声音开关按钮点击两次后，按钮状态没有恢复打开！")
            self.assertEqual(sound_status, False, "横屏声音开关按钮点击两次后，声音没有开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏显示快速模式按钮
    def test_turbo_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.turbo_btn_visible()
        try:
            self.assertEqual(visible, True, "横屏不会显示快速模式按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏快速模式按钮默认状态为1x，滚轴滚动方式是普通速度
    def test_turbo_btn_default_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "1x", "横屏快速模式按钮默认状态不是1x")
            self.assertEqual(spin_status, False, "横屏滚轴默认滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏快速模式按钮可点击否
    def test_turbo_btn_touchable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.turbo_btn_touchable()
        try:
            self.assertEqual(touchable, True, "横屏快速模式按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏启动快速模式，快速模式按钮状态为2x，滚轴滚动方式为快速
    def test_turbo_btn_click_status(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.turbo_btn_click()
        sleep(1)
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "2x", "横屏启动快速模式，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "横屏启动快速模式，滚轴滚动方式不是快速！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏PC端显示返回大厅按钮
    def test_home_btn_visible(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.home_btn_visible()
        try:
            self.assertEqual(visible, False, "横屏PC端会显示返回大厅按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证横屏试玩显示游戏记录按钮
    def test_game_record_btn_enable(self):
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        enable = self.common.game_record_btn_enable()
        try:
            self.assertEqual(enable, False, "横屏试玩会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise 

    #
    #
    # ------------------------------------------------------------------------ 竖屏模式 ------------------------------------------------------------------------
    #
    #

    # 验证竖屏显示左侧主菜单按钮
    def test_main_menu_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.main_menu_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏不会显示主菜单按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏左侧主菜单默认为展开状态
    def test_main_menu_default_expand_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        expand = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(expand, "expandPPC", "竖屏左侧主菜单默认不是展开状态！")
            self.assertEqual(info_btn, True, "竖屏左侧主菜单展开时不会显示奖金表按钮！")
            self.assertEqual(help_btn, True, "竖屏左侧主菜单展开时不会显示帮助按钮！")
            self.assertEqual(voice_btn, True, "竖屏左侧主菜单展开时不会显示声音按钮！")
            self.assertEqual(turbo_btn, True, "竖屏左侧主菜单展开时不会显示快速按钮！")
            self.assertEqual(home_btn, False, "竖屏PC端左侧主菜单展开时，会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "竖屏试玩左侧主菜单展开时，会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏整个左侧主菜单可点击否
    def test_main_menu_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.main_menu_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏整个左侧主菜单不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击左侧主菜单按钮后是否折叠
    def test_main_menu_btn_click_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        status = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(status, "retractP", "竖屏点击左侧主菜单按钮后不会折叠！")
            self.assertEqual(info_btn, False, "竖屏左侧主菜单折叠时会显示奖金表按钮！")
            self.assertEqual(help_btn, False, "竖屏左侧主菜单折叠时会显示帮助按钮！")
            self.assertEqual(voice_btn, False, "竖屏左侧主菜单折叠时会显示声音按钮！")
            self.assertEqual(turbo_btn, False, "竖屏左侧主菜单折叠时会显示快速按钮！")
            self.assertEqual(home_btn, False, "竖屏PC端左侧主菜单折叠时会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "竖屏试玩左侧主菜单折叠时会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击左侧主菜单按钮两次后恢复展开状态
    def test_main_menu_btn_click_twice_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        self.common.main_menu_btn_click()
        sleep(1)
        status = self.common.main_menu_expand()
        info_btn = self.common.info_btn_visible()
        help_btn = self.common.help_btn_visible()
        voice_btn = self.common.voice_btn_visible()
        turbo_btn = self.common.turbo_btn_visible()
        home_btn = self.common.home_btn_visible()
        game_record_btn = self.common.game_record_btn_enable()
        try:
            self.assertEqual(status, "expandPPC", "竖屏点击左侧主菜单按钮两次后不会恢复展开状态！")
            self.assertEqual(info_btn, True, "竖屏点击左侧主菜单按钮两次后不会显示奖金表按钮！")
            self.assertEqual(help_btn, True, "竖屏点击左侧主菜单按钮两次后不会显示帮助按钮！")
            self.assertEqual(voice_btn, True, "竖屏点击左侧主菜单按钮两次后不会显示声音按钮！")
            self.assertEqual(turbo_btn, True, "竖屏点击左侧主菜单按钮两次后不会显示快速按钮！")
            self.assertEqual(home_btn, False, "竖屏PC端点击左侧主菜单按钮两次后，会显示返回大厅按钮！")
            self.assertEqual(game_record_btn, False, "竖屏试玩点击左侧主菜单按钮两次后，会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏显示奖金表按钮
    def test_info_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.info_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏奖金表按钮默认不会显示！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏奖金表按钮可点击否
    def test_info_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.info_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏奖金表按钮不能点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击奖金表按钮后，显示奖金表场景
    def test_info_btn_click_info_view_showing_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        showing = self.common.info_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏点击奖金表按钮后，不会显示奖金表场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏奖金表场景显示返回按钮
    def test_info_view_return_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        visible = self.common.info_view_return_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏奖金表场景，不会显示返回按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏奖金表场景返回按钮可点击否
    def test_info_view_return_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        touchable = self.common.info_view_return_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏奖金表场景返回按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击奖金表返回按钮，奖金表场景消失
    def test_return_btn_click_info_view_dispear_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.info_btn_click()
        sleep(1)
        self.common.info_view_return_btn_click()
        sleep(1)
        dispear = self.common.info_view_dispear()
        try:
            self.assertEqual(dispear, None, "竖屏点击奖金表返回按钮，奖金表场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏显示帮助按钮
    def test_help_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.help_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏不会显示帮助按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏帮助按钮可点击否
    def test_help_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.help_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏帮助按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击帮助按钮后，显示帮助场景
    def test_help_btn_click_help_view_showing_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        showing = self.common.help_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏点击帮助按钮后，不会显示帮助场景！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏帮助场景显示返回按钮
    def test_help_view_return_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        visible = self.common.help_view_return_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏帮助场景不会显示返回按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏帮助场景返回按钮可点击否
    def test_help_view_return_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        touchable = self.common.help_view_return_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏帮助场景返回按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏点击帮助场景返回按钮，帮助场景消失
    def test_return_btn_click_help_view_dispear_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.help_btn_click()
        sleep(1)
        self.common.help_view_return_btn_click()
        sleep(1)
        dispear = self.common.help_view_dispear()
        try:
            self.assertEqual(dispear, None, "竖屏点击帮助场景返回按钮，帮助场景不会消失！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏显示声音开关按钮
    def test_voice_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.voice_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏不会显示声音开关按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏声音开关按钮可点击否
    def test_voice_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.voice_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏声音开关按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏声音开关按钮点击后，按钮状态改变，声音关闭
    def test_voice_btn_click_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        voice_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()
        try:
            self.assertEqual(voice_status, "silience", "竖屏声音开关按钮点击后，按钮状态不会改变！")
            self.assertEqual(sound_status, True, "竖屏声音开关按钮点击后，声音不会关闭！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏声音开关按钮点击两次后，按钮状态恢复打开，声音开启
    def test_voice_btn_click_twice_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        self.common.voice_btn_click()
        sleep(1)
        voice_status = self.common.voice_btn_status()
        sound_status = self.common.sound_status()
        try:
            self.assertEqual(voice_status, "normal", "竖屏声音开关按钮点击两次后，按钮状态没有恢复打开！")
            self.assertEqual(sound_status, False, "竖屏声音开关按钮点击两次后，声音没有开启！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏显示快速模式按钮
    def test_turbo_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.turbo_btn_visible()
        try:
            self.assertEqual(visible, True, "竖屏不会显示快速模式按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏快速模式按钮默认状态为1x，滚轴滚动方式是普通速度
    def test_turbo_btn_default_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "1x", "竖屏快速模式按钮默认状态不是1x")
            self.assertEqual(spin_status, False, "竖屏滚轴默认滚动方式不是普通速度！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏快速模式按钮可点击否
    def test_turbo_btn_touchable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        touchable = self.common.turbo_btn_touchable()
        try:
            self.assertEqual(touchable, True, "竖屏快速模式按钮不可点击！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏启动快速模式，快速模式按钮状态为2x，滚轴滚动方式为快速
    def test_turbo_btn_click_status_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        self.common.turbo_btn_click()
        sleep(1)
        turbo_btn_status = self.common.turbo_btn_status()
        spin_status = self.common.spin_is_in_turbo()
        try:
            self.assertEqual(turbo_btn_status, "2x", "竖屏启动快速模式，快速模式按钮状态不是2x！")
            self.assertEqual(spin_status, True, "竖屏启动快速模式，滚轴滚动方式不是快速！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏PC端显示返回大厅按钮
    def test_home_btn_visible_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        visible = self.common.home_btn_visible()
        try:
            self.assertEqual(visible, False, "竖屏PC端会显示返回大厅按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise

    # 验证竖屏试玩显示游戏记录按钮
    def test_game_record_btn_enable_portrait(self):
        self.common.portrait()
        self.common.loading_bar()
        sleep(1)
        self.common.sound_view_yes_btn_click()
        sleep(1)
        enable = self.common.game_record_btn_enable()
        try:
            self.assertEqual(enable, False, "竖屏试玩会显示游戏记录按钮！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
