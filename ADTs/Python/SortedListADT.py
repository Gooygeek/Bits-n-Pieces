###############################################################################
#
#
#
###############################################################################


class SList:
    def __init__(self, array=[]):
        self.count = 0
        self.the_array = []
        if array != []:
            for item in array:
                self.add(item)

    def __repr__(self):
        return str(self.the_array)

    def __len__(self):
        return self.count

    def __contains__(self, item):
        if self._binary_search(item) == -1:
            return False
        return True

    def __getitem__(self, index):
        return self.the_array[index]

    def add(self, new_item):
        # Find correct position
        index = 0
        while index < self.count and new_item > self.the_array[index]:
            index += 1

        # Move items to right to make space
        self.the_array.append(None)
        for i in range(self.count - 1, index - 1, -1):
            self.the_array[i + 1] = self.the_array[i]

        # Insert new_item
        self.the_array[index] = new_item
        self.count += 1
        return

    def delete(self, index):
        value = self.the_array[index]
        self.the_array = self.the_array[:index] + self.the_array[:index + 1]
        self.count -= 1
        return value

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
