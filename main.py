from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")

def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):    #use _ when variable is not required
            grid[i].append(color)
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(12)
    
    try:
        row, col = get_row_col_from_pos(pos)
        text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
        win.blit(text_surface, (5 , HEIGHT - TOOLBAR_HEIGHT))
    except IndexError:
        for button in buttons:
            if not button.hover(pos):
                continue
            if button.text == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.text == "Erase":
                text_surface = pos_font.render("Erase", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            r,g,b = button.color
            text_surface = pos_font.render("( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)
            
            win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
    

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_button.draw(win)

    draw_mouse_position_text(win)
    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= ROWS:
        raise IndexError
    return row, col

run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
button_width = 40
button_height = 40

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42

buttons = []

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]) )

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS)/2)]) )


buttons.append(Button(WIDTH - button_space, button_y_top_row, button_width, 40, WHITE, "Erase", BLACK))
buttons.append(Button(WIDTH - button_space, button_y_bot_row, button_width, 40, WHITE, "Clear", BLACK))

draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT/2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

<<<<<<< Updated upstream
=======
button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42

buttons = []

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]) )

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS)/2)]) )


buttons.append(Button(WIDTH - button_space, button_y_top_row, button_width, 40, WHITE, "Erase", BLACK))
buttons.append(Button(WIDTH - button_space, button_y_bot_row, button_width, 40, WHITE, "Clear", BLACK))
>>>>>>> Stashed changes
while run:
    clock.tick(FPS) #limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #if user closed the program
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        break
                    drawing_color = button.color
                    draw_button.color = drawing_color
                    break

    draw(WIN, grid, buttons)
    
pygame.quit()
