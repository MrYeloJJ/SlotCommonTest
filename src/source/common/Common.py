# coding=utf-8

""""

公共操作类，包括验证大厅、打开游戏、游戏内按钮点击等操作

"""

from src.source.common.Data import Data
from time import sleep


class Common(object):

    # 进入大厅并打开游戏
    def start(self, driver):
        message = Data().get_excel_message()
        lobby = message[0]
        game = message[1]

        self.get_lobby(driver, lobby)
        self.switch_page(driver)
        self.find_game(driver, game)
        self.switch_game_window(driver)

    # 进入大厅并判断是否正常进入
    def get_lobby(self, driver, lobby):
        try:
            driver.get(lobby)
            sleep(1)
            title = driver.title
            self.assertEqual(title, "as", "进入大厅失败！")
        except AssertionError as e:
            print(e)

    # 切换到slot标签页
    @staticmethod
    def switch_page(driver):
        try:
            sleep(1)
            driver.find_element_by_css_selector("a[href = '#type_107']").click()
        except Exception as e:
            print(e)

    # 根据游戏名字查找并打开游戏
    @staticmethod
    def find_game(driver, game):
        try:
            sleep(1)
            driver.find_element_by_link_text(game).click()
        except Exception as e:
            print(e)

    # 切换到游戏窗口
    @staticmethod
    def switch_game_window(driver):
        try:
            game_window = driver.window_handles[-1]
            driver.switch_to.window(game_window)
        except Exception as e:
            print(e)

    # 进入载入场景
    @staticmethod
    def loading_showing(driver):
        try:
            showing_js = "var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);return loading.isShowing;"
            showing = driver.execute_script(showing_js)
            return showing
        except Exception as e:
            print(e)

    # 载入场景进度条
    @staticmethod
    def loading_bar(driver):
        while True:
            try:
                progress_bar = driver.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                     "return loading.contentPane.m_progressBar.value;")
            except Exception as e:
                print(e)

            if progress_bar == 100:
                try:
                    tip = driver.execute_script("var loading = UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);"
                                                "return loading.contentPane.m_progressBar.m_title.textField.text;")
                    return tip
                except Exception as e:
                    print(e)
                break

    # 载入完成后进入主场景
    @staticmethod
    def enter_main_scence(driver):
        try:
            showing = driver.execute_script("return UIManager.instance.getWindowByName(window.Loading.FUILoadingView.URL, UIManager.instance.commonView);")
            return showing
        except Exception as e:
            print(e)
