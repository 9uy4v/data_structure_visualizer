import pygame
import sys
import math

from node import Node
from linked_list import LinkedList

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

# Array to visualize
array = [150, 30, 60, 200, 120, 90, 250]



# ======================================================================================






# Function to draw an array    
def draw_array(array, iterators : list[int] = []):
    screen.fill(BACKGROUND)

    cell_size = width / (len(array)+1) - 10

    margin = cell_size * 0.05

    arr_x = (width - cell_size * len(array)) / 2
    arr_y = (height - cell_size) / 2
    pygame.draw.rect(screen,PRIMARY,(arr_x,arr_y,cell_size*len(array), cell_size))

    for i, value in enumerate(array):
        x = arr_x  + i * (cell_size)  + margin/2
        y = (height - cell_size + margin) / 2
        if(iterators.__contains__(i)):
            cell_color = ITERATORS_COLORS[iterators.index(i) % 10]
        else:
            cell_color = BACKGROUND
         
        pygame.draw.rect(screen,cell_color,(x,y,cell_size - margin,cell_size - margin))
        
        text = font.render(str(value),True, WHITE,cell_color)
        text_rect = text.get_rect(center= (x + cell_size/2, y + cell_size/2))

        screen.blit(text,text_rect)


    pygame.display.flip()




# ======================================================================================
# Nodes- linked lists, graphs and binary tree


def ease_out(t):
    return 1 - (1-t) ** 3 # An exponantial function that fits the curve of Ease Out

def current_location(node_location : list[tuple[int,int]], eased_t):
    cur_x = node_location[0][0] + (node_location[1][0] - node_location[0][0]) * eased_t
    cur_y = node_location[0][1] + (node_location[1][1] - node_location[0][1]) * eased_t
    return cur_x, cur_y 
    

def animate_nodes(nodes_locations : list[list[tuple[int,int]]], nodes_data : list[Node], connections : list[tuple[Node]]):
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

            nodes_data[i].setPos(cur_pos)
        
        # Clearing Screen
        screen.fill(BACKGROUND)

        # Draw edges
        for connection in connections:
            pygame.draw.line(screen, WHITE,connection[0].pos,connection[1].pos, 2)

        # Draw Nodes
        for node in nodes_data:
            pygame.draw.circle(screen, PRIMARY, node.pos, 35)
            pygame.draw.circle(screen, BACKGROUND, node.pos, 32)
            # TODO : add value of node inside of it

        pygame.display.flip()
        
        clock.tick(60) # Makes sure this is rendered at 60 fps

                    
def draw_linked_list(linked_list : LinkedList):
    head = linked_list.head
    nodes = []
    length = 0
    animation_vectors = []
    connections = []

    # Converting LinkedList to an array
    while head:
        nodes.append(head)
        head = head.next
        length += 1

    margin = 250

    for i,node in enumerate(nodes):
        x = 50 + i *( 35 + margin / 2)
        y = (height - 35) /2

        animation_vector = [node.pos , (x,y)]
        animation_vectors.append(animation_vector)

        if(node.next):
            connections.append((node, node.next))
    
    animate_nodes(animation_vectors, nodes, connections)

        
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    


    draw_linked_list(linked_list)
    pygame.time.wait(1000)
