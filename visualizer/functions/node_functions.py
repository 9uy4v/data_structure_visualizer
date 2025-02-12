import pygame

from visualizer.data_structures import Node
from visualizer import general as vis

def ease_out(t):
    return 1 - (1-t) ** 3 # An exponential function that fits the curve of the Ease Out animation

def current_location(node_location : tuple[tuple[int,int]], eased_t):
    # Calculating the current position of the node based on the progress of the animation
    cur_x = node_location[0][0] + (node_location[1][0] - node_location[0][0]) * eased_t
    cur_y = node_location[0][1] + (node_location[1][1] - node_location[0][1]) * eased_t
    
    return cur_x, cur_y 
    

def animate_nodes(nodes_locations : list[tuple[tuple[int,int]]], nodes_data : list[Node], connections : list[tuple[Node,Node]], highlight : list = [], sec_highlight : list = [], disabled : list = []):
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
        
        font_size = Node.node_radius / 1.5 # TODO Fix font size calculation

        # Clearing Screen
        vis.screen.fill(vis.BACKGROUND)

        # Draw edges
        for connection in connections:
            color = vis.WHITE

            if connection in highlight:
                color = vis.ITERATORS_COLORS[0]
            if connection in sec_highlight:
                color = vis.ITERATORS_COLORS[1]
            if connection in disabled:
                color = vis.ITERATORS_COLORS[2]

            pygame.draw.line(vis.screen, color, connection[0].pos, connection[1].pos, 2)

        # Draw Nodes
        for node in nodes_data:
            color = vis.BACKGROUND

            if node in highlight:
                color = vis.ITERATORS_COLORS[0]
            elif node in sec_highlight:
                color = vis.ITERATORS_COLORS[1]
            elif node in disabled:
                color = vis.ITERATORS_COLORS[2]

                
            pygame.draw.circle(vis.screen, vis.PRIMARY, node.pos, Node.node_radius)
            pygame.draw.circle(vis.screen, color, node.pos, Node.node_radius * 0.9)
            vis.display_text(str(node.data) , node.pos, font_size, color)

        pygame.display.flip()
        
        vis.clock.tick(60) # Makes sure this is rendered at 60 fps
    
    pygame.time.wait(500) # Shows result for half a second