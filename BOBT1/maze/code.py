import pygame
from pygame import *
class Game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s, p_height, p_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(p_height,p_width))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Hruk(Game):
    d = "left"
    def ruh (self):
        if self.rect.x <=470:
            self.d = "right"
        if self.rect.x >=620:
            self.d = "left"

        if self.d == "left":
            self.rect.x -= self.speed 
        else:
            self.rect.x += self.speed 
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hihi = 0
max = 0


class Move(Game):
    def move(self):
        global hihi
        global max
        keys = key.get_pressed()
        if hihi == 0:
            if keys[K_LEFT] and self.rect.x>5:
                self.rect.x -=  self.speed
            if keys[K_RIGHT] and self.rect.x<620:
                self.rect.x +=  self.speed
            if keys[K_UP] and self.rect.y>5:
                self.rect.y -=  self.speed
            if keys[K_DOWN] and self.rect.y<420:
                self.rect.y +=  self.speed
        else:
            if keys[K_LEFT]:
                self.rect.x -=  self.speed
            if keys[K_RIGHT]:
                self.rect.x +=  self.speed
            if keys[K_UP]:
                self.rect.y -=  self.speed
            if keys[K_DOWN]:
                self.rect.y +=  self.speed
        if keys[K_p] and keys[K_z]:
            hihi = 1
        if keys[K_m] and keys[K_x]:
            hihi = 1
            max = 1
            mixer.music.load("max.mp3")
            mixer.music.play()
class You_Win():
    def __init__(self):  
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
window = display.set_mode((700,600))
display.set_caption("Maze v0.1")

olimpia = transform.scale(image.load("болото_хіхі.jpg"),(700,600))
AAAAA = Move ("маленький_хрюк.jpg",5,400,4, 90,90)
Hruku = Hruk("мініхрюк.jpg",550,280,2, 90,90)
Puk = Game ("сало.webp",530,440,0,90,90)
Puk_Puk = Game("you_win.jpg", 0,0, 0,700,600)
w1 = Wall(154,205,50,100,20,370,10)
w2 = Wall(154,205,50,100,20,10,300)
w4 = Wall(154,205,50,470,130,10,300)
w5 = Wall(154,205,50,100,430,380,10)
w6 = Wall(154,205,50,240,150,10,290)
w7 = Wall(154,205,50,50,20,380,10)
w8 = Wall(154,205,50,350,20,10,290)
clock = time.Clock()
FPS = 60


game = True
mixer.init()
mixer.music.load("природа.mp3")
mixer.music.play()

muhahaha = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if max == 1:
        x = AAAAA.rect.x
        y = AAAAA.rect.y
        AAAAA = Move ("max.png",x,y,20, 130,130)
        olimpia = transform.scale(image.load("monza.png"),(700,600))
        Puk = Game ("max_podium.png",530,440,0,150,150)
        Hruku = Hruk("checo.png",550,280,2, 150,150)
        Puk_Puk = Game("you_won.png", 0,0, 0,700,600)
        max = 0
    window.blit(olimpia, (0, 0))
    AAAAA.move()
    Hruku.ruh()
    AAAAA.reset()
    Hruku.reset()
    Puk.reset()
    w1.draw_wall()
    w2.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    w8.draw_wall()
    if muhahaha == 1:
        Puk_Puk.reset()
        pygame.time.delay(4000)
        game = False

    Hruk_rect = AAAAA.rect
    Puk_rect = Puk.rect

    if Hruk_rect.colliderect(Puk_rect):
        Puk_Puk.reset()
        muhahaha = 1
    if hihi == 0:
        if Hruk_rect.colliderect(w1) or Hruk_rect.colliderect(w2):
            game = False
        if Hruk_rect.colliderect(w4) or Hruk_rect.colliderect(w5):
            game = False
        if Hruk_rect.colliderect(w6) or Hruk_rect.colliderect(w7) or Hruk_rect.colliderect(w8):
            game = False
        if Hruk_rect.colliderect(Hruku):
            game = False
    display.update()
    clock.tick(FPS)
