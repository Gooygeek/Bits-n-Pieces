#
#
#


from LNode import Node
from LList_Iterator import LListIterator


class LList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count is 0

    @staticmethod
    def is_full():
        return False

    def reset(self):
        self.__init__()

    def __len__(self):
        return self.count

    def __str__(self):
        for k in range(len(self)):
            print(self.print_at_index(k))
        return ""

    def print_structure(self):  # can be modified to work better than str()
        node = self.head
        while node is not None:
            print(node, end=" ")
            node = node.next
        print()

    def print_at_index(self, index):
        if (index > len(self)) or (index < (-1 * (len(self)))):
            raise IndexError("Index out of range")
        elif index < 0:
            node = self._getnode(len(self) + index)
            return node.item
        else:   
            node = self._getnode(index)
            return node.item

    def insert(self, index, item):
        if index < 0:  # negatives?
            index = 0
        elif index > len(self):
            index = len(self)
        if index is 0:
            self.head = Node(item, self.head)
            self.count += 1
        else:
            node = self._getnode(index - 1)
            node.next = Node(item, node.next)
            self.count += 1

    def delete(self, index):
        if self.is_empty():
            raise IndexError("List is empty")
        if index < 0 or index > len(self):
            raise IndexError("index out of range")

        if index is 0:
            self.head = self.head.next
        else:
            node = self._getnode(index - 1)
            node.next = node.next.next
        self.count -= 1

    def _getnode(self, index):
        node = self.head

        for _ in range(index):
            node = node.next
        return node

    def __contains__(self, item):
        # noinspection PyTypeChecker
        return self._contains_aux(self.head, item)

    def _contains_aux(self, current, item):
        if current is None:  # base case
            return False
        elif current == item:
            return True
        else:
            return self._contains_aux(current.next, item)

    def copy(self):
        new_list = LList()
        self._copy_aux(self.head, new_list)
        return new_list

    def _copy_aux(self, node, new_list):
        if node is not None:
            self._copy_aux(node.next, new_list)
            new_list.insert(0, node.item)

    def __iter__(self):
        return LListIterator(self.head)
