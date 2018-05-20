#
#
#


class BinarySearchTreeNode:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __contains__(self, key):
        # noinspection PyTypeChecker
        return self.contains_aux(self.root, key)

    def contains_aux(self, current, key):
        if current is None:  # base case: empty
            raise KeyError("key not found")
        elif key == current.key:  # base case: found
            return True
        elif key < current.key:
            return self.contains_aux(current.left, key)
        else:  # key > current.key
            return self.contains_aux(current.right, key)

    def __getitem__(self, key):  # use 'BST[key]'
        # noinspection PyTypeChecker
        return self.getitem_aux(self.root, key)

    def getitem_aux(self, current, key):
        if current is None:  # base case: empty
            raise KeyError("key not found")
        elif key == current.key:  # base case: found
            return current.item
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            return self.getitem_aux(current.right, key)

    def __setitem__(self, key, item):  # use 'BST[key] = item'
        self.root = self.setitem_aux(self.root, key, item)

    def setitem_aux(self, current, key, item):
        if current is None:  # base case: at the leaf
            current = BinarySearchTreeNode(key, item)
        elif key < current.key:
            current.left = self.setitem_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.setitem_aux(current.right, key, item)
        else:  # key == current.key
            current.item = item
        return current

    def __delitem__(self, key):  # use 'del BST[key]'
        node = self.delitem_aux1(key, self.root)
        if key == node.left.key:
            next_node = "right"
            if node.left.left == None:
                node.left = node.left.right
            elif node.left.right == None:
                node.left = node.left.left
            else:
                self.delitem_aux2(key)
        elif key == node.right.key:
            next_node = "right"
            if node.right.left == None:
                node.left = node.left.right
            elif node.right.right == None:
                node.left = node.left.left
            else:
                self.delitem_aux2(key)




    def delitem_aux1(self, key, current):
        if current is None:  # base case: empty
            raise KeyError("key not found")
        elif key < current.key:
            if key == current.left.key:  # base case: found
                return current.left
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            if key == current.right.key:
                return current.left
            return self.getitem_aux(current.right, key)


######Write deleting code from lecture 30
