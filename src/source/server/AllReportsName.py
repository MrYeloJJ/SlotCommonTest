# encoding=utf-8

import os


class AllReportsName(object):
    def __init__(self):
        self.root_url = "http://127.0.0.1:5000/"
        self.report_path = "../../result"
        self.report_list = []

    def get_name_and_url(self):
        for i in os.listdir(self.report_path):
            report_dict = {}
            if i.startswith("【"):
                url = self.root_url + "report/" + i
                report_dict["report_name"] = i
                report_dict["url"] = url
                self.report_list.append(report_dict)

        return self.report_list
