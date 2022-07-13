import pygame
pygame.init()
pygame.font.init()

WHITE           = (255, 255, 255)
BLACK           = (0, 0, 0)
RED             = (255, 0, 0)
GREEN           = (0, 255, 0)
BLUE            = (0, 0, 255)
GREEN           = (0, 255, 0)
MAROON          = (255, 0, 0)
LIME            = (0, 255, 0)
BLUE            = (0, 0, 255)
GRAY            = (120, 120, 120)
LIGHTGRAY       = (180, 180, 180)
NAVY            = (0, 0, 128)
GRAY            = (128, 128, 128)
SILVER          = (192, 192, 192)
DARKGRAY        = (50, 50, 50)


FPS             = 120
WIDTH, HEIGHT   = 600, 700
ROWS = COLS     = 40    #increase to have smaller pixels
TOOLBAR_HEIGHT  = HEIGHT - WIDTH
PIXEL_SIZE      = WIDTH // COLS
BG_COLOR        = WHITE
DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("arial", size)


FPS             = 120

WIDTH, HEIGHT   = 600, 700

ROWS = COLS     = 40    #increase to have smaller pixels

TOOLBAR_HEIGHT  = HEIGHT - WIDTH

RIGHT_TOOLBAR_WIDTH = 75

PIXEL_SIZE      = WIDTH // COLS

BG_COLOR        = WHITE

DRAW_GRID_LINES = True

MOUSE_POSITION_TEXT_SIZE = 12

BRUSH_SIZE = 1  #can be 2, 3, 4 or any other value

def get_font(size):
    return pygame.font.SysFont("arial", size)