#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

from lxml.etree import tostring
from lxml import etree
import requests
import sys

class RSSParser:
    def __init__(self):
        self.url = sys.argv[1]

    def stringify_children(self, node):
        for c in node.getchildren():
            for i in c.getchildren():
                print("---------------------------")
                print(tostring(i))
                print("---------------------------")

    def request_resource(self):
        r = requests.get(self.url)
        node = etree.fromstring(r.content)
        return self.stringify_children(node)

def main():
    parse = RSSParser()
    new_data = parse.request_resource()

if __name__ == '__main__':
    main()
