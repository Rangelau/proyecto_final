
from json import load
from msilib.schema import Font
from tkinter import font
import pygame as pg
import random 


Ancho = 800
Alto = 600

negro = (0, 0, 0)
blanco=(255,255,255)

pg.init()
pg.mixer.init()
pantalla_principal = pg.display.set_mode((Ancho, Alto))
pg.display.set_caption("Futuplanet")
clock = pg.time.Clock()

#creamos una funcion draw_tex que nos permita al llamarla solo poner los parametros de la funcion y diuje

def pintar_texto(pantalla,texto,tamaño,centerx,centery):
    font=pg.font.Font("game/fuentes/thevil.ttf",tamaño)
    texto_pantalla=font.render(texto,True,blanco)
    texto_rect=texto_pantalla.get_rect()
    texto_rect.midtop= (centerx,centery)
    pantalla.blit(texto_pantalla,texto_rect)

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
    def __init__(self):
         super().__init__()
        
         #self.image = pg.image.load("game/imagenes/ag.png").convert()
         self.image=random.choice(enemigos_imagenes)
         self.image.set_colorkey(negro)
        
         self.rect=self.image.get_rect()
         self.rect.centerx= random.randint(100,500)
         self.rect.centery= random.randint(100,500)
         self.vx=random.randint(1,5)
         self.vy=random.randint(1,5)
         
         
         
         
         
    def update(self):
        self.rect.centerx -= self.vx
        #self.rect.centery -= self.vy
        #se le suman 25  para aumentar el ancho de la pantalla, igualmente en el sentido -25
        if self.rect.right >Ancho+25 or self.rect.left<-25:
              self.rect.centerx= random.randint(0,800)
              #self.rect.centery= random.randrange(100,500)
              self.vx=random.randrange(1,3)
              
#Creamos una lista vacia que nos permitio cargar las imagenes con el fin de que cuando salgan los asteroides se vean en tamaños diferentes             
enemigos_imagenes=[]
fotos_enemigos=["game/imagenes/ag.png","game/imagenes/ag1.png","game/imagenes/ag2.png","game/imagenes/ag3.png"]             
#interamos sobre la lista enemigos y agregamos a la lista vacia la imagen que va correspondiendo
for img in fotos_enemigos:
    enemigos_imagenes.append(pg.image.load(img).convert())


fondo_pantalla=pg.image.load("game/imagenes/fondo.jpeg")
     
#Vamos a incluir todos los sprite que vamos creando        
lista_objetos = pg.sprite.Group()

#voy a crear variable que me permitra almacenar el grupo de  enemigos

lista_enemigos= pg.sprite.Group()


jugador = Jugador()
lista_objetos.add(jugador)

for i in range (8):
    enemigo=Enemigos()
    lista_objetos.add(enemigo)
    lista_enemigos.add(enemigo)
    
vidas=5

movimiento_jugador = True
while  movimiento_jugador:
  
    clock.tick(60)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            movimiento_jugador = False
        
    lista_objetos.update()
    
    #comprobaremos las colisiones de los enemigos con el jugardor
    
    colisiones=pg.sprite.spritecollide(jugador,lista_enemigos,True)
    
    #if jugador==colisiones:
    #    vidas -=1

    pantalla_principal.blit(fondo_pantalla,(0,0))
    lista_objetos.draw(pantalla_principal)
    
    #vidas
    pintar_texto(pantalla_principal,str(vidas),40,Ancho//2,10)
   
    pg.display.flip()

pg.quit()


