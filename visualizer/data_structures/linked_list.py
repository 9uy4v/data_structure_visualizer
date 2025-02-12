from visualizer.data_structures.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def push_value(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def push(self, node : Node):
        if not self.head:
            self.head = node
            return
        
        current = self.head
        while current.next:
            current = current.next 

        current.next = node

    def pop(self):
        temp = self.head
        self.head = self.head.next

        temp.next = None
        return temp

