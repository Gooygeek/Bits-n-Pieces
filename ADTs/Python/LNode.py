#
#
#


class Node:
    def __init__(self, item=None, link=None):
        self.item = item
        self.next = link

    def __str__(self):
        return str(self.item)
