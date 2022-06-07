import pygame
import random
import data as D
from player import Player

player = Player()
class Rock(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.Rock_image = pygame.image.load("images/rock.png")
        self.Rock_image = pygame.transform.scale(self.Rock_image, (100, 100))
        self.rect = self.Rock_image.get_rect()
        self.rect.x = random.randint(0, (D.Game_width-D.pixel))
        self.rect.y = 0
        self.rect_y_change = 6
    
    def positionate_rock(self):
        D.screen.blit(self.Rock_image, (self.rect))

    def Fall_rock(self):
        self.rect.y += self.rect_y_change
    
    def Update_rock_position(self):
        if self.rect.y >= D.Game_height and self.rect.y <= (D.Game_height+200):
            self.rect.y = (0-D.pixel)
            self.rect.x = random.randint(0, (D.Game_width-100))
            D.screen.blit(self.Rock_image, (self.rect)) 
        
    
            
