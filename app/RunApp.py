# encoding=utf-8

from multiprocessing import Process
import os
from flask import Flask, request, jsonify, redirect
from app.main.SlotReport import SlotReport
from app.main.GameAttr import GameAttr
from app.main.SlotTestDoc import SlotTestDoc
from app.automaticTest.slot.source.common.RunAllTests import RunAllTests

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def my_site():
    return redirect("https://gelomen.github.io")


# 运行slot所有用例
@app.route("/slot/RunAllTests", methods=["POST"])
def run_all_slot_tests():
    data_json = request.json
    print("主进程：" + str(os.getpid()))
    p = Process(target=run_slot_all, args=(data_json,))
    p.start()
    # p.join()
    return jsonify({"pid": p.pid}), 200


def run_slot_all(data_json):
    print("子进程：" + str(os.getpid()))
    with app.app_context():
        try:
            GameAttr().set_attr(data_json)
            RunAllTests().run()
        except Exception:
            raise


# 停止所有测试
@app.route("/StopAllTests/<pid>", methods=["GET"])
def stop_all_tests(pid):
    print("目标进程：" + str(pid))
    try:
        os.system("taskkill /pid " + str(pid) + " -t -f")
        return jsonify({"code": 200, "msg": "测试停止"}), 200
    except Exception as e:
        return jsonify({"code": 500, "msg": "停止失败", "log": str(e)}), 500


# 获取slot所有用例名字和描述
@app.route("/slot/allTestDoc", methods=["GET"])
def all_slot_test_doc():
    return SlotTestDoc().get_doc()


# 获取slot所有测试报告
@app.route("/slot/allReports", methods=["GET"])
def all_slot_reports():
    return SlotReport().get_slot_report_url()


# slot报告链接
@app.route("/slot/report/<report_name>", methods=["GET"])
def slot_report(report_name):
    return SlotReport().open_report(report_name)


# 删除slot报告
@app.route("/slot/delete_report/<report_name>", methods=["GET"])
def delete_slot_report(report_name):
    return SlotReport().delete_report(report_name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
