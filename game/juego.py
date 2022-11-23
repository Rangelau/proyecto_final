

import pygame as pg

from game.entidades import Alto,Ancho,Inicio_juego

class Contolador:
    def __init__(self):
        pantalla_principal= pg.display.set_mode((Ancho,Alto))
        clock = pg.time.Clock()

        self.pantallas=[Inicio_juego]
        self.inicio_juego=Inicio_juego(pantalla_principal)

c=Contolador()
