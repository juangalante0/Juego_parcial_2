from pygame.locals import *
from nivel_uno import *
from nivel_dos import *
from nivel_tres import *
from nivel import *
from GUI_form_prueba import FormPrueba
from GUI_form_inicio import FormInicio
from GUI_form_win import FormWin
import pygame
import sqlite3

#from manejador_niveles import Manejador_niveles

ANCHO,ALTO = 1900,900
FPS = 18 #para desacelerar la pantalla

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

form_pausa = FormPrueba(PANTALLA, 200, 100, 900, 350, "Brown", "Yellow", 3, False)
form_inicio = FormInicio(PANTALLA, 0, 0, 1900, 900, r"Imagenes\todas las imagenes\fondo_inicio.jpg", "gold", 3, True)
form_game_over = FormGameOver(PANTALLA, 0, 0, 1900, 900, r"Imagenes\todas las imagenes\fondo_game_over.jpg", "gold", 3, False)
form_game_over.recibir_form_inicio(form_inicio)
form_win = FormWin(PANTALLA, 0, 0, 1900, 900, r"Imagenes\todas las imagenes\fondo_4.jpg", "gold", 3, False)
form_win.recibir_form_inicio(form_inicio)

puntos_finales = 0
pausado = False
bandera = True
carga_final = True

def crear_tabla(conexion):
    sentencia = '''
                create table if not exists Jugadores
                (
                    id_jugador integer primary key autoincrement,
                    nombre text,
                    puntos integer
                )

                '''
    conexion.execute(sentencia)
    #print("tabla creada")

def insertar_datos(conexion, nombre, puntos):
    
    sentencia = '''
                insert into Jugadores(nombre, puntos) values(?,?)
                '''
    conexion.execute(sentencia, (nombre, puntos))

while bandera:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == QUIT:
            bandera = False
        if evento.type == MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                form_pausa.active = not form_pausa.active
                pausado = not pausado
                


    jugar = form_inicio.esta_jugando

    if jugar and not pausado:
        nivel_actual = form_inicio.obtener_nivel_actual()
        nivel_actual.update()
        nivel_actual.actualizar(form_game_over)
        nivel_actual.tiempo()
        completo = nivel_actual.esta_nivel_completado()
        if completo == True:
            form_win.active = True
            form_win.caja_texto()
            puntos = nivel_actual.obtener_jugador().obtener_puntos()
            #print(puntos)
            puntos_finales += puntos
            cargar_base_datos = True

    nombre = form_win.obtener_nombre_jugador()
    # print(f"aca de nuevo {nombre}")
    # print(f"puntos finales {puntos_finales}")

    form_inicio.update(eventos)
    form_pausa.update(eventos)
    form_game_over.update(eventos)
    form_win.update(eventos)

    cargar_datos = form_win.cargar_nombre()

    if cargar_datos and cargar_base_datos and carga_final:

        with sqlite3.connect("./base_de_datos_akuji.db") as conexion:
            try:
                crear_tabla(conexion)
            
                if nombre and puntos_finales:
                    insertar_datos(conexion, nombre, puntos_finales)

            except BaseException as error:
                print(error)
        carga_final = False


    pygame.display.update()




def actualizar_tabla(conexion, puntos):

    sentencia = 'update Jugadores set puntos = ?'

    cursor = conexion.execute(sentencia,(puntos,))
