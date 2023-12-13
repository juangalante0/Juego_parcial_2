from nivel import *
import sys
from clase_personaje import *
from pygame.locals import *
from clase_plataforma import *
from clase_enemigo import *
from configuraciones import *
from objetos_especiales import *
from clase_vidas import * 

class nivel_tres(Nivel):
    def __init__(self, pantalla):

        pygame.init()

        self.pantalla = pantalla

        #ANCHO W - ALTO H
        self.ANCHO = pantalla.get_width()
        self.ALTO = pantalla.get_height()

        #PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

        #Fondo
        fondo = pygame.image.load(r"Imagenes\todas las imagenes\fondo_nivel_3.png")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO)) 


        diccionario_animaciones = {}
        diccionario_animaciones['derecha'] = personaje_derecha
        diccionario_animaciones['quieto'] =  personaje_quieto
        diccionario_animaciones['izquierda'] = personaje_izquierda
        diccionario_animaciones['salta'] = personaje_salta
        diccionario_animaciones['salta_iz'] = perosnaje_salta_iz
        diccionario_animaciones['quieto_iz'] = personaje_quieto_iz

        self.akuji = Personaje(diccionario_animaciones, 50, 600, (60, 50), 10, "quieto")
        piso = Plataforma(110, 785, 1700, 20, pantalla)
        plataforma = Plataforma(0, 720, 110, 10, pantalla)
        plataforma_2 = Plataforma(1790, 720, 110, 10, pantalla)
        plataforma_uno_lado = Plataforma(110, 720, 10, 60, pantalla)
        plataforma_dos_lado = Plataforma(1790, 720, 10, 60, pantalla)
        plataforma_dos_laldo_2 = Plataforma(0, 900, 10, 55, pantalla)
        plataforma_right_2 = Plataforma(0, 900, 10, 55, pantalla)


        self.plataforma_movil_i = Plataforma(300, 600, 190, 10, pantalla)
        self.plataforma_movil_d = Plataforma(1695, 450, 190, 10, pantalla)
        self.plataforma_movil_z = Plataforma(800, 300, 190, 10, pantalla)

        pared_izquierda = Plataforma(0, 0, 10, 900, pantalla)
        pared_derecha = Plataforma(1890, 0, 10, 900, pantalla)


        self.diccionario_plataformas = {}
        self.diccionario_plataformas["plataforma"] = plataforma
        self.diccionario_plataformas["plataforma_2"] = plataforma_2
        self.diccionario_plataformas["plataforma_movil_i"] = self.plataforma_movil_i
        self.diccionario_plataformas["plataforma_movil_d"] = self.plataforma_movil_d
        self.diccionario_plataformas["plataforma_movil_z"] = self.plataforma_movil_z
        self.diccionario_plataformas["piso"] = piso
        self.diccionario_plataformas["pared_izquierda"] = pared_izquierda
        self.diccionario_plataformas["pared_derecha"] = pared_derecha
        self.diccionario_plataformas["plataforma_uno_lado"] = plataforma_uno_lado
        self.diccionario_plataformas["plataforma_dos_lado"] = plataforma_dos_lado
        self.diccionario_plataformas["plataforma_uno_lado_2"] = plataforma_right_2
        self.diccionario_plataformas["plataforma_dos_lado_2"] = plataforma_dos_laldo_2

        self.akuji.rectangulo.bottom = plataforma.plataforma_rect.top

        diccionario_animaciones_jefes = {"jefe": jefe_nivel_1, "mascota": mascota_jefe_a, "mascota_b": mascota_jefe_b}
        diccionario_animaciones_jefe_final = {"jefe": jefe_nivel_1}

        # #JEFEEESSSSS

        posicion_mascota_a = pygame.Rect(1600, 720, 150, 50)
        self.mascota_a = Enemigo(diccionario_animaciones_jefes, "mascota", posicion_mascota_a, (150, 70))
        posicion_mascota_b = pygame.Rect(300, 720, 150, 50)
        self.mascota_b = Enemigo(diccionario_animaciones_jefes, "mascota_b", posicion_mascota_b, (150, 70))
        posicion_jefe_nivel_1 = pygame.Rect(1800, 0, 50, 150)
        self.jefe_nivel_1 = Enemigo(diccionario_animaciones_jefe_final, "jefe", posicion_jefe_nivel_1, (150, 150))
        self.lista_enemigos = [self.jefe_nivel_1, self.mascota_a, self.mascota_b, self.jefe_nivel_1, self.jefe_nivel_1]


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
        
        self.jefe_nivel_1.actualizar(self.pantalla, self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.mascota_a.actualizar(self.pantalla,self.ANCHO, self.ALTO, self.diccionario_plataformas)
        self.mascota_b.actualizar(self.pantalla,self.ANCHO, self.ALTO, self.diccionario_plataformas)

        self.plataforma_movil_i.mover_plataforma_horizontal(self.pantalla)
        self.plataforma_movil_d.mover_plataforma_horizontal(self.pantalla)
        self.plataforma_movil_z.mover_plataforma_horizontal(self.pantalla)

        self.akuji.sistema_puntos(self.pantalla)
        self.akuji.colision_plataformas(self.diccionario_plataformas)
        self.akuji.verificar_colision_enemigo(self.lista_enemigos, self.pantalla)
        lista_premios = self.premio_2.obtener_lista_premios()
        self.akuji.verificar_colision_proyectil(self.akuji.lista_proyectiles, self.lista_enemigos, lista_premios)
        self.akuji.verificar_colision_premio(lista_premios)


        for premio in lista_premios:
            premio.actualizar(self.pantalla)
        
        #self.premio_2.actualizar(self.pantalla)
        
        self.jefe_nivel_1.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        # self.enemigo_rosa_3.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
        
        self.vidas_.mostrar(self.pantalla, self.akuji, form_game_over)

        # self.enemigo_premio.proyectiles_enemigos_h(self.lista_enemigos, self.pantalla, self.akuji)
            

