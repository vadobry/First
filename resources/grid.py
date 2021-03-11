"""Game, project for learning"""
import pygame
pygame.init()
size = [255, 255]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT, MARGIN = 20, 20, 5
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
color = WHITE
DONE = False
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
grid[1][5] = 1
while not DONE:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
    """fill the screen with white"""
    screen.fill(BLACK)
    """flip display"""
    for column in range(10):
        for row in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(100)
pygame.quit()
