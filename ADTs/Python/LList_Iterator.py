#
#
#


class LListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.current.item
            self.current = self.current.next
            return item
        except AttributeError:
            raise StopIteration
