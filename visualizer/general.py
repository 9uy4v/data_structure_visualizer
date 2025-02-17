import pygame
import threading

width, height = 800, 600
screen = None
clock = None

# Colors
WHITE = (255, 255, 255)
BACKGROUND = (40,40,40)
PRIMARY = (25,185,50)
BLACK = (0,0,0)

ITERATORS_COLORS = {'highlight' : (0, 180, 0),
                    'sec_highlight' : (0, 100, 0),
                    'disabled' : (139, 0, 0), }

algo_thread = None # Thread that runs the visualized algorithms

def init():
    global screen, clock

    pygame.init()

    # Basic display settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Visualization")
    screen.fill(BACKGROUND)

    print(f"Screen initialized: {screen}")  # Debugging

    clock = pygame.time.Clock()

    pygame.display.flip()

def display_text(val : str, pos : tuple[int,int] , font_size = 16 ,cell_color = BACKGROUND):
    font = pygame.font.SysFont(None, int (font_size))
    text = font.render(str(val),True, WHITE,cell_color) 
    text_rect = text.get_rect(center= pos)

    screen.blit(text,text_rect)

# Running a visualization algorithm in a thread and limiting it to one at a time
def start_algo(func,data):
    global algo_thread

    if algo_thread is None or not algo_thread.is_alive():
        algo_thread = threading.Thread(target=func, args=data)
        algo_thread.start()