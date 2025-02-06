from node import Node
class Graph:

    def __init__(self, nodes : list[Node] = [], connections : list[tuple[Node,Node]] = []):
        self.nodes = nodes
        self.connections = connections 

    def add_node(self,node : Node , connections : list[tuple[Node,Node]] = []):
        self.nodes.append(node)
        self.connections.extend(connections)