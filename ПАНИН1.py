from pygame import *


window = display.set_mode((1000,700))
display.set_caption("Теннис")
fon = transform.scale(image.load('араер.jpg'),(1000,700))

font.init()
font = font.SysFont('Arial',35)

class Game_Sprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Game_Sprite):
    def control(self):
        buttons = key.get_pressed()
        if buttons[K_w] and self.rect.y>5:
            self.rect.y-= self.speed
        if buttons[K_s] and self.rect.y<600:
            self.rect.y+= self.speed
    def control1(self):
        buttons = key.get_pressed()
        if buttons[K_i] and self.rect.y>5:
            self.rect.y-= self.speed
        if buttons[K_k] and self.rect.y<600:
            self.rect.y+= self.speed

game = True
finish = False
clock = time.Clock()
pl1 = Player('рфр.jpg',20,300,100,100,15)
pl2 = Player('рфр.jpg',900,300,100,100,15)
ball = Player('h.jpg',500,300,120,50,0)
lose_1 = font.render('Емае первый',True,(255,255,255))
lose_2 = font.render('Емае второй',True,(255,255,255))
ball_speed_x =6
ball_speed_y =6
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(fon,(0,0))
        pl1.reset()
        pl1.control()
        
        pl2.reset()
        pl2.control1()
        ball.reset()
        ball.rect.x +=ball_speed_x
        ball.rect.y +=ball_speed_y
        if ball.rect.y < 0 or ball.rect.y > 650:
            ball_speed_y *= -1
        if ball.rect.x <0:
            finish = True
            window.blit(lose_1,(400,300))
        if ball.rect.x >1000:
            finish = True
            window.blit(lose_2,(400,300))
        if sprite.collide_rect(pl1,ball) or sprite.collide_rect(pl2,ball):
            ball_speed_y *=1
            ball_speed_x *=-1
            
            
        display.update()
        
        
        
    clock.tick(60)
