import pygame

width, height = 800, 600
screen = None
clock = None

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (40,40,40)
PRIMARY = (25,185,50)
BLACK = (0,0,0)
ITERATORS_COLORS = [(0, 180, 0), (0, 100, 0), (139, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 99, 71)]

def init():
    global screen, clock

    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    screen.fill(BACKGROUND) # Setting background Color
    print(f"Screen initialized: {screen is not None}")

    clock = pygame.time.Clock()

    pygame.display.set_caption("Array Visualization") 

    pygame.display.flip()



def display_text(val : str, pos : tuple[int,int] , font_size = 16 ,cell_color = BACKGROUND):
    font = pygame.font.SysFont(None, int (font_size))
    text = font.render(str(val),True, WHITE,cell_color) 
    text_rect = text.get_rect(center= pos)

    screen.blit(text,text_rect)