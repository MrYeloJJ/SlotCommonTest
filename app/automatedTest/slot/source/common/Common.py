# coding=utf-8

""""" 公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作 """""
from selenium.webdriver.support.select import Select
from app.main.GameAttr import GameAttr
from app.automatedTest.slot.lib.HTMLTestReportCN import DirAndFiles
from time import sleep
from datetime import datetime
import locale


class Common(object):
    # 初始化browser、lobby和game等数据
    def __init__(self, browser=None):
        self.lobby = GameAttr.get_attr("lobby")                             # 大厅地址
        self.username = GameAttr.get_attr("username")                       # 用户名
        self.password = GameAttr.get_attr("password")                       # 密码
        self.game_id = eval(str(GameAttr.get_attr("game_id")))              # 游戏id
        self.game_name = GameAttr.get_attr("game_name")                     # 游戏名字
        self.full_line = eval(str(GameAttr.get_attr("full_line")))          # 是否满线
        self.full_line_mulitiplier = \
            GameAttr.get_attr("full_line_mulitiplier")                      # 满线项目总赌注倍数
        self.line_num_min = GameAttr.get_attr("line_num_min")               # 最小线数
        self.line_num_max = GameAttr.get_attr("line_num_max")               # 最大线数
        self.line_cost = eval(str(GameAttr.get_attr("line_cost")))               # 所有线注
        self.auto_game_times = eval(str(GameAttr.get_attr("auto_game_times")))   # 所有自动游戏次数
        self.browser = browser
        self.daf = DirAndFiles()
        self.add_script = ""            # 多开情况需改为 "window.frames[0].frames."

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
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 登录
    def login(self):
        try:
            sl = Select(self.browser.find_element_by_name("agent_i"))
            sl.select_by_value("22ddd189593051fd88ca58dc8111563e-lobby2")

            self.browser.find_element_by_class_name("top_login_img").click()
            self.browser.find_element_by_id("username").send_keys(self.username)
            sleep(1)
            self.browser.find_element_by_id("password").send_keys(self.password)
            self.browser.find_element_by_id("login-reg").click()
            sleep(1)
            self.browser.switch_to.alert.accept()

            name = self.browser.find_element_by_class_name("photo").text
            lobby_username = name.strip()

            try:
                assert lobby_username == self.username
            except AssertionError:
                print("用户名不一致，登录失败！")
                self.daf.get_screenshot(self.browser)
                raise

            # 余额小于1000时点击加钱按钮
            lobby_chips_num = self.lobby_chips()["lobby_chips_num"]
            if lobby_chips_num < 1000:
                self.add_chip()

        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 大厅加钱
    def add_chip(self):
        try:
            self.browser.find_element_by_class_name("add-chip").click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 大厅减钱
    def red_chip(self):
        try:
            self.browser.find_element_by_class_name("red-chip").click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 大厅余额
    def lobby_chips(self):
        try:
            # WebDriverWait(self.browser, 30, 0.5).until(ec.presence_of_element_located((By.CLASS_NAME, "chips")), "等待30秒，不会显示大厅余额！")
            lobby_chips_num = self.browser.find_element_by_class_name("chips").text
            # 格式化货币
            locale.setlocale(locale.LC_ALL, "")
            lobby_chips = "¥" + locale.format("%.2f", eval(lobby_chips_num), 1)
            return {"lobby_chips": lobby_chips, "lobby_chips_num": eval(lobby_chips_num)}
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 切换到slot标签页
    def switch_page(self):
        try:
            # WebDriverWait(self.browser, 30, 0.5).until(ec.presence_of_element_located((By.ID, "type_107")), "等待30秒，找不到slot标签页！")
            self.browser.find_element_by_css_selector("a[href = '#type_107']").click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 根据游戏名字查找并打开游戏
    def find_game(self):
        try:
            # WebDriverWait(self.browser, 30, 0.5).until(ec.presence_of_element_located((By.LINK_TEXT, self.game_name)), "等待30秒，找不到游戏" + self.game_name + "！")
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
        self.browser.set_window_size(width=1136, height=660)

    # 设置当前分辨率为竖屏
    def portrait(self):
        self.browser.set_window_size(width=370, height=660)

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

    # 载入场景 显示背景图片, [tuple: True, False]
    def loading_view_background_visible(self):
        try:
            final_visible = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_bgGraph.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 显示logo, [tuple: True, False]
    def loading_view_logo_visible(self):
        try:
            final_visible = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_logoImg.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 显示进度标题, [tuple: True, False]
    def loading_view_progress_title_visible(self):
        try:
            final_visible = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.m_title.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 进度标题数值, [str: "0%"]
    def loading_view_progress_title_value(self):
        try:
            text = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                               + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.m_title.textField.text;")
            return text
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 显示进度条, [tuple: True, False]
    def loading_view_progress_bar_visible(self):
        try:
            final_visible = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.visible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 进度条数值, [tuple: 0]
    def loading_view_progress_bar_value(self):
        try:
            value = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_progressBar.value;")
            return value
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 载入场景 显示版本号, [tuple: True, False]
    def loading_view_version_visible(self):
        try:
            final_visible = self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonView);return loading.contentPane.m_version.finalVisible;")
            return final_visible
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
            # self.daf.get_screenshot(self.browser)
            raise

    # 等待进入加载场景
    def wait_for_loading_view_showing(self):
        time = 30
        start_time = datetime.now()
        while True:
            try:
                self.browser.execute_script("var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "window.Loading.FUILoadingView.URL, "
                                            + self.add_script + "UIManager.instance.commonView);return loading.isShowing;")
                break
            except Exception:
                end_time = datetime.now()
                cost_time = (end_time - start_time).seconds

                if cost_time >= time:
                    print("等待" + str(time) + "秒，不会进入loading场景！")
                    self.daf.get_screenshot(self.browser)
                    raise

    # 等待加载完成
    def wait_for_loading_bar_completed(self):
        time = 30
        start_time = datetime.now()
        while True:
            try:
                bar_value = self.loading_view_progress_bar_value()
            except Exception:
                self.daf.get_screenshot(self.browser)
                raise

            end_time = datetime.now()
            cost_time = (end_time - start_time).seconds

            if bar_value == 100:
                break
            else:
                if cost_time >= time:
                    try:
                        assert bar_value == 100
                    except AssertionError:
                        print("等待" + str(time) + "秒，进度条不会走满！")
                        self.daf.get_screenshot(self.browser)
                        raise

    # 等待加载场景消失
    def wait_for_loading_view_dispear(self):
        time = 30
        start_time = datetime.now()
        while True:
            sleep(1)
            try:
                self.loading_view_dispear()
                break
            except Exception:
                # self.daf.get_screenshot(self.browser)
                # raise

                end_time = datetime.now()
                cost_time = (end_time - start_time).seconds

                if cost_time >= time:
                    print("等待" + str(time) + "秒，loading场景不会消失！")
                    self.daf.get_screenshot(self.browser)
                    raise

    # 等待加载完成
    def loading_pass(self):
        self.wait_for_loading_view_showing()

        self.wait_for_loading_bar_completed()

        self.wait_for_loading_view_dispear()

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

    # 显示主场景横屏背景图片, [tuple: True, False]
    def bg_view_visible(self):
        try:
            final_visible = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.contentPane.m_bgView.finalVisible;")
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示主场景竖屏背景图片, [tuple: True, False]
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

    # 获取游戏当前状态, [tuple: None]  None: 普通游戏
    def get_game_current_status(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.rollingResult.nextState;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 快要中免费或小游戏之前的列加速, [tuple: True, False]
    def get_scroller_speed_up(self):
        try:
            status = self.browser.execute_script("return " + self.add_script + "UIManager.instance.mainView.slotMachine.scroller.ruleTaskManager.ruleMap.values[0].task.isRunning;")
            return status
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 等待滚轴滚动
    def wait_for_rolling(self, time):
        start_time = datetime.now()
        while True:
            slot_status = self.slot_machine_rolling()

            end_time = datetime.now()
            cost_time = (end_time - start_time).seconds

            if slot_status:
                break
            else:
                if cost_time >= time:
                    try:
                        assert slot_status is True
                    except AssertionError:
                        print("等待" + str(time) + "秒，滚轴不会旋转！")
                        self.daf.get_screenshot(self.browser)
                        raise

    # 等待滚轴停止
    def wait_for_rolling_stop(self, time, just_rolling=False):
        if just_rolling:
            start_time = datetime.now()
            while True:
                slot_status = self.slot_machine_rolling()

                end_time = datetime.now()
                cost_time = (end_time - start_time).seconds

                if slot_status is False:
                    break
                else:
                    if cost_time >= time:
                        try:
                            assert slot_status is False
                        except AssertionError:
                            print("等待" + str(time) + "秒，滚轴不会停止！")
                            self.daf.get_screenshot(self.browser)
                            raise
        else:
            start_time = datetime.now()
            while True:
                slot_status = self.slot_machine_rolling()
                mask_status = self.mask_view_showing()

                end_time = datetime.now()
                cost_time = (end_time - start_time).seconds

                if slot_status is False and mask_status is False:
                    break
                else:
                    if cost_time >= time:
                        try:
                            assert slot_status is True
                        except AssertionError:
                            print("等待" + str(time) + "秒，滚轴不会停止！")
                            self.daf.get_screenshot(self.browser)
                            raise

                        try:
                            assert mask_status is True
                        except AssertionError:
                            print("等待" + str(time) + "秒，蒙板不会消失！")
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
            showing = self.browser.execute_script("var infoView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Application.instance.mainModule.FUIInfoView.URL);"
                                                  "return infoView.isShowing;")
            return showing
        except Exception:
            showing = self.browser.execute_script("var infoView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUINewInfoView.URL);"
                                                  "return infoView.isShowing;")
            return showing
        except BaseException:
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
            final_visible = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;"
                                                        "return autoGameView.finalVisible;")
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

    # 自动游戏设置面板，拖动条按钮在拖动条的位置, [tuple: 100(default)]
    def auto_game_view_slider_value(self):
        try:
            value = self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_slider.value;")
            return value
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 自动游戏设置面板，改变自动次数
    def auto_game_view_change_auto_time(self, index):
        try:
            self.browser.execute_script("var autoGameView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIAutoGameSettingView.URL, "
                                        + self.add_script + "UIManager.instance.commonUILayer).contentPane;"
                                        "var i = " + str(index) + ";" + self.add_script + "SpinManager.instance.autoTimes = " + self.add_script + "DataGame.getData("
                                        + self.add_script + "DataGame.getKeys())['autoSpinTimes'][i];"
                                        "autoGameView.m_slider.value = 100 * i / " + self.add_script + "DataGame.getData(" + self.add_script + "DataGame.getKeys())['autoSpinTimes'].length;")
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
                                                + self.add_script + "UIManager.instance.commonUILayer).contentPane;return autoGameView.m_startBtn.displayObject.event('click');")
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
    def info_bar_view_banner_tips_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_bannerTipsLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额标题文字, [str]
    def info_bar_view_has_money_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_hasMoneyTitleL.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 余额数值, [str]
    def info_bar_view_has_money_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_hasMoneyLabelL.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数标题文字, [str]
    def info_bar_view_line_num_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineNumTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线数数值, [str]
    def info_bar_view_line_num_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineNumLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线注标题文字, [str]
    def info_bar_view_line_cost_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineCostTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 线注数值, [str]
    def info_bar_view_line_cost_label(self):
        try:
            label = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_lineCostLabel.textField.text;")
            return label
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 总赌注标题文字, [str]
    def info_bar_view_bet_money_title(self):
        try:
            title = self.browser.execute_script("return " + self.add_script + "UIManager.instance.commonView.contentPane.m_infoBarViewL.m_betTitle.textField.text;")
            return title
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 总赌注数值, [str]
    def info_bar_view_bet_money_label(self):
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
    def lack_of_money_view_dispear(self):
        try:
            dispear = self.browser.execute_script("return " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUILackOfMoneyAlertView.URL, "
                                                  + self.add_script + "UIManager.instance.tipsLayer);")
            return dispear
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ 滚轴中奖奖金 ------------------------------------------------------------------------
    #
    #

    # 总奖金, [tuple: 0]
    def total_win(self):
        try:
            total_win = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.totalWin;")
            return total_win
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 滚轴奖金, [tuple: 0]
    def spin_coin(self):
        try:
            spin_coin = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.spinWin;")
            return spin_coin
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # JP奖金, [tuple: 0]
    def jp_coin(self):
        try:
            jp_coin = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.rollingResult.spinResult.jpCoin;")
            return jp_coin
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 小游戏奖金, [tuple: 0]
    def little_game_coin(self):
        try:
            lg_coin = self.browser.execute_script("return " + self.add_script + "SpinManager.instance.rollingResult.spinResult.lgCoin;")
            return lg_coin
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 非满线项目，获取某条线的奖金，[tuple: 0]
    def line_spin_coin(self, line_id):
        try:
            spin_coin = self.browser.execute_script("var lineResult = " + self.add_script + "SpinManager.instance.rollingResult.spinResult.lineResult;"
                                                    + "var spinCoin = 0;for(i=0;i<lineResult.length;i++){var lineId = lineResult[i].lineId;if(lineId == " + str(int(line_id)) + "){"
                                                    + "spinCoin = lineResult[i].spinCoin;}} return spinCoin;")
            return spin_coin
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    #
    #
    # ------------------------------------------------------------------------ GM窗口 ------------------------------------------------------------------------
    #
    #

    # 打开GM窗口
    def show_gm_view(self):
        try:
            self.browser.execute_script(self.add_script + "UIManager.instance.showGMView();")
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 输入GM指令
    def gm_input(self, text):
        try:
            self.browser.execute_script("var GMView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIGmView.URL, "
                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;GMView.m_content.m_gmInput.text = " + text)
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 让余额为0
    def set_chips_to_zero(self):
        try:
            self.show_gm_view()
            sleep(0.5)
            chips = self.info_bar_view_has_money_label()
            gm = "\"!jq -" + chips.replace("¥", "").replace(",", "").replace(".", "") + "\""
            self.gm_input(gm)
            self.gm_confirm_btn_click()
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击GM确定按钮
    def gm_confirm_btn_click(self):
        try:
            self.browser.execute_script("var GMView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIGmView.URL, "
                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;GMView.m_content.m_confirmBtn.displayObject.event('click');")
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击GM取消按钮
    def gm_cancel_btn_click(self):
        try:
            self.browser.execute_script("var GMView = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script + "Common.FUIGmView.URL, "
                                        + self.add_script + "UIManager.instance.tipsLayer).contentPane;GMView.m_content.m_cancelBtn.displayObject.event('click');")
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise
