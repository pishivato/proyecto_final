import pygame

#paleta de colores
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#DImensiones de la Ventana del juego
Game_width = 500
Game_height = 500

#tamano estandar de pixel 
pixel = 64

#Caida de la piedra 
decrement = Game_height-pixel
#Inicializar la pantalla
screen = pygame.display.set_mode((Game_height, Game_width))
#screen.fill(BLUE)