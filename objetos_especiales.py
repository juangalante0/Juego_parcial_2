from configuraciones import *

class Objetos_especiales:
    def __init__(self, animacion, posicion, tamaño, que_premio):
       
        self.animacion = animacion
        reescalar_imagenes(self.animacion, tamaño)
        #self.tamaño = tamaño
        self.rectangulo = posicion
        self.que_premio = que_premio
        self.aparecer = False
        self.recogido = False
        self.desaparecer = False
        self.animacion_actual = self.animacion[self.que_premio]
        self.lista_premios = []


    def animar(self, pantalla):


        if self.aparecer == True:
            pantalla.blit(self.animacion_actual[0], self.rectangulo)

    def animar_ojo(self, pantalla):
        
        if self.desaparecer == False:
            pantalla.blit(self.animacion_actual[0], self.rectangulo)

    def generar_premios(self, diccionario_premios):
        #x = 300
        pos_x = 200
        for _ in range(14):
            pos_x += 98
            pos_y = 200
            posicion_ojo = pygame.Rect(pos_x, pos_y, 50, 50)
            ojos = Objetos_especiales(diccionario_premios, posicion_ojo, (30, 30), "premio_ojo")
            self.lista_premios.append(ojos)
        

    def obtener_lista_premios(self):
         
         return self.lista_premios
         
         
    def actualizar(self, pantalla):

        match self.que_premio:

            case "premio_1":
                    self.animacion_actual = self.animacion["premio_1"]
                    self.animar(pantalla)
            case "premio_ojo":
                    self.animacion_actual = self.animacion["premio_ojo"]
                    self.animar_ojo(pantalla)
            # case "puerta":
            #         if  == True:
            #             self.animacion_actual = self.animacion["puerta"]
            #             self.animar_ojo(pantalla)


                  



    

    
        
    

