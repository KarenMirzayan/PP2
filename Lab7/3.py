import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True
x = 320
y = 240
screen.fill((255, 255, 255))
pygame.display.update()
clock = pygame.time.Clock()
pygame.display.set_caption("Ball game")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    if x - 25 < 0:
        x = 25
    if x + 25 > 640:
        x = 615
    if y - 25 < 0:
        y = 25
    if y + 25 > 480:
        y = 455

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    clock.tick(60)        
pygame.quit()