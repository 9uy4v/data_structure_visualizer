import math

from visualizer.data_structures import Graph,Node
from visualizer.general import *
from visualizer.functions.node_functions import animate_nodes

def draw_graph(graph : Graph, highlight : list = [], sec_highlight : list = [], disabled : list = []):
    handle_events()  # Add event handling
    animation_vectors = []
    length = len(graph.nodes)


    # Calculating the radius of the nodes
    node_radius = width / (length * 2 + 1) / 1.5
    Node.node_radius = node_radius

    # Nodes in graph will be arranged in a circle
    for i,node in enumerate(graph.nodes):
        # Calculating node angle based on index
        angle = (2 * math.pi / length) * i  

        # Calculating node position based on angle
        x = width / 2 + height / 3 * math.cos(angle)  
        y = height / 2 + height / 3 * math.sin(angle)  

        animation_vector = [node.pos , (x,y)]
        animation_vectors.append(animation_vector)
    
    # Drawing the positioned nodes on screen and animating them if their position has changed
    animate_nodes(animation_vectors , graph.nodes, graph.connections, highlight, sec_highlight, disabled)