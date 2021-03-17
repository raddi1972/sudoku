import find_empty
import solver
import creator
import pygame


def begin():
    pygame.font.init()

    screen = pygame.display.set_mode((600, 700))            # Screen Display

    pygame.display.set_caption("GRID")          # Setting caption
    #img = pygame.image.load('icon.png')
    # pygame.display.set_icon(img)

    x = 0
    y = 0
    len = 600 / 9       # Length and width of each cell
    value_entered = 0

    font1 = pygame.font.SysFont("Bahnschrift", 40)
    screen.fill((0, 0, 255))
    text1 = font1.render("LOADING.....", 1, (0, 0, 0))
    screen.blit(text1, (100, 250))
    pygame.display.flip()

    # Default Sudoku Board.
    grd_obj = creator.Sudoku()                 # Rudransh code
    grid = grd_obj.grid

    def get_cord(pos):          # Gets mouse position
        global x
        x = pos[0] // len
        global y
        y = pos[1] // len

    # Highlight the cell selected (Red lines)

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * len - 3,
                                                   (y + i) * len), (x * len + len + 3, (y + i) * len), 7)
            pygame.draw.line(screen, (255, 0, 0), ((x + i) * len,
                                                   y * len), ((x + i) * len, y * len + len), 7)

    # Function to draw required lines for making Sudoku grid

    def draw():
        # Draw the lines
        for i in range(9):
            for j in range(9):
                if j % 3 == 0 and j != 0:  # vertical lines
                    pygame.draw.line(screen, (0, 0, 0),
                                     (j * len, 0), (j * len, 600), 6)

                if i % 3 == 0 and i != 0:             # horizontal lines
                    pygame.draw.line(screen, (0, 0, 0),
                                     (0, i * len), (600, i * len), 6)

                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                    i * len, j * len, len, len), 2)

                if grid[i][j] != 0:
                    # Fill gird with default numbers specified
                    value_text = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                    screen.blit(value_text, (i * len + 17, j * len))

        # Fill value entered in cell

    def put_num(val):
        value_text = font1.render(str(val), 1, (0, 0, 0))
        screen.blit(value_text, (x * len + 17, y * len))

    def valid(G, pos, num):
        draw_box()
        for i in range(9):  # row wise
            # it isn't the same number we're checking for by comparing coords
            if G[i][pos[1]] == num and (i, pos[1]) != pos:
                return False

        for j in range(9):  # column wise
            # Same row but not same number
            if G[pos[0]][j] == num and (pos[0], j) != pos:
                return False

        return True

    def result():
        text1 = font1.render("FINISHED PRESS R or D", True, (0, 0, 0))
        screen.blit(text1, (20, 570))

    running = True
    t1 = 0
    t2 = 0
    rs = 0
    error = 0
    # The loop thats keep the window running
    while running:

        # White color background
        screen.fill((255, 255, 255))
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                running = False
                # Get the mouse postion to insert number
            if event.type == pygame.MOUSEBUTTONDOWN:
                t1 = 1
                pos = pygame.mouse.get_pos()
                get_cord(pos)
                # Get the number to be inserted if key pressed
            if event.type == pygame.KEYDOWN:
                draw_box()
                if event.key == pygame.K_LEFT:
                    x -= 1
                    t1 = 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                    t1 = 1
                if event.key == pygame.K_UP:
                    y -= 1
                    t1 = 1
                if event.key == pygame.K_DOWN:
                    y += 1
                    t1 = 1
                if event.key == pygame.K_1:
                    value_entered = 1
                if event.key == pygame.K_2:
                    value_entered = 2
                if event.key == pygame.K_3:
                    value_entered = 3
                if event.key == pygame.K_4:
                    value_entered = 4
                if event.key == pygame.K_5:
                    value_entered = 5
                if event.key == pygame.K_6:
                    value_entered = 6
                if event.key == pygame.K_7:
                    value_entered = 7
                if event.key == pygame.K_8:
                    value_entered = 8
                if event.key == pygame.K_9:
                    value_entered = 9
                if event.key == pygame.K_s:
                    t2 = 1

        if type(find_empty.find_empty(grid)) != tuple and t2 == 0:
            lst1 = [0]
            solver.solve_sudoku(grid, lst1, 2)

            if(grid == lst1[1]):
                text1 = font1.render("Successfull", 1, (0, 0, 0))
                screen.blit(text1, (20, 600))

            else:
                text1 = font1.render("Incorrect", 1, (0, 0, 0))
                screen.blit(text1, (20, 600))

        elif type(find_empty.find_empty(grid)) == tuple and t2 == 0:
            text1 = font1.render("Best of Luck", 1, (0, 0, 0))
            screen.blit(text1, (20, 600))

        if t2 == 1:
            grid = grd_obj.solution
            draw()
            draw_box()

            text1 = font1.render("FINISHED SUCCESSFULLY", True, (0, 0, 0))
            screen.blit(text1, (20, 600))

        if value_entered != 0:

            if valid(grid, (int(x), int(y)), value_entered) == True:
                put_num(value_entered)
                draw_box()
                grid[int(x)][int(y)] = value_entered
                t1 = 0
            else:
                grid[int(x)][int(y)] = 0

            value_entered = 0

        draw()
        if t1 == 1:
            draw_box()

        # Update window
        pygame.display.update()
