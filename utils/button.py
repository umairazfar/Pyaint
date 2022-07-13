from turtle import pos
from .settings import *

class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK, shape = "rectangle"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.shape = shape
        self.text_color = text_color

    def draw(self, win):
        if self.shape == "rectangle":
            pygame.draw.rect(win, self.color,(self.x, self.y, self.width, self.height))
            pygame.draw.rect(win, BLACK,(self.x, self.y, self.width, self.height), 2)

        elif self.shape == "ellipse":
            pygame.draw.ellipse(win, self.color, (self.x, self.y, self.width, self.height)) #fill
            pygame.draw.ellipse(win, BLACK, (self.x, self.y, self.width, self.height), 2) #border

        if self.text:
            button_font = get_font(int(self.width/2) - 6)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True

    def hover(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True