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

    def delete(self, index):
        valid_index = 0 <= index < self.count
        if valid_index:
            for i in range(index, self.count - 1):
                self.the_array[i] = self.the_array[i + 1]
            self.count -= 1
        return valid_index

    def add(self, new_item):
        has_space_left = not self.is_full()
        if has_space_left:

            # find correct position
            index = 0
            if not self.is_empty():
                while index < self.count and new_item > self.the_array[index]:
                    index += 1

            # move items to right to make space
            for i in range(self.count - 1, index - 1, -1):
                self.the_array[i + 1] = self.the_array[i]

            # insert new_item
            self.the_array[index] = new_item
            self.count += 1
        return has_space_left

    def __contains__(self, item):
        if self._binary_search(item) == -1:
            return False
        return True

    def index(self, item):
        pos = self._binary_search(item)
        if pos == -1:
            raise ValueError(str(item) + " not in list")
        while pos >= 0 and self.the_array[pos] == item:
            pos -= 1
        return pos + 1

    def _binary_search(self, item):
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.the_array[mid] == item:
                return mid
            elif self.the_array[mid] > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1
