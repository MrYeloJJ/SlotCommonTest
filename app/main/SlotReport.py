# encoding=utf-8

import os
import shutil


class SlotReport(object):
    def __init__(self):
        self.root_url = "http://127.0.0.1:5000/"
        self.slot_report_path = "./static/slot/"
        self.report_list = []

    def get_slot_report_url(self):
        for i in os.listdir(self.slot_report_path):
            report_dict = {}
            if i.startswith("【"):
                url = self.root_url + "slot/report/" + i
                del_url = self.root_url + "slot/delete_report/" + i
                report_dict["report_name"] = i
                report_dict["url"] = url
                report_dict["del_url"] = del_url
                self.report_list.append(report_dict)

        return self.report_list

    def open_report(self, report_name):
        report_url = self.slot_report_path + str(report_name) + "/" + str(report_name) + ".html"
        return report_url

    def delete_report(self, report_name):
        for i in os.listdir(self.slot_report_path):
            if i == report_name:
                try:
                    shutil.rmtree(self.slot_report_path + report_name)
                except Exception:
                    raise
