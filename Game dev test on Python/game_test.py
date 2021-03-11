import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
pi = 3.141592653


def draw_stick_figure(screen_, x, y):
    # Голова
    pygame.draw.ellipse(screen_, black, [1 + x, y, 10, 10], 0)

    # Ноги
    pygame.draw.line(screen_, black, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen_, black, [5 + x, 17 + y], [0 + x, 27 + y], 2)

    # Тело
    pygame.draw.line(screen_, red, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Руки
    pygame.draw.line(screen_, red, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen_, red, [5 + x, 7 + y], [1 + x, 17 + y], 2)


size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
# Оставаться в цикле, пока пользователь не нажмёт на кнопку закрытия окна
done = False

# Используется для контроля частоты обновления экрана
clock = pygame.time.Clock()
x_rect = 50
y_rect = 50
x_rect_change = 5
y_rect_change = 5
star_list = []
# Скорость, пикселей за кадр
x_speed = 0
y_speed = 0

# Текущая позиция
x_coord = 10
y_coord = 10
# Спрятать курсор мыши
pygame.mouse.set_visible(0)
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    star_list.append([x, y])
# -------- Основной цикл программы -----------
while not done:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # Пользоцатель нажимает на клавишу
    # noinspection PyUnboundLocalVariable
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -3
        if event.key == pygame.K_RIGHT:
            x_speed = 3
        if event.key == pygame.K_UP:
            y_speed = -3
        if event.key == pygame.K_DOWN:
            y_speed = 3

    # Пользователь отпускает клавишу
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

    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    # pos = pygame.mouse.get_pos()
    # xpos=pos[0]
    # ypos=pos[1]
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(grey)

    # --- Drawing code should go here

    # Обработать каждую звезду из списка
    for i in range(len(star_list)):
        # Draw the star
        pygame.draw.circle(screen, white, star_list[i], 2)
        star_list[i][1] += 1
        # Если снежинка упала за границу экрана
        if star_list[i][1] > 500:
            # Вернуть её наверх
            y = random.randrange(-50, -10)
            star_list[i][1] = y
            # Дать ей новую позицию x
            x = random.randrange(0, 500)
            star_list[i][0] = x

    draw_stick_figure(screen, x_coord, y_coord)
    # Воспроизвести текст. "True" значит,
    # что текст будет сглаженным (anti-aliased).
    # Чёрный - цвет. Переменную black мы задали ранее,
    # списком [0,0,0]
    # Заметьте: эта строка создаёт картинку с буквами,
    # но пока не выводит её на экран.
    # # font =pygame.font.Font(None,36)
    # # text = font.render("My text",True,black)
    #
    # # Вывести сделанную картинку на экран в точке (250, 250)
    # screen.blit(text, [250,250])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
