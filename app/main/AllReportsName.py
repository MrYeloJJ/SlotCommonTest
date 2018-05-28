# encoding=utf-8

import os


class AllReportsName(object):
    def __init__(self):
        self.root_url = "http://127.0.0.1:5000/"
        self.slot_report_path = "./static/slot/"
        self.report_list = []

    def get_slot_report_url(self):
        for i in os.listdir(self.slot_report_path):
            report_dict = {}
            if i.startswith("【"):
                url = self.root_url + "slot/report/" + i
                report_dict["report_name"] = i
                report_dict["url"] = url
                self.report_list.append(report_dict)

        return self.report_list
