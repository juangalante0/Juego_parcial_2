import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
from manejador_niveles import Manejador_niveles
import re

    
class FormInicio(Form):
    def __init__(self, screen, x,y,w,h, image_path, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h, None, color_border, border_size, active)

        ##COMPLETAR
        self.bandera_play = False
        #self.txt_nombre = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, "Comic Sans MS", 15, "Black")
        self.background_image = pygame.image.load(image_path)
        self.background_image = pygame.transform.scale(self.background_image, (1900, 900))

        self.esta_jugando = False

        #self.btn_play = Button(self._slave, x, y, 450, 600, 100, 50, "gold", "White", self.btn_play_click, "", "Jugar", "Verdana", 15, "Black")
        self.btn_play_nivel_1 = Button(self._slave, x, y, 400, 250, 200, 50, "gold", "white", self.btn_play_click, "nivel_uno", "Nivel 1", "Verdana", 15, "Black")
        self.btn_play_nivel_2 = Button(self._slave, x, y, 400, 350, 200, 50, "Gray", "white", self.btn_play_click, "nivel_dos", "Nivel 2", "Verdana", 15, "Black")
        self.btn_play_nivel_3 = Button(self._slave, x, y, 400, 450, 200, 50, "Gray", "white", self.btn_play_click, "nivel_tres", "Nivel 3", "Verdana", 15, "Black")

        self.nivel_completado = False
        self.bandera_nivel_2 = False
        self.bandera_nivel_3 = False

        #self.lista_widgets.append(self.txt_nombre)
        #self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_play_nivel_1)
        self.lista_widgets.append(self.btn_play_nivel_2)
        self.lista_widgets.append(self.btn_play_nivel_3)

        self.manejador_niveles = Manejador_niveles(screen)
        self.nivel_actual = self.manejador_niveles.obtener_nivel("nivel_uno")
        
        
    def render(self):
        self._slave.blit(self.background_image, (0, 0))
        super().render()


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        if self.nivel_actual.esta_nivel_completado() and not self.active:
            self.active = True
            self.esta_jugando = False
            self.btn_play_nivel_2._color_background = "gold"
            self.btn_play_nivel_2.render()
        elif self.nivel_actual.esta_nivel_1_completado():
             self.bandera_nivel_2 = True
        elif self.nivel_actual.esta_nivel_2_completado():
            self.btn_play_nivel_3._color_background = "gold"
            self.btn_play_nivel_3.render()
            self.bandera_nivel_3 = True
            
            

    def btn_play_click(self, param):
          
        if self.bandera_play:
            self.active = True
            self.esta_jugando = False

        regex = re.compile(f'.*({param})$')

        if regex.match("btn_play_nivel_uno"):
                self.nivel_actual = self.manejador_niveles.obtener_nivel(param)
                self.nivel_actual.empieza()
                self.active = False
                self.esta_jugando = True
                self.nivel_actual.empieza()

                return self.nivel_actual

        elif regex.match("btn_play_nivel_dos"):
            if self.nivel_actual.esta_nivel_1_completado() or self.bandera_nivel_2 == True:
                self.nivel_actual = self.manejador_niveles.obtener_nivel(param)
                self.nivel_actual.empieza()
                self.active = False
                self.esta_jugando = True
                self.nivel_actual.empieza()

                return self.nivel_actual

        elif regex.match("btn_play_nivel_tres"):

            if self.nivel_actual.esta_nivel_2_completado() or self.bandera_nivel_3 == True:

                self.nivel_actual = self.manejador_niveles.obtener_nivel(param)
                self.nivel_actual.empieza()
                self.active = False
                self.esta_jugando = True
                self.nivel_actual.empieza()

                return self.nivel_actual

        self.bandera_play = not self.bandera_play
        
    
    def obtener_nivel_actual(self):
        #print("obtener nivel")
        return self.nivel_actual
    
    def jugando(self):
        return self.esta_jugando

      