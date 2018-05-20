# authour = Kieran Goldsworthy
# date created = 18/5
# date modified = 20/5


class BinaryTree:
    # desc = the binary tree object
    def __init__(self):
        # desc = starts the tree
        # parameters = None
        # time complexity:
        # best = O(1)
        # worst = O(1)
        self.root = None

    def is_empty(self):
        # desc = returns if the tree is emtpy or not
        # parameters = None
        # time complexity:
        # best = O(1)
        # worst = O(1)
        return self.root is None

    def add(self, item, bit_str):
        # desc = add an item to the tree
        # parameters = the item to add and where to put it (string)
        # pre-conditions = the string must be binary
        # time complexity:
        # best = O(N)
        # worst = O(N)
        bit_str_itr = iter(bit_str)  # gets an iterator for the binary string
        self.root = self.add_aux(self.root, item, bit_str_itr)  # calls the recursive function

    def add_aux(self, current, item, bit_str_itr):
        # desc = recursive function for adding
        # parameters = the current node, the item to add, the binary string iterator
        # pre-conditions = the current node must be valid, the binary string iterator must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is None:  # node does not exist
            current = TreeNode(None, None, None)  # creates a node

        try:
            bit = next(bit_str_itr)  # gets the next bit in the binary string
            if bit == '0':  # decides if it needs to go left or right
                current.left = self.add_aux(current.left, item, bit_str_itr)  # goes to the next node
            elif bit == '1':
                current.right = self.add_aux(current.right, item, bit_str_itr)
        except StopIteration:  # binary string is ended
            current.item = item  # sets the item to return

        return current  # returns the current node

    def delete(self, bit_str):
        self.add(None, bit_str)

    def item(self, bit_str):
        # desc = gets the item at a given position
        # parameters = the position as a string
        # pre-conditions = the sting must be a binary string
        # time complexity:
        # best = O(N)
        # worst = O(N)
        if self.is_empty():
            return "Tree is empty"
        else:
            bit_str_itr = iter(bit_str)  # makes an iterator for the binary string
            current = self.root  # first node
            # noinspection PyBroadException
            try:  # catches unexpected error
                for _ in range(len(bit_str)):  # for the length of the string
                    bit = next(bit_str_itr)  # next bit
                    if bit == '0':  # decides to go left or right
                        current = current.left
                    elif bit == '1':
                        current = current.right

                return current.item  # returns the item
            except:
                return 'node does not exist'

    def print_preorder(self):
        # desc = prints the tree
        # parameters = None
        # time complexity:
        # best = O(N)
        # worst = O(N)
        self.print_preorder_aux(self.root)  # call recursive function

    def print_preorder_aux(self, current):
        # desc = recursive function for print_preorder
        # parameters = the current node
        # pre-conditions = the current node must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is not None:  # if not the base case
            print(current)  # 3prints the current node
            self.print_preorder_aux(current.left)  # calls to print the left subtree
            self.print_preorder_aux(current.right)  # calls to print the right subtree

    def print_inorder(self):
        # desc = prints the tree
        # parameters = None
        # time complexity:
        # best = O(N)
        # worst = O(N)
        self.print_inorder_aux(self.root)  # call recursive function

    def print_inorder_aux(self, current):
        # desc = recursive function for print_inorder
        # parameters = the current node
        # pre-conditions = the current node must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is not None:  # if not the base case
            self.print_inorder_aux(current.left)  # calls to print the left subtree
            print(current)  # prints the current node
            self.print_inorder_aux(current.right)  # calls to print the right subtree

    def print_postorder(self):
        # desc = prints the tree
        # parameters = None
        # time complexity:
        # best = O(N)
        # worst = O(N)
        self.print_postorder_aux(self.root)  # call recursive function

    def print_postorder_aux(self, current):
        # desc = recursive function for print_postorder
        # parameters = the current node
        # pre-conditions = the current node must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is not None:  # if not the base case
            self.print_postorder_aux(current.left)  # calls to print the left subtree
            self.print_postorder_aux(current.right)  # calls to print the right subtree
            print(current)  # prints the current node
  
    def __len__(self):
        # desc = returns the size of the tree
        # parameters = None
        # time complexity:
        # best = O(N)
        # worst = O(N)
        return self.len_aux(self.root)  # calls the recursive function

    def len_aux(self, current):
        # desc = recursive function for the length
        # parameters = the current node
        # pre-conditions = the current node must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is None:  # base case
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(
                current.right)  # call recursive function, combine and return

    def get_leaves(self):
        # desc = creates a list of all the leaves
        # parameters = None
        # time complexity:
        # best = O(N)
        # worst = O(N)
        a_list = []  # creates the list
        self.get_leaves_aux(self.root, a_list)  # calls teh recursive function
        return a_list  # return the result

    def get_leaves_aux(self, current, a_list):
        # desc = recursive function for get_leaves
        # parameters = the current node and the list
        # pre-conditions = both the current node and the list must be valid
        # time complexity:
        # best = O(1)
        # worst = O(1)
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, a_list)
                self.get_leaves_aux(current.right, a_list)

    @staticmethod
    def is_leaf(current):
        # desc = determines if a node is a leaf or not
        # parameters = the node
        # pre-conditions = the node must be valid
        # post-conditions = returns tue or false
        # time complexity:
        # best = O(1)
        # worst = O(1)
        return current.left is None and current.right is None


class TreeNode:
    # desc = the node object
    def __init__(self, item=None, left=None, right=None):
        # desc = creates teh node and its variables
        # parameters = the item to add, and its left and right children
        # pre-conditions = the right and left children should either be other nodes, or left blank
        # time complexity:
        # best = O(1)
        # worst = O(1)
        self.item = item
        self.right = right
        self.left = left

    def __str__(self):
        # desc = prints the item
        # parameters = None
        # time complexity:
        # best = O(1)
        # worst = O(1)
        return str(self.item)
