import pygame
from configuraciones import plataforma_movil
from configuraciones import plataforma_movil_nivel_3


class Plataforma:
    def __init__(self, coordenada_a, coordenada_b, largo, ancho, ventana):

        self.coordenada_a = coordenada_a
        self.coordenada_b = coordenada_b
        self.largo = largo
        self.ancho = ancho
        self.ventana = ventana
        self.plataforma_rect = pygame.Rect(self.coordenada_a, self.coordenada_b, self.largo, self.ancho)
        self.dar_vuelta = False

    
    def rectangulo_plataforma(self):
        #pygame.draw.rect(self.ventana, "red", self.plataforma_rect, 3)
        return self.plataforma_rect
    
    def plataforma_top(self):
        return self.plataforma_rect.top
    

    def mostrar_plataforma(self, pantalla):

    
        velocidad = 2

        if self.coordenada_b >= 750:
            self.dar_vuelta = False
        elif self.coordenada_b <= 250:
            self.dar_vuelta= True

        if self.dar_vuelta == True:
            self.coordenada_b += velocidad
        else:
            self.coordenada_b -= velocidad

        self.plataforma_rect.topleft = (self.coordenada_a, self.coordenada_b)
        pantalla.blit(plataforma_movil, (self.coordenada_a, self.coordenada_b))


    def mover_plataforma_horizontal(self, pantalla):
        
        velocidad = 4

        if self.coordenada_a >= 1600:
            self.dar_vuelta = False
        elif self.coordenada_a <= 250:
            self.dar_vuelta= True

        if self.dar_vuelta == True:
            self.coordenada_a += velocidad
        else:
            self.coordenada_a -= velocidad

        self.plataforma_rect.topleft = (self.coordenada_a, self.coordenada_b)
        pantalla.blit(plataforma_movil_nivel_3, (self.coordenada_a, self.coordenada_b))


