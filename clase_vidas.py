from configuraciones import game_over
import pygame
from GUI_form_game_over import FormGameOver

class Vidas:
    def __init__(self, imagenes, posicion, pantalla):

        self.imagenes = imagenes
        self.rectangulo = posicion
        self.ya_murio = False

    def mostrar(self, pantalla, akuji, form_game_over):

        for i in range (len(self.rectangulo)):
            for x in range (len(self.imagenes)):
                
                if akuji.vidas == 3:
                    pantalla.blit(self.imagenes[0], self.rectangulo[0])
                    pantalla.blit(self.imagenes[1], self.rectangulo[1])
                    pantalla.blit(self.imagenes[2], self.rectangulo[2])
                elif akuji.vidas == 2:
                    pantalla.blit(self.imagenes[0], self.rectangulo[0])
                    pantalla.blit(self.imagenes[1], self.rectangulo[1])
                elif akuji.vidas == 1:
                    pantalla.blit(self.imagenes[0], self.rectangulo[0])
                else:
                    if not self.ya_murio:
                        form_game_over.active = True
                        self.ya_murio = True
                    
#                    reescalar_game_over = pygame.transform.scale(game_over, (1900, 900))
#                    pantalla.blit(reescalar_game_over, (0, 0))
                    
                    




