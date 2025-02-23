import pygame
from minesweeper import Minesweeper
from draw import draw_rect
# Initialize Pygame
pygame.init()

# Setup
screen_info = pygame.display.Info()
WINDOW_WIDTH = screen_info.current_w * 0.9
WINDOW_HEIGHT = screen_info.current_h * 0.9
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
# Using simple names with the custom RGB values
RED = (215, 38, 0)  # Sinopia
BLUE = (9, 86, 191)  # Sapphire
GREEN = (55, 151, 17)  # Slimy Green
YELLOW = (236, 212, 7)  # Safety Yellow
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Minesweeper2D(Minesweeper):

    def __init__(self):
        super().__init__()
        self.init_game()

    def render_board(self):
        ...

