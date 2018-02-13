# coding=utf-8

""""

公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作

"""

from src.source.common.Data import Data
from src.source.common.DirAndFiles import DirAndFiles
from time import sleep


class Common(object):
    # 初始化driver、lobby和game等数据
    def __init__(self, driver):
        self.message = Data().get_message()
        self.lobby = self.message[0]
        self.game = self.message[1]
        self.driver = driver
        self.dir_and_files = DirAndFiles(self.driver)

    # 进入大厅并打开游戏
    def start(self):
        self.get_lobby()
        self.switch_page()
        self.find_game()
        self.switch_game_window()

    # 进入大厅并判断是否正常进入
    def get_lobby(self):
        try:
            self.driver.get(self.lobby)
            sleep(1)
            title = self.driver.title
            assert title == "as", "进入大厅失败！"
        except AssertionError:
            self.dir_and_files.get_screen_shot()
            raise

    # 切换到slot标签页
    def switch_page(self):
        try:
            sleep(1)
            self.driver.find_element_by_css_selector("a[href = '#type_107']").click()
        except Exception:
            self.dir_and_files.get_screen_shot()
            raise

    # 根据游戏名字查找并打开游戏
    def find_game(self):
        try:
            sleep(1)
            self.driver.find_element_by_link_text(self.game).click()
        except Exception:
            self.dir_and_files.get_screen_shot()
            raise

    # 切换到游戏窗口
    def switch_game_window(self):
        try:
            game_window = self.driver.window_handles[-1]
            self.driver.switch_to.window(game_window)
        except Exception:
            self.dir_and_files.get_screen_shot()
            raise

    # 进入载入场景
    def loading_view_showing(self):
        try:
            showing_js = "var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);return loading.isShowing;"
            showing = self.driver.execute_script(showing_js)
            return showing
        except Exception:
            self.dir_and_files.get_screen_shot()
            raise

    # 载入场景进度条
    def loading_bar(self):

        while True:
            try:
                progress_bar = self.driver.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                          "return loading.contentPane.m_progressBar.value;")
            except Exception:
                self.dir_and_files.get_screen_shot()
                raise

            if progress_bar == 100:
                try:
                    tip = self.driver.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                     "return loading.contentPane.m_progressBar.m_title.textField.text;")
                    return tip
                except Exception:
                    self.dir_and_files.get_screen_shot()
                    raise

    # 载入场景消失
    def loading_view_dispear(self):
        try:
            showing = self.driver.execute_script("return UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);")
            return showing
        except Exception:
            self.dir_and_files.get_screen_shot()
            raise
