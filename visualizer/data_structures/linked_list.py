from visualizer.data_structures.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # Adding a value to the end of the linked list
    def push_value(self, data):
        new_node = Node(data) # Creating a node based on given data
        # If list is empty set new node as head
        if not self.head:
            self.head = new_node
            return
        
        current = self.head

        # If it isn't first node add to end
        while current.next:
            current = current.next
        
        current.next = new_node
    
    # Adding a node to the end of the linked list
    def push(self, node : Node):

        # If list is empty set new node as head
        if not self.head:
            self.head = node
            return
        
        current = self.head
        
        # If it isn't first node add to end
        while current.next:
            current = current.next 

        current.next = node
        node.next = None

    # Removing a node from the front of the linked list
    def pop(self):
        temp = self.head
        self.head = self.head.next # Setting the head to be the next node

        # Reseting the attributes of theh popped node
        temp.next = None

        return temp

