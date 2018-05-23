# encoding=utf-8

from flask import Flask, request, jsonify, send_file
from server.AllReportsName import AllReportsName
from server.automaticTest.source.common.GameAttr import GameAttr
from server.TestCaseDoc import TestCaseDoc
from server.automaticTest.source.common.RunAllTests import RunAllTests

app = Flask(__name__)

# @app.route("/")
# def my_site():
#     return redirect("https://gelomen.github.io")


# 运行所有用例
@app.route("/RunAllTests", methods=["POST"])
def run_all_tests():
    data_json = request.json
    GameAttr().set_attr(data_json)
    RunAllTests().run()
    return "测试结束"


# 获取所有用例名字和描述
@app.route("/allTestDoc")
def all_test_doc():
    return TestCaseDoc().get_doc()


# 获取所有测试报告
@app.route("/allReports", methods=["GET"])
def all_reports():
    report_name = AllReportsName().get_name_and_url()
    return jsonify(report_name)


# 报告连接
@app.route("/report/<report_name>", methods=["GET"])
def report(report_name):
    return send_file("../../result/" + str(report_name) + "/" + str(report_name) + ".html")


if __name__ == "__main__":
    app.run(debug=True)
