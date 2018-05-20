#
#
#


class List:
    def __init__(self, size):
        assert size > 0, "size must be positive"
        self.the_array = size * [None]
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.the_array)

    def add(self, new_item):  # adds to the end only
        has_space_left = not self.is_full()
        if has_space_left:
            self.the_array[self.count] = new_item
            self.count += 1
        return has_space_left

    def delete(self, index):
        valid_index = 0 <= index < self.count
        if valid_index:
            for i in range(index, self.count - 1):
                self.the_array[i] = self.the_array[i + 1]
            self.count -= 1
        return valid_index

    def __contains__(self, item):
        for k in range(len(self)):
            if item == self.the_array[k]:
                return True
        return False

    def index(self, item):
        for k in range(len(self)):
            if item == self.the_array[k]:
                return k
        raise ValueError(str(item) + " not in list")
