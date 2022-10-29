

import pygame as pg
import random 


Ancho = 800
Alto = 600

negro = (0, 0, 0)
blanco=(255,255,255)
verde=(0,255,0)

pg.init()
pg.mixer.init()
pantalla_principal = pg.display.set_mode((Ancho, Alto))
pg.display.set_caption("Futuplanet")
clock = pg.time.Clock()

#creamos una funcion draw_tex que nos permita al llamarla solo poner los parametros de la funcion y diuje

def pintar_texto(pantalla,texto,tamaño,centerx,centery):
    font=pg.font.SysFont("serif",tamaño)
    texto_pantalla=font.render(texto,True,blanco)
    texto_rect=texto_pantalla.get_rect()
    texto_rect.midtop= (centerx,centery)
    pantalla.blit(texto_pantalla,texto_rect)
    
def pintar_barra_energia(pantalla,centerx,centery,porcentaje):
    longitud_barra=100
    ancho_barra=10
    porcentaje_barra_allenar=(porcentaje/100)*longitud_barra
    borde=pg.Rect(centerx,centery,longitud_barra,ancho_barra)
    porcentaje_barra_allenar=pg.Rect(centerx,centery,porcentaje_barra_allenar,ancho_barra)
    pg.draw.rect(pantalla,verde,porcentaje_barra_allenar)
    pg.draw.rect(pantalla,negro,borde,2)

class Jugador(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("game/imagenes/nave.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centerx = Ancho // 2-300
        self.rect.centery = Alto//2
        
        self.vy=0
        self.energia_nave=100

    def update(self):
        
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
            
    def disparo(self):
        bala=Bala(self.rect.centerx,self.rect.centery)
        lista_objetos.add(bala)
        lista_balas.add(bala)
        disparo.play()
        
        

class Enemigos(pg.sprite.Sprite):
    def __init__(self):
         super().__init__()
        
         #self.image = pg.image.load("game/imagenes/ag.png").convert()
         self.image=random.choice(enemigos_imagenes)
         self.image.set_colorkey(negro)
        
         self.rect=self.image.get_rect()
         self.rect.centerx= random.randrange(0,900)
         #self.rect.centerx= random.randrange(300,900)
          
        # self.rect.centerx= random.randint(100,500) 
         self.rect.centery= random.randrange(100,500)
         self.vx=random.randint(1,4)
         self.vy=random.randint(1,4)
               
    def update(self):
        self.rect.centerx -= self.vx
        #self.rect.centery -= self.vy
        #se le suman 25  para aumentar el ancho de la pantalla, igualmente en el sentido -25
        if self.rect.right >Ancho+25 or self.rect.left<-25:
              self.rect.centerx= random.randint(0,800)
              #self.rect.centery= random.randrange(100,500)
              self.vx=random.randint(1,8)

                 
class Bala(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pg.image.load("game/imagenes/bala.png")
        self.image.set_colorkey(negro)
        self.rect=self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.vx=10
        
    def update(self):
        self.rect.centerx+=self.vx
        #if self.rect.left < 0:
         #    self.kill()
        #vamos a desaparcer las balasde las listas para que no me ocupe espacio de memoria
        

        #Creamos una lista vacia que nos permitio cargar las imagenes con el fin de que cuando salgan los asteroides se vean en tamaños diferentes             
enemigos_imagenes=[]
fotos_enemigos=["game/imagenes/a1.png","game/imagenes/a4.png","game/imagenes/a5.png","game/imagenes/a7.png"]             
#interamos sobre la lista enemigos y agregamos a la lista vacia la imagen que va correspondiendo
for imagen in fotos_enemigos:
    enemigos_imagenes.append(pg.image.load(imagen).convert())
		

fondo_pantalla=pg.image.load("game/imagenes/fondo.jpg").convert()
disparo=pg.mixer.Sound("game/sonido/burst fire.mp3")
sonido_explosicion=pg.mixer.Sound("game/sonido/explosion.wav")
pg.mixer.music.load("game/sonido/general.ogg")
pg.mixer.music.set_volume(0.1)
     
#Vamos a incluir todos los sprite que vamos creando        
lista_objetos = pg.sprite.Group()

#voy a crear variable que me permitra almacenar el grupo de  enemigos

lista_enemigos= pg.sprite.Group()
lista_balas=pg.sprite.Group()


jugador = Jugador()
lista_objetos.add(jugador)

for i in range (4):
    enemigo=Enemigos()
    lista_objetos.add(enemigo)
    lista_enemigos.add(enemigo)
    
puntaje=0
#la musica se va a reproducir durante todo el juego para eso es el loops=-1

pg.mixer.music.play(loops=-1)

movimiento_jugador = True
while  movimiento_jugador:
    clock.tick(60)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            movimiento_jugador = False
            
        elif evento.type==pg.KEYDOWN:
             if evento.key==pg.K_SPACE:
                  jugador.disparo()
    
    lista_objetos.update()
    #colisiones enemigo con  bala de un grupo contra otro grupo
    colisiones=pg.sprite.groupcollide(lista_enemigos,lista_balas,True,True)
    
    for choque in colisiones:
        puntaje+=1
        #sonido_explosicion.play()
        "creamos nuevamente los enemigos para que cuando me choquen aparezca nuevamente"
        enemigo=Enemigos()
        lista_objetos.add(enemigo)
        lista_enemigos.add(enemigo)  
 
    
    #comprobaremos las colisiones de los enemigos con el jugardor
    
    colisiones=pg.sprite.spritecollide(jugador,lista_enemigos,True)
    for choque in colisiones:
        jugador.energia_nave -=10
        enemigo=Enemigos()
        lista_objetos.add(enemigo)
        lista_enemigos.add(enemigo)
        if jugador.energia_nave<=0:
            movimiento_jugador=False
        

    pantalla_principal.blit(fondo_pantalla,(0,0))
    lista_objetos.draw(pantalla_principal)
    
    #puntaje
    pintar_texto(pantalla_principal,str(puntaje),40,Ancho//2,10)
    #vidas
    pintar_barra_energia(pantalla_principal,5,5,jugador.energia_nave)
   
    pg.display.flip()

pg.quit()


