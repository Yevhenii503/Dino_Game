import pygame

width = 900
height = 550
fps = 30
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
purple = (128, 0, 128)
x1 = 130
y1 = 230
x2 = 900
y2 = 230
x3 = 900
y3 = 300
x4 = 900
speed = 15
jump = False
jump_count = 10


class Dino(pygame.sprite.Sprite):
    def __init__(self, screen_1):
        self.screen = screen_1
        self.image = pygame.image.load('img/dino_icon.png')
        self.rect = self.image.get_rect(x=x1, y=y1)
        self.screen_rect = screen_1.get_rect()


def jumping():
    global jump
    global jump_count
    keys = pygame.key.get_pressed()
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True

    else:
        if jump_count >= -10:
            if jump_count < 0:
                dino.rect.y += (jump_count ** 2) / 1.5
            else:
                dino.rect.y -= (jump_count ** 2) / 2
            jump_count -= 1.2
        else:
            jump_count = 10
            jump = False


class Cactus(pygame.sprite.Sprite):
    def __init__(self, screen_1):
        self.screen = screen_1
        self.image = pygame.image.load('img/Cactus.png')
        self.rect = self.image.get_rect(x=x2, y=y2)

    def update(self):
        self.rect.x -= speed
        if self.rect.right <= 0:
            self.rect.x = x2


class Road1(pygame.sprite.Sprite):
    def __init__(self, screen_1):
        self.screen = screen_1
        self.image = pygame.image.load('img/road.png')
        self.rect = self.image.get_rect(x=0, y=y3)

    def update(self):
        self.rect.x -= speed
        if road2.rect.right == 900:
            self.rect.x = 900


class Road2(pygame.sprite.Sprite):
    def __init__(self, screen_1):
        self.screen = screen_1
        self.image = pygame.image.load('img/road2.png')
        self.rect = self.image.get_rect(x=x4, y=y3)

    def update(self):
        self.rect.x -= speed
        if road1.rect.right == 900:
            self.rect.x = 900


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dino')
clock = pygame.time.Clock()


def message(msg, color, x, y, size):
    font_style = pygame.font.SysFont("bahnschrift", size)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (x, y))


dino = Dino(screen)
cactus = Cactus(screen)
dino_rect = dino.rect
cactus_rect = cactus.rect
road1 = Road1(screen)
road1_rect = road1.rect
road2 = Road2(screen)
score = 0


def game_loop():
    running = False
    run = True
    while run:
        screen.fill(gray)
        clock.tick(fps)
        message('Dino Game', purple, 220, 40, 90)
        message('For Start game press Space', black, 200, 170, 40)
        pygame.display.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    running = True
    game_over = False
    global jump
    global jump_count
    while running:
        global score, speed
        while game_over:
            screen.fill(gray)
            message('Game Over', red, 200, 40, 100)
            message('R = play again', black, 300, 170, 50)
            message('Q = Exit', black, 300, 240, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    if event.key == pygame.K_r:
                        score = 0
                        cactus_rect.x = x2
                        game_loop()

        screen.fill(white)

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True

        keys = pygame.key.get_pressed()
        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            jumping()

        if dino_rect.colliderect(cactus_rect):
            game_over = True

        score += 1

        message(f"Score {score}", black, 700, 60, 35)
        screen.blit(road1.image, road1.rect)
        screen.blit(road2.image, road2.rect)
        road1.update()
        road2.update()

        screen.blit(dino.image, dino.rect)
        screen.blit(cactus.image, cactus.rect)
        cactus.update()

        pygame.display.update()

        pygame.display.flip()
    pygame.quit()
    quit()


game_loop()
