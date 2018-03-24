# coding=utf-8

""""" 公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作 """""

from src.source.common.Config import Config
from src.lib.HTMLTestReportCN import DirAndFiles
from time import sleep


class Common(object):
    # 初始化browser、lobby和game等数据
    def __init__(self, browser):
        self.message = Config().get_message()
        self.lobby = self.message["lobby"]                      # 大厅地址
        self.game_id = self.message["game_id"]                  # 游戏id
        self.game_name = self.message["game_name"]              # 游戏名字
        self.full_line = self.message["full_line"]              # 是否满线
        self.line_num_min = self.message["line_num_min"]        # 最小线数
        self.line_num_max = self.message["line_num_max"]        # 最大线数
        self.line_cost = self.message["line_cost"]              # 所有线注
        self.auto_game_times = self.message["auto_game_times"]  # 所有自动游戏次数
        self.browser = browser
        self.daf = DirAndFiles()
        self.add_script = "window.frames[0].frames."                                    # 多开情况需改为 "window.frames[0].frames."

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
            self.browser.find_element_by_link_text(self.game_name).click()
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
    # ------------------------------------------------------------------------ 游戏基本参数 ------------------------------------------------------------------------
    #
    #

    # 游戏id, [tuple]
    def get_game_id(self):
        try:
            game_id = self.browser.execute_script("return " + self.add_script + "DataGame.getIds(" + self.add_script + "DataGame.getKeys())[0];")
            return game_id
        except Exception:
            raise

    # 游戏名字, [str]
    def get_game_name(self):
        try:
            game_name = self.browser.execute_script("return " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['name'];")
            return game_name
        except Exception:
            raise

    # 最大线数, [tuple]
    def get_max_line_num(self):
        try:
            max_line_num = self.browser.execute_script("return " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['maxLines'];")
            return max_line_num
        except Exception:
            raise

    # 最小线数, [tuple]
    def get_min_line_num(self):
        try:
            min_line_num = self.browser.execute_script("return " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['minLines'];")
            return min_line_num
        except Exception:
            raise

    # 线注列表, [list]
    def get_line_cost_list(self):
        try:
            line_cost_list = self.browser.execute_script("return " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['lineValue'];")
            return tuple(line_cost_list)
        except Exception:
            raise

    # 自动游戏次数列表, [list]
    def get_auto_game_times_list(self):
        try:
            auto_game_times_list = self.browser.execute_script("return " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['autoSpinTimes'];")
            return tuple(auto_game_times_list)
        except Exception:
            raise

    #
    #
    # ------------------------------------------------------------------------ 载入场景 ------------------------------------------------------------------------
    #
    #

    # 进入载入场景, [tuple: True, False]
    def loading_view_showing(self):
        try:
            showing = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                  + self.add_script + "UIManager.instance.commonView);return loading.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景进度条, [str]
    def loading_bar(self):

        while True:
            try:
                progress_bar = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                           + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.value;")
            except Exception:
                self.daf.get_screenshot(self.browser)
                raise

            if progress_bar == 100:
                try:
                    tip = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                      + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.m_title.textField.text;")
                    return tip
                except Exception:
                    self.daf.get_screenshot(self.browser)
                    raise

    # 载入场景消失, [tuple: None]
    def loading_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                  + self.add_script + "UIManager.instance.commonView);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 主视图和公共视图 ------------------------------------------------------------------------
    #
    #

    # 显示主视图, [tuple: True, False]
    def main_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainViewContainer.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景和公共模块, [tuple: True, False]
    def common_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示滚轴, [tuple: True, False]
    def slot_machine_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.contentPane.m_slotMachineView.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景背景图片, [tuple: True, False]
    def bg_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.contentPane.m_bgView.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景底部背景图片, [tuple: True, False]
    def bottom_bg_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.contentPane.m_bottomBgP.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示灰色蒙板, [tuple: True, False]
    def mask_view_showing(self):
        try:
            showing = self.browser.execute_script("return " + self.add_script + "UIManager.instance.maskView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击灰色蒙板, [tuple: True, False]
    def mask_view_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.maskView.displayObject.event('click')")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 声音开关提示窗口 ------------------------------------------------------------------------
    #
    #

    # 显示声音开关提示窗口, [tuple: True, False]
    def sound_view_showing(self):
        try:
            showing = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);return soundWindow.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口消失, [tuple: None]
    def sound_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口的标题文字, [str]
    def sound_view_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                               + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_n4.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，显示切换按钮, [tuple: True, False]
    def sound_view_toggle_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_showingToggle.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮可点击, [tuple: True, False]
    def sound_view_toggle_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_showingToggle.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮的文字, [str]
    def sound_view_toggle_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                               + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_n7.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的切换按钮, [tuple: True, False]
    def sound_view_toggle_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_showingToggle.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，切换按钮状态, [str: down, up]
    def sound_view_toggle_status(self):
        try:
            status = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                 + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_showingToggle.m_button.selectedPage;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “是” 按钮, [tuple: True, False]
    def sound_view_yes_btn_showing(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_yesBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “是” 按钮, [str: 是]
    def sound_view_yes_btn_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                               + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_yesBtn.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击, [tuple: True, False]
    def sound_view_yes_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_yesBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮, [tuple: True, False]
    def sound_view_yes_btn_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_yesBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “否” 按钮, [tuple: True, False]
    def sound_view_no_btn_showing(self):
        try:
            final_visible = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_noBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关提示窗口的 “否” 按钮, [str: 否]
    def sound_view_no_btn_text(self):
        try:
            text = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                               + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_noBtn.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关提示窗口，“是”按钮可点击, [tuple: True, False]
    def sound_view_no_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_noBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关提示窗口的 “是” 按钮, [tuple: True, False]
    def sound_view_no_btn_click(self):
        try:
            click = self.browser.execute_script("var soundWindow = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableSoundView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return soundWindow.m_noBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 左侧主菜单 ------------------------------------------------------------------------
    #
    #

    # 显示左侧主菜单, [tuple: True, False]
    def main_menu_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 左侧主菜单展开状态, [str: retractL, expandLPC, retractP, expandPPC] expandLPC：横展， retractL：横叠， expandPPC：竖展， retractP：竖叠
    def main_menu_expand(self):
        try:
            expand = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_expandCtl.selectedPage;")
            return expand
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 整个左侧菜单可点击否, [tuple: True, False]
    def main_menu_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击左侧主菜单按钮, [tuple: True, False]
    def main_menu_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示奖金表按钮, [tuple: True, False]
    def info_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 奖金表按钮可点击否, [tuple: True, False]
    def info_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击奖金表按钮, [tuple: True, False]
    def info_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_infoBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示奖金表场景, [tuple: True, False]
    def info_view_showing(self):
        try:
            showing = self.browser.execute_script("var infoView = (function () {var CustomInfoViewClass = " + self.add_script + "Application.instance.mainModule.FUIInfoView; var url;"
                                                  "if(CustomInfoViewClass){url = CustomInfoViewClass.URL;}"
                                                  "else if(" + self.add_script + "Application.instance.mainModule.InfoView['templateType'] == 'NewInfoView'){"
                                                  "url = " + self.add_script + "Common.FUINewInfoView.URL;}"
                                                  "else{url = " + self.add_script + "Common.FUIInfoView.URL;}"
                                                  "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                  "return infoView.isShowing")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示奖金表场景的返回按钮, [tuple: True, False]
    def info_view_return_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var infoView = (function () {var CustomInfoViewClass = " + self.add_script + "Application.instance.mainModule.FUIInfoView; var url;"
                                                        "if(CustomInfoViewClass){url = CustomInfoViewClass.URL;}"
                                                        "else if(" + self.add_script + "Application.instance.mainModule.InfoView['templateType'] == 'NewInfoView'){"
                                                        "url = " + self.add_script + "Common.FUINewInfoView.URL;}"
                                                        "else{url = " + self.add_script + "Common.FUIInfoView.URL;}"
                                                        "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                        "return infoView.contentPane.m_returnBtnContainer.m_returnBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 奖金表场景，返回按钮可点击否, [tuple: True, False]
    def info_view_return_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var infoView = (function () {var CustomInfoViewClass = " + self.add_script + "Application.instance.mainModule.FUIInfoView; var url;"
                                                    "if(CustomInfoViewClass){url = CustomInfoViewClass.URL;}"
                                                    "else if(" + self.add_script + "Application.instance.mainModule.InfoView['templateType'] == 'NewInfoView'){"
                                                    "url = " + self.add_script + "Common.FUINewInfoView.URL;}"
                                                    "else{url = " + self.add_script + "Common.FUIInfoView.URL;}"
                                                    "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                    "return infoView.contentPane.m_returnBtnContainer.m_returnBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 奖金表场景，点击返回按钮, [tuple: True, False]
    def info_view_return_btn_click(self):
        try:
            click = self.browser.execute_script("var infoView = (function () {var CustomInfoViewClass = " + self.add_script + "Application.instance.mainModule.FUIInfoView; var url;"
                                                "if(CustomInfoViewClass){url = CustomInfoViewClass.URL;}"
                                                "else if(" + self.add_script + "Application.instance.mainModule.InfoView['templateType'] == 'NewInfoView'){"
                                                "url = " + self.add_script + "Common.FUINewInfoView.URL;}"
                                                "else{url = " + self.add_script + "Common.FUIInfoView.URL;}"
                                                "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                "return infoView.contentPane.m_returnBtnContainer.m_returnBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 奖金表场景消失, [tuple: None]
    def info_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return (function () {var CustomInfoViewClass = " + self.add_script + "Application.instance.mainModule.FUIInfoView; var url;"
                                                  "if(CustomInfoViewClass){url = CustomInfoViewClass.URL;}"
                                                  "else if(" + self.add_script + "Application.instance.mainModule.InfoView['templateType'] == 'NewInfoView'){"
                                                  "url = " + self.add_script + "Common.FUINewInfoView.URL;}"
                                                  "else{url = " + self.add_script + "Common.FUIInfoView.URL;}"
                                                  "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示帮助按钮, [tuple: True, False]
    def help_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助按钮可点击否, [tuple: True, False]
    def help_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击帮助按钮, [tuple: True, False]
    def help_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_helpBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示帮助场景, [tuple: True, False]
    def help_view_showing(self):
        try:
            showing = self.browser.execute_script("var helpView = (function () {var CustomHelpClass = " + self.add_script + "Application.instance.mainModule.FUIHelpView; var url;"
                                                  "if(CustomHelpClass){url = CustomHelpClass.URL }"
                                                  "else if(" + self.add_script + "Application.instance.mainModule.HelpView['templateType'] == 'NewHelpView'){"
                                                  "url = " + self.add_script + "Common.FUINewHelpView.URL;}"
                                                  "else{url = " + self.add_script + "Common.FUIHelpView.URL}"
                                                  "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                  "return helpView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助场景，显示返回按钮, [tuple: True, False]
    def help_view_return_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var helpView = (function () {var CustomHelpClass = " + self.add_script + "Application.instance.mainModule.FUIHelpView; var url;"
                                                        "if(CustomHelpClass){url = CustomHelpClass.URL }"
                                                        "else if(" + self.add_script + "Application.instance.mainModule.HelpView['templateType'] == 'NewHelpView'){"
                                                        "url = " + self.add_script + "Common.FUINewHelpView.URL;}"
                                                        "else{url = " + self.add_script + "Common.FUIHelpView.URL}"
                                                        "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                        "return helpView.contentPane.m_returnBtnContainer.m_returnBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助场景，返回按钮可点击否, [tuple: True, False]
    def help_view_return_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var helpView = (function () {var CustomHelpClass = " + self.add_script + "Application.instance.mainModule.FUIHelpView; var url;"
                                                    "if(CustomHelpClass){url = CustomHelpClass.URL }"
                                                    "else if(" + self.add_script + "Application.instance.mainModule.HelpView['templateType'] == 'NewHelpView'){"
                                                    "url = " + self.add_script + "Common.FUINewHelpView.URL;}"
                                                    "else{url = " + self.add_script + "Common.FUIHelpView.URL}"
                                                    "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                    "return helpView.contentPane.m_returnBtnContainer.m_returnBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助场景，点击返回按钮, [tuple: True, False]
    def help_view_return_btn_click(self):
        try:
            click = self.browser.execute_script("var helpView = (function () {var CustomHelpClass = " + self.add_script + "Application.instance.mainModule.FUIHelpView; var url;"
                                                "if(CustomHelpClass){url = CustomHelpClass.URL }"
                                                "else if(" + self.add_script + "Application.instance.mainModule.HelpView['templateType'] == 'NewHelpView'){"
                                                "url = " + self.add_script + "Common.FUINewHelpView.URL;}"
                                                "else{url = " + self.add_script + "Common.FUIHelpView.URL}"
                                                "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());"
                                                "return helpView.contentPane.m_returnBtnContainer.m_returnBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 帮助场景消失, [tuple: None]
    def help_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return (function () {var CustomHelpClass = " + self.add_script + "Application.instance.mainModule.FUIHelpView; var url;"
                                                  "if(CustomHelpClass){url = " + self.add_script + "CustomHelpClass.URL }"
                                                  "else if(" + self.add_script + "Application.instance.mainModule.HelpView['templateType'] == 'NewHelpView'){"
                                                  "url = " + self.add_script + "Common.FUINewHelpView.URL;}"
                                                  "else{url = " + self.add_script + "Common.FUIHelpView.URL}"
                                                  "return " + self.add_script + "UIManager.instance.getWindowByName(url);}());")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示声音开关按钮, [tuple: True, False]
    def voice_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关按钮可点击否, [tuple: True, False]
    def voice_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击声音开关按钮, [tuple: True, False]
    def voice_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关按钮状态, [str: normal, silience]
    def voice_btn_status(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_voiceBtn.m_iconCtl.selectedPage;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 声音开关、播放状态, [tuple: True, False], true为关闭，false为开启
    def sound_status(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "SoundManager.instance.ismanualColseMusic;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示快速模式按钮, [tuple: True, False]
    def turbo_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式按钮可点击否, [tuple: True, False]
    def turbo_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击快速模式按钮, [tuple: True, False]
    def turbo_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式按钮状态, [str: 1x, 2x]
    def turbo_btn_status(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_turboBtn.m_iconCtl.selectedPage;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示返回大厅按钮, [tuple: True, False]
    def home_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 返回大厅按钮可点击否, [tuple: True, False]
    def home_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击返回大厅按钮, [tuple: True, False]
    def home_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_homeBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示游戏记录按钮, [tuple: True, False]
    def game_record_btn_enable(self):
        try:
            enable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.enabled;")
            return enable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 游戏记录按钮可点击否, [tuple: True, False]
    def game_record_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击游戏记录按钮, [tuple: True, False]
    def game_record_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 右侧线数线注设置 ------------------------------------------------------------------------
    #
    #

    # 显示线数线注设置按钮, [tuple: True, False]
    def setting_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置按钮可点击否, [tuple: True, False]
    def setting_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击线数线注设置按钮, [tuple: True, False]
    def setting_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_settingBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示线数线注设置面板, [tuple: True, False]
    def setting_view_showing(self):
        try:
            showing = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                  + self.add_script + "UIManager.instance.commonUILayer);return settingView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示关闭按钮, [tuple: True, False]
    def setting_view_close_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_frame.m_closeButton.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，关闭按钮可点击否, [tuple: True, False]
    def setting_view_close_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_frame.m_closeButton.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击关闭按钮, [tuple: True, False]
    def setting_view_close_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_frame.m_closeButton.displayObject.event('click')")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板消失, [tuple: None]
    def setting_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                  + self.add_script + "UIManager.instance.commonUILayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线数标题, [str]
    def setting_view_line_num_text(self):
        try:
            text = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                               + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_n52.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线数数值, [str]
    def setting_view_line_num(self):
        try:
            num = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                              + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineNumLabel.textField.text;")
            return num
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线数 - 按钮, [tuple: True, False]
    def setting_view_line_num_min_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineMinusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线数 - 按钮 可点击否, [tuple: True, False]
    def setting_view_line_num_min_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineMinusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线数 - 按钮, [tuple: True, False]
    def setting_view_line_num_min_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineMinusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线数 + 按钮, [tuple: True, False]
    def setting_view_line_num_plus_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_linePlusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线数 + 按钮 可点击否, [tuple: True, False]
    def setting_view_line_num_plus_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_linePlusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线数 + 按钮, [tuple: True, False]
    def setting_view_line_num_plus_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_linePlusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线注标题, [str]
    def setting_view_line_cost_text(self):
        try:
            text = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                               + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_n54.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板的线注数值, [str]
    def setting_view_line_cost(self):
        try:
            num = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                              + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostLabel.textField.text;")
            return num
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线注 - 按钮, [tuple: True, False]
    def setting_view_line_cost_min_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostMinusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线注 - 按钮 可点击否, [tuple: True, False]
    def setting_view_line_cost_min_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostMinusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线注 - 按钮, [tuple: True, False]
    def setting_view_line_cost_min_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostMinusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，显示线注 + 按钮, [tuple: True, False]
    def setting_view_line_cost_plus_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostPlusBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，线注 + 按钮 可点击否, [tuple: True, False]
    def setting_view_line_cost_plus_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostPlusBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数线注设置面板，点击 线注 + 按钮, [tuple: True, False]
    def setting_view_line_cost_plus_btn_click(self):
        try:
            click = self.browser.execute_script("var settingView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILineSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return settingView.m_lineCostPlusBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 右侧自动游戏设置 ------------------------------------------------------------------------
    #
    #

    # 显示自动游戏按钮, [tuple: True, False]
    def auto_game_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏按钮可点击否, [tuple: True, False]
    def auto_game_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击自动游戏按钮, [tuple: True, False]
    def auto_game_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_autoGameSettingBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示自动游戏设置面板, [tuple: True, False]
    def auto_game_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer);")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示关闭按钮, [tuple: True, False]
    def auto_game_view_close_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_frame.m_closeButton.finalVisible")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，关闭按钮可点击否, [tuple: True, False]
    def auto_game_view_close_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_frame.m_closeButton.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，点击关闭按钮, [tuple: True, False]
    def auto_game_view_close_btn_click(self):
        try:
            click = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_frame.m_closeButton.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板消失, [tuple: None]
    def auto_game_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                  + self.add_script + "UIManager.instance.commonUILayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示旋转小图标, [tuple: True, False]
    def auto_game_view_icon_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_n50.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，自动次数文字, [str]
    def auto_game_view_auto_time_text(self):
        try:
            text = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                               + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_autoTimesLabel.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示拖动条, [tuple: True, False]
    def auto_game_view_slider_bar_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_slider.m_bar.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示拖动条按钮, [tuple: True, False]
    def auto_game_view_slider_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_slider.m_grip.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，改变自动次数，并返回面板上的自动次数, [str: “25次旋转”]
    def auto_game_view_change_auto_time(self, index):
        try:
            text = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                               + self.add_script + "UIManager.instance.commonUILayer).contentPane;"
                                               "var i = " + str(index) + ";" + self.add_script + "SpinManager.instance.autoTimes = " + self.add_script + "DataGame.getData("
                                               + self.add_script + "DataGame.getKeys())['autoSpinTimes'][i];"
                                               "autoGameView.m_slider.value = 100 * i / " + self.add_script + "DataGame.getData(DataGame.getKeys())['autoSpinTimes'].length;"
                                               "return autoGameView.m_autoTimesLabel.textField.text")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，显示开始按钮, [tuple: True, False]
    def auto_game_view_start_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_startBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，开始按钮文字, [str]
    def auto_game_view_start_btn_text(self):
        try:
            text = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                               + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_startBtn.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，开始按钮可点击否, [tuple: True, False]
    def auto_game_view_start_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                    + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_startBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，点击开始按钮, [tuple: True, False]
    def auto_game_view_start_btn_click(self):
        try:
            click = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_startBtn.displayObject.event('click')；")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 旋转按钮 及 旋转状态 ------------------------------------------------------------------------
    #
    #

    # 显示旋转按钮, [tuple: True, False]
    def start_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 旋转按钮可点击否, [tuple: True, False]
    def start_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击旋转按钮, [tuple: True, False]
    def start_btn_click(self):
        try:
            click = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 旋转按钮状态, [str: stopped, playing]
    def start_btn_status(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.m_autoGameCtl.selectedPage;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 旋转按钮图标url, [str], 旋转前后分别获得返回值，再进行比较，不一致则代表旋转和停止图标不一致
    def start_btn_icon_url(self):
        try:
            url = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.m_n22.url;")
            return url
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 滚轴滚动状态, [tuple: True, False]
    def slot_machine_rolling(self):
        try:
            rolling = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.slotMachine.isRolling;")
            return rolling
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式状态, [tuple: True, False]
    def spin_is_in_turbo(self):
        try:
            turbo = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.isInTurbo;")
            return turbo
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动旋转状态, [tuple: True, False]
    def spin_is_in_auto(self):
        try:
            auto = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.isInAuto;")
            return auto
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏过程，停止按钮上的文字或次数, [str: 199, 直到]
    def in_auto_spin_btn_text(self):
        try:
            text = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.m_autoTimesLabel.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 下导航栏 ------------------------------------------------------------------------
    #
    #

    # 提示文字内容, [str]
    def banner_tips_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_bannerTipsLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额标题文字, [str]
    def has_money_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_hasMoneyTitleL.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额数值, [str]
    def has_money_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_hasMoneyLabelL.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数标题文字, [str]
    def line_num_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineNumTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数数值, [str]
    def line_num_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineNumLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线注标题文字, [str]
    def line_cost_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineCostTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线注数值, [str]
    def line_cost_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineCostLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 总赌注标题文字, [str]
    def bet_money_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_betTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 总赌注数值, [str]
    def bet_money_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_betMoneyLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 快速模式窗口 ------------------------------------------------------------------------
    #
    #

    # 显示快速模式窗口, [tuple: True, False]
    def turbo_mode_view_showing(self):
        try:
            showing = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);return turboView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，显示关闭按钮, [tuple: True, False]
    def turbo_mode_view_close_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_frame.m_closeButton.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，关闭按钮可点击否, [tuple: True, False]
    def turbo_mode_view_close_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_frame.m_closeButton.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，点击关闭按钮, [tuple: True, False]
    def turbo_mode_view_close_btn_click(self):
        try:
            click = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_frame.m_closeButton.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口消失, [tuple: None]
    def turbo_mode_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，提示文字（长）, [str]
    def turbo_mode_view_title_long(self):
        try:
            title = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_n4.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #  快速模式窗口，提示文字（短）, [str]
    def turbo_mode_view_title_short(self):
        try:
            title = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_n6.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，显示启动按钮, [tuple: True, False]
    def turbo_mode_view_enable_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_enableBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，启动按钮提示文字, [str]
    def turbo_mode_view_enable_btn_text(self):
        try:
            text = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                               + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_enableBtn.m_title.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，启动按钮可点击否, [tuple: True, False]
    def turbo_mode_view_enable_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_enableBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快速模式窗口，点击启动按钮, [tuple: True, False]
    def turbo_mode_view_enable_btn_click(self):
        try:
            click = self.browser.execute_script("var turboView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIEnableTurboModeView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return turboView.m_enableBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 余额不足窗口 ------------------------------------------------------------------------
    #
    #

    # 显示余额不足窗口, [tuple: True, False]
    def lack_of_money_view_showing(self):
        try:
            showing = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);return lackMoneyView.isShowing;")
            return showing
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口，显示标题文字, [str]
    def lack_of_money_title(self):
        try:
            title = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return lackMoneyView.m_n1.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口，显示确定按钮, [tuple: True, False]
    def lack_of_money_ok_btn_visible(self):
        try:
            final_visible = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;return lackMoneyView.m_okBtn.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口，确定按钮文字, [str]
    def lack_of_money_ok_btn_title(self):
        try:
            title = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return lackMoneyView.m_okBtn.m_title.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口，确定按钮可点击否, [tuple: True, False]
    def lack_of_money_ok_btn_touchable(self):
        try:
            touchable = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                    + self.add_script + "UIManager.instance.tipsLayer).contentPane;return lackMoneyView.m_okBtn.touchable;")
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口，点击确定按钮, [tuple: True, False]
    def lack_of_money_ok_btn_click(self):
        try:
            click = self.browser.execute_script("var lackMoneyView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                + self.add_script + "UIManager.instance.tipsLayer).contentPane;return lackMoneyView.m_okBtn.displayObject.event('click');")
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额不足窗口消失, [tuple: None]
    def lack_of_money_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise
