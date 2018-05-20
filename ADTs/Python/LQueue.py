#
#
#


from LNode import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    @staticmethod
    def is_full():
        return False

    def reset(self):
        self.__init__()

    def append(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        temp = self.front.item
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        return temp
