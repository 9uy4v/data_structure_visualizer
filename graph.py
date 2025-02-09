from node import Node
class Graph:

    def __init__(self, nodes : list[Node] = [], connections : list[tuple[Node,Node]] = []):
        self.nodes = nodes
        self.connections = connections 

    def add_node(self,node : Node , connected_nodes : list[Node] = []):
        self.nodes.append(node)
        self.connections.extend((node, connected_node) for connected_node in connected_nodes)