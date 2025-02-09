from node import Node

class BinaryTree:

    def __init__(self, head : Node, left : "BinaryTree" = None, right : "BinaryTree" = None):
        self.head = head
        self.left = left
        self.right = right