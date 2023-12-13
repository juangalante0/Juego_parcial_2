from nivel import *
import sys
from clase_personaje import *
from pygame.locals import *
from clase_plataforma import *
from clase_enemigo import *
from configuraciones import *
from objetos_especiales import *
from clase_vidas import * 

class nivel_dos(Nivel):
    def __init__(self, pantalla):

        pygame.init()

        self.pantalla = pantalla

        #ANCHO W - ALTO H
        self.ANCHO = pantalla.get_width()
        self.ALTO = pantalla.get_height()

        #PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

        #Fondo
        fondo = pygame.image.load(r"Imagenes\todas las imagenes\fondo_nivel_2.png")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO)) 


        diccionario_animaciones = {}
        diccionario_animaciones['derecha'] = personaje_derecha
        diccionario_animaciones['quieto'] =  personaje_quieto
        diccionario_animaciones['izquierda'] = personaje_izquierda
        diccionario_animaciones['salta'] = personaje_salta
        diccionario_animaciones['salta_iz'] = perosnaje_salta_iz
        diccionario_animaciones['quieto_iz'] = personaje_quieto_iz

        self.akuji = Personaje(diccionario_animaciones, 50, 160, (60, 50), 10, "quieto")
        piso = Plataforma(0, 860, 1900, 20, pantalla)
        plataforma = Plataforma(305, 539, 1300, 10, pantalla)
        plataforma_2 = Plataforma(306, 248, 1300, 10, pantalla)
        self.plataforma_movil_i = Plataforma(0, 750, 190, 10, pantalla)
        self.plataforma_movil_d = Plataforma(1695, 750, 190, 10, pantalla)
        pared_izquierda = Plataforma(0, 0, 10, 900, pantalla)
        pared_derecha = Plataforma(1890, 0, 10, 900, pantalla)
        plataforma_dos_lado = Plataforma(300, 545, 10, 55, pantalla)
        plataforma_right = Plataforma(1600, 545, 10, 55, pantalla)
        plataforma_dos_laldo_2 = Plataforma(1600, 250, 10, 55, pantalla)
        plataforma_right_2 = Plataforma(300, 250, 10, 55, pantalla)


        self.diccionario_plataformas = {}
        self.diccionario_plataformas["plataforma"] = plataforma
        self.diccionario_plataformas["plataforma_2"] = plataforma_2
        self.diccionario_plataformas["plataforma_movil_i"] = self.plataforma_movil_i
        self.diccionario_plataformas["plataforma_movil_d"] = self.plataforma_movil_d
        self.diccionario_plataformas["piso"] = piso
        self.diccionario_plataformas["pared_izquierda"] = pared_izquierda
        self.diccionario_plataformas["pared_derecha"] = pared_derecha
        self.diccionario_plataformas["plataforma_uno_lado"] = plataforma_right
        self.diccionario_plataformas["plataforma_dos_lado"] = plataforma_dos_lado
        self.diccionario_plataformas["plataforma_uno_lado_2"] = plataforma_right_2
        self.diccionario_plataformas["plataforma_dos_lado_2"] = plataforma_dos_laldo_2

        self.akuji.rectangulo.bottom = piso.plataforma_rect.top
        ##################enemigo
        diccionario_animaciones_enemigo = {"izquierda": enemigo_verde,
                                        "derecha": enemigo_verde,
                                        "flotador": enemigo_flotador,
                                        "estatico": enemigo_lap,
                                        "escarabajo": enemigo_escarabajo, 
                                        "enemigo_escarabajo_iz": enemigo_escarabajo_iz,
                                        "enemigo_premio": enemigo_premio,
                                        "enemigo_rosa": enemigo_rosa_img,
                                        "bomba": enemigo_bomba
                                        }

        diccionario_animaciones_jefes = {"jefe": jefe_nivel_1}


        posicion_enemigo_verde = pygame.Rect(1800, 600, 50, 50)
        self.enemigo_verde = Enemigo(diccionario_animaciones_enemigo, "izquierda", posicion_enemigo_verde, (50, 50) )
        self.enemigo_verde.rectangulo.bottom = piso.plataforma_rect.top
        posicion_enemigo_rosa = pygame.Rect(800, 600, 50, 50)
        self.enemigo_rosa = Enemigo(diccionario_animaciones_enemigo, "enemigo_rosa", posicion_enemigo_rosa, (50, 50))
        self.enemigo_rosa.rectangulo.bottom = plataforma.plataforma_rect.top
        posicion_enemigo_rosa_2 = pygame.Rect(300, 600, 50, 50)
        self.enemigo_rosa_2 = Enemigo(diccionario_animaciones_enemigo, "enemigo_rosa", posicion_enemigo_rosa_2, (50, 50))
        self.enemigo_rosa_2.rectangulo.bottom = plataforma.plataforma_rect.top
        posicion_enemigo_rosa_3 = pygame.Rect(1400, 600, 50, 50)
        self.enemigo_rosa_3 = Enemigo(diccionario_animaciones_enemigo, "enemigo_rosa", posicion_enemigo_rosa_3, (50, 50))
        self.enemigo_rosa_3.rectangulo.bottom = plataforma.plataforma_rect.top

        # for i in range(50):
        pos_x = randint(50, 1850)
        posicion_bomba = pygame.Rect(pos_x, -100, 50, 50)
        self.bomba = Enemigo(diccionario_animaciones_enemigo, "bomba", posicion_bomba, (50, 50))
        
        self.bomba.generar_bombas_aleatorias(30, diccionario_animaciones_enemigo)




        # #JEFEEESSSSS
        # posicion_jefe_nivel_1 = pygame.Rect(1800, 0, 50, 150)
        # self.jefe_nivel_1 = Enemigo(diccionario_animaciones_jefes, "jefe", posicion_jefe_nivel_1, (150, 150))
        # self.jefe_nivel_1.rectangulo.bottom = plataforma_4.plataforma_rect.top


        self.lista_enemigos = [self.enemigo_verde, self.enemigo_rosa, self.enemigo_rosa_2, self.enemigo_rosa_3, self.bomba]
        #self.lista_bombas = [self.bomba]


        #################################PREMIO

        diccionario_animaciones_premios = {"premio_ojo": premio_ojo}

        posicion_premio_2 = pygame.Rect(300, 200, 30,30)
        self.premio_2 = Objetos_especiales(diccionario_animaciones_premios, posicion_premio_2, (30, 30), "premio_ojo")

        self.premio_2.generar_premios(diccionario_animaciones_premios)
        # posicion_premio = pygame.Rect(1800, 0, 50, 40)
        # self.premio = Objetos_especiales(diccionario_animaciones_premios, posicion_premio, (40, 40), "premio_1")
        # self.premio.rectangulo.bottom = plataforma_2.plataforma_rect.top


        #self.lista_premios = [self.premio_2]

        #######################
        posicion_vidas = pygame.Rect(1390, 12, 30, 30)
        posicion_vidas_2 = pygame.Rect(1420, 12, 30, 30)
        posicion_vidas_3 = pygame.Rect(1450, 12, 30, 30)
        lista_vidas = [posicion_vidas, posicion_vidas_2, posicion_vidas_3]
        self.vidas_ = Vidas(vida, lista_vidas, pantalla)

        super().__init__(pantalla, self.akuji, fondo, fondo_vidas, fondo_puntos)
   
    def actualizar (self, form_game_over):

        self.akuji.actualizar(self.pantalla)
        
        self.enemigo_verde.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_rosa.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_rosa_2.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.enemigo_rosa_3.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.bomba.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)



        lista_bombas = self.bomba.obtener_lista_bombas()
        
        for bomba in lista_bombas:
            bomba.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
            self.akuji.verificar_colision_enemigo(lista_bombas, self.pantalla)



        # self.enemigo_estatico.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        # self.enemigo_escarabajo.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        # self.enemigo_premio.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        # self.jefe_nivel_1.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)

        self.plataforma_movil_i.mostrar_plataforma(self.pantalla)
        self.plataforma_movil_d.mostrar_plataforma(self.pantalla)

        self.akuji.colision_plataformas(self.diccionario_plataformas)
        self.akuji.verificar_colision_enemigo(self.lista_enemigos, self.pantalla)
        lista_premios = self.premio_2.obtener_lista_premios()
        self.akuji.verificar_colision_proyectil(self.akuji.lista_proyectiles, self.lista_enemigos, lista_premios)
        self.akuji.verificar_colision_premio(lista_premios)


        for premio in lista_premios:
            premio.actualizar(self.pantalla)
        
        #self.premio_2.actualizar(self.pantalla)
        self.akuji.sistema_puntos(self.pantalla)
        
        self.enemigo_rosa.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        self.enemigo_rosa_2.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        self.enemigo_rosa_3.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        
        self.vidas_.mostrar(self.pantalla, self.akuji, form_game_over)

        # self.enemigo_premio.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
            

