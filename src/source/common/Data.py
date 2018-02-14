# coding=utf-8

""""""""""""""""""""""""""""""""""""""
"                                    "
"       读取测试目标大厅和游戏名字        "
"                                    "
""""""""""""""""""""""""""""""""""""""

from xml.dom.minidom import parse
import xml.dom.minidom


class Data(object):

    def __init__(self):
        self.xml = "../../assets/data.xml"

    def get_message(self):
        dom_tree = xml.dom.minidom.parse(self.xml)
        collection = dom_tree.documentElement

        target = collection.getElementsByTagName("target")[0].childNodes[0].data
        messages = collection.getElementsByTagName("data")

        for msg in messages:
            environment = msg.getAttribute("environment")
            if environment == target:
                lobby = msg.getElementsByTagName("lobby")[0].childNodes[0].data
                game = msg.getElementsByTagName("game")[0].childNodes[0].data

                return lobby, game
