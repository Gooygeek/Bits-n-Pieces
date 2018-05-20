#
#
#


class Stack:
    def __init__(self, size):
        assert size > 0, "size must be positive"
        self.array = [None] * size
        self.top = -1
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        tmp_stack = Stack(len(self))
        tmp_string = ""
        for _ in range(len(self)):
            tmp_value = self.pop()
            tmp_string = (tmp_string + str(tmp_value) + " ")
            tmp_stack.push(tmp_value)
        for _ in range(len(tmp_stack)):
            self.push(tmp_stack.pop())
        return tmp_string

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        self.count += -1
        self.top += -1
        return self.array[self.top + 1]

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")

        self.top += 1
        self.array[self.top] = item
        self.count += 1

    def size(self):
        return self.count

    def print(self):
        for _ in range(len(self)):
            print(self.pop())
