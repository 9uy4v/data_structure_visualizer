from visualizer.data_structures.node import Node

class BinaryTree:

    def __init__(self, head : Node, left : "BinaryTree" = None, right : "BinaryTree" = None):
        self.head = head
        self.left = left
        self.right = right
    
    # Setting function for left and right child node
    
    def set_right(self, right : "BinaryTree" = None):
        self.right = right

    def set_left(self, left : "BinaryTree" = None):
        self.left = left