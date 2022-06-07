import pygame
import data as D

class GameOver:
    image = pygame.image.load("images/gameover.jpg")
    image = pygame.transform.scale(image, (600,600))

    def G_O(self):
        D.screen.blit(self.image, (-15, -60))

    def Quit(self):
        pygame.quit()

    def loop(self):
        while True:
            self.G_O()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            pygame.display.update()
