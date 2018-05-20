#
#
#


class Queue:
    def __init__(self, size):
        assert size > 0, "Size should be positive"
        self.the_array = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):
        return self.rear >= len(self.the_array)

    def is_empty(self):
        return self.count == 0

    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, new_item):
        assert not self.is_full(), "Queue is full"
        self.the_array[self.rear] = new_item
        self.rear += 1
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.the_array[self.front]
        self.front += 1
        self.count -= 1
        return item
