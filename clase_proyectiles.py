import pygame

class Proyectiles:
    def __init__(self, x, y, direccion, proyectil):
        self.superficie = proyectil
        self.superficie = pygame.transform.scale(self.superficie, (30, 10))

        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

    def actualizar(self):
        if self.direccion == "derecha" or self.direccion == "quieto":
            self.rectangulo.x += 10
        elif self.direccion == "izquierda":
            self.rectangulo.x -= 10
    

   



        