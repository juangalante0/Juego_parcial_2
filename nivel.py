import pygame
import sys
from configuraciones import fondo_tiempo

class Nivel:
    def __init__(self, pantalla, personaje_principal, imagen_fondo, fondo_vidas, fondo_puntos):

        self.pantalla = pantalla
        self.jugador = personaje_principal
       # self.plataformas = plataformas
        self.img_fondo = imagen_fondo
        self.fondo_vidas = fondo_vidas
        self.fondo_puntos = fondo_puntos
        self.tiempo_inicial = 60
        self.tiempo_actual = self.tiempo_inicial
        self.tiempo_ultimo = self.tiempo_inicial
        self.tiempo_transcurrido = 0
        self.tick_inicial = 0
        self.bandera_disparo = False
        self.tiempo_ultimo_disparo = 0
        


    
    def update (self):

        self.leer_imputs()
        self.actualizar_pantalla()
    

    def leer_imputs (self):

        teclas = pygame.key.get_pressed()
    
        if teclas [pygame.K_RIGHT]:
            self.jugador.que_hace = "derecha"
            self.bandera_disparo = True
        elif teclas [pygame.K_LEFT]:
            self.jugador.que_hace = "izquierda"
            self.bandera_disparo = True
        elif teclas [pygame.K_UP]:
            self.jugador.que_hace = "salta"
            self.bandera_disparo = True
        else:
            self.jugador.que_hace = "quieto"
            self.bandera_disparo = True

        if teclas[pygame.K_SPACE] and self.bandera_disparo:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo >= 800:
                self.jugador.lanzar_proyectiles()
                self.bandera_disparo = False
                self.tiempo_ultimo_disparo = tiempo_actual

    def actualizar_pantalla(self):

        self.pantalla.blit(self.img_fondo, (0, 0))
        self.pantalla.blit(self.fondo_vidas, (1300, 5))
        self.pantalla.blit(self.fondo_puntos, (1485, 5))

    def empieza(self):
        self.tick_inicial = pygame.time.get_ticks()

    def tiempo(self):
        segundos =  (pygame.time.get_ticks() // 1000) - (self.tick_inicial // 1000)
        self.tiempo_actual = self.tiempo_inicial - segundos
        
        if self.tiempo_actual != self.tiempo_ultimo:
            self.tiempo_ultimo = self.tiempo_actual
            self.tiempo_transcurrido += 1
        font = pygame.font.SysFont("Arial", 30)
        if self.tiempo_inicial - self.tiempo_transcurrido <= 0:
            self.tiempo_inicial += 60

        tiempo_surface = font.render(str(self.tiempo_inicial - self.tiempo_transcurrido), False, (0, 0, 0)) 

        self.pantalla.blit(fondo_tiempo, (1650, 5))
        self.pantalla.blit(tiempo_surface, (1750, 5))

        if self.tiempo_actual <= 0:
            self.jugador.muere()
            self.empieza()

    def esta_nivel_completado(self):
        completado = False

        if len(self.lista_enemigos) == 0:
            completado = True

        if len(self.lista_enemigos) == 1 and self.lista_enemigos[0].que_enemigo == "bomba":
            completado = True

        return completado

    def esta_nivel_2_completado(self):
        completado = False

        if len(self.lista_enemigos) == 1 and self.lista_enemigos[0].que_enemigo == "bomba":
            completado = True

        return completado

    def esta_nivel_1_completado(self):
        completado = False

        if len(self.lista_enemigos) == 0:
            completado = True

        return completado
    
    def obtener_jugador(self):
        return self.jugador


        

                


