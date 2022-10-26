import pygame as pg

Ancho = 800
Alto = 600

negro = (0, 0, 0)

pg.init()
pg.mixer.init()
pantalla_principal = pg.display.set_mode((Ancho, Alto))
pg.display.set_caption("Futuplanet")
clock = pg.time.Clock()

class Jugador(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("game/imagenes/nave.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centerx = Ancho // 2
        self.rect.centery = Alto//2
        self.w=100
        self.h=56
        
        self.vx = 0
        self.vy=0

    def update(self):
        self.speed_x = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_DOWN]:
            self.vy = 5
        if keystate[pg.K_UP]:
            self.vy = -5
            
        self.rect.centery +=self.vy
        
        if self.rect.bottom > Alto:
            self.rect.bottom = Alto
        if self.rect.top< 0:
            self.rect.top = 0
        
        

lista_objetos = pg.sprite.Group()


jugador = Jugador()
lista_objetos.add(jugador)



movimiento_jugador = True
while movimiento_jugador:
  
    clock.tick(60)

    for evento in pg.event.get():
      
        if evento.type == pg.QUIT:
            movimiento_jugador = False
        

    # 
    lista_objetos.update()


    pantalla_principal.fill(negro)
    lista_objetos.draw(pantalla_principal)
   
    pg.display.flip()

pg.quit()


