
from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
victory = mixer.Sound("money.ogg")
losing = mixer.Sound("kick.ogg")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (45, 45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x >= 630:
            self.direction = "left"
        if self.rect.x <= 470:
            self.direction = "right"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 

class wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hero = Player("hero.png", 5, 430, 5)
enemy = Enemy("cyborg.png", 630, 300, 3)
goal = GameSprite("treasure.png", 580, 430, 0)
w1 = wall(154, 205, 50, 100, 20, 450, 10)
w2 = wall(154, 205, 50, 100, 480, 350, 10)
w3 = wall(154, 205, 50, 100, 20, 10, 380)
w4 = wall(154, 205, 50, 200, 130, 10, 350)
w5 = wall(154, 205, 50, 450, 130, 10, 360)
w6 = wall(154, 205, 50, 300, 20, 10, 350)
w7 = wall(154, 205, 50, 390, 120, 130, 10)

clock = time.Clock()
fps = 60
game = True
finish = False

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN", True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        hero.update()
        enemy.update()
        hero.reset()
        enemy.reset()
        goal.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(hero, goal):
            finish = True
            window.blit(win, (200, 200))
            victory.play()

        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7):
            finish = True
            window.blit(lose, (200, 200))
            losing.play()

    display.update()
    clock.tick(fps)