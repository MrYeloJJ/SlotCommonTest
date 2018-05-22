# encoding=utf-8


from flask import Flask, request, redirect
from src.source.common.GameAttr import GameAttr
from src.source.common.RunAllTests import RunAllTests

app = Flask(__name__)


# @app.route("/")
# def my_site():
#     return redirect("https://gelomen.github.io")


@app.route("/RunAllTests", methods=["POST"])
def run_all_tests():
    data_json = request.json
    GameAttr().set_attr(data_json)
    RunAllTests().run()


if __name__ == "__main__":
    app.run(debug=True)
