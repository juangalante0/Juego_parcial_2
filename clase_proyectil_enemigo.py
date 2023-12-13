
from clase_proyectiles import Proyectiles
from configuraciones import proyectil_enemigo
from configuraciones import sonido_disparo_enemigo
import pygame
import random

class Proyectiles_enemigo():
    def __init__(self, rectangulo, direccion):
        #self.imagen = imagen
        self.rectangulo = rectangulo
        self.direccion = direccion
        self.lista_proyectiles = []
        self.tiempo_entre_disparos = random.randint(3000, 7000)  
        self.ultimo_disparo = pygame.time.get_ticks()
        self.tiempo_limite_disparo = 3000
        self.puede_disparar = True
        self.personaje_rect = None
       
    def lanzar_proyectiles_enemigo(self, esta_muerto):
        tiempo_actual = pygame.time.get_ticks()

        if not esta_muerto:
            if tiempo_actual - self.ultimo_disparo >= self.tiempo_entre_disparos and tiempo_actual - self.ultimo_disparo <= self.tiempo_entre_disparos + self.tiempo_limite_disparo and self.puede_disparar:
                x = None
                y = self.rectangulo.centery + 10

                if self.direccion == "derecha":
                    x = self.rectangulo.right
                elif self.direccion == "izquierda":
                    x = self.rectangulo.left

                self.ultimo_disparo = pygame.time.get_ticks()

                if x is not None:
                    proyectil = Proyectiles(x, y, self.direccion, proyectil_enemigo)
                    self.lista_proyectiles.append(proyectil)
                    sonido_disparo_enemigo.play()
                    self.puede_disparar = False

            if tiempo_actual > self.ultimo_disparo + self.tiempo_limite_disparo:
                self.puede_disparar = True

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def verificar_colision_proyectil_enemigo(self, akuji):
        for proyectil in self.lista_proyectiles:
            if proyectil.rectangulo.colliderect(akuji.rectangulo):
                akuji.muere()
                self.lista_proyectiles.remove(proyectil)
    
    
    

    def actualizar_proyectiles_enemigo(self, pantalla):
        i = 0

        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]

            pantalla.blit(p.superficie, p.rectangulo)
            p.actualizar()

            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            
            i += 1
    
    