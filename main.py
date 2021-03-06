'''
you will need to install:
pygame
math
random
'''

import pygame
from pygame.locals import *
import random
from character_class_v2 import Character
from Enemy import enemy
from Button import button

# Intialize pygame
pygame.init()

font = pygame.font.SysFont("font/Pixeltype.ttf",75)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((800, 600))

########################################################################################
# Players data
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0



# Enemies data
Enemy_list = []

num_of_enemies = 6
mx, my = pygame.mouse.get_pos()

# Player object
character = Character(playerX,playerY,playerX_change,playerY_change,mx,my)



# Entity groups
#print(zombie)
# for i in range (num_of_enemies):
#     Enemy_list.append(enemy(rect_lst))


# zombie_group = pygame.sprite.Group()#

for i in range(num_of_enemies):
    EnemyX = random.randint(0, 725)
    EnemyY = random.randint(0, 600)
    # if EnemyX == character.X and EnemyY == character.Y:
    zombie = enemy(EnemyX, EnemyY)
    Enemy_list.append(zombie)


def main_menu():
    while True:
        screen.fill(BLACK)

        Play_Button = button(400,275,WHITE,font,'PLAY')
        Exit_Button = button(400, 325, WHITE, font, 'EXIT')
        Play_Button.display_content(screen)
        Exit_Button.display_content(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Play_Button.press(mx,my):
                        game()
                    else:
                        if Exit_Button.press(mx,my):
                            pygame.quit()
                            exit()

        pygame.display.update()










# -------- Main Program Loop -----------
def game():
    running = True

    while running:

        # Background colour
        screen.fill(WHITE)

        # Adding the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            # Fire button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                   character.fire()





        for e in Enemy_list:
            if character.has_collided(e.rect) == True:
                running = False
                e.destroy(Enemy_list)
                EnemyX = random.randint(0, 725)
                EnemyY = random.randint(0, 600)
                zombie = enemy(EnemyX, EnemyY)
                Enemy_list.append(zombie)

            # Bullet list
        for bullet in character.bullets:
            bullet.move()
            bullet.draw(screen)
            for e in Enemy_list:
               if bullet.has_collided(e.rect) == True:
                   e.destroy(Enemy_list)
                   bullet.destroy(character.bullets)
                   EnemyX = random.randint(0, 725)
                   EnemyY = random.randint(0, 600)
                   zombie = enemy(EnemyX, EnemyY)
                   Enemy_list.append(zombie)

        enemy.updateAllZombies(Enemy_list,character.X,character.Y)
        first_run = False
        # character.has_collided(zombie.rect)
        character.update()
        pygame.display.update()



# Calling main program
main_menu()
