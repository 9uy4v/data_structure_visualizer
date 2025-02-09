class Node:
    # static variable
    node_radius = 35

    def __init__(self, data):
        self.data = data
        self.next = None
        self.pos = (400,500)