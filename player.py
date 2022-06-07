
import pygame
import data as D


class Player():
    
    def __init__(self):
        self.player_image = pygame.image.load("images/player.png")
        self.player_image = pygame.transform.scale(self.player_image, (75, 75))
        self.rect = self.player_image.get_rect()
        self.rect.x = 300
        self.rect.y = 320
        self.player_image_running = pygame.image.load("images/player_running.png")
        self.player_image_running = pygame.transform.scale(self.player_image_running, (75,75))
        self.player_image_fliped = self.player_image
        self.flag_swip =False
        self.vel = 5
        self.score = 0