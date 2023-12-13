import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
import sqlite3

def traer_jugadores(conexion):

    sentencia = 'select * from Jugadores order by puntos desc limit 5'
    cursor = conexion.execute(sentencia)

    diccionario = []

    for fila in cursor:
        item = {}
        item["jugador"] = fila[1]
        item["puntos"] = fila[2]

        diccionario.append(item)

    return diccionario
    
class FormPrueba(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        ##COMPLETAR
        self.bandera_play = True 
        self.volumen = 0.2
        #self.volunmen_efectos = 0.2
        pygame.mixer.init()
        pygame.mixer.music.load(r"musica\DANCE m.mp3")
        #pygame.mixer.music.load("")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        #self.txt_nombre = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, "Comic Sans MS", 15, "Black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "White", self.btn_play_click, "hola", "Musica Off", "Verdana", 15, "Black")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Red", "yellow")

        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, porcentaje_volumen, "Comic Sans MS", 15, "White", "Imagenes\Recursos\Table.png")
        self.btn_tabla = Button_Image(self._slave, x, y, 225, 100, 50, 50, "Imagenes\Recursos\Menu_BTN.png", self.btn_tabla_click, "")
        

        #self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)


    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
         self.volumen = self.slider_volumen.value
         self.label_volumen.update(lista_eventos)
         self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
         pygame.mixer.music.set_volume(self.volumen)
        
        
    
    def btn_play_click(self, param):
        if self.bandera_play:
           pygame.mixer.music.pause()
           self.btn_play._color_background = "Yellow"
           self.btn_play.set_text("Musica On")
        else:
           pygame.mixer.music.unpause()
           self.btn_play._color_background = "Red"
           self.btn_play.set_text("Musica Off")

        
        self.bandera_play = not self.bandera_play
    
    
    def btn_tabla_click(self, param):

        with sqlite3.connect("./base_de_datos_akuji.db") as conexion:
            try:
               diccionario = traer_jugadores(conexion)
            except BaseException as error:
                print(error)
       
        nuevo_form = FormMenuScore(screen = self._master,
                                x = 250,
                                y = 25,
                                w = 500,
                                h = 550,
                                color_background = "green",
                                color_border = "gold",
                                active = True,
                                path_image = r"Imagenes\todas las imagenes\fondo_tabla_puntos.jpg",
                                margen_x = 10,
                                margen_y = 100,
                                espacio = 10,
                                scoreboard = diccionario)
        self.show_dialog(nuevo_form)