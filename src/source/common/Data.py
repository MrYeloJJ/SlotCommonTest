# coding=utf-8

""""

读取大厅、游戏名字等数据

"""


from xml.dom.minidom import parse
import xml.dom.minidom


class Data(object):

    @staticmethod
    def get_message():
        dom_tree = xml.dom.minidom.parse("../../assets/data.xml")
        collection = dom_tree.documentElement

        target = collection.getElementsByTagName("target")[0].childNodes[0].data
        messages = collection.getElementsByTagName("data")

        for msg in messages:
            environment = msg.getAttribute("environment")
            if environment == target:
                lobby = msg.getElementsByTagName("lobby")[0].childNodes[0].data
                game = msg.getElementsByTagName("game")[0].childNodes[0].data

                return lobby, game
