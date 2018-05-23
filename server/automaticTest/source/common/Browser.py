# coding=utf-8

from selenium import webdriver


class Browser(object):

    # webdriver 初始化
    @staticmethod
    def browser(headless=True):
        if headless:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="./automaticTest/lib/chromedriver.exe")
        else:
            browser = webdriver.Chrome(executable_path="./automaticTest/lib/chromedriver.exe")

        return browser
