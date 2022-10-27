
import pygame as pg
import random 


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
        self.rect.centerx = Ancho // 2-300
        self.rect.centery = Alto//2
        self.w=100
        self.h=56
        
        self.vx = 0
        self.vy=0

    def update(self):
        self.vx = 0
        self.vy=0
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

class Enemigos(pg.sprite.Sprite):
    def __init__(self,w=40,h=40):
         super().__init__()
         self.w=w
         self.h=h
         self.image = pg.image.load("game/imagenes/a6.png").convert()
         self.image.set_colorkey(negro)
        
         self.rect=self.image.get_rect()
         self.rect.centerx= random.randrange(Ancho+self.rect.left)
         self.rect.centery= random.randrange(100,500)
         self.vx=random.randrange(1,10)
         
         
    def update(self):
        self.rect.centerx -= self.vx
        
        
        
        

lista_objetos = pg.sprite.Group()

#voy a crear variable que me permitra almacenar el grupo de  enemigos

lista_enemigos= pg.sprite.Group()


jugador = Jugador()
lista_objetos.add(jugador)

for i in range (8):
    enemigo=Enemigos()
    lista_objetos.add(enemigo)
    lista_enemigos.add(enemigo)



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


