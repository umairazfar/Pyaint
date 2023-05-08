from utils import *
import pygame as pygame
import time
WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False


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

def historyFunction(win,hist):
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('History', True, (30,144,255), white)
    win.blit(text, (700, HEIGHT - 690))
    font2 = pygame.font.Font('freesansbold.ttf',15)
    if(len(hist)>0):
        for x in range(len(hist)):
            if(hist[x][0]=="E"):
                text2 = font2.render("Erase", True, (0,0,0), white)
            elif(hist[x][0]=="Undo"):
                text2 = font2.render("Undo", True, (0,0,0), white)
            elif(hist[x][0]=="Redo"):
                text2 = font2.render("Redo", True, (0,0,0), white)
            elif(hist[x][0]=="A"):
                text2 = font2.render("Animate", True, (0,0,0), white)
            elif(hist[x][0]=="Brush Size Change"):
                stri=""
                stri=hist[x][0]+" --> Size:"+str(hist[x][1])
                text2 = font2.render(stri, True, (0,0,0), white)
            else:
                stri=""
                stri=hist[x][0]+" --> Color:"+str(hist[x][1])
                text2 = font2.render(stri, True, (0,0,0), white)
            win.blit(text2, (700, HEIGHT - (650-(x*20))))

def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
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
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Change":
                text_surface = pos_font.render("Swap Toolbar", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Undo":
                text_surface = pos_font.render("Undo", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Redo":
                text_surface = pos_font.render("Redo", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "history":
                text_surface = pos_font.render("History", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Animate":
                text_surface = pos_font.render("Animate", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            r,g,b = button.color
            text_surface = pos_font.render("( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)

            win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))

        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break

def draw(win, grid, buttons,history):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    draw_mouse_position_text(win)
    historyFunction(win,history)
    pygame.display.update()


def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small/2, 480, size_small, size_small, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_medium/2, 510, size_medium, size_medium, drawing_color, None, None, "ellipse") ,
        Button(rtb_x - size_large/2, 550, size_large, size_large, drawing_color, None, None, "ellipse")
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if ((BRUSH_SIZE == 1 and button.width == size_small) or (BRUSH_SIZE == 2 and button.width == size_medium) or (BRUSH_SIZE == 3 and button.width == size_large)):
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(win, border_color, (button.x, button.y, button.width, button.height), border_width) #border

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= ROWS:
        raise IndexError
    return row, col

def paint_using_brush(row, col, size,color):
    if size == 1:
        grid[row][col] = color
    else: #for values greater than 1
        r = row-size+1
        c = col-size+1

        for i in range(size*2-1):
            for j in range(size*2-1):
                if r+i<0 or c+j<0 or r+i>=ROWS or c+j>=COLS:
                    continue
                grid[r+i][c+j] = color


# Checks whether the coordinated are within the canvas
def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1

def fill_bucket(row, col, color):

  # Visiting array
  vis = [[0 for i in range(101)] for j in range(101)]

  # Creating queue for bfs
  obj = []

  # Pushing pair of {x, y}
  obj.append([row, col])

  # Marking {x, y} as visited
  vis[row][col] = 1

  # Until queue is empty
  while len(obj) > 0:

    # Extracting front pair
    coord = obj[0]
    x = coord[0]
    y = coord[1]
    preColor = grid[x][y]

    grid[x][y] = color

    # Popping front pair of queue
    obj.pop(0)

    # For Upside Pixel or Cell
    if inBounds(x + 1, y) == 1 and vis[x + 1][y] == 0 and grid[x + 1][y] == preColor:
      obj.append([x + 1, y])
      vis[x + 1][y] = 1

    # For Downside Pixel or Cell
    if inBounds(x - 1, y) == 1 and vis[x - 1][y] == 0 and grid[x - 1][y] == preColor:
      obj.append([x - 1, y])
      vis[x - 1][y] = 1

    # For Right side Pixel or Cell
    if inBounds(x, y + 1) == 1 and vis[x][y + 1] == 0 and grid[x][y + 1] == preColor:
      obj.append([x, y + 1])
      vis[x][y + 1] = 1

    # For Left side Pixel or Cell
    if inBounds(x, y - 1) == 1 and vis[x][y - 1] == 0 and grid[x][y - 1] == preColor:
      obj.append([x, y - 1])
      vis[x][y - 1] = 1


run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH/2
brush_widths = [
    Button(rtb_x - size_small/2, 480, size_small, size_small, drawing_color, None, "ellipse"),
    Button(rtb_x - size_medium/2, 510, size_medium, size_medium, drawing_color, None, "ellipse") ,
    Button(rtb_x - size_large/2, 550, size_large, size_large, drawing_color, None, "ellipse")
]

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42


# Adding Buttons
buttons = []

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]) )

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS)/2)]) )

#Right toolbar buttonst
 #need to add change toolbar button.
#for i in range(10):
#        buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,name="Change"))#Change toolbar buttons
#    else:
#        buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,"B"+str(i-1), BLACK))#append tools

buttons.append(Button(HEIGHT - 2*button_width,(0*button_height)+5,button_width,button_height,WHITE,name="Undo",image_url="assets/undo.png"))
buttons.append(Button(HEIGHT - 2*button_width,(1*button_height)+10,button_width,button_height,WHITE,name="Redo",image_url="assets/redo.png"))#append tools
buttons.append(Button(HEIGHT - 2*button_width,(2*button_height)+20,button_width,button_height,WHITE,name="history",image_url="assets/history.png"))
buttons.append(Button(HEIGHT - 2*button_width,(3*button_height)+35,button_width,button_height,WHITE,name="Animate",image_url="assets/animate.png"))
buttons.append(Button(WIDTH - button_space, button_y_top_row, button_width, button_height, WHITE, "Erase", BLACK))  # Erase Button
buttons.append(Button(WIDTH - button_space, button_y_bot_row, button_width, button_height, WHITE, "Clear", BLACK))  # Clear Button
buttons.append(Button(WIDTH - 3*button_space + 5, button_y_top_row,button_width-5, button_height-5, name = "FillBucket",image_url="assets/paint-bucket.png")) #FillBucket
buttons.append(Button(WIDTH - 3*button_space + 45, button_y_top_row,button_width-5, button_height-5, name = "Brush",image_url="assets/paint-brush.png")) #Brush
buttons.append(Button(HEIGHT - 2*button_width+330,(0*button_height)+5,button_width,button_height,WHITE,name="Close",image_url="assets/close.png"))


draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT/2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)
x,y=0,0
stack=[]
stack2=[]
history=[]
oldLength=0
lastAction=""

while run:
    clock.tick(FPS) #limiting FPS to 60 or any other value
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #if user closed the program
            run = False

        keys=pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0]:

            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                if(x!=row or y!=col):
                    stack.append((row,col,STATE,drawing_color,BRUSH_SIZE))
                    if(lastAction!="Brush" and STATE=="COLOR" and lastAction!="Erase"):
                        history.append(("Brush Applied",drawing_color,BRUSH_SIZE))
                        lastAction="Brush"
                    elif(STATE=="FILL"):
                        history.append(("Bucket Applied",drawing_color))
                        lastAction="Bucket"
                    x=row
                    y=col


                if STATE == "COLOR":
                    for i in range(len(stack)):
                        if(stack[i][2]=="COLOR"):
                            paint_using_brush(stack[i][0],stack[i][1], stack[i][4],stack[i][3])

                if STATE == "FILL":
                    for i in range(len(stack)):
                        if(stack[i][2]=="FILL"):
                            fill_bucket(stack[i][0], stack[i][1], stack[i][3])


            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        STATE = "COLOR"
                        history.append(("Clear"))
                        lastAction="Clear"
                        break

                    if button.name == "Undo":
                        grid=init_grid(ROWS, COLS, BG_COLOR)
                        if(len(stack)>0):
                            temp=stack.pop()
                            stack2.append(temp)
                            if(lastAction!="Undo"):
                                history.append(("Undo",temp))
                                lastAction="Undo"
                        for i in range(len(stack)):
                            if(stack[i][2]=="COLOR"):
                                paint_using_brush(stack[i][0],stack[i][1],stack[i][4],stack[i][3])
                            elif(stack[i][2]=="FILL"):
                                fill_bucket(stack[i][0], stack[i][1], stack[i][3])

                        break
                    if button.name == "Redo":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        if(len(stack2)>0):
                            temp2=stack2.pop()
                            stack.append(temp2)
                            if(lastAction!="Redo"):
                                history.append(("Redo",temp))
                                lastAction="Redo"
                        for i in range(len(stack)):
                            if(stack[i][2]=="COLOR"):
                                paint_using_brush(stack[i][0],stack[i][1],stack[i][4],stack[i][3])
                            elif(stack[i][2]=="FILL"):
                                fill_bucket(stack[i][0], stack[i][1], stack[i][3])
                        break
                    if button.name == "history":
                        WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH+330, HEIGHT))
                        break
                    if button.name == "Close":
                        WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
                        break

                    if button.name == "Animate":
                        history.append(("Animate"))
                        lastAction="Animate"
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        draw(WIN, grid, buttons,history)
                        for i in range(len(stack)):
                            time.sleep(0.25)
                            if(stack[i][2]=="COLOR"):
                                paint_using_brush(stack[i][0],stack[i][1],stack[i][4],stack[i][3])
                                draw(WIN, grid, buttons,history)
                            elif(stack[i][2]=="FILL"):
                                fill_bucket(stack[i][0], stack[i][1], stack[i][3])
                                draw(WIN, grid, buttons,history)
                        break

                    if button.name == "FillBucket":
                        STATE = "FILL"
                        history.append(("Bucket Selected",drawing_color))
                        lastAction="FillBucket"
                        break

                    if button.name == "Change":
                        Change = not Change
                        for i in range(10):
                            if i == 0:
                                buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,name="Change"))
                            else:
                                if Change == False:
                                    buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,"B"+str(i-1), BLACK))
                                if Change == True:
                                   buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,"C"+str(i-1), BLACK))
                        break

                    if button.name == "Brush":
                        STATE = "COLOR"
                        history.append(("Brush Selected",drawing_color,BRUSH_SIZE))
                        lastAction="Brush"
                        break

                    drawing_color = button.color
                    draw_button.color = drawing_color
                    if(drawing_color==(255,255,255)):
                        history.append(("Erase"))
                        lastAction="Erase"
                    else:
                        history.append(("Color Change",drawing_color))
                        lastAction="Color Change"
                    break

                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    #set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                        history.append(("Brush Size Change",BRUSH_SIZE))
                        lastAction="Brush Size Change"
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                        history.append(("Brush Size Change",BRUSH_SIZE))
                        lastAction="Brush Size Change"
                    elif button.width == size_large:
                        BRUSH_SIZE = 3
                        history.append(("Brush Size Change",BRUSH_SIZE))
                        lastAction="Brush Size Change"

                    STATE = "COLOR"

    draw(WIN, grid, buttons,history)

pygame.quit()
