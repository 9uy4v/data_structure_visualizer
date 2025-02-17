import pygame

from visualizer import general as vis

def draw_array(array, highlights : list[int] = [], sec_highlight : list[int] = [], disabled : list[int] = []):
    vis.handle_events()  # Use centralized event handling
    vis.screen.fill(vis.BACKGROUND)

    # Calculating each cell size
    cell_size = vis.width / (len(array)+1) - 10

    margin = cell_size * 0.05

    # Drawing the border of the array
    arr_x = (vis.width - cell_size * len(array)) / 2
    arr_y = (vis.height - cell_size) / 2
    pygame.draw.rect(vis.screen,vis.PRIMARY,(arr_x,arr_y,cell_size*len(array), cell_size))

    for i, value in enumerate(array):
        # Calculating the posotion of each cell
        x = arr_x  + i * (cell_size)  + margin/2
        y = (vis.height - cell_size + margin) / 2
        font_size = cell_size / 2 

        # Selecting the background color of the cell by given parameters
        if i in highlights:
            cell_color = vis.ITERATORS_COLORS['highlight']
        elif i in sec_highlight:
            cell_color = vis.ITERATORS_COLORS['sec_highlight']
        elif i in disabled:
            cell_color = vis.ITERATORS_COLORS['disabled']
        else: 
            cell_color = vis.BACKGROUND
         
        # Drawing the cell
        pygame.draw.rect(vis.screen,cell_color,(x,y,cell_size - margin,cell_size - margin))
        
        # Displaying text in cell
        vis.display_text(str(value) , (x + cell_size/2, y + cell_size/2) , font_size ,cell_color)

    pygame.display.flip()

    pygame.time.wait(500) # Shows result for half a second
