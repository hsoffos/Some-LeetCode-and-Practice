# Importing required functions
from BinaryTree import *


def are_identical(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        print(root1.data, root2.data)
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    return False


def main():
    input1 = [100, 50, 200, 25, 125, 350]
    obj1 = BinaryTree(input1)

    input2 = [4, 2, 6, 1, 5, 7]
    obj2 = BinaryTree(input2)

    input3 = [100, 25, 200, 50, 125, 350]
    obj3 = BinaryTree(input3)

    test_case_root1 = [obj1.root, obj1.root, obj1.root, obj1.root, None]
    test_case_root2 = [obj1.root, obj2.root, obj3.root, None, None]

    for i in range(len(test_case_root1)):
        if i > 0:
            print("\n")

        # Displaying level-order traversal of trees being tested
        print((i + 1), ".\tIdentical Tree: ", end="")

        # Calling our areIdentical() function to check if tree are identical
        if are_identical(test_case_root1[i], test_case_root2[i]):
            print("true")
        else:
            print("false")
        print(
            "----------------------------------------------------------------", end="")


if __name__ == '__main__':
    main()
