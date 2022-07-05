import pygame
pygame.init()
pygame.font.init()

WHITE           = (255, 255, 255)
BLACK           = (0, 0, 0)
RED             = (255, 0, 0)
GREEN           = (0, 255, 0)
BLUE            = (0, 0, 255)
GRAY            = (120, 120, 120)
LIGHTGRAY       = (180, 180, 180)
DARKGRAY        = (50, 50, 50)

FPS             = 120

WIDTH, HEIGHT   = 600, 700

ROWS = COLS     = 40    #increase to have smaller pixels

TOOLBAR_HEIGHT  = HEIGHT - WIDTH

PIXEL_SIZE      = WIDTH // COLS

BG_COLOR        = WHITE

DRAW_GRID_LINES = True

MOUSE_POSITION_TEXT_SIZE = 12

BRUSH_SIZE = 2

def get_font(size):
    return pygame.font.SysFont("arial", size)