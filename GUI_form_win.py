import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
    
class FormWin(Form):
    def __init__(self, screen, x,y,w,h, image_path, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h, None, color_border, border_size, active)

        ##COMPLETAR
        self.bandera_play = False
        self.txt_nombre = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, "Comic Sans MS", 15, "Black")
        self.texto_ingresado = self.txt_nombre.get_text()
        self.background_image = pygame.image.load(image_path)
        self.background_image = pygame.transform.scale(self.background_image, (1900, 900))

        self.btn_play = Button(self._slave, x, y, 450, 600, 200, 70, "gold", "White", self.btn_play_click, "", "Siguiente", "Verdana", 15, "Black")
        
        self.contador = 2
        #self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play)
        self.cargar = False

    def recibir_form_inicio(self, form_inicio):
        self.form_inicio = form_inicio

    
    def render(self):
        self._slave.blit(self.background_image, (0, 0))
        super().render()


    def update(self, lista_eventos):
        #print(self.active)
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos) 
        
    
    def btn_play_click(self, param):
        self.active = False
        self.form_inicio.active = True
        self.contador -= 1
        if self.contador < 0:
            self.cargar = True
    def caja_texto(self):
        
        #print(f"contador de formwin {self.contador}")

        if self.contador == 0:
            self.lista_widgets.append(self.txt_nombre)
            
        
    def obtener_nombre_jugador(self):

        return self.txt_nombre.get_text()
    

    def cargar_nombre(self):

        if self.cargar:
            return True
        
    
    

    



          

      