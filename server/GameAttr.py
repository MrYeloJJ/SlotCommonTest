# encoding=utf-8

import json

attr_dict = {}


class GameAttr(object):

    @staticmethod
    def set_attr(data_json):
        attr = json.loads(str(data_json).replace("'", "\""))
        attr_dict["lobby"] = attr["lobby"]
        attr_dict["tester"] = attr["tester"]
        attr_dict["username"] = attr["username"]
        attr_dict["password"] = attr["password"]
        attr_dict["game_id"] = attr["gameId"]
        attr_dict["game_name"] = attr["gameName"]
        attr_dict["full_line"] = attr["fullLine"]
        attr_dict["full_line_mulitiplier"] = attr["fullLineMulitiplier"]
        attr_dict["line_num_min"] = attr["lineNumMin"]
        attr_dict["line_num_max"] = attr["lineNumMax"]
        attr_dict["line_cost"] = attr["lineCost"]
        attr_dict["auto_game_times"] = attr["autoGameTimes"]

    @staticmethod
    def get_attr(name):
        try:
            value = attr_dict[name]
        except KeyError:
            value = None
        return value


if __name__ == "__main__":
    GameAttr().set_attr('{"id":"1"}')
    GameAttr().get_attr("id")
