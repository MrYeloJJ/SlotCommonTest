# encoding=utf-8

import os
import shutil
from flask import jsonify, redirect
from app.main.HostIp import get_host_ip


class SlotReport(object):
    def __init__(self):
        current_ip = get_host_ip()
        self.root_url = "http://" + current_ip + ":5000/"
        self.slot_report_path = "./static/slot/"
        self.report_list = []

    def get_slot_report_url(self):
        try:
            for i in os.listdir(self.slot_report_path):
                report_dict = {}
                if i.startswith("["):
                    url = self.root_url + "slot/report/" + i
                    del_url = self.root_url + "slot/delete_report/" + i
                    report_dict["report_name"] = i
                    report_dict["url"] = url
                    report_dict["del_url"] = del_url
                    self.report_list.append(report_dict)

            return jsonify(self.report_list)
        except Exception as e:
            return jsonify({"code": 500, "msg": "获取失败", "log": str(e)}), 500

    def open_report(self, report_name):
        dir_list = os.listdir(self.slot_report_path)
        for i in dir_list:
            if i == report_name:
                report_url = self.slot_report_path + str(report_name) + "/" + str(report_name) + ".html"
                return redirect(report_url)
            elif i == dir_list[len(dir_list)-1]:
                return jsonify({"code": 404, "msg": "报告不存在"}), 404

    def delete_report(self, report_name):
        dir_list = os.listdir(self.slot_report_path)
        for i in dir_list:
            if i == report_name:
                try:
                    shutil.rmtree(self.slot_report_path + report_name)
                    return jsonify({"code": 200, "msg": "删除成功"}), 200
                except Exception as e:
                    return jsonify({"code": 400, "msg": "删除失败", "log": str(e)}), 400
            elif i == dir_list[len(dir_list)-1]:
                return jsonify({"code": 404, "msg": "找不到报告"}), 404
