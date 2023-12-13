from pygame.locals import * 
from nivel_uno import nivel_uno
from nivel_dos import nivel_dos
from nivel_tres import nivel_tres

class Manejador_niveles:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.niveles = {"nivel_uno": nivel_uno, "nivel_dos": nivel_dos, "nivel_tres": nivel_tres}

    def obtener_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self.pantalla)
    