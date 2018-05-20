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

    def __len__(self):
        return self.count

    def is_empty(self):
            return len(self) == 0

    def is_full(self):
        return len(self) >= len(self.the_array)

    def append(self, new_item):
        assert not self.is_full(), "Queue is full"
        self.the_array[self.rear] = new_item
        self.rear = (self.rear + 1) % len(self.the_array)
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.the_array[self.front]
        self.front = (self.front + 1) % len(self.the_array)
        self.count -= 1
        return item

    def print_items(self):
        index = self.front
        for _ in range(self.count):
            print(str(self.the_array[index]))
            index = (index + 1) % len(self.the_array)
