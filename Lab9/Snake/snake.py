from os import scandir
from select import select
import pygame, random, time

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
FPS = 5

BLOCK_SIZE = 20
MAX_LEVEL = 2

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        self.list = []

        f = open("Lab9\Snake\levels\level{}.txt".format(level), "r")
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))
                    self.list.append([x, y])

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.list = [[10, 11]]
        self.dx = 0
        self.dy = 0
        self.level = 0
        self.last_x = 10
        self.last_y = 11

    def move(self):
        self.last_x = self.body[-1].x
        self.last_y = self.body[-1].y
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.list[i][0] = self.list[i-1][0]
            self.list[i][1] = self.list[i-1][1]

        self.body[0].x += self.dx 
        self.body[0].y += self.dy
        self.list[0][0] += self.dx 
        self.list[0][1] += self.dy

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        global wall, snake, score
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                if food.value[0] == 1:
                    score += 1
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                elif food.value[0] == 2:
                    score += 2
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                food.relocate(wall, self)

snake = Snake()
wall = Wall(snake.level)

def check_per():
    global wall, snake
    f = True
    while f:
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        if [x, y] not in wall.list and [x, y] not in snake.list:
            return Point(x, y)
class Food:
    def __init__(self):
        self.location = check_per()
        self.value = random.choices([1, 2], weights=[80, 20], k = 1)
        if self.value[0] == 1:
            self.R = 0
            self.G = 255
            self.B = 0
        elif self.value[0] == 2:
            self.R = 255
            self.G = 215
            self.B = 0

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        if self.value[0] == 1:
            pygame.draw.rect(SCREEN, (self.R, self.G, self.B), rect)
        else:
            pygame.draw.rect(SCREEN, (self.R, self.G, self.B), rect)
    def update_color(self):
        if self.R > 0:
            self.R -= 3
            if self.R < 0:
                self.R = 0
        if self.G > 0:
            self.G -= 3
            if self.G < 0:
                self.G = 0
        if self.B > 0:
            self.B -= 3
            if self.B < 0:
                self.B = 0

    def relocate(self, wall, snake):
        f = True
        while f:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            if [x, y] not in wall.list and [x, y] not in snake.list:
                self.location = Point(x, y)
                f = False
                self.value = random.choices([1, 2], weights=[80, 20], k = 1)
                if self.value[0] == 1:
                    self.R = 0
                    self.G = 255
                    self.B = 0
                elif self.value[0] == 2:
                    self.R = 255
                    self.G = 215
                    self.B = 0


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

#Quit game if snake hits wall or borders or itself
def game_over(wall, snake):
    for i in range(len(wall.body)):
        if snake.body[0].x == wall.body[i].x and snake.body[0].y == wall.body[i].y:
            return False
    if snake.body[0].x < 0 or snake.body[0].x > 19 or snake.body[0].y < 0 or snake.body[0].y > 19:
        return False
    for i in range(1, len(snake.body)):
        if snake.body[0].x == snake.body[i].x and snake.body[0].y == snake.body[i].y:
            return False
    return True


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

food = Food()

level = 1
score = 0
font = pygame.font.SysFont("Verdana", 200)
font_small = pygame.font.SysFont("Verdana", 60)
font_smaller = pygame.font.SysFont("Verdana", 30)
gameover = font_small.render("Game over!", True, "Black")
gameover_rect = gameover.get_rect().center

FOODROT = pygame.USEREVENT + 1
pygame.time.set_timer(FOODROT, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
        if event.type == FOODROT:
            food.update_color()
            pygame.display.update()
            if food.R == 0 and food.G == 0 and food.B == 0:
                food.relocate(wall, snake)
    
    snake.move()

    #If game ends
    f = game_over(wall, snake)
    if not f:
        SCREEN.fill((0, 150, 255))
        SCREEN.blit(gameover, (200-gameover_rect[0], 180-gameover_rect[1]))
        scr = font_smaller.render(f"Your score is {score}", True, "Black")
        scr_rect = scr.get_rect().center
        SCREEN.blit(scr, (200-scr_rect[0], 220-scr_rect[1]))
        pygame.display.update()
        time.sleep(2)
        running = False
        pygame.quit()

    #Grow snake when it collects food
    snake.check_collision(food)

    #Level progression
    if len(snake.body) > 6:
        newLevel = (snake.level + 1) % MAX_LEVEL
        snake = Snake()
        snake.level = newLevel
        wall = Wall(snake.level)
        food.location = Point(3, 10)
        level += 1
        FPS += 1   
    #Show current level
    SCREEN.fill(BLACK)
    level_txt = font.render(f"{level}", True, (255, 255, 255))
    level_rect = level_txt.get_rect().center
    SCREEN.blit(level_txt, (200-level_rect[0], 200-level_rect[1]))
    
    snake.draw()
    food.draw()
    wall.draw()
    
    drawGrid()
    
    pygame.display.update()
    CLOCK.tick(FPS)

pygame.quit()
quit()