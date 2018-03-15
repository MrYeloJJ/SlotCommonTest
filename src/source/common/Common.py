# coding=utf-8

""""" 公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作 """""

from src.source.common.Data import Data
from src.lib.HTMLTestReportCN import DirAndFiles
from time import sleep


class Common(object):
    # 初始化browser、lobby和game等数据
    def __init__(self, browser):
        self.message = Data().get_message()
        self.lobby = self.message["lobby"]
        self.game = self.message["game"]
        self.browser = browser
        self.daf = DirAndFiles()

    # 进入大厅并打开游戏
    def start(self):
        self.get_lobby()
        self.switch_page()
        self.find_game()
        self.switch_game_window()

    # 进入大厅并判断是否正常进入
    def get_lobby(self):
        try:
            self.browser.get(self.lobby)
            sleep(1)
            title = self.browser.title
            assert title == "as", "进入大厅失败！"
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 切换到slot标签页
    def switch_page(self):
        try:
            sleep(1)
            self.browser.find_element_by_css_selector("a[href = '#type_107']").click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 根据游戏名字查找并打开游戏
    def find_game(self):
        try:
            sleep(1)
            self.browser.find_element_by_link_text(self.game).click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 切换到游戏窗口
    def switch_game_window(self):
        try:
            game_window = self.browser.window_handles[-1]
            self.browser.switch_to.window(game_window)
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 设置当前分辨率为横屏
    def landscape(self):
        self.browser.set_window_size(width=1100, height=894, windowHandle="current")

    # 设置当前分辨率为竖屏
    def portrait(self):
        self.browser.set_window_size(width=413, height=894, windowHandle="current")

    #
    #
    # ------------------------------------------------------------------------ 载入场景 ------------------------------------------------------------------------
    #
    #

    # 进入载入场景
    def loading_view_showing(self):
        try:
            showing = self.browser.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                  "return loading.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景进度条
    def loading_bar(self):

        while True:
            try:
                progress_bar = self.browser.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                           "return loading.contentPane.m_progressBar.value;")
            except Exception:
                self.daf.get_screenshot(self.browser)
                raise

            if progress_bar == 100:
                try:
                    tip = self.browser.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                      "return loading.contentPane.m_progressBar.m_title.textField.text;")
                    return tip
                except Exception:
                    self.daf.get_screenshot(self.browser)
                    raise

    # 载入场景消失
    def loading_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 主视图和公共视图 ------------------------------------------------------------------------
    #
    #

    # 显示主视图
    def main_view_visible(self):
        try:
            main_view = self.browser.execute_script("return UIManager.instance.mainViewContainer.visible;")
            return main_view
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景和公共模块
    def common_view_visible(self):
        try:
            common_view = self.browser.execute_script("return UIManager.instance.commonView.visible;")
            return common_view
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 声音开关提示窗口 ------------------------------------------------------------------------
    #
    #

    # 显示声音开关提示窗口
    def sound_window_showing(self):
        try:
            showing = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer);"
                                                  "return soundWindow.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口消失
    def sound_window_dispear(self):
        try:
            dispear = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer);"
                                                  "return soundWindow;")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口的标题文字
    def sound_window_text(self):
        try:
            sound_window_text = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                            "return soundWindow.m_n4.text;")
            return sound_window_text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮
    def sound_window_toggle_button_visible(self):
        try:
            toggle_button_visible = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                                "return soundWindow.m_showingToggle.visible;")
            return toggle_button_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮可点击
    def sound_window_toggle_button_touchable(self):
        try:
            toggle_button_touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                                  "return soundWindow.m_showingToggle.touchable;")
            return toggle_button_touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮的文字
    def sound_window_toggle_text(self):
        try:
            toggle_text = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                      "return soundWindow.m_n7.text;")
            return toggle_text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的切换按钮
    def sound_window_toggle_click(self):
        try:
            toggle_click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                       "return soundWindow.m_showingToggle.displayObject.event('click');")
            return toggle_click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮状态，0代表开启，1代表关闭
    def sound_window_toggle_status(self):
        try:
            toggle_status = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                        "return soundWindow.m_showingToggle.m_button.selectedIndex;")
            return toggle_status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “是” 按钮
    def sound_window_yes_button_showing(self):
        try:
            yes_button_showing = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                             "return soundWindow.m_yesBtn.visible;")
            return yes_button_showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击
    def sound_window_yes_button_touchable(self):
        try:
            yes_button_touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                               "return soundWindow.m_yesBtn.touchable;")
            return yes_button_touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮
    def sound_window_yes_button_click(self):
        try:
            yes_button_click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                           "return soundWindow.m_yesBtn.displayObject.event('click');")
            return yes_button_click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “否” 按钮
    def sound_window_no_button_showing(self):
        try:
            no_button_showing = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                            "return soundWindow.m_noBtn.visible;")
            return no_button_showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击
    def sound_window_no_button_touchable(self):
        try:
            no_button_touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                              "return soundWindow.m_noBtn.touchable;")
            return no_button_touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮
    def sound_window_no_button_click(self):
        try:
            no_button_click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                          "return soundWindow.m_noBtn.displayObject.event('click');")
            return no_button_click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 左侧主菜单 ------------------------------------------------------------------------
    #
    #

    # 显示左侧主菜单
    def main_menu_button_visible(self):
        try:
            main_menu_button_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.visible;")
            return main_menu_button_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 左侧主菜单展开状态，1为折叠，2为展开
    def main_menu_expand(self):
        try:
            expand = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_expandCtl.selectedIndex;")
            return expand
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 左侧主菜单展开方向，往下为1，往右为4
    def main_menu_expand_direction(self):
        try:
            direction = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_expandCtl.selectedIndex;")
            return direction
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击左侧主菜单按钮
    def main_menu_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示奖金表按钮
    def info_button_visible(self):
        try:
            visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.visible;")
            return visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 奖金表按钮可点击否
    def info_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击奖金表按钮
    def info_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示帮助按钮
    def help_button_visible(self):
        try:
            visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.visible;")
            return visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助按钮可点击否
    def help_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击帮助按钮
    def help_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关按钮
    def voice_button_visible(self):
        try:
            visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.visible;")
            return visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关按钮可点击否
    def voice_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关按钮
    def voice_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关按钮状态，打开状态为0，关闭状态为1
    def voice_button_status(self):
        try:
            status = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.m_iconCtl.selectedIndex;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示快速切换按钮
    def turbo_button_visible(self):
        try:
            visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.visible;")
            return visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速切换按钮可点击否
    def turbo_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击快速切换按钮
    def turbo_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速切换按钮状态，普通转为0，快速转为1
    def turbo_button_status(self):
        try:
            status = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.m_iconCtl.selectedIndex;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

