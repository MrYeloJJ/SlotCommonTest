# encoding=utf-8

import configparser


class Config(object):

    def __init__(self):
        self.config_url = "../../assets/config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_url, encoding="utf-8")
        self.section = "config"

    def get_message(self):

        lobby = self.config.get(self.section, "lobby")
        game_id = eval(self.config.get(self.section, "gameId"))
        game_name = self.config.get(self.section, "gameName")
        full_line = eval(self.config.get(self.section, "fullLine"))
        line_num_min = eval(self.config.get(self.section, "lineNumMin"))
        line_num_max = eval(self.config.get(self.section, "lineNumMax"))
        line_cost = eval(self.config.get(self.section, "lineCost"))
        auto_game_times = eval(self.config.get(self.section, "autoGameTimes"))

        return {"lobby": lobby, "game_id": game_id, "game_name": game_name, "full_line": full_line,
                "line_num_min": line_num_min, "line_num_max": line_num_max, "line_cost": line_cost,
                "auto_game_times": auto_game_times}


if __name__ == "__main__":
    Config().get_message()
