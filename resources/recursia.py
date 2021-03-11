"""Game, project for learning"""
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def recursive_rectangle(x, y, w, h):
    pygame.draw.rect(screen, WHITE, [x, y, w, h], 1)
    if w > 14:
        x += w * .1
        y += h * .1
        w *= .8
        h *= .8
        recursive_rectangle(x, y, w, h)


def recursive_draw(x, y, width, height, count):
    pygame.draw.line(screen, BLUE, [x + width * .25, height // 2 + y], [x + width * .75, height // 2 + y], 3)
    pygame.draw.line(screen, BLUE, [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25, (height * 1.5) // 2 + y], 3)
    pygame.draw.line(screen, BLUE, [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y], 3)

    if count > 0:
        count -= 1
        # Верхний левый
        recursive_draw(x, y, width // 2, height // 2, count)
        # Верхний правый
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        # Нижний левый
        recursive_draw(x, y + width // 2, width // 2, height // 2, count)
        # Нижний правый
        recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)


pygame.init()
size = [700, 700]

WIDTH, HEIGHT, MARGIN = 20, 20, 5
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
color = WHITE
DONE = False
# recursive rectangle data
x_pos = 10
y_pos = 10
width = 20
height = 20

while not DONE:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are done so we exit this loop

    screen_width = pygame.display.get_surface().get_width()
    screen_height = pygame.display.get_surface().get_height()

    """fill the screen with white"""
    screen.fill(BLACK)
    """flip display"""
    recursive_rectangle(10, 10, 680, 680)
    fractal_level = 2
    recursive_draw(0, 0, 700, 700, fractal_level)
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(100)
pygame.quit()
