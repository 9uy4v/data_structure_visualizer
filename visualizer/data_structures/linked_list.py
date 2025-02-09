from visualizer.data_structures.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop(self):
        temp = self.head
        self.head = self.head.next

        temp.next = None
        return temp

