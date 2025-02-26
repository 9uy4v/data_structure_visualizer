from visualizer.data_structures import *
import visualizer as vis


# ====================== Algorithms =====================================
def bubble_sort(arr):
  
    for n in range(len(arr) - 1, 0, -1):
        
        swapped = False  

        for i in range(n):

            vis.draw_array(arr, highlight=[i], sec_highlight=[i+1], disabled=[z for z in range(n+1,len(arr))])

            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

                vis.draw_array(arr, highlight=[i+1], sec_highlight=[i], disabled=[z for z in range(n+1,len(arr))])
                    
        if not swapped:
            break
    
    # Display sorted array
    index_arr = [i for i in range(len(arr))]
    vis.draw_array(arr, sec_highlight=index_arr)
    vis.draw_array(arr)
    vis.draw_array(arr, sec_highlight=index_arr)
    vis.draw_array(arr)
    vis.draw_array(arr, sec_highlight=index_arr)
    vis.draw_array(arr)
    vis.draw_array(arr, sec_highlight=index_arr)
    
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

def reverse_queue(queue: LinkedList):
    if queue.head is None:
        return
    
    vis.draw_linked_list(queue, disabled=[queue.head])
    cur = queue.pop()

    vis.draw_linked_list(queue)
    reverse_queue(queue)

    queue.push(cur)
    vis.draw_linked_list(queue, highlight=[cur])

def mirror_tree(root : BinaryTree):
    if not root or (not root.left and not root.right):
        return

    vis.draw_binary_tree(root, highlight=[root.head])
    vis.draw_binary_tree(root, highlight=[root.right.head or None,], sec_highlight=[root.left.head or None,])
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    vis.draw_binary_tree(root, duration= 350, highlight=[root.left.head or None,], sec_highlight=[root.right.head or None,])
    vis.draw_binary_tree(root, duration= 150, highlight=[root.left.head or None,],)

    mirror_tree(root.left)
    vis.draw_binary_tree(root, duration=150, highlight=[root.right.head or None])
    mirror_tree(root.right)

    vis.draw_binary_tree(root, duration= 100)

def build_linked_list():
    x = 0
    queue = LinkedList(); 
    print('Building a Queue')

    while (x != -1):
        x = input('enter a number: ')
        queue.push_value(x)
        vis.draw_linked_list(queue)

    return queue

def add_leaf(root : BinaryTree, rl):
    x = 0

    if (rl == '1'):
        x = input('enter value: ')
        root.right = BinaryTree(Node(x))
        x = 0
    elif (rl == '2'):
        x = input('enter value: ')
        root.left = BinaryTree(Node(x))
        x = 0 
    else:
        x = -1 
    
    return x

def build_binary_tree(): 
    x = input('enter tree root: ')

    root = BinaryTree(Node(x))

    while(x != -1):

        vis.draw_binary_tree(root)

        cur = root
        while(True):
            if cur.left == None and cur.right == None:
                rl = input('Do you want to add to the: \n\t1. Right \n\t2. Left\n(-1 to Exit)')
                x = add_leaf(cur, rl)
                break
            elif cur.left == None:
                ac = input('Do you want to: \n\t1. Move Right \n\t2. Add to Left\n(-1 to Exit)')
                if (ac == '1'):
                    cur = cur.right
                elif (ac == '2'):
                    x = add_leaf(cur,ac)
                    break 
            elif cur.right == None:
                ac = input('Do you want to: \n\t1. Add to Right \n\t2. Move Left\n(-1 to Exit)')
                if (ac == '1'):
                    x = add_leaf(cur,ac)
                    break
                elif (ac == '2'):
                    cur = cur.left
            elif cur.left != None and cur.right != None:
                ac = input('Do you want to: \n\t1. Move Right \n\t2. Move Left\n(-1 to Exit)')
                if (ac == '1'):
                    cur = cur.right
                elif (ac == '2'):
                    cur = cur.left
                else: 
                    x = -1
                    break
    
    return root

# Array to visualize
array = [150, 30, 60, 200, 120, 90, 250]
        
# Linked list to visualize
linked_list = LinkedList()
linked_list.push_value(10)
linked_list.push_value(20)
linked_list.push_value(30)
linked_list.push_value(40)
linked_list.push_value(50)
linked_list.push_value(60)
linked_list.push_value(70)

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

vis.init()

# linked_list = build_linked_list()
# tree = build_binary_tree()

mirror_tree(tree)
bubble_sort(array)
reverse_queue(linked_list)
BFS(graph, graph.nodes[0])

vis.exit()