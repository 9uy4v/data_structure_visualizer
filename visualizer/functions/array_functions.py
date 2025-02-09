import pygame

from visualizer.general import *

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
