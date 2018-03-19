# coding=utf-8

""""" 公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作 """""

from src.source.common.Config import Config
from src.lib.HTMLTestReportCN import DirAndFiles
from time import sleep


class Common(object):
    # 初始化browser、lobby和game等数据
    def __init__(self, browser):
        self.message = Config().get_message()
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
            new_handle = self.browser.window_handles[-1]
            self.browser.switch_to.window(new_handle)
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 设置当前分辨率为横屏
    def landscape(self):
        self.browser.set_window_size(width=1100, height=894)

    # 设置当前分辨率为竖屏
    def portrait(self):
        self.browser.set_window_size(width=413, height=894)

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
            final_visible = self.browser.execute_script("return UIManager.instance.mainViewContainer.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景和公共模块
    def common_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 声音开关提示窗口 ------------------------------------------------------------------------
    #
    #

    # 显示声音开关提示窗口
    def sound_view_showing(self):
        try:
            showing = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer);"
                                                  "return soundWindow.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口消失
    def sound_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口的标题文字
    def sound_view_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                               "return soundWindow.m_n4.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮
    def sound_view_toggle_button_visible(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                        "return soundWindow.m_showingToggle.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮可点击
    def sound_view_toggle_button_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                    "return soundWindow.m_showingToggle.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮的文字
    def sound_view_toggle_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                               "return soundWindow.m_n7.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的切换按钮
    def sound_view_toggle_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                "return soundWindow.m_showingToggle.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮状态，0代表开启，1代表关闭
    def sound_view_toggle_status(self):
        try:
            status = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                 "return soundWindow.m_showingToggle.m_button.selectedIndex;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “是” 按钮
    def sound_view_yes_button_showing(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                        "return soundWindow.m_yesBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击
    def sound_view_yes_button_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                    "return soundWindow.m_yesBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮
    def sound_view_yes_button_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                "return soundWindow.m_yesBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “否” 按钮
    def sound_view_no_button_showing(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                        "return soundWindow.m_noBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击
    def sound_view_no_button_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                    "return soundWindow.m_noBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮
    def sound_view_no_button_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = UIManager.instance.getWindowByName(Common.FUIEnableSoundView.URL, UIManager.instance.tipsLayer).contentPane;"
                                                "return soundWindow.m_noBtn.displayObject.event('click');")
            return click
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
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.finalVisible;")
            return final_visible
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
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.finalVisible;")
            return final_visible
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
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.finalVisible;")
            return final_visible
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
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.finalVisible;")
            return final_visible
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
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.finalVisible;")
            return final_visible
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

    # 显示返回大厅按钮
    def home_button_visible(self):
        try:
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 返回大厅按钮可点击否
    def home_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击返回大厅按钮
    def home_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示游戏记录按钮
    def game_record_button_enable(self):
        try:
            enable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.enabled;")
            return enable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 游戏记录按钮可点击否
    def game_record_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击游戏记录按钮
    def game_record_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 右侧线数线注设置 ------------------------------------------------------------------------
    #
    #

    # 显示线数线注设置按钮
    def setting_button_visible(self):
        try:
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置按钮可点击否
    def setting_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击线数线注设置按钮
    def setting_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示线数线注设置面板
    def setting_view_showing(self):
        try:
            showing = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer);"
                                                  "return settingView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示关闭按钮
    def setting_view_close_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return settingView.m_frame.m_closeButton.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，关闭按钮可点击否
    def setting_view_close_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return settingView.m_frame.m_closeButton.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击关闭按钮
    def setting_view_close_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return settingView.m_frame.m_closeButton.displayObject.event('click')")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板消失
    def setting_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线数标题
    def setting_view_line_num_text(self):
        try:
            text = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                               "return settingView.m_n52.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线数数值
    def setting_view_line_num(self):
        try:
            num = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                              "return settingView.m_lineNumLabel.textField.text;")
            return num
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线数 - 按钮
    def setting_view_line_num_min_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return settingView.m_lineMinusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线数 - 按钮 可点击否
    def setting_view_line_num_min_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return settingView.m_lineMinusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线数 - 按钮
    def setting_view_line_num_min_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return settingView.m_lineMinusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线数 + 按钮
    def setting_view_line_num_plus_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return settingView.m_linePlusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线数 + 按钮 可点击否
    def setting_view_line_num_plus_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return settingView.m_linePlusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线数 + 按钮
    def setting_view_line_num_plus_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return settingView.m_linePlusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线注标题
    def setting_view_line_cost_text(self):
        try:
            text = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                               "return settingView.m_n54.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线注数值
    def setting_view_line_cost(self):
        try:
            num = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                              "return settingView.m_lineCostLabel.textField.text;")
            return num
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线注 - 按钮
    def setting_view_line_cost_min_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return settingView.m_lineCostMinusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线注 - 按钮 可点击否
    def setting_view_line_cost_min_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return settingView.m_lineCostMinusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线注 - 按钮
    def setting_view_line_cost_min_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return settingView.m_lineCostMinusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线注 + 按钮
    def setting_view_line_cost_plus_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return settingView.m_lineCostPlusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线注 + 按钮 可点击否
    def setting_view_line_cost_plus_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return settingView.m_lineCostPlusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线注 + 按钮
    def setting_view_line_cost_plus_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = UIManager.instance.getWindowByName(Common.FUILineSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return settingView.m_lineCostPlusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 右侧自动游戏设置 ------------------------------------------------------------------------
    #
    #

    # 显示自动游戏按钮
    def auto_game_button_visible(self):
        try:
            final_visible = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏按钮可点击否
    def auto_game_button_touchable(self):
        try:
            touchable = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击自动游戏按钮
    def auto_game_button_click(self):
        try:
            click = self.browser.execute_script("return UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示自动游戏设置面板
    def auto_game_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer);")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示关闭按钮
    def auto_game_view_close_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.m_frame.m_closeButton.finalVisible")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，关闭按钮可点击否
    def auto_game_view_close_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return autoGameView.m_frame.m_closeButton.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，点击关闭按钮
    def auto_game_view_close_btn_click(self):
        try:
            click = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                "return autoGameView.m_frame.m_closeButton.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板消失
    def auto_game_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示旋转小图标
    def auto_game_view_icon_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.m_n50.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，自动次数文字
    def auto_game_view_auto_time_text(self):
        try:
            text = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                               "return autoGameView.m_autoTimesLabel.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示拖动条
    def auto_game_view_slider_bar_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.m_slider.m_bar.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示拖动条按钮
    def auto_game_view_slider_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.m_slider.m_grip.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示开始按钮
    def auto_game_view_start_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.m_startBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，开始按钮文字
    def auto_game_view_start_btn_text(self):
        try:
            text = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                               "return autoGameView.m_startBtn.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise 

    # 自动游戏设置面板，开始按钮可点击否
    def auto_game_view_start_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var autoGameView = UIManager.instance.getWindowByName(Common.FUIAutoGameSettingView.URL, UIManager.instance.commonUILayer).contentPane;"
                                                    "return autoGameView.m_startBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    












































