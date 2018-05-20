#authour = Kieran Goldsworthy + ?
#date created = 25/5
#date modified = 28/5


class MaxHeap:
    #a heap with the largest value at the root

    def __init__(self):
        self.count = 0
        self.array = [None]

    def __len__(self):
        return self.count

    def rise(self, k):
        while k > 1 and self.array[k] > self.array[k // 2]:
            self.array[k], self.array[k // 2] = self.array[k // 2], self.array[k]
            k //= 2

    def add(self, item):
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = item
        else:
            self.array.append(item)

        self.count += 1
        self.rise(self.count)

    def get_max(self):
        if not self.count == 0:
            item = self.array[1]
            self.array[1], self.array[self.count] = self.array[self.count], self.array[1]
            self.array[self.count] = None
            self.count -= 1
            self.sink(1)

            return item
        else:
            return "Queue is empty"

    def sink(self, k):
        while 2 * k <= self.count:
            child = self.largest_child(k)
            if self.array[k] >= self.array[child]:
                break
            self.array[child], self.array[k] = self.array[k], self.array[child]
            k = child

    def largest_child(self, k):
        if 2 * k == self.count or self.array[2 * k] > self.array[(2 * k) + 1]:
            return 2 * k
        else:
            return (2 * k) + 1

    def print_no_order(self):
        for i in range(self.count):
            print(self.array[i + 1])


class MinHeap:
    #A heap that has the smallest element at the root

    def __init__(self):
        #desc. = sets the initialised values
        #parameters = None
        #time complexity: O(1), no loops
        self.count = 0
        self.array = [None]

    def __len__(self):
        #desc. = returns the size
        #parameters = None
        #time complexity: O(1), no loops
        return self.count

    def rise(self, k):
        #desc. = makes a child rise until its heap ordered
        #parameters = a number
        #pre-conditions = n must be the index of an element
        #time complexity: best = O(1), worst = O(Log(N))
        while k > 1 and self.array[k] < self.array[k // 2]:
            self.array[k], self.array[k // 2] = self.array[k // 2], self.array[k]
            k //= 2

    def add(self, item):
        #desc. = adds a new element
        #parameters = an item
        #pre-conditions = item must be a number
        #time complexity: best = O(1), worst = O(Log(N)), inherited from the rise function
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = item
        else:
            self.array.append(item)

        self.count += 1
        self.rise(self.count)

    def get_min(self):
        #desc. = gets the first element
        #parameters = None
        #time complexity: best = O(1), worst = O(log(N)), inherited from the sink function
        if not self.count == 0:
            item = self.array[1]
            self.array[1], self.array[self.count] = self.array[self.count], self.array[1]
            self.array[self.count] = None
            self.count -= 1
            self.sink(1)

            return item
        else:
            return "Queue is empty"

    def sink(self, k):
        #desc. = makes the first element sink until its heap ordered
        #parameters = a number
        #pre-conditions = n must be the index of an element
        #time complexity: best = O(1), worst = O(log(N)), straight away or all the list
        while 2 * k <= self.count:
            child = self.smallest_child(k)
            if self.array[k] <= self.array[child]:
                break
            self.array[child], self.array[k] = self.array[k], self.array[child]
            k = child

    def smallest_child(self, k):
        #desc. = gets the smallest child of an element
        #parameters = a number
        #pre-conditions = n must be the index of an element
        #post-condition = returned is the index location of the smallest child
        #time complexity: O(1), no loops
        if (2 * k == self.count) or (self.array[2 * k] < self.array[(2 * k) + 1]):
            return 2 * k
        else:
            return (2 * k) + 1

    def print_no_order(self):
        #desc. = prints the queue in the order it appears in the array
        #parameters = None
        #time complexity: O(N)
        for i in range(self.count):
            print(self.array[i + 1])

    def print_in_order(self):
        #desc. = prints the queue in order
        #parameters = None
        #time complexity: O(N)
        if len(self) == 0:
            print("Queue is empty")
        else:
            tmp_list = []
            while len(self) > 0:
                next_item = self.get_min()
                tmp_list.append(next_item)
                print(next_item)
            while len(tmp_list) > 0:
                self.add(tmp_list.pop())
