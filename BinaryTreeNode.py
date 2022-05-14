class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only sometimes
        self.next = None
        self.parent = None
        self.count = 0
