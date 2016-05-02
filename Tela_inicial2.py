
import pygame, sys
from pygame.locals import *
import socket


#inicia pygame

pygame.init()

#inicia janela
windowSurface = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("Adivinha!!")

# inicia as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 30)

teste = 0

def Tela_inicial():
    surface_font_score = font.render("What is the number?", True, (255,255,255))
    screen.blit(surface_font_score, (10,10))
     
def blit_font():
    surface_font_score = font.render("Tell me a number ", True, (255,0,0))
    surface_font_score1 = font.render("Player1 = %d " %(teste) , True, (255,255,255))
    surface_font_score2 = font.render("Player2  ", True, (255,255,255))
    screen.blit(background, (0, 0))
    screen.blit(surface_font_score, (10,10))
    screen.blit(surface_font_score1, (10,60))
    screen.blit(surface_font_score2, (10,110))


window = pygame.display.set_mode((800, 600))

screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))



def new_game():
    pygame.event.pump()
    key = pygame.key.get_pressed()

    global teste
      
    if key[pygame.K_LEFT]:
        blit_font()
        pygame.display.update()

        blit_font()
        pygame.display.update()
        teste = teste + 1

               
        

# roda o loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            new_game()
           
            

            
            
        







