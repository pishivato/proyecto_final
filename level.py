from player import Player
from rock import Rock
from question import Pregunta
from gameover import GameOver
import data as D
import pygame
import random

pygame.init()

#instancias
player = Player()
rock = Rock()
Qtn = Pregunta()
G_O = GameOver()


class Level:

    Background_image = pygame.image.load("images/background(1).png")
    Background_image = pygame.transform.scale(Background_image, (600,600))


    def Set_screen(self):
        D.screen.blit(self.Background_image, (-15, -60))
    
    def Update(self):
        rock.positionate_rock()    
        pygame.display.update()
   

    def Boundaries(self):
        if player.rect.x >= (D.Game_width - D.pixel-10):
            player.rect.x = (D.Game_width - D.pixel-10)
        
        if player.rect.x <= 0:
            player.rect.x = 0
    
    def Crash(self):
        
        if pygame.sprite.collide_rect(player, rock):
            
            rock.rect.x = random.randint(D.Game_width+100, 600)
            rock.rect.y = (0-D.pixel)
            rock.rect_y_change += 2
            answer = Qtn.Preguntas()
            if answer == True:
                player.score += 1
                pygame.time.delay(1000)
            else:
                G_O.G_O()
                G_O.loop()
    def play(self):
        while True:
            #Funciones
            self.Set_screen()
            self.Boundaries()
            self.Crash()

            #Controles

            userimput = pygame.key.get_pressed()
            if userimput[pygame.K_LEFT]:
                player.player_image_fliped = pygame.transform.flip(player.player_image_running, True, False)
                player.flag_swip = True
                player.rect.x -= player.vel
            if userimput[pygame.K_RIGHT]:
                player.player_image_fliped = pygame.transform.flip(player.player_image_running, False, False)
                player.flag_swip = False
                player.rect.x += player.vel
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break           
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                        if player.flag_swip == False:
                            player.player_image_fliped = player.player_image
                        else:
                            player.player_image_fliped = pygame.transform.flip(player.player_image, True, False)

            #Posicionamiento y actualizacion de jugador y roca
            D.screen.blit(player.player_image_fliped, (player.rect))
            rock.Update_rock_position()
            rock.Fall_rock()
            
            #refresco de pantalla
            self.Update()

            
            