from configuraciones import *
from clase_proyectiles import *
from objetos_especiales import *
from clase_puntaje import *

class Personaje:
    def __init__(self, animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x, pos_y, *tamaño) #el asterisco desarma la tupla
        #self.rectangulo = self.animaciones["quieto"][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = velocidad

        self.que_hace = que_hace
        self.contador_pasos = 0

        self.animacion_actual = self.animaciones[self.que_hace]

        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -20

        self.limite_velocidad_salto = 18
        self.esta_saltando = False
        self.caminata_anterior = "quieto"

        self.vidas = 3
        self.vida_jefe = 3
        self.puntos = 0
        self.lista_proyectiles = []
        self.akuji_muerto = False
    
    def aplicar_gravedad(self, pantalla):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            
    def colision_plataformas(self, plataformas):

        for plataforma in plataformas.values():

            if self.rectangulo.colliderect(plataformas["pared_izquierda"].rectangulo_plataforma()):
                self.rectangulo.left = plataformas["pared_izquierda"].plataforma_rect.right

            elif self.rectangulo.colliderect(plataformas["pared_derecha"].rectangulo_plataforma()):
                self.rectangulo.right = plataformas["pared_derecha"].plataforma_rect.left

            elif self.rectangulo.colliderect(plataformas["plataforma_uno_lado"].rectangulo_plataforma()):
                self.rectangulo.left = plataformas["plataforma_uno_lado"].plataforma_rect.right

            elif self.rectangulo.colliderect(plataformas["plataforma_dos_lado"].rectangulo_plataforma()):
                self.rectangulo.right = plataformas["plataforma_dos_lado"].plataforma_rect.left

            elif self.rectangulo.colliderect(plataformas["plataforma_dos_lado_2"].rectangulo_plataforma()):
                self.rectangulo.left = plataformas["plataforma_dos_lado_2"].plataforma_rect.right
            
            elif self.rectangulo.colliderect(plataformas["plataforma_uno_lado_2"].rectangulo_plataforma()):
                self.rectangulo.right = plataformas["plataforma_uno_lado_2"].plataforma_rect.left
            
            elif self.rectangulo.colliderect(plataforma.rectangulo_plataforma()):

                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.rectangulo.bottom = plataforma.plataforma_top()
                break
            else:
                self.esta_saltando = True
            
    def lanzar_proyectiles(self):
        x = None

        y = self.rectangulo.centery + 10
        if self.caminata_anterior == "derecha":
            x = self.rectangulo.right
        elif self.caminata_anterior == "izquierda":
            x = self.rectangulo.left
        
        if x is not None:
            proyectil = Proyectiles(x, y, self.caminata_anterior, proyectil_i)
            self.lista_proyectiles.append(proyectil)
        sonido_disparo_akuji.play()
        
     
    def verificar_colision_proyectil(self, lista_proyectiles, lista_enemigos, premio):

        for proyectil in lista_proyectiles:
            for enemigo in lista_enemigos:
                

                if enemigo.rectangulo.colliderect(proyectil.rectangulo):
                    
                    enemigo.muere(lista_enemigos, premio)
                    self.lista_proyectiles.remove(proyectil)
                    self.puntos += 300
                    lista_enemigos.remove(enemigo)

    def actualizar_proyectiles(self, pantalla):
        i = 0

        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]

            pantalla.blit(p.superficie, p.rectangulo)
            p.actualizar()

            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1
    
    def sistema_puntos(self, pantalla):

        puntaje = Puntos(self.puntos, "Arial", "black", 25)
        puntaje.escribir(pantalla)

    def obtener_puntos(self):
        return self.puntos
    
    def muere(self):
        
        if self.vidas > 1:
            self.rectangulo.x = 50
            self.rectangulo.y = 600
            self.vidas -= 1
            sonido_muerte_akuji.play()
            if not self.akuji_muerto:
                self.puntos -= 200
                
        else:
            self.vidas -= 1
            self.rectangulo.y = 1000
            if not self.akuji_muerto:
                self.puntos -= 200
                sonido_muerte_akuji.play()
        
        if self.vidas <= 0:
            self.akuji_muerto = True

    
    def verificar_colision_enemigo(self, lista_enemigos, pantalla):

        if self.rectangulo.y > 800 and self.rectangulo.y > 1000:
            self.muere()


        for enemigo in lista_enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo):

                #enemigo.muriendo = True
                self.muere()
                enemigo.animar(pantalla)


    def verificar_colision_premio(self, lista_premios):
            
            for premio in lista_premios:

                if premio.rectangulo.colliderect(self.rectangulo) and not premio.recogido:
                    self.puntos += 1000
                    premio.recogido = True
                    premio.aparecer = False
                    premio.desaparecer = True
                    sonido_premio.play()
                    print(len(lista_premios))

                # elif lista_premios[1].rectangulo.colliderect(self.rectangulo):
                #     self.puntos += 300
                #     lista_premios[1].aparecer = False  

            
                    
    
    def desplazar(self):
        
        if self.que_hace == "izquierda":
             self.caminata_anterior = "izquierda"
             self.rectangulo.x -= self.velocidad
             
        elif self.que_hace == "derecha":
            self.caminata_anterior = "derecha"
            self.rectangulo.x += self.velocidad

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0 
        
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1 



    def actualizar(self, pantalla):

        match self.que_hace:
            case "derecha":
                #self.caminata_anterior = "derecha"
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                self.animacion_actual = self.animaciones["salta"]
                self.desplazar()

            case "izquierda":
                #self.caminata_anterior = "izquierda"
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                self.animacion_actual = self.animaciones["salta_iz"]
                self.desplazar()

            case "quieto":
                if not self.esta_saltando:
                    if self.caminata_anterior != "izquierda":
                        self.animacion_actual = self.animaciones["quieto"]
                    else:
                        self.animacion_actual = self.animaciones["quieto_iz"]

                self.animar(pantalla)

            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    if self.caminata_anterior != "izquierda":
                        self.animacion_actual = self.animaciones["salta"]
                    else:
                        self.animacion_actual = self.animaciones["salta_iz"]
                self.animar(pantalla)

        #print(f"puntos {self.puntos}")
        #print(f"vidas {self.vidas}")

        self.actualizar_proyectiles(pantalla)
        self.aplicar_gravedad(pantalla)