import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))


    return lista_girada




def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)


personaje_quieto = [pygame.image.load(r"Imagenes\todas las imagenes\quieto_de.png")]

personaje_quieto_iz = girar_imagenes(personaje_quieto, True, False)


personaje_derecha = [pygame.image.load(r"Imagenes\todas las imagenes\camina_de_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\camina_de.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\camina_de_3.png")]

personaje_izquierda = [pygame.image.load(r"Imagenes\todas las imagenes\camina_iz_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\camina_iz.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\camina_iz_3.png")]

personaje_salta = [pygame.image.load(r"Imagenes\todas las imagenes\salta_de.png")]

perosnaje_salta_iz = girar_imagenes(personaje_salta, True, False)

enemigo_camina_derecha = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_gris_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_gris_2.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_gris_3.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_gris_4.png")]

enemigo_camina_izquierda = girar_imagenes(enemigo_camina_derecha, True, False)

enemigo_flotador = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_biss.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_biss.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_bisss.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_1_bisss.png")]

enemigo_lap = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\6.png")]


enemigo_escarabajo = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_bis.png"),
                      pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_bis.png"),
                      pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_biss.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_biss.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel1_biss.png"),]

enemigo_escarabajo_iz = girar_imagenes(enemigo_escarabajo, True, False)

enemigo_verde = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde.png"),
                 pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde.png"),
                 pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_2.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_2.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_verde_2.png")]

enemigo_rosa_img = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_nivel_2_bis.png")
                    
                    ]

proyectil_i = pygame.image.load(r"Imagenes\todas las imagenes\proyectil_super_de.png")

proyectil_enemigo = pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\5.png")

vida = [pygame.image.load(r"Imagenes\todas las imagenes\Vida.png"),
        pygame.image.load(r"Imagenes\todas las imagenes\Vida.png"),
        pygame.image.load(r"Imagenes\todas las imagenes\Vida.png")]

jefe_nivel_1 = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1.png"),
                pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1.png"),
                pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1_bis.png"),
                    pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\jefe_nivel_1_bis.png")]

premio_i = [pygame.image.load(r"Imagenes\todas las imagenes\premio.png")]

enemigo_premio = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_premio_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_premio_2.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\enemigo_premio.png")]

fondo_vidas = pygame.image.load(r"Imagenes\todas las imagenes\fondo_vidas.png")

fondo_puntos = pygame.image.load(r"Imagenes\todas las imagenes\fondo_puntos.png")

fondo_tiempo = pygame.image.load(r"Imagenes\todas las imagenes\fondo_tiempo.png")

plataforma_movil = pygame.image.load(r"Imagenes\todas las imagenes\plataforma_movil.png")

plataforma_movil_nivel_3 = pygame.image.load(r"Imagenes\todas las imagenes\plataforma_movil_nivel_3.png")

premio_ojo = [pygame.image.load(r"Imagenes\todas las imagenes\ojo.png")]

enemigo_bomba = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\bombas.png")]

mascota_jefe_a = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_11.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_11.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_11.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1111.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_1111.png")]

mascota_jefe = [pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2.png"),
                pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2.png"),
                pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_2222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_22222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_22222.png"),
                  pygame.image.load(r"Imagenes\todas las imagenes\enemigos_nivel_1\mascota_jefe_22222.png")
                  ]
mascota_jefe_b = girar_imagenes(mascota_jefe, True, False)

game_over = pygame.image.load(r"Imagenes\todas las imagenes\fondo_game_over.jpg")


puerta = [pygame.image.load(r"Imagenes\todas las imagenes\puerta.png")]

fuego = [pygame.image.load(r"Imagenes\todas las imagenes\fuego.png")]

pygame.mixer.init()
sonido_aparicion_akuji = pygame.mixer.Sound(r"musica\efectos_sonido\aparece_akuji.wav")
sonido_disparo_akuji = pygame.mixer.Sound(r"musica\efectos_sonido\disparo_akuji.wav")
sonido_disparo_enemigo = pygame.mixer.Sound(r"musica\efectos_sonido\disparo_enemigo.wav")
sonido_muerte_akuji = pygame.mixer.Sound(r"musica\efectos_sonido\muerte_akuji.wav")
sonido_muerte_enemigo = pygame.mixer.Sound(r"musica\efectos_sonido\muerte_enemigo.wav")
sonido_jefe = pygame.mixer.Sound(r"musica\efectos_sonido\sonido_jefe.wav")
sonido_premio = pygame.mixer.Sound(r"musica\efectos_sonido\sonido_premio.wav")

#pryectil_fantasma = pygame.image.load(r"Imagenes\todas las imagenes\bola_fuego_iz.png")