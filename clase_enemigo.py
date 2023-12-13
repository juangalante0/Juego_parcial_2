from configuraciones import *
from clase_personaje import *
from random import randint
from objetos_especiales import *
from clase_proyectil_enemigo import *

class Enemigo:
    def __init__(self, animaciones, que_enemigo, posicion, tamaño):
        self.animaciones = animaciones
        self.tamaño = tamaño
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = posicion
        self.contador_pasos = 0
        self.esta_muerto = False

        self.que_enemigo = que_enemigo
        self.tiempo_aparicion = 3000
        self.tiempo_anterior = 0
        self.aparece = False

        self.flag_escarabajo = False

        self.animacion_actual = self.animaciones[self.que_enemigo]
        #self.animacion_actual = self.animaciones["izquierda"]
        self.lista_proyectiles = []
        self.lista_bombas = []

        self.todos_muertos = False
        self.dar_vuelta = False
        self.dar_vuelta_flotador = False
        self.vidas_jefe = 3
        self.disparo = "izquierda"
        self.proyectiles_enemigo = Proyectiles_enemigo(self.rectangulo, self.disparo) 
        #self.nivel_terminado = False


    def proyectiles_enemigos_h(self, lista_enemigos, pantalla, akuji):
        
        self.proyectiles_enemigo.lanzar_proyectiles_enemigo(self.esta_muerto)
        self.proyectiles_enemigo.actualizar_proyectiles_enemigo(pantalla)
        self.proyectiles_enemigo.verificar_colision_proyectil_enemigo(akuji)
        

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0 
        
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1 

    def caida_bomba(self):
        self.rectangulo.y += 5

    def avanzar(self, plataformas):
        self.rectangulo.x -= 1
        self.disparo = "izquierda"
        self.proyectiles_enemigo.actualizar_direccion(self.disparo) 

        for plataforma in plataformas:
            if self.rectangulo.colliderect(plataformas["pared_izquierda"].rectangulo_plataforma()):
                self.dar_vuelta = True


    def avanzar_reves(self, plataformas):

        self.rectangulo.x += 1
        self.disparo = "derecha"
        self.proyectiles_enemigo.actualizar_direccion(self.disparo) 

        for plataforma in plataformas:
            if self.rectangulo.colliderect(plataformas["pared_derecha"].rectangulo_plataforma()):
                self.dar_vuelta_flotador = True

    def movimiento_jefe(self):
        if randint(0, 100) < 5: 
            self.rectangulo.x += randint(-5, 5)

        if self.esta_muerto:
            self.rectangulo.x = 3000

    def jefe_act(self, ANCHO, ALTO):
        
        tiempo_actual = pygame.time.get_ticks()
        #print(self.aparece)

        if tiempo_actual - self.tiempo_anterior >= self.tiempo_aparicion:

            self.aparece = not self.aparece
            self.tiempo_anterior = tiempo_actual

            if self.aparece and self.que_enemigo == "jefe":
                
                self.rectangulo.x = randint(0, ANCHO - self.rectangulo.width)
                self.rectangulo.y = randint(0, 700 - self.rectangulo.height)
                sonido_jefe.play()


    def generar_bombas_aleatorias(self, cantidad, diccionario_animaciones_enemigo):
        for _ in range(cantidad):
            pos_x = randint(50, 1850)
            pos_y = randint(-5000, -100)
            posicion_bomba = pygame.Rect(pos_x, pos_y, 50, 50)
            bomba = Enemigo(diccionario_animaciones_enemigo, "bomba", posicion_bomba, (50, 50))
            self.lista_bombas.append(bomba)

    def obtener_lista_bombas(self):
        return self.lista_bombas
          

    def no_avanzar(self):
        self.rectangulo = pygame.Rect(0, 0, 100, 100)
    
    def actualizar(self, pantalla, ANCHO, ALTO, plataformas):

        self.jefe_act(ANCHO, ALTO)

        match self.que_enemigo:

            case "izquierda":
                if self.esta_muerto == False:

                    if self.dar_vuelta == True:
                        self.animacion_actual = self.animaciones["derecha"]
                        self.avanzar_reves(plataformas)
                    else:
                        self.animacion_actual = self.animaciones["izquierda"]
                        self.avanzar(plataformas)
                    self.animar(pantalla)

            case "flotador":

                if self.rectangulo.x >= 1220:
                    self.dar_vuelta_flotador = True
                elif self.rectangulo.x <= 605:
                    self.dar_vuelta_flotador = False

                if self.dar_vuelta_flotador == True:
                    self.animacion_actual = self.animaciones["flotador"]
                    self.avanzar(plataformas)
                else:
                    self.animacion_actual = self.animaciones["flotador"]
                    self.avanzar_reves(plataformas)
                self.animar(pantalla)

            case "estatico":
                if self.aparece == True:
                    self.animacion_actual = self.animaciones["estatico"]
                    self.animar(pantalla)
               
            case "enemigo_escarabajo_iz":

                if self.flag_escarabajo == True:
                    self.animacion_actual = self.animaciones["escarabajo"]
                    self.avanzar(plataformas)
                    if self.rectangulo.x <= 350:
                        self.flag_escarabajo = False
                else:
                    self.animacion_actual = self.animaciones["enemigo_escarabajo_iz"]
                    self.avanzar_reves(plataformas)
                    if self.rectangulo.x >= 800:
                        self.flag_escarabajo = True
                self.animar(pantalla)
            case "jefe":
                
                if self.todos_muertos == True:
                    self.animacion_actual = self.animaciones["jefe"]
                    #self.avanzar()
                    self.movimiento_jefe()
                    self.animar(pantalla)
                else:
                    self.no_avanzar()

            case "enemigo_premio":
                
                self.animacion_actual = self.animaciones["enemigo_premio"]
                self.animar(pantalla)
                #self.avanzar(plataformas)
            case "enemigo_rosa":

                if self.rectangulo.x >= 1550:
                    self.dar_vuelta_flotador = True
                elif self.rectangulo.x <= 305:
                    self.dar_vuelta_flotador = False
                
                if self.dar_vuelta_flotador == True:
                    self.avanzar(plataformas)
                else:
                    self.avanzar_reves(plataformas)
                self.animar(pantalla)
            case "bomba":
                self.caida_bomba()
                self.animar(pantalla)
            case "mascota":
                self.animar(pantalla)
                self.avanzar(plataformas)
            case "mascota_b":
                self.animar(pantalla)
                self.avanzar_reves(plataformas)

    def muere(self, lista_enemigos, premio):
        sonido_muerte_enemigo.play()

        match self.que_enemigo:
            case "izquierda":
                self.esta_muerto = True

            case "flotador":
                self.rectangulo.y += 900
                self.esta_muerto = True

            case "estatico":
                self.rectangulo.y += 1000
                self.esta_muerto = True

            case "enemigo_escarabajo_iz":
                self.rectangulo.y += 2000
                self.esta_muerto = True

                for enemigo in lista_enemigos:
                    enemigo.todos_muertos = True

            case "jefe":
                
                self.vidas_jefe -= 1
                if self.vidas_jefe <= 0:
                    self.esta_muerto = True
                else:
                    self.rectangulo.x = randint(0, 1900 - self.rectangulo.width)
                    self.rectangulo.y = randint(0, 700 - self.rectangulo.height)

            case "enemigo_premio":

                for p in premio:
                    p.aparecer = True

                self.rectangulo.y = 1000
                self.esta_muerto = True
            case "enemigo_rosa":
                self.rectangulo.y = 1200
                self.esta_muerto = True
            case "mascota":
                self.esta_muerto = True
                for enemigo in lista_enemigos:
                    enemigo.todos_muertos = True
                self.rectangulo.y = 1200
            case "mascota_b":
                self.esta_muerto = True
                self.rectangulo.y = 1200
    
    # def nivel_terminado(self):
    #     return self.nivel_terminado
