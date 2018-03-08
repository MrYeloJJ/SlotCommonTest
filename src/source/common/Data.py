# coding=utf-8

""""" 读取测试目标大厅和游戏名字 """""

from xml.dom.minidom import parse
import xml.dom.minidom


class Data(object):

    def __init__(self):
        self.xml = "../../assets/data.xml"

    def get_message(self):
        dom_tree = xml.dom.minidom.parse(self.xml)
        data = dom_tree.documentElement

        lobby = data.getElementsByTagName("lobby")[0].childNodes[0].data
        game = data.getElementsByTagName("game")[0].childNodes[0].data

        return {"lobby": lobby, "game": game}
