class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pos = (400,200)
    
    def setPos(self, pos):
        self.pos = pos
        