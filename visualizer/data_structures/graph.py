from visualizer.data_structures.node import Node

class Graph:

    def __init__(self, nodes : list[Node] = [], connections : list[tuple[Node]] = []):
        self.nodes = nodes
        self.connections = connections 

    # Add a node to the graph
    def add_node(self,node : Node , connected_nodes : list[Node] = []):
        self.nodes.append(node) # Adding node to nodes list
        
        # Adding connections to node
        self.connections.extend((node, connected_node) for connected_node in connected_nodes)