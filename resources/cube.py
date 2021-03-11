"""Game, project for learning"""
import pygame

out_left_x = 200
out_left_y = 200


def draw_cube(screen_, x, y):

    p1 = [(200 - x, 200 - y), (500 - x, 200 - y), (500 - x, 500 - y), (200 - x, 500 - y)]
    p2 = [(250 + x, 250 + y), (450 + x, 250 + y), (450 + x, 450 + y), (250 + x, 450 + y)]
    p3 = [(200 - x, 200 - y), (500 - x, 200 - y), (450 + x, 250 + y), (250 + x, 250 + y)]
    p4 = [(250 + x, 450 + y), (450 + x, 450 + y), (500 - x, 500 - y), (200 - x, 500 - y)]
    if (p1[0][0]>170) and (p1[0][0]<530):
        p1 = [(200 - x, 200 - y), (500 - x, 200 - y), (500 - x, 500 - y), (200 - x, 500 - y)]
        p3 = [(200 - x, 200 - y), (500 - x, 200 - y), (450 + x, 250 + y), (250 + x, 250 + y)]
        p4 = [(250 + x, 450 + y), (450 + x, 450 + y), (500 - x, 500 - y), (200 - x, 500 - y)]
        print(p1[0][0])
    else:
        p1 = [(140 + x, 200 - y), (500 - x, 200 - y), (500 - x, 500 - y), (140 + x, 500 - y)]
        p3 = [(140 + x, 200 - y), (500 - x, 200 - y), (450 + x, 250 + y), (250 + x, 250 + y)]
        p4 = [(250 + x, 450 + y), (450 + x, 450 + y), (500 - x, 500 - y), (140 + x, 500 - y)]
        print(p1[0][0])
    pygame.draw.polygon(screen, WHITE, p1, 1)
    pygame.draw.polygon(screen, WHITE, p2, 1)
    pygame.draw.polygon(screen, WHITE, p3, 1)
    pygame.draw.polygon(screen, WHITE, p4, 1)


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
size = [1000, 1000]

WIDTH, HEIGHT, MARGIN = 20, 20, 5
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
color = WHITE
DONE = False
# recursive rectangle data
# Скорость, пикселей за кадр
x_speed = 0
y_speed = 0

# Текущая позиция
x_coord = 10
y_coord = 10

while not DONE:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are done so we exit this loop
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -1
        if event.key == pygame.K_RIGHT:
            x_speed = 1
        if event.key == pygame.K_UP:
            y_speed = -1
        if event.key == pygame.K_DOWN:
            y_speed = 1
    if event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_LEFT:
            x_speed = 0
        if event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0

    """fill the screen with white"""
    screen.fill(BLACK)
    
    """flip display"""
    draw_cube(screen, x_coord, y_coord)
    pygame.display.flip()
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    # --- Limit to 60 frames per second
    clock.tick(100)
pygame.quit()
