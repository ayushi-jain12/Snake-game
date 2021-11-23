#Snake game using pygame

#importing required libraries
import pygame
import sys
import time 
import random

#checking for errors during initialisation
errors=pygame.init()
if errors[1]>0:
    print(f'{errors[1]} errors while initialising, Exiting game..')
    sys.exit(-1)
else:
    print('Game initialised successfully')


#initialising game window
fx=800  #frame sizes
fy=600
pygame.display.set_caption('Snake Game')
window=pygame.display.set_mode((fx,fy))


#frames per second controller
fps=pygame.time.Clock()
speed=10


#defining colors
#rgb
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
#other colors
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
yellow=pygame.Color(255,255,0)
cyan=pygame.Color(0,255,255)


#required variables
score=0
snake_pos=[50,50]
body=[[50,50],[40,50],[30,50]]
food_pos=[500,400]
change_pos=True
direction='RIGHT'
change_dir=direction


#function to display game over and score
def game_over():
    my_font=pygame.font.SysFont('luximono',90)
    game_over_surface = my_font.render('GAME OVER!!', True,red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (fx/2, fy/4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#function to show score when the game is over
def show_score(when):
    if when==0:
        score_font =pygame.font.SysFont('luximono',60)
        score_surface = score_font.render('Score : ' + str(score), True,cyan)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (fx/2, fy/1.5)
    else:
        score_font =pygame.font.SysFont('luximono',20)
        score_surface = score_font.render('Score : ' + str(score), True,white)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (fx/10, 15)

    window.blit(score_surface, score_rect)

#main game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_dir = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_dir = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_dir = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_dir  = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_dir == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_dir == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_dir == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_dir  == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        change_pos= False
    else:
        body.pop()

    # Spawning food on the screen
    if not change_pos:
        food_pos = [random.randrange(1, (fx//10)) * 10, random.randrange(1, (fy//10)) * 10]
    change_pos = True


    window.fill(black)
    for pos in body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window,yellow, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
        
    if snake_pos[0]<0 or snake_pos[0]>fx-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > fy-10:
        game_over()
        
    # Touching the snake body
    for block in body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
      
    show_score(1)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    speed=score/5+15
    fps.tick(speed)
 
