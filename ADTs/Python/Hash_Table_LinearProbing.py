#
#
#


class LinearProbeTable:
    def __init__(self, size=7919):
        self.count = 0
        self.array = [None] * size
        self.size = size

    def __len__(self):
        return self.count

    def hash(self, key):
        value = 0
        a = 31415
        b = 27183
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.size
            a = a * b % (self.size - 1)
        return value

    def __setitem__(self, key, data):
        position = self.hash(key)
        for _ in range(self.size):
            if self.array[position] is None:  # found empty slot
                self.array[position] = (key, data)
                self.count += 1
                return
            elif self.array[position][0] == key:  # found key
                self.array[position] = (key, data)
                return
            else:  # not found, try next
                position = (position + 1) % self.size
        self.rehash()
        self.__setitem__(key, data)

    def rehash(self):
        self.size *= 101
        old_table = []
        for i in range(len(self)):
            old_table[i] = self.array[i]
        self.array = [None] * self.size
        for i in range(len(self)):
            to_rehash = old_table[i]
            self.__setitem__(hash(to_rehash[0]), to_rehash[1])

    def __getitem__(self, key):
        position = self.hash(key)
        for _ in range(self.size):
            if self.array[position] is None:  # found empty slot
                return None
            elif self.array[position][0] == key:  # found key
                return self.array[position][1]
            else:  # not found, try next
                position = (position + 1) % self.size
        raise KeyError(key)
