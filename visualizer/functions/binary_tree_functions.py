from visualizer.data_structures import BinaryTree,Node
from visualizer import general as vis
from visualizer.functions.node_functions import animate_nodes

# Mapping the tree to a node array and a connection array
def map_tree(tree : BinaryTree, nodes : list[Node] , connections : list[tuple[Node,Node]]):
    cur = tree.head 
    right_height = left_height = 0

    nodes.append(cur) # Adds the current node to the nodes list

    # Adding the connection between the current node and his children
    if tree.left != None:
        connections.append((cur,tree.left.head))

        # Calling the function on the left son
        left_height = map_tree(tree.left, nodes, connections)

    if tree.right != None:
        connections.append((cur,tree.right.head))

        # Calling the function on the left son
        right_height = map_tree(tree.right, nodes, connections)

    return max(right_height, left_height) + 1

# Positioning each of the tree's nodes on the screen 
def position_tree(tree : BinaryTree, animation_vectors : list[tuple[tuple[int,int]]], start_end : tuple[int,int], cur_height, height_block):

    x_pos = sum(start_end) / 2
    y_pos =  vis.height - (height_block * cur_height)

    animation_vectors.append((tree.head.pos, (x_pos, y_pos)))

    if tree.left != None:
        position_tree(tree.left , animation_vectors, (start_end[0], x_pos), cur_height - 1, height_block)

    if tree.right != None:
        position_tree(tree.right, animation_vectors, (x_pos, start_end[1]), cur_height - 1, height_block)

def draw_binary_tree(tree : BinaryTree):
    nodes = []
    connections = []
    animation_vectors = []

    # Mapping the tree to a node array and a connection array
    tree_height = map_tree(tree ,nodes, connections)

    height_block = vis.height / (tree_height + 1) # Calculating the spacing  
    Node.node_radius = min(height_block , vis.width / 2 ** (tree_height -1)) / 2

    # Positioning all of tree's nodes on screen
    position_tree(tree, animation_vectors, (0,vis.width), tree_height, height_block)

    # Drawing the positioned nodes on screen and animating them if their position has changed
    animate_nodes(animation_vectors, nodes, connections)