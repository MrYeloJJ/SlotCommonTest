# coding=utf-8

import inspect
import datetime
import os


class DirAndFiles(object):

    def __init__(self, driver):
        self.driver = driver
        self.path = "../../assets/report/"

    def create_dir(self):
        now = str(datetime.datetime.now().strftime("%Y-%m-%d(%H-%M-%S)"))
        dir_path = self.path + now

        # 判断文件夹是否存在，不存在则创建
        is_dir = os.path.isdir(dir_path)
        if not is_dir:
            os.makedirs(dir_path)

    def get_new_folder(self):
        lists = os.listdir(self.path)
        # 按时间排序
        lists.sort(key=lambda fn: os.path.getmtime(self.path + "\\" + fn))
        # 获取最新文件或文件夹
        new_folder = os.path.join(self.path, lists[-1])
        return new_folder

    def get_screen_shot(self):
        # 获取调用此函数的函数名
        func_name = inspect.stack()[1][3]

        # 获取最新文件夹的名字，并将截图保存在该文件夹下
        new_folder = self.get_new_folder()
        img_path = new_folder + "/" + func_name + ".png"

        # 有可能同个测试步骤出错，截图名字一样导致覆盖文件，所以名字存在则增加id
        i = 1
        while True:
            is_file = os.path.isfile(img_path)
            if is_file:
                img_path = new_folder + "/" + func_name + "_" + str(i) + ".png"
                i += 1
            else:
                break

        self.driver.get_screenshot_as_file(img_path)
