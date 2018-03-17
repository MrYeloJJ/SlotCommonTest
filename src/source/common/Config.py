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
        game = self.config.get(self.section, "game")
        full_line = self.config.get(self.section, "fullLine")
        line_num = self.config.get(self.section, "lineNum")
        line_cost = eval(self.config.get(self.section, "lineCost"))

        return {"lobby": lobby, "game": game, "full_line": full_line,
                "line_num": line_num, "line_cost": line_cost}


if __name__ == "__main__":
    Config().get_message()
