from nivel import *
import sys
from clase_personaje import *
from pygame.locals import *
from clase_plataforma import *
from clase_enemigo import *
from configuraciones import *
from objetos_especiales import *
from clase_vidas import * 

class nivel_uno(Nivel):
    def __init__(self, pantalla):

        pygame.init()

        self.pantalla = pantalla

        #ANCHO W - ALTO H
        self.ANCHO = pantalla.get_width()
        self.ALTO = pantalla.get_height()

        #PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

        #Fondo
        fondo = pygame.image.load(r"Imagenes\todas las imagenes\fondo_nivel_1.png")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO)) 

        diccionario_animaciones = {}
        diccionario_animaciones['derecha'] = personaje_derecha
        diccionario_animaciones['quieto'] =  personaje_quieto
        diccionario_animaciones['izquierda'] = personaje_izquierda
        diccionario_animaciones['salta'] = personaje_salta
        diccionario_animaciones['salta_iz'] = perosnaje_salta_iz
        diccionario_animaciones['quieto_iz'] = personaje_quieto_iz

        self.akuji = Personaje(diccionario_animaciones, 50, 160, (60, 50), 10, "quieto")
        piso = Plataforma(0, 855, 678, 20, pantalla)
        piso_2 = Plataforma(935, 855, 1023, 20, pantalla)
        plataforma = Plataforma(601, 498, 675, 10, pantalla)
        plataforma_bottom = Plataforma(601, 547, 675, 10, pantalla)
        plataforma_dos_lado = Plataforma(600, 505, 10, 55, pantalla)
        plataforma_right = Plataforma(1272, 510, 10, 50, pantalla)#
        plataforma_2 = Plataforma(344, 329, 500, 10, pantalla)
        plataforma_3 = Plataforma(1110, 782, 190, 100, pantalla)
        plataforma_4 = Plataforma(1486, 680, 400, 10, pantalla)
        plataforma_5 = Plataforma(1710, 516, 400, 60, pantalla)
        plataforma_6 = Plataforma(0, 194, 397, 60, pantalla)
        #plataforma_7 = Plataforma(1300, 600, 100, 20, pantalla)
        pared_izquierda = Plataforma(0, 0, 10, 900, pantalla)
        pared_derecha = Plataforma(1890, 0, 10, 900, pantalla)
        plataforma_dos_laldo_2 = Plataforma(838, 334, 10, 45, pantalla)
        plataforma_right_2 = Plataforma(1486, 690, 10, 45, pantalla)

        #plataformas = [piso, piso_2, plataforma, plataforma_2, plataforma_3, plataforma_4, plataforma_5, plataforma_6]

        self.diccionario_plataformas = {}
        self.diccionario_plataformas["plataforma"] = plataforma
        self.diccionario_plataformas["plataforma_2"] = plataforma_2
        self.diccionario_plataformas["plataforma_3"] = plataforma_3
        self.diccionario_plataformas["plataforma_4"] = plataforma_4
        self.diccionario_plataformas["plataforma_5"] = plataforma_5
        self.diccionario_plataformas["plataforma_6"] = plataforma_6
       # self.diccionario_plataformas["plataforma_7"] = plataforma_7
        self.diccionario_plataformas["piso"] = piso
        self.diccionario_plataformas["piso_2"] = piso_2
        self.diccionario_plataformas["plataforma_bottom"] =  plataforma_bottom
        self.diccionario_plataformas["plataforma_uno_lado"] = plataforma_right
        self.diccionario_plataformas["plataforma_dos_lado"] = plataforma_dos_lado
        self.diccionario_plataformas["plataforma_uno_lado_2"] = plataforma_right_2
        self.diccionario_plataformas["plataforma_dos_lado_2"] = plataforma_dos_laldo_2


        self.diccionario_plataformas["pared_izquierda"] = pared_izquierda
        self.diccionario_plataformas["pared_derecha"] = pared_derecha

        self.akuji.rectangulo.bottom = piso.plataforma_rect.top
        ##################enemigo
        diccionario_animaciones_enemigo = {"izquierda": enemigo_camina_izquierda,
                                        "derecha": enemigo_camina_derecha,
                                        "flotador": enemigo_flotador,
                                        "estatico": enemigo_lap,
                                        "escarabajo": enemigo_escarabajo, 
                                        "enemigo_escarabajo_iz": enemigo_escarabajo_iz,
                                        "enemigo_premio": enemigo_premio
                                        }

        #diccionario_animaciones_jefes = {"jefe": jefe_nivel_1}


        posicion_un_enemigo = pygame.Rect(600, 600, 50, 50)
        self.un_enemigo = Enemigo(diccionario_animaciones_enemigo, "izquierda", posicion_un_enemigo, (50, 50) )
        self.un_enemigo.rectangulo.bottom = piso.plataforma_rect.top
        posicion_enemigo_dos = pygame.Rect(800, 0, 50, 50)
        self.enemigo_dos = Enemigo(diccionario_animaciones_enemigo, "flotador", posicion_enemigo_dos, (50, 50))
        self.enemigo_dos.rectangulo.bottom = plataforma.plataforma_rect.top
        posicion_enemigo_estatico = pygame.Rect(1710, 0, 50, 50)
        self.enemigo_estatico = Enemigo(diccionario_animaciones_enemigo, "estatico", posicion_enemigo_estatico, (50, 50))
        self.enemigo_estatico.rectangulo.bottom = plataforma_5.plataforma_rect.top
        posicion_enemigo_escarabajo = pygame.Rect(360, 400, 50, 50)
        self.enemigo_escarabajo = Enemigo(diccionario_animaciones_enemigo, "enemigo_escarabajo_iz", posicion_enemigo_escarabajo, (50, 50) )
        self.enemigo_escarabajo.rectangulo.bottom = plataforma_2.plataforma_rect.top

        posicion_enemigo_premio = pygame.Rect(1800, 300, 50, 50)
        self.enemigo_premio = Enemigo(diccionario_animaciones_enemigo, "enemigo_premio", posicion_enemigo_premio, (50, 50))
        self.enemigo_premio.rectangulo.bottom = plataforma_4.plataforma_rect.top
        #JEFEEESSSSS
        # posicion_jefe_nivel_1 = pygame.Rect(1800, 0, 50, 150)
        # self.jefe_nivel_1 = Enemigo(diccionario_animaciones_jefes, "jefe", posicion_jefe_nivel_1, (150, 150))
        # self.jefe_nivel_1.rectangulo.bottom = plataforma_4.plataforma_rect.top


        self.lista_enemigos = [self.un_enemigo, self.enemigo_dos, self.enemigo_estatico, self.enemigo_escarabajo, self.enemigo_premio]


        #################################PREMIO

        diccionario_animaciones_premios = {"premio_1": premio_i,
                                           "premio_ojo": premio_ojo,
                                           "puerta": puerta}

        posicion_premio = pygame.Rect(1800, 0, 50, 40)
        self.premio = Objetos_especiales(diccionario_animaciones_premios, posicion_premio, (40, 40), "premio_1")
        self.premio.rectangulo.bottom = plataforma_4.plataforma_rect.top
        posicion_premio_2 = pygame.Rect(678, 675, 30,30)
        self.premio_2 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_2, (30, 30), "premio_ojo")
        posicion_premio_3 = pygame.Rect(758, 675, 30,30)
        self.premio_3 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_3, (30, 30), "premio_ojo")
        posicion_premio_4 = pygame.Rect(833, 675, 30,30)
        self.premio_4 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_4, (30, 30), "premio_ojo")
        posicion_premio_5 = pygame.Rect(908, 675, 30,30)
        self.premio_5 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_5, (30, 30), "premio_ojo")
        posicion_premio_6 = pygame.Rect(1450, 800, 30,30)
        self.premio_6 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_6, (30, 30), "premio_ojo")
        posicion_premio_7 = pygame.Rect(1550, 800, 30,30)
        self.premio_7 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_7, (30, 30), "premio_ojo")
        posicion_premio_8 = pygame.Rect(1650, 800, 30,30)
        self.premio_8 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_8, (30, 30), "premio_ojo")
        posicion_premio_9 = pygame.Rect(1750, 800, 30,30)
        self.premio_9 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_9, (30, 30), "premio_ojo")
        posicion_puerta = pygame.Rect(50, 150, 30,30)
        self.puerta = Objetos_especiales(diccionario_animaciones_premios, posicion_puerta, (30,30), "puerta")



        self.lista_premios = [self.premio, self.premio_2, self.premio_3, self.premio_4, self.premio_5, self.premio_6, self.premio_7, self.premio_8, self.premio_9, self.puerta]

        #######################
        posicion_vidas = pygame.Rect(1390, 12, 30, 30)
        posicion_vidas_2 = pygame.Rect(1420, 12, 30, 30)
        posicion_vidas_3 = pygame.Rect(1450, 12, 30, 30)
        lista_vidas = [posicion_vidas, posicion_vidas_2, posicion_vidas_3]
        self.vidas_ = Vidas(vida, lista_vidas, pantalla)

        super().__init__(pantalla, self.akuji, fondo, fondo_vidas, fondo_puntos)
   
    def actualizar (self, form_game_over):

        self.akuji.actualizar(self.pantalla)
        #akuji.actualizar(PANTALLA, piso_2)
        self.un_enemigo.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_dos.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_estatico.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_escarabajo.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_premio.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        #self.jefe_nivel_1.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)


        self.akuji.colision_plataformas(self.diccionario_plataformas)
        self.akuji.verificar_colision_enemigo(self.lista_enemigos, self.pantalla)
        self.akuji.verificar_colision_proyectil(self.akuji.lista_proyectiles, self.lista_enemigos, self.lista_premios)
        self.akuji.verificar_colision_premio(self.lista_premios)
        self.premio.actualizar(self.pantalla)
        self.akuji.sistema_puntos(self.pantalla)
        self.premio_2.actualizar(self.pantalla)
        self.premio_3.actualizar(self.pantalla)
        self.premio_4.actualizar(self.pantalla)
        self.premio_5.actualizar(self.pantalla)
        self.premio_6.actualizar(self.pantalla)
        self.premio_7.actualizar(self.pantalla)
        self.premio_8.actualizar(self.pantalla)
        self.premio_9.actualizar(self.pantalla)
        self.puerta.actualizar(self.pantalla)
        
        self.un_enemigo.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        self.enemigo_premio.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
            
        self.vidas_.mostrar(self.pantalla, self.akuji, form_game_over)
