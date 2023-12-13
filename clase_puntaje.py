import pygame



class Puntos:
    def __init__(self, texto, font, color, tamaño):

        self.font = font
        self.color = color
        self.texto = texto
        self.tamaño = tamaño


    
    def escribir(self, pantalla):

        self.texto = str(self.texto)

        fuente = pygame.font.SysFont(self.font, self.tamaño)
        texto = fuente.render(self.texto, True, self.color)
        pantalla.blit(texto, (1580, 7))