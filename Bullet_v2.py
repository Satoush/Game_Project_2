import pygame
import math

screen = pygame.display.set_mode((800, 600))


class bullet():
    def __init__(self,Image_path,colour ,pos_X, pos_Y,velocity,player_angle,mx,my):
        self.Image_path = Image_path
        self.image = pygame.image.load(Image_path)
        self.rect = self.image.get_rect(center=(400, 300))
        self.colour = colour
        self.posX = pos_X
        self.posY = pos_Y
        self.velocity = velocity
        self.player_angle = player_angle
        ##################################################
        angle = math.atan2(my - pos_Y, mx - pos_X)
        self.dx = math.cos(angle) * velocity
        self.dy = math.sin(angle) * velocity
       # players x and z`


    def move(self):
        self.posX += self.dx
        self.posY += self.dy
        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)


    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        rotated_image = pygame.transform.rotate(self.image, self.player_angle)  # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.posX, self.posY))

    def destroy(self,bullet_array):
        bullet_array.remove(self)
        del self

    def has_collided(self, Enemy):
        if self.rect.colliderect(Enemy):
            print('hit')
            return True


    def update(self):
        #self.move()
        self.destroy()














