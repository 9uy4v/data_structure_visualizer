class Node:
    # static variable
    node_radius = 35

    def __init__(self, data):
        self.data = data
        self.next = None
        self.pos = (400,500)
    
    def setPos(self, pos):
        self.pos = pos
        