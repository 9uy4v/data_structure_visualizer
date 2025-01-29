import pygame
import sys

def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            draw_array(arr, [i,i+1,n+1])
            pygame.time.wait(1000)

            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True

                draw_array(arr, [i+1 ,i, n+1])
                pygame.time.wait(1000)
            

        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (40,40,40)
PRIMARY = (25,185,50)
ITERATORS_COLORS = [(0, 180, 0), (0, 100, 0), (139, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 99, 71)]

# Initialize Pygame
pygame.init()

# Set the display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen.fill(BACKGROUND) # Setting background Color
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Array Visualization") 

# Array to visualize
array = [150, 30, 60, 200, 120, 90, 250]


# Function to draw the array    
def draw_array(array, iterators : list[int] = []):
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

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BACKGROUND)


    # Draw the array
    draw_array(array)
    bubble_sort(array)
    pygame.event.post(pygame.QUIT)

    pygame.time.wait(1000)