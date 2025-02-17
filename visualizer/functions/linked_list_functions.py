from visualizer.data_structures import LinkedList, Node
from visualizer.general import *
from visualizer.functions.node_functions import animate_nodes

def draw_linked_list(linked_list : LinkedList, highlights : list[Node] = [], sec_highlight : list[Node] = [], disabled : list[Node] = []):
    handle_events()  # Add event handling
    head = linked_list.head
    nodes = []
    animation_vectors = []
    connections = []
    length = 0

    # Converting LinkedList to an array
    while head:
        nodes.append(head)
        head = head.next
        length += 1

    # Calculating the radius of the nodes
    node_radius = width / (length * 2 + 1) / 1.5

    # Setting the calculated node radius as a static variable in the node class
    Node.node_radius = node_radius  

    # Calculating the margin based on the number and size of the nodes
    margin = (width - node_radius * 2 * length) / (length + 1)
    
    for i,node in enumerate(nodes):
        # Calculating the position of each node 
        x = margin + node_radius + i * ( node_radius * 2 + margin)
        y = height / 2

        animation_vector = [node.pos , (x,y)]
        animation_vectors.append(animation_vector)

        # Connection nodes in order
        if(node.next):
            connections.append((node, node.next))
    
    # Drawing the positioned nodes on screen and animating them if their position has changed
    animate_nodes(animation_vectors, nodes, connections, highlights, sec_highlight, disabled)