import pygame
import sys
from visualizer.data_structures import *
import visualizer as vis
vis.init() # Initializes screen


# ====================== Algorithms =====================================
def bubble_sort(arr):
  
    for n in range(len(arr) - 1, 0, -1):
        
        swapped = False  

        for i in range(n):

            vis.draw_array(arr, [i,i+1,n+1])
            pygame.time.delay(1000)

            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

                vis.draw_array(arr, [i+1 ,i, n+1])
                pygame.time.delay(1000)
                    
        if not swapped:
            break

def BFS(graph: Graph, start: Node):
    visited = []
    queue = LinkedList()
    queue.push(start)
    
    while queue.head:
        current = queue.pop()
        
        if current not in visited:
            vis.draw_graph(graph, highlight=[current], sec_highlight=[], disabled=visited)
            
            for connection in graph.connections:
                if current in connection:
                    other = connection[connection.index(current) -1]
                
                    if other not in visited:
                        vis.draw_graph(graph, highlight=[current], sec_highlight=[connection, other], disabled=visited)
                        queue.push(other)

            visited.append(current)       

# Array to visualize
array = [150, 30, 60, 200, 120, 90, 250]
        
# Linked list to visualize
linked_list = LinkedList()
linked_list.push_value(10)

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
    
    vis.start_algo(BFS, (graph, graph.nodes[0]))

    pygame.time.wait(1000)