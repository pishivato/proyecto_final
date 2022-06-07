from tkinter import*
from tkinter import messagebox
import level as lvl
import data as D
import pygame

pygame.init()

wind = Tk()
wind.withdraw()
l = lvl.Level()

class Main():
    image = pygame.image.load("images/back_g1.jpg")
    image = pygame.transform.scale(image, (600, 600))
    
    def Home(self):
        D.screen.blit(self.image, (-15, -60))

    def Start(self):
        answer = messagebox.askquestion("Inicio de Esquiva la Roca", "Jugar(Yes)/Salir(No)")
        if answer == "yes":
            l.play()
        else:
            self.Quit()
    
    def Quit(self):
        pygame.quit()

main = Main()
    
while True:
    main.Home()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    main.Start()
    
    pygame.display.update()
