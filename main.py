import pygame
from pygame import mixer
from paddle import Paddle
from ball import Ball
pygame.init()
screen = pygame.display.set_mode((700,500))
BLUE = (0,0,255)
LIME = 	(0,255,0)
#mixer.music.load("c:/Users/Aakanksha Chhavi/Desktop/Games/Pong/bounce.wav")
#mixer.music.play(-1)

pygame.display.set_caption("PONG")
icon = pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Games/Pong/pong_icon.png")
pygame.display.set_icon(icon)
    
Paddle_A = Paddle(LIME,10,100)
Paddle_A.rect.x = 20
Paddle_A.rect.y = 200

Paddle_B = Paddle(LIME,10,100)
Paddle_B.rect.x = 670
Paddle_B.rect.y = 200

Ball = Ball(LIME,10,10)
Ball.rect.x = 345
Ball.rect.y = 195

sprite_list = pygame.sprite.Group()
sprite_list.add(Paddle_A)
sprite_list.add(Paddle_B)  
sprite_list.add(Ball)
score_A = 0
score_B = 0
font = pygame.font.Font('freesansbold.ttf',30)

def show_score(x,y,score_val,p):
    if p == "A":
        score = font.render("Player A: "+str(score_val),True,(255,255,255))
        screen.blit(score,(x,y))
    else:
        score = font.render("Player B: "+str(score_val),True,(255,255,255))
        screen.blit(score,(x,y))



running = True
while running:
    screen.fill((0,0,128))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:     
        Paddle_B.move_up(5)
    elif keys[pygame.K_d]:
        Paddle_B.move_down(5)
    elif keys[pygame.K_w]:
        Paddle_A.move_up(5)
    elif keys[pygame.K_s]:
        Paddle_A.move_down(5)
        
    if Ball.rect.x > 790:
        score_A += 1
        Ball.velocity[0] = -Ball.velocity[0]
    elif Ball.rect.x < 0:
        score_B += 1
        Ball.velocity[0] = -Ball.velocity[0]
    elif Ball.rect.y > 490:
        Ball.velocity[1] = -Ball.velocity[1]
    elif Ball.rect.y < 0:
        Ball.velocity[1] = -Ball.velocity[1]
                
    pygame.draw.line(screen, LIME, [349, 0], [349, 500], 8)
    sprite_list.update()
    sprite_list.draw(screen)
    show_score(100,10,score_A,"A")
    show_score(420,10,score_B,"B")
    
    pygame.display.update()

        