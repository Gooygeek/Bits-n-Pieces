#
#
#


from LNode import Node


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    @staticmethod
    def is_full():
        return False

    def reset(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        assert not self.is_empty(), "Stack is empty"
        item = self.top.item
        self.top = self.top.next
        return item
