import pygame
import sys
import math 
import random

from node import Node
from linked_list import LinkedList
from graph import Graph
from binary_tree import BinaryTree

# ====================== Algorithms =====================================
def bubble_sort(arr):
  
    for n in range(len(arr) - 1, 0, -1):
        
        swapped = False  

        for i in range(n):

            draw_array(arr, [i,i+1,n+1])
            pygame.time.wait(1000)

            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

                draw_array(arr, [i+1 ,i, n+1])
                pygame.time.wait(1000)
                    
        if not swapped:
            break

# ====================== General & init ===================================

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (40,40,40)
PRIMARY = (25,185,50)
BLACK = (0,0,0)
ITERATORS_COLORS = [(0, 180, 0), (0, 100, 0), (139, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 99, 71)]

# Initialize Pygame
pygame.init()

# Set the display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen.fill(BACKGROUND) # Setting background Color
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()

pygame.display.set_caption("Array Visualization") 


def display_text(val : str, pos : tuple[int,int] , font_size = 16 ,cell_color = BACKGROUND):
    font = pygame.font.SysFont(None, int (font_size))
    text = font.render(str(val),True, WHITE,cell_color) 
    text_rect = text.get_rect(center= pos)

    screen.blit(text,text_rect)

# ====================== Arrays =========================================================

# Function to draw an array    
def draw_array(array, iterators : list[int] = []):
    screen.fill(BACKGROUND)

    # Calculating each cell size
    cell_size = width / (len(array)+1) - 10

    margin = cell_size * 0.05

    # Drawing the border of the array
    arr_x = (width - cell_size * len(array)) / 2
    arr_y = (height - cell_size) / 2
    pygame.draw.rect(screen,PRIMARY,(arr_x,arr_y,cell_size*len(array), cell_size))

    for i, value in enumerate(array):
        # Calculating the posotion of each cell
        x = arr_x  + i * (cell_size)  + margin/2
        y = (height - cell_size + margin) / 2
        font_size = cell_size / 2 

        # Coloring cell according to algorithm
        if(iterators.__contains__(i)):
            cell_color = ITERATORS_COLORS[iterators.index(i) % 10]
        else:
            cell_color = BACKGROUND
         
         # Drawing the cell
        pygame.draw.rect(screen,cell_color,(x,y,cell_size - margin,cell_size - margin))
        
        display_text(str(value) , (x + cell_size/2, y + cell_size/2) , font_size ,cell_color)

    pygame.display.flip()

# ========================== General Node Functions ===============================
#                      linked lists, graphs and binary tree

def ease_out(t):
    return 1 - (1-t) ** 3 # An exponential function that fits the curve of the Ease Out animation

def current_location(node_location : tuple[tuple[int,int]], eased_t):
    # Calculating the current position of the node based on the progress of the animation
    cur_x = node_location[0][0] + (node_location[1][0] - node_location[0][0]) * eased_t
    cur_y = node_location[0][1] + (node_location[1][1] - node_location[0][1]) * eased_t
    
    return cur_x, cur_y 
    

def animate_nodes(nodes_locations : list[tuple[tuple[int,int]]], nodes_data : list[Node], connections : list[tuple[Node,Node]]):
    duration = 500
    start_time = pygame.time.get_ticks()
    t = 0
    while t < 1:
        # Calculating the progression of the animation
        elapsed = pygame.time.get_ticks() - start_time        
        t = min(elapsed/duration,1)

        eased_t = ease_out(t)

        # Calculate current position for each Node
        for i,node_location in enumerate(nodes_locations): 
            cur_pos = current_location(node_location , eased_t)

            nodes_data[i].pos = cur_pos
        
        font_size = Node.node_radius / 2 

        # Clearing Screen
        screen.fill(BACKGROUND)

        # Draw edges
        for connection in connections:
            pygame.draw.line(screen, WHITE,connection[0].pos,connection[1].pos, 2)

        # Draw Nodes
        for node in nodes_data:
            pygame.draw.circle(screen, PRIMARY, node.pos, Node.node_radius)
            pygame.draw.circle(screen, BACKGROUND, node.pos, Node.node_radius * 0.9)
            display_text(str(node.data) , node.pos, font_size)

        pygame.display.flip()
        
        clock.tick(60) # Makes sure this is rendered at 60 fps

# ======================= Linked Lists ============================================
      
def draw_linked_list(linked_list : LinkedList):
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
    
    animate_nodes(animation_vectors, nodes, connections)

# ======================= Graphs ====================================================

def draw_graph(graph : Graph):
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
    
    animate_nodes(animation_vectors , graph.nodes, graph.connections)

# ======================= Binary Tree =========================================

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

def position_tree(tree : BinaryTree, animation_vectors : list[tuple[tuple[int,int]]], start_end : tuple[int,int], cur_height, height_block):

    x_pos = sum(start_end) / 2
    y_pos =  height - (height_block * cur_height)

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

    height_block = height / (tree_height + 1) # Calculating the spacing  
    Node.node_radius = min(height_block , width / 2 ** (tree_height -1)) / 2 # TODO : add margin if needed

    position_tree(tree, animation_vectors, (0,width), tree_height, height_block)

    animate_nodes(animation_vectors, nodes, connections)

# ======================= Variables initialization ============================

# Array to visualize
array = [150, 30, 60, 200, 120, 90, 250]
        
# Linked list to visualize
linked_list = LinkedList()
linked_list.append(10)

# Graph to visualize
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
graph = Graph([node_1,node_2,node_3,node_4,node_5], [(node_1,node_3), (node_2,node_5), (node_2,node_4), (node_3,node_4), (node_1,node_5), (node_2,node_3), (node_4,node_1)])

# Binary tree to visualize
nodes = [Node(f"Node{i}") for i in range(25)]

tree = BinaryTree(
    nodes[0],
    BinaryTree(
        nodes[1],
        BinaryTree(
            nodes[3],
            BinaryTree(nodes[7], BinaryTree(nodes[15]), BinaryTree(nodes[16])),
            BinaryTree(nodes[8], BinaryTree(nodes[17]), BinaryTree(nodes[18]))
        ),
        BinaryTree(
            nodes[4],
            BinaryTree(nodes[9], BinaryTree(nodes[19]), BinaryTree(nodes[20])),
            BinaryTree(nodes[10], BinaryTree(nodes[21]), BinaryTree(nodes[22]))
        )
    ),
    BinaryTree(
        nodes[2],
        BinaryTree(
            nodes[5],
            BinaryTree(nodes[11], BinaryTree(nodes[23]), BinaryTree(nodes[24])),
            BinaryTree(nodes[12])
        ),
        BinaryTree(nodes[6], BinaryTree(nodes[13]), BinaryTree(nodes[14]))
    )
)

# =========================== Main ===============================

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    draw_binary_tree(tree)
    
    pygame.time.wait(1000)