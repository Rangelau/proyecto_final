"""

    #eventos

    def bucle_priciapl(self):

        en_juego=True
        while en_juego:
            num_vidas=3
            nivel_juego=1

            partida=False
            inicio=True

            while inicio:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        inicio = False
                        en_juego = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            inicio = False
                            partida = True

                self.pantalla_principal.fill(negro)

                mensaje_bienvenida = [
                    "                      MISIÓN A FUTUPLANET",
                    "     Tras meses de viaje en misión a FUTUPLANET se",
                    "    interponen en tu camino tres cinturones de asteroides",
                    "  que te dificultan el paso y amenazan con no dejarte pasar.",
                    "   Intenta Chocarlos para conseguir finalizar tu misión.",
                    "",
                    "                Pulsa 'ENTER' para empezar"
                    ]
                
                for frase in mensaje_bienvenida:
                    bienvenida=self.fuente.render(frase,True,blanco)  
                    self.pantalla_principal.blit(bienvenida,(150,80))

                pg.display.update()



        while partida:
            final_juego=False
            self.enemigos=Enemigos
            self.enemigos=nivel_juego*2

        puntaje=0

        pg.mixer.music.play(loops=-1)
        
        nivel_juego=True

        while nivel_juego:
            metronomo.tick(60)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    nivel_juego = False
                    partida=False
                    en_juego=False

                if evento.type==pg.KEYDOWN:
                    if evento.key==pg.K_SPACE:
                        jugador.disparo()
    
            lista_objetos.update()

            colisiones=pg.sprite.groupcollide(lista_enemigos,lista_balas,True,True)
    
            for colision in colisiones:
                puntaje +=10
                if puntaje ==50:
                    nivel_juego+=1
                "creamos nuevamente los enemigos para que cuando me choquen aparezca nuevamente"
                enemigo=Enemigos()
                lista_objetos.add(enemigo)
                lista_enemigos.add(enemigo)   
        
            
            #comprobaremos las colisiones de los enemigos con el jugardor
            
            colisiones=pg.sprite.spritecollide(jugador,lista_enemigos,True)
            
            for choque in colisiones:
                num_vidas -=1 
                sonido_explosicion.play()
                explosion=Explosion(choque.rect.center)
                lista_objetos.add(explosion)
                enemigo=Enemigos()
                lista_objetos.add(enemigo)
                lista_enemigos.add(enemigo)
                if num_vidas==0:
                    ganando=False
                    final_juego=True

                if nivel_juego>3:
                    ganando=True
                    final_juego=True

                    
            self.pantalla_principal.blit(fondo_pantalla,(0,0))
            lista_objetos.draw(self.pantalla_principal)

            pintar_texto(self.pantalla_principal,str(nivel_juego),40,(760,10))
            pintar_texto(self.pantalla_principal,str(num_vidas),40,(40,10))
            pintar_texto(self.pantalla_principal,str(puntaje),40,Ancho//2,10)

            pg.display.flip()

        while final_juego:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    final_juego = False
                    partida=False
                    en_juego=False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_n:
                        final_juego = False
                        partida = False
                        en_juego = False

                    if event.key == pg.K_s:
                        final_juego = False
                        partida = False
                    
                    
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

            if ganando:
                historia = historia_ganado
            else:
                historia = historia_perdido

           
            for frase in historia:
                
                texto = pintar_texto(self.pantalla_principal,str(frase),20,150,80)
                pg.display.flip()
               
partida=Inicio_juego()
pg.quit()




        while partida:
            final_juego=False
            self.enemigos=Enemigos
            self.enemigos=nivel_juego*2

        puntaje=0

        pg.mixer.music.play(loops=-1)
        
        nivel_juego=True

        while nivel_juego:
            metronomo.tick(60)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    nivel_juego = False
                    partida=False
                    en_juego=False

                if evento.type==pg.KEYDOWN:
                    if evento.key==pg.K_SPACE:
                        jugador.disparo()
    
            lista_objetos.update()

            colisiones=pg.sprite.groupcollide(lista_enemigos,lista_balas,True,True)
    
            for colision in colisiones:
                puntaje +=10
                if puntaje ==50:
                    nivel_juego+=1
                "creamos nuevamente los enemigos para que cuando me choquen aparezca nuevamente"
                enemigo=Enemigos()
                lista_objetos.add(enemigo)
                lista_enemigos.add(enemigo)   
        
            
            #comprobaremos las colisiones de los enemigos con el jugardor
            
            colisiones=pg.sprite.spritecollide(jugador,lista_enemigos,True)
            
            for choque in colisiones:
                num_vidas -=1 
                sonido_explosicion.play()
                explosion=Explosion(choque.rect.center)
                lista_objetos.add(explosion)
                enemigo=Enemigos()
                lista_objetos.add(enemigo)
                lista_enemigos.add(enemigo)
                if num_vidas==0:
                    ganando=False
                    final_juego=True

                if nivel_juego>3:
                    ganando=True
                    final_juego=True

                    
            self.pantalla_principal.blit(fondo_pantalla,(0,0))
            lista_objetos.draw(self.pantalla_principal)

            pintar_texto(self.pantalla_principal,str(nivel_juego),40,(760,10))
            pintar_texto(self.pantalla_principal,str(num_vidas),40,(40,10))
            pintar_texto(self.pantalla_principal,str(puntaje),40,Ancho//2,10)

            pg.display.flip()

        while final_juego:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    final_juego = False
                    partida=False
                    en_juego=False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_n:
                        final_juego = False
                        partida = False
                        en_juego = False

                    if event.key == pg.K_s:
                        final_juego = False
                        partida = False
                    
                    
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

            if ganando:
                historia = historia_ganado
            else:
                historia = historia_perdido

           
            for frase in historia:
                
                texto = pintar_texto(self.pantalla_principal,str(frase),20,150,80)
                pg.display.flip()
               

pg.quit()
"""