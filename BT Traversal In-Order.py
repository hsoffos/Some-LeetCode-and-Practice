from collections import deque
from BinaryTree import *


# Function that prints the in-order traversal of the binary tree
def inorder_iterative(root):
    result = ""
    if not root:
        # If the root is None, we simply print None
        print("None", end="")
    else:
        # Initializing the stack
        stk = deque()
        curr_node = root

        # This loop will keep printing the tree node in "L N R" fashion
        # until the current node is None or the stack becomes empty
        while stk or curr_node:
            # If the current node is not None, we push it into the stack and point it
            # to its left child and skip to the next iteration
            if curr_node:
                stk.append(curr_node)
                curr_node = curr_node.left
                continue

            # Current node is None, meaning that it's time to print the nodes in the "L"
            # sub-tree
            # So, printing and popping the top-most element of the stack
            result += str(stk[-1].data) + ", "
            curr_node = stk[-1].right
            stk.pop()

        # Truncating right most comma
        result_ = result[:-2]
        print(str(result_), end = "")


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
                            "In-Order Traversal of a None tree: "]

    for i in range(len(test_case_roots)):
        if i > 0:
            print()
        print(str(i + 1) + ".\tBinary Tree:\t" + test_case_statements[i], end="")

    # Printing the in-order list using the method we just implemented
        inorder_iterative(test_case_roots[i])
    print("\n-----------------------------------")


if __name__ == '__main__':
    main()
