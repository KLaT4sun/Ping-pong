from pygame import *

window = display.set_mode((500,300))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('stol.jpg'), (500,300))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)

        

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font2 = font.SysFont('Arial',40)
font1 = font.SysFont('Arial',70)
win = font1.render('You win!',True,(0,215,0))
lose = font1.render('You lose!',True,(215,0,0))
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
    clock.tick(FPS)
    display.update()