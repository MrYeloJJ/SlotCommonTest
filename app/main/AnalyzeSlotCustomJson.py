# encoding=utf-8

import json
from app.main.GameAttr import GameAttr
from app.automatedTest.slot.source.common.CustomRun import CustomRun


class AnalyzeSlotCustomJson(object):

    @staticmethod
    def analyze_json(data_json):
        data = json.loads(data_json)

        game_attr = data[0]["game_attr"]
        GameAttr().set_attr(game_attr)

        test_list = data[0]["test_case"]
        CustomRun().run(test_list)


if __name__ == "__main__":
    source_data = [{"game_attr": {
                "lobby": "https://lobby.fg.blizzmi.cn",
                "tester": "Gelomen",
                "username": "automatedTest1",
                "password": "123456",
                "gameId": "3303",
                "gameName": "众神之王",
                "fullLine": "True",
                "fullLineMulitiplier": "50",
                "lineNumMin": "1",
                "lineNumMax": "25",
                "lineCost": "1, 2, 5, 10, 50, 100, 500, 1000",
                "autoGameTimes": "25, 50, 100, 200, 500, -1"
            },
            "test_case": [
                {"key": "TestMainMenu","value": "test_voice_btn_click_refresh"},
                {"key": "TestMainMenu","value": "test_turbo_btn_click_refresh"},
                {"key": "TestMainMenu","value": "test_voice_btn_click_refresh_portrait"},
                {"key": "TestMainMenu","value": "test_turbo_btn_click_refresh_portrait"},
            ]
        }
    ]

    my_json = json.dumps(source_data)
    AnalyzeSlotCustomJson().analyze_json(my_json)
