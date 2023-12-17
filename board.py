"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : fini
"""

from random import randint
from alien import Alien
from spaceship import Spaceship
from wall import Wall
from bullet import Bullet




# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:

    # méthode d'initialisation  
    def __init__(self, game, score_var, life_var, difficulty):
        # définition des variables utiles
        self.__game = game
        self.__spaceship1 = Spaceship()
        self.__wall_list = [Wall(), Wall(), Wall()]
        self.__bottom_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645, fill = 'green', outline = "green")
        self.__top_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635, fill = 'green', outline = "green")
        self.__alien_list = []
        self.__rec_alien_list = []
        self.__dead_alien = 0
        self.__direction_alien = 1
        self.__speed = int(2000 / difficulty)
        self.__score = 0
        self.__score_var = score_var
        self.__life_var = life_var
        self.__bullet_cooldown = 0
        self.__gameover = 0
        self.__rec_wall_list = []
        
    # méthode créant des aliens au début de la partie et au début de chaque vague
    # utilise alien_list, rec_alien_list, direction_alien et la class Alien
    # sort une matrice de 5 par 10 alien et des rectangles associées
    def create_alien(self):
        self.__alien_list = []
        self.__rec_alien_list = []
        self.__direction_alien = 1
        for i in range(5):
            self.__alien_list.append([])
            self.__rec_alien_list.append([])
            for j in range(10):
                self.__alien_list[i].append( Alien( 0.12 + j * 0.05, 0.05 + i * 0.07))
                self.__rec_alien_list[i].append(self.__game.create_rectangle(self.__alien_list[i][j].getx() * 820, self.__alien_list[i][j].gety() * 620, self.__alien_list[i][j].getx() * 820 + 30, self.__alien_list[i][j].gety() * 620 + 30, fill = 'green', outline = 'green'))


    # méthode créant des murs au début de la partie
    # utilise rec_wall_list
    # sortie :  3 matrices de 3 par 6 contenant des rectangles
    def create_wall(self):
        for j in range(3):
            self.__rec_wall_list.append([])
            for k in range(3):
                self.__rec_wall_list[j].append([])
                for l in range(6):
                    self.__rec_wall_list[j][k].append(self.__game.create_rectangle(170 + j*200 + l*20, 450 + k*20, 190 + j*200 + l*20, 470 + k*20, fill = 'green', outline = "black"))



    # méthode permettant la gestion des déplacements des aliens et finis la partie quand les aliens sont en bas de page.
    # cette méthode utilise d'autres méthodes (getx, move_x, move_y) propre à l'objet  
    # entrée: l'objet
    # sortie: un déplacement des alien (déplacement d'objets) ou un écran de fin de partie si les aliens sont en bas de pages.
    
    def move_alien(self):
        if self.__gameover == 0:
            # nombre de  tir que le joueur peut tirer entre chaque déplacement d'alien
            self.__bullet_cooldown = 2  
            
            
            for i in range(5):
                
                # quand ils atteignent la limite au bord droit, ils changent de direction: 
                if self.__alien_list[i][9].getx() > 0.95 :
                    self.__direction_alien = -1
                    
                    for j in range(10):
                        self.__alien_list[i][j].move_y()
                        self.__alien_list[i][j].setx(1 - (9 - j) * 0.05)
                        
                # de même pour la limite au bord gauche:           
                if self.__alien_list[i][0].getx() < 0.06: 
                    self.__direction_alien = 1
                    
                    for j in range(10):
                        self.__alien_list[i][j].move_y()
                        self.__alien_list[i][j].setx(j * 0.05 + 0.01)
                        
            # cas où les aliens sont entre l'intervalle autorisé de l'écran,
            # ils se déplacent dans la dernière direction donnée
            for i in range(5):
                for j in range(10):
                    self.__alien_list[i][j].move_x( self.__direction_alien )
                    self.__game.coords(self.__rec_alien_list[i][j], self.__alien_list[i][j].getx() * 820, self.__alien_list[i][j].gety() * 620, self.__alien_list[i][j].getx() * 820 + 30, self.__alien_list[i][j].gety() * 620 + 30)
                    if self.__alien_list[i][j].getlife() == 1:
                        lower_alien = (i,j) # indices de l'alien le plus bas
            
            
            # si les aliens arrivent en bas de la zone autorisée alors le joueur a perdu
            if self.__alien_list[lower_alien[0]][lower_alien[1]].gety() > 0.95:
                self.__gameover = 1
                self.you_lose()
            # autrement, on actualise le jeu
            else:
                self.__game.after(self.__speed, self.move_alien)
        
    
    
    # Méthode générale gérant les tirs du vaisseau et les déplacements du vaisseau
    # entree : objet et event (appui sur la touche espace)
    # sortie : déplacement et apparition de la balle, déplacement du vaisseau
    
    def key_pressed(self, event):    
        
        # Méthode gérant les tirs du vaisseau
        # entree : aucune
        # sortie : création d'une balle en provenance du vaisseau
        def spaceship_shoot():
            new_bullet = Bullet(self.__spaceship1.getx(), 0.9)
            rec_bullet = self.__game.create_rectangle(new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10, fill = 'white', outline = "white")
            
            # Méthode gérant le déplacement de la balle venant du vaisseau
            # entrée: aucune
            # sortie: déplacement de la balle en fonction de sa position et d'une éventuelle collsisison
            def move_bullet():
                
                # On exécute des changements seulement si la balle est encore en vie
                if new_bullet.getlife() == 1:
                    new_bullet.move_y(-1)
                    self.__game.coords(rec_bullet, new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10)
                    
                    # si la balle dépasse la zone autorisé de l'écran, elle disparaît
                    if new_bullet.gety() <= 0:
                        new_bullet.setlife(0)
                        self.__game.delete(rec_bullet)
                    
                    # autrement, on évalue une possible collision et on actualise le jeu
                    else:
                        self.collision(new_bullet, rec_bullet, "spaceship")
                        self.__game.after(10, move_bullet)
            
            move_bullet()


        # Méthode gérant le déplacement du vaisseau
        # entrée: aucune
        # sortie: déplacement ou blocage du vaisseau en fonction de sa position
        def move_spaceship1():
            self.__spaceship1.move(direction)
            self.__game.coords(self.__bottom_spaceship1, self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645)
            self.__game.coords(self.__top_spaceship1, self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635)

        # On exécute des changements seulement si le joueur n'a pas perdu
        if self.__gameover == 0:
            touche = event.keysym
            direction = 0
            # si on détecte un appui sur la touche espace, alors le vaisseau tire
            if touche == "space":
                if self.__bullet_cooldown > 0:
                    spaceship_shoot()
                    self.__bullet_cooldown -= 1
            # si on détecte un appui sur la touche flèche droite, le vaisseau va à droite
            elif touche == "Right" and self.__spaceship1.getx() < 0.98:
                direction = 1
                move_spaceship1()
            # de même pour la touche gauche
            elif touche == "Left" and self.__spaceship1.getx() > 0.02:
                direction = -1
                move_spaceship1()
    
    
    # Méthode gérant les collisions balle/mur ou balle/alien
    # entrée : self, l'objet "bullet", l'objet "rec_bullet", et une source du tir 
    # sortie: disparition d'un bloc du mur ou disparition d'un alien ou retrait d'une vie
    #         pour le joueur, changement du score
    
    def collision(self, bullet, rec_bullet, source):
        
        # On éxcecute des changements que si le joueur n'a pas perdu
        if self.__gameover == 0:
            (x1,y1,x2,y2) = self.__game.coords(rec_bullet) 
            x = (x2 + x1) / 2
            y = (y2 + y1) / 2
            
            # Dans le cas d'un tir alien:
            # on parcourt la liste des briques du mur
            for j in range(3):
                for k in range(3):
                    for l in range(6):
                        # si la brique est encore encore en vie
                        if self.__wall_list[j].get_state()[k][l] == 1:
                            coords = self.__game.coords(self.__rec_wall_list[j][k][l])
                            # et qu'il y a collision, alors elle disparaît:
                            if x > coords[0] and y > coords[1] and x < coords[2] and y < coords[3]:
                                self.__wall_list[j].destroy(k, l)
                                self.__game.delete(self.__rec_wall_list[j][k][l])
                                self.__game.delete(rec_bullet)
                                bullet.setlife(0)

            # si le tir provient du vaisseau vers un alien:
            # on parcourt la liste des aliens
            if source == "spaceship":
                for i in range(5):
                    for j in range(10):
                        
                        # si l'alien est encore en vie
                        if self.__alien_list[i][j].getlife() == 1:
                            coords_alien = self.__game.coords(self.__rec_alien_list[i][j])
                            
                            # et qu'il  a collision, alors lui et la balle disparaîssent:
                            if (x1 > coords_alien[0] and y > coords_alien[1] and x1 < coords_alien[2] and y < coords_alien[3]) or (x2 > coords_alien[0] and y > coords_alien[1] and x2 < coords_alien[2] and y < coords_alien[3]):
                                self.__alien_list[i][j].setlife(0)
                                self.__game.delete(self.__rec_alien_list[i][j])
                                self.__game.delete(rec_bullet)
                                bullet.setlife(0)
                                self.__score += 20
                                self.__score_var.set("Score : " + str(self.__score))
                                self.__dead_alien += 1
                                
                            
            # cas du tir alien vers le vaisseau:        
            elif source == "alien":
                coords_spaceship = self.__game.coords(self.__bottom_spaceship1)
                # s'il y a collision entre le tir et le vaisseau, on retire une vie, et efface la balle.
                if (x1 > coords_spaceship[0] and y > coords_spaceship[1] and x1 < coords_spaceship[2] and y < coords_spaceship[3]) or (x2 > coords_spaceship[0] and y > coords_spaceship[1] and x2 < coords_spaceship[2] and y < coords_spaceship[3]):
                    self.__spaceship1.damage()
                    self.__game.delete(rec_bullet)
                    bullet.setlife(0)
                    self.__life_var.set("Life : " + str(self.__spaceship1.getlife()))
                    
                    # si le joueur n'a plus de vie, il perd, appel de you_lose
                    if self.__spaceship1.getlife() == 0:
                        self.__gameover = 1
                        self.you_lose()
        
            # si il n'y a plus d'aliens, on en fait réapparaître appel de create_alien
            if self.__dead_alien == 50:
                self.__speed -= 100
                self.__dead_alien = 0
                self.create_alien()
        

    # Méthode gérant les tirs d'un alien.
    # entree : l'objet
    # sortie : un tir provenant d'un alien
    
    def tir_alien(self):
        # On exécute des changement seulement si le joueur n'a pas perdu.
        if self.__gameover == 0:
            # Choix aléatoire d'un instant pour tirer
            nbr = randint(1,4)
            
            if nbr == 1:
                # choix aléatoire d'un alien sur une ligne et sur une colonne
                i,j = randint(0,4),randint(0,9)
                
                # On le fait tirer seulement si il est toujours en vie
                if self.__alien_list[i][j].getlife() == 1:
                    new_bullet = Bullet(self.__alien_list[i][j].getx(), self.__alien_list[i][j].gety())
                    rec_bullet = self.__game.create_rectangle(new_bullet.getx() * 820, new_bullet.gety() * 650 + 30, new_bullet.getx() * 820 + 5, new_bullet.gety() * 650 + 40, fill = 'white', outline = "white")
                    
                    # Sous-méthode gérant le déplacement d'une balle provenant d'un alien
                    # entrée: aucune
                    # sortie: déplacement ou non de la balle en fonction d'une éventuelle collision ou de sa position.
                    
                    def move_bullet():
                        
                        # On exécute des changements seulement si la balle est en vie
                        if new_bullet.getlife() == 1:
                            new_bullet.move_y(1)
                            self.__game.coords(rec_bullet, new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10)
                            
                            # si la balle est hors de la zone autorisée de l'écran, alors elle disparaît
                            if new_bullet.gety() <= 0:
                                new_bullet.setlife(0)
                                self.__game.delete(rec_bullet)
                            # autrement, on vérifie qu'il n'y a pas de collision et on actualise le jeu
                            else:
                                self.collision(new_bullet, rec_bullet, "alien")
                                self.__game.after(10, move_bullet)
                    
                    move_bullet()
            
            self.__game.after(int(self.__speed/4), self.tir_alien)

    
    # Méthode gérant le cas où le joueur n'a plus de vie
    # entrée: l'objet
    # sortie: effacement de tout ce qu'il y a sur la partie jeur, affichage de "GAME OVER !" et du score

    def you_lose(self):
        self.__game.delete('all')
        self.__game.create_text(425, 100, text = "GAME OVER !", font  = ("Times New Roman", 15, "bold"), fill = "white")
        self.__game.create_text(425, 200, text = "Score : " + str(self.__score), font  = ("Times New Roman", 15, "bold"), fill = "white")
    
    
    # Méthode permettant de modifier la valeur de la variable gameover
    # entrée : self
    # sortie : modification de la variable gameover
    def set_gameover(self, value):
        self.__gameover = value
