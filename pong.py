
from ast import Break
from turtle import screensize
import pygame
import sys
from random import randint
pygame.init()
clock = pygame.time.Clock()
width=1280
height=960
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
playerw=10
playerh=140
botw=10
both=140
pygame.display.set_caption("Pong")
font = pygame.font.Font('freesansbold.ttf', 32)
ball = pygame.Rect(width/2-15, height/2 -15,30, 30)
player = pygame.Rect(width-20, height/2-70, playerw, playerh)
opponent =pygame.Rect(10, height/2-70, botw, both)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

bspeedx = 7
bspeedy = 7

global botspeed
botspeed=0


def start():
    ball.x=width/2-15
    ball.y=width/2-15
def bot():
    if opponent.top < ball.y:
        opponent.y += randint(1, 9)
    if opponent.top > ball.y:
            opponent.y -= randint(1, 9)

    

def controller():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and player.top > 20:
            player.y-=10
        if event.key == pygame.K_DOWN and player.bottom < height-20:
            player.y+=10

bcolor=white
pcolor=white

score_bot=0
bottext = font.render(str(score_bot), True, bcolor)
bottextRect = bottext.get_rect()         
bottextRect.center = (width/2 -30, height/2)  


score_player = 0
playertext = font.render(str(score_player), True, pcolor)
playertextRect = playertext.get_rect()         
playertextRect.center = (width/2 +30, height/2)  



while True:
    
    if int(score_bot)%10 == 0:
        pass
    if score_bot > score_player:
        bcolor="green"
        pcolor="red"
    elif score_bot < score_player:
        bcolor="red"
        pcolor="green"
    elif score_bot == score_player:
        bcolor="white"
        pcolor="white"
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    bot()
    controller()
    ball.x +=bspeedx
    ball.y +=bspeedy

    if ball.top <= 0 or ball.bottom >= height:
        bspeedy*=-1
    if ball.right > width or ball.left < 0:
        if ball.left < 0:
            score_player+=1
        elif ball.right > width:
            score_bot+=1
        bspeedy=7
        bspeedx=7
        start()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        bspeedx*=-1

    bspeedx+=0.001
    bspeedy+=0.001
    bottext = font.render(str(score_bot), True, bcolor)
    playertext = font.render(str(score_player), True, pcolor)
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2,0), (width/2, height))
    screen.blit(bottext, bottextRect)
    screen.blit(playertext, playertextRect)
    pygame.display.flip()
    clock.tick(60)

