from BinaryTree import *


class InorderIterator:
    def __init__(self, root):
        # Initializing the stack variable
        self.stk = []

        # Assuming that when iterator is initialized
        # it is always at the first element of tree in its in-order
        self.populate_iterator(root)

    def populate_iterator(self, root):
        while root:
            self.stk.append(root)
            root = root.left

    def has_next(self):
        if not self.stk:
            return False
        else:
            return True

    def get_next(self):  # get_next returns null if there are no more elements in tree
        if not self.stk:
            return None

        r_val = self.stk[-1]
        del self.stk[-1]
        temp = r_val.right
        self.populate_iterator(temp)

        return r_val

# Iterator helper function (Don't modify it)
# This function returns the in-order list of nodes using the hasNext() and
# getNext() methods


def inorder_using_iterator(root):
    iter = InorderIterator(root)
    result = ""
    while iter.has_next():
        ptr = iter.get_next()
        if iter.has_next():
            result += str(ptr.data) + ", "
        else:
            result += str(ptr.data)
    if result == "":
        result = "None"
    return result











def main():
    input1 = [100, 50, 200, 25, 75, 125, 300, 12, 35, 60]
    obj1 = BinaryTree(input1)

    input1.sort()
    obj2 = BinaryTree(input1)

    input3 = list(reversed(input1))
    obj3 = BinaryTree(input3)

    # Creating a single node binary tree with obj as obj4
    input4 = [100]
    obj4 = BinaryTree(input4)

    test_case_roots = [obj1.root, obj2.root, obj3.root, obj4.root, None]
    test_case_statements = ["In-Order Traversal of a normal binary search tree: ",
                            "In-Order Traversal of a right degenerate binary search tree: ",
                            "In-Order Traversal of a left degenerate binary search tree: ",
                            "In-Order Traversal of a single node binary tree: ",
                            "In-Order Traversal of a null tree: "]

    for i in range(len(test_case_roots)):
        if i > 0:
            print()

        print(str((i + 1)) + ".\tBinary Tree:\t" + test_case_statements[i])

        # Printing the in-order list using the method we just implemented
        print("\t" + inorder_using_iterator(test_case_roots[i]))
        print("--------------------------------------------")


if __name__ == '__main__':
    main()

