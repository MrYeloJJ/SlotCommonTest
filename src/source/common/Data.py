# coding=utf-8

""""

读取大厅、游戏名字等数据

"""


from xml.dom.minidom import parse
import xml.dom.minidom


class Data(object):

    def __init__(self, environment):
        self.environment = environment

    def get_message(self):
        dom_tree = xml.dom.minidom.parse("../../assets/data.xml")
        collection = dom_tree.documentElement

        messages = collection.getElementsByTagName("data")

        for msg in messages:
            environment = msg.getAttribute("environment")
            if environment == self.environment:
                lobby = msg.getElementsByTagName("lobby")[0].childNodes[0].data
                game = msg.getElementsByTagName("game")[0].childNodes[0].data

                return lobby, game
