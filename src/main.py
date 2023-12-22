import pygame
import sys

#Inicia Pygame
pygame.init()

#Configuración ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mi RPG')


#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    #Logica del juego y dibujo

    pygame.display.flip()
