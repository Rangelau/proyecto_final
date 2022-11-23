import random

import pygame as pg

Ancho = 800
Alto = 600

negro = (0, 0, 0)
blanco=(255,255,255)
verde=(0,255,0)

pg.init()
pg.mixer.init()
clock = pg.time.Clock()


#creamos una funcion draw_tex que nos permita al llamarla solo poner los parametros de la funcion y diuje

def pintar_texto(pantalla,texto,tamaño,centerx,centery):
    font=pg.font.SysFont("serif",tamaño)
    texto_pantalla=font.render(texto,True,blanco)
    texto_rect=texto_pantalla.get_rect()
    texto_rect.midtop= (centerx,centery)
    pantalla.blit(texto_pantalla,texto_rect)
    
def pintar_barra_vida(pantalla,centerx,centery,porcentaje):
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
        self.barra_vida=100

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
        disparo=pg.mixer.Sound("game/sonido/burst fire.mp3")
        disparo.play()
        
        

class Enemigos(pg.sprite.Sprite):
    def __init__(self):
         super().__init__()
        
         #self.image = pg.image.load("game/imagenes/ag.png").convert()
         self.image=random.choice(enemigos_imagenes)
         self.image.set_colorkey(negro)
        
         self.rect=self.image.get_rect()
         self.rect.centerx= random.randrange(400,900)
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

enemigos=pg.display.set_mode((400,900))
enemigos_imagenes=[]
fotos_enemigos=["game/imagenes/a1.png","game/imagenes/a4.png","game/imagenes/a5.png","game/imagenes/a7.png"]             
#interamos sobre la lista enemigos y agregamos a la lista vacia la imagen que va correspondiendo
for imagen in fotos_enemigos:
    enemigos_imagenes.append(pg.image.load(imagen).convert())
                 
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
        #   if self.rect.left < 0:
         #    self.kill()
        #vamos a desaparcer las balasde las listas para que no me ocupe espacio de memoria


class Explosion(pg.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = animacion_explosion[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.fotograma = 0 #esta variable es la que va a ir aumentando para que salga el valor de la imagen para ir dando la ilusión de la animacion
		self.actualizacion = pg.time.get_ticks()
		self.velocidad_explosion = 50 #velocidad de la explosion
        

	def update(self):
		tiempo_actualexplosion= pg.time.get_ticks()
		if tiempo_actualexplosion - self.actualizacion> self.velocidad_explosion:
                    self.actualizacion=tiempo_actualexplosion
                    self.fotograma += 1
                    if self.fotograma ==len(animacion_explosion):
                        self.kill()
                    else:
                        centery=self.rect.center
                        #centerx=self.rect.center
                        self.image=animacion_explosion[self.fotograma]
                        self.rect=self.image.get_rect()
                        self.rect.center=centery
                        #self.rect.center=centerx

#animacion explosiones

animacion_explosion=[]  		
for i in range (6):
    animacion= "game/imagenes/explo0{}.png".format(i)
    imagen=pg.image.load(animacion).convert()
    imagen.set_colorkey(negro) 
    img_tranf=pg.transform.scale(imagen,(70,70))
    animacion_explosion.append(img_tranf)


#Vamos a incluir todos los sprite que vamos creando        
lista_objetos = pg.sprite.Group()

#voy a crear variable que me permitra almacenar el grupo de  enemigos

lista_enemigos= pg.sprite.Group()
lista_balas=pg.sprite.Group()

"""
class Portada:
    def __init__(self,pantalla):
        self.pantalla_principal= pantalla
        
        self.imagenFondo=pg.image.load("game/imagenes/fondo_inicio.jpg")
        self.fuente=pg.font.Font("game/fuentes/Roboto-Medium.ttf",40)
        self.fuente1=pg.font.Font("game/fuentes/Roboto-Medium.ttf",25)

        pg.display.set_caption("Futuplanet")
        



    def bucle_principal(self):
        
        game_over = False
        
    
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True  

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
       
       

                    #self.pantalla_principal.fill(negro)

            self.pantalla_principal.blit(self.imagenFondo,(0,0)) 

            
            m1=self.fuente.render("MISIÓN A FUTUPLANET",True,blanco)  
            m2=self.fuente1.render("Tras meses de viaje en misión a futuplanet se interponen",True,blanco)
            m3=self.fuente1.render(" en tu camino tres cinturones de asteroides", True,blanco)
            m4=self.fuente1.render("que te dificultan el paso y amenazan con no dejarte pasar",True,blanco)
            m5=self.fuente1.render("intenta chocarlos para conseguir finalizar tu misión.",True,blanco)
            m6=self.fuente1.render("Pulsa 'ENTER' para empezar.",True,blanco)

            self.pantalla_principal.blit(m1,(200,135))
            self.pantalla_principal.blit(m2,(90,200))
            self.pantalla_principal.blit(m3,(170,235))
            self.pantalla_principal.blit(m4,(90,270))
            self.pantalla_principal.blit(m5,(120,305))
            self.pantalla_principal.blit(m6,(240,360))



            pg.display.flip()


#creamos un ventana para todo el juego, luego llamamos la clase pantalla de partida y le ponemos como parametro la ventana que creamos y del juego ejecutamos la funcion play
ventana_juego= pg.display.set_mode((Ancho,Alto))
juego=Portada(ventana_juego)
juego.bucle_principal()

"""

class Pantalla_de_partida:
    def __init__(self,pantalla):
        self.jugador=Jugador
        self.enemigo=Enemigos
        self.bala=Bala
        self.explosion=Explosion
        self.pantalla_principal=pantalla
        self.imagen_fondo=pg.image.load("game/imagenes/fondo.jpg").convert()
        self.sonido_explosion=pg.mixer.Sound("game/sonido/explosion.wav")
        #self.sonido_disparo=pg.mixer.Sound("game/sonido/burst fire.mp3") #crear sonido en la clase jugador y llmarlo
        self.fuente_puntaje=pg.font.Font("game/fuentes/Roboto-Medium.ttf",40)
        self.metronomo=clock
        self.num_vidas=3
        self.nivel_juego=1
        self.puntaje=0
        

    def play(self):

    
        self.num_vidas=3
        self.nivel_juego=1
        self.puntaje=0

        #pg.mixer.music.play(loops=-1)
        
        game_over = False
       

        while not game_over:
            self.metronomo.tick(60)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over=True

                if evento.type==pg.KEYDOWN:
                    if evento.key==pg.K_SPACE:
                        self.jugador()

            lista_objetos.update()

            colisiones=pg.sprite.groupcollide(lista_enemigos,lista_balas,True,True)
    
            for choque in colisiones:
                self.puntaje +=10
                if self.puntaje ==50:
                    self.nivel_juego+=1
                "creamos nuevamente los enemigos para que cuando me choquen aparezca nuevamente"

    #mensaje has ganado el primer nivel.
            self.pantalla_principal.blit(self.imagen_fondo,(0,0))
            m1=self.fuente.render("Has pasado el primer nivel de está misión",True,blanco)
            self.pantalla_principal.blit(m1,(200,135)) 

                self.enemigo=Enemigos()
                #agregar mas enemigos y con mas velocidad
                lista_objetos.add(self.enemigo)
                lista_enemigos.add(self.enemigo)   
        
            
            #comprobaremos las colisiones de los enemigos con el jugardor
            
            colisiones=pg.sprite.spritecollide(self.jugador,lista_enemigos,True)
            
            for choque in colisiones:
                self.num_vidas -=1 
                self.sonido_explosion.play()
                explosion=Explosion(choque.rect.center)
                lista_objetos.add(explosion)
                self.enemigo=Enemigos()
                lista_objetos.add(self.enemigo)
                lista_enemigos.add(self.enemigo)
                if self.num_vidas==0:
                    self.ganando=False
                    game_over=True

                if self.nivel_juego>3:
                    self.ganando=True
                    game_over=True

                    
            self.pantalla_principal.blit(self.imagen_fondo,(0,0))
            lista_objetos.draw(self.pantalla_principal)
            pintar_texto(self.pantalla_principal,str(self.puntaje), 40,Ancho//2,10)
            pintar_texto(self.pantalla_principal,str(self.num_vidas),5,5)

ventana_juego= pg.display.set_mode((Ancho,Alto))
juego=Pantalla_de_partida(ventana_juego)
juego.play()

    
"""
            
class Final_juego:
     def __init__(self,pantalla):
        self.pantalla_principal= pantalla
        self.ganando=3
        
        self.imagenFondo=pg.image.load("game/imagenes/fondo_inicio.jpg")
        self.fuente=pg.font.Font("game/fuentes/Roboto-Medium.ttf",40)
        self.fuente1=pg.font.Font("game/fuentes/Roboto-Medium.ttf",25)

        pg.display.set_caption("Fin de Misión")


     def bucle_principal(self):
      
        game_over=False
        while not game_over:



            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                    

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_n:
                        game_over= False
                        

                    if evento.key == pg.K_s:
                        game_over = False
                        
                self.pantalla_principal.fill(negro)
            
            historia_perdido = [
                "    No has conseguido llegar a Júpiter. Los cinturones",
                "   de asteroides han destruido tu nave. Pero has tenido",
                "   suerte y te han recogido unos chatarreros del espacio.",
                "  ¿Quieres volverlo a intentar a borde de una nueva nave?",
                "",
                "              Pulsa 's' para volverlo a intentar",
                "              Pulsa 'n' para salir del juego"]

            historia_ganado = [
                "  Has conseguido llegar a Júpiter y completar tu misión.",
                "  Los cinturones de asteroides no han conseguido pararte.",
                "       Te has convertido en un héroe del espacio.",
                "       ¿Quieres embarcarte en una nueva misión?",
                "", 
                "              Pulsa 's' para volver a jugar",
                "              Pulsa 'n' para salir del juego"]

            #si ganando es =true mostraria historia_ganando
            
            

            
            if self.ganando:
                historia=historia_ganado
            else:
                historia_perdido
            
            y=80
            for frase in historia:
                texto=self.fuente1.render(frase,True,blanco)
                self.pantalla_principal.blit(texto,(150,y))
                y+=80
            
            pg.display.flip()


#creamos un ventana para todo el juego, luego llamamos la clase pantalla de partida y le ponemos como parametro la ventana que creamos y del juego ejecutamos la funcion play
ventana_juego= pg.display.set_mode((Ancho,Alto))
juego=Final_juego(ventana_juego)
juego.bucle_principal()

"""


