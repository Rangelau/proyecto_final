import pygame, random

Ancho = 800
Alto = 600

negro = (0, 0, 0)

pygame.init()
pygame.mixer.init()
pantalla_principal = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Futuplanet")
clock = pygame.time.Clock()

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("game/imagenes/nave.png").convert()
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
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.vx = -5
        if keystate[pygame.K_UP]:
            self.vx = 5
            
        self.rect.centerx +=self.vx
        
        if self.rect.right > Ancho:
            self.rect.right = Ancho
        if self.rect.left < 0:
            self.rect.left = 0
        
        

lista_objetos = pygame.sprite.Group()


jugador = Jugador()
lista_objetos.add(jugador)


# Game Loop
movimiento_jugador = True
while movimiento_jugador:
    # Keep loop running at the right speed
    clock.tick(60)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            movimiento_jugador = False
        

    # Update
    lista_objetos.update()

    #Draw / Render
    pantalla_principal.fill(negro)
    lista_objetos.draw(pantalla_principal)
    # *after* drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()


"""
Ancho = 800
Alto = 600

negro = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Futuplanet")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("game/imagenes/nave.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centerx = Ancho // 2
        self.rect.centery = Alto//2
        self.w=100
        self.h=56
        
        self.speed_x = 0
        self.speed_y=0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.speed_x = -5
        if keystate[pygame.K_UP]:
            self.speed_x = 5
            
        self.rect.centerx +=self.speed_x
        
        if self.rect.right > Ancho:
            self.rect.right = Ancho
        if self.rect.left < 0:
            self.rect.left = 0
        
        

all_sprites = pygame.sprite.Group()


player = Player()
all_sprites.add(player)


# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(60)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        

    # Update
    all_sprites.update()

    #Draw / Render
    screen.fill(negro)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()
"""