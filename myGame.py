import pygame
import os
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((900, 600))


# musics
#pygame.mixer.music.load(r'D:\My Github\Head_Ball_Game\background_music.mp3')
#pygame.mixer.music.play(-1)


# Title and Icon
pygame.display.set_caption(r"Head Ball 2")
icon = pygame.image.load(r"D:\My Github\Head_Ball_Game\header.png")
pygame.display.set_icon(icon)
field = pygame.image.load(r"D:\My Github\Head_Ball_Game\field.jpg")
PlayerImg1 = pygame.image.load(r"D:\My Github\Head_Ball_Game\PlayerImg1.png")
PlayerImg2 = pygame.image.load(r"D:\My Github\Head_Ball_Game\PlayerImg2.png")
ballImg = pygame.image.load(r"D:\My Github\Head_Ball_Game\ball.png")

Player1X = 50
Player1Y = 250
Player2X = 780
Player2Y = 250
ball_X = 450-32
ball_Y = random.randint(100,500)

Player1Y_change = 0
Player2Y_change = 0
ball_X_change = 4
ball_Y_change = 4

score_player1 = 0
score_player2 = 0

clock = pygame.time.Clock()

field_top = screen.get_height() - field.get_height()
field_left = screen.get_width()/2 - field.get_width()/2

def ball(x , y):
    screen.blit(ballImg, (x , y))

def player1(x , y):
    screen.blit(PlayerImg1, (x , y))

def player2(x , y):
    screen.blit(PlayerImg2, (x , y))

def distance(x1, y1, x2, y2):
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dis


clock = pygame.time.Clock()
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player1Y_change = -3
            if event.key == pygame.K_DOWN:
                Player1Y_change = 3
            if event.key == pygame.K_1:
                Player2Y_change = -3
            if event.key == pygame.K_2:
                Player2Y_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_1 or event.key == pygame.K_2:
                Player1Y_change = 0
                Player2Y_change = 0

    screen.blit(field, (field_left, field_top))
    pygame.draw.rect(screen , (87,6,3) , [0,150,33,300])
    pygame.draw.rect(screen , (87,6,3) , [864,150,39,300])


    if Player1Y < 10:
        Player1Y = 10
    elif Player1Y > 523:
        Player1Y = 523

    if Player2Y < 10:
        Player2Y = 10
    elif Player2Y > 523:
        Player2Y = 523


    if ball_X < 0:
        ball_X = 0
        ball_X_change = ball_X_change * -1

    elif ball_X >= 850:
        ball_X = 850
        ball_X_change = ball_X_change * -1

    if ball_Y <= 0:
        ball_Y = 0
        ball_Y_change = ball_Y_change * -1

    elif ball_Y > 536:
        ball_Y = 536
        ball_Y_change = ball_Y_change * -1

    if distance(ball_X + 32 , ball_Y + 32 , Player1X + 32 , Player1Y + 32) < 20:
        ball_X = 70
        ball_X_change = ball_X_change * -1



    elif distance(ball_X + 32 , ball_Y + 32 , Player2X + 32 , Player2Y + 32) < 20:
        ball_X = 750
        ball_X_change = ball_X_change * -1

    if ball_Y > 100 and ball_Y < 400 and ball_X == 0:
        goal_sound = mixer.Sound(r'D:\My Github\Head_Ball_Game\goal.mp3')
        goal_sound.play()
        score_player2 += 1

    if ball_Y > 100 and ball_Y < 400 and ball_X == 850:
        goal_sound = mixer.Sound(r'D:\My Github\Head_Ball_Game\goal.mp3')
        goal_sound.play()
        score_player1 += 1


    Player1Y += Player1Y_change
    Player2Y += Player2Y_change
    ball_X += ball_X_change
    ball_Y += ball_Y_change





    ball(ball_X , ball_Y)
    player1(Player1X , Player1Y)
    player2(Player2X , Player2Y)

    #print(ball_X, ", ", ball_Y)
    pygame.draw.rect(screen,(0, 0, 0),[0,550,450,50],5)
    pygame.draw.rect(screen,(0, 0, 0),[450,550,450,50],5)

    font= pygame.font.SysFont('impact', 30, False, False)

    text1 = font.render("SCORE  =  " + str(score_player1), True, (255, 0, 0))
    text2 = font.render("SCORE  =  " + str(score_player2), True, (255, 0, 0))
    screen.blit(text1,[150,550])
    screen.blit(text2,[550,550])


    #pygame.display.update()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

os._exit(0)
