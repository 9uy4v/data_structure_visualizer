import sys
import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

width, height = 800, 600
screen = None
clock = None
running = True

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (40,40,40)
PRIMARY = (25,185,50)
BLACK = (0,0,0)

ITERATORS_COLORS = {'highlight' : (0, 180, 0),
                    'sec_highlight' : (0, 100, 0),
                    'disabled' : (139, 0, 0), }

def init():
    global screen, clock, running

    running = True

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(BACKGROUND)
    pygame.display.set_caption("Visualization")

    clock = pygame.time.Clock()

    pygame.display.flip()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def display_text(val : str, pos : tuple[int,int] , font_size = 16 ,cell_color = BACKGROUND):
    font = pygame.font.SysFont(None, int(font_size))
    text = font.render(str(val), True, WHITE, cell_color) 
    text_rect = text.get_rect(center=pos)
    
    screen.blit(text, text_rect)

def exit():
    global running
    running = False
    pygame.quit()
    sys.exit()