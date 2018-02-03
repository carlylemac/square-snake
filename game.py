import pygame, random

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption(':(')
done = False
is_blue = True
colors = [(0, 128, 255),(255, 100, 0),(255,215,0),(255,0,255),(46,139,87),(220,20,60),(240,255,255)]
x = 30
y = 30
power = 0
big = 30
p = 0
cx = 300
cy = 200

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y = y - 4
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y = y + 4
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x = x - 4
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x = x + 4
    if pressed[pygame.K_q]:
        done = True
    if cx - 10 <= x <= cx + 10 and cy - 10 <= y <= cy + 10:
        if power == 1:
            power = 0
            p = 0
            big = big + 4
        elif power == 0:
            power = 1
            big = big + 4

    screen.fill(pygame.Color(60,60,60))
    number = random.randint(0,5)
    if power == 0:
        pygame.draw.circle(screen, (0,255,154), (cx,cy), 5)
    if power == 1:
        if p == 0:
            cy = random.randint(10, 490)
            cx = random.randint(10, 590)
            p = p + 1
        pygame.draw.circle(screen, (0,255,154), (cx,cy), 5)
    pygame.draw.rect(screen, colors[number], pygame.Rect(x,y,big,big))

    pygame.display.flip()
    clock.tick(80)
