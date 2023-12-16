"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : 
- soucoupe volante
- bonne pratique
"""

import tkinter as tk
from random import randint
from alien import Alien
from spaceship import Spaceship
from wall import Wall
from bullet import Bullet




# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:

    # méthode d'initialisation, crée les murs (objets), le vaisseau(objets), les aliens (liste)  
    #  game (=la fenetre), les rectangles (affichage graphique des objets)
    # comme des attributs pour l'objet Board
      
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
    # sort 3 matrices de 3 par 6 contenant des rectangles
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
        self.__bullet_cooldown = 2  # nombre de  tir que le joueur peut tirer entre chaque déplacement d'alien
        for i in range(5):
            if self.__alien_list[i][9].getx() > 0.95 : #limite au bord droit
                self.__direction_alien = -1
                
                for j in range(10):
                    self.__alien_list[i][j].move_y()
                    self.__alien_list[i][j].setx(1 - (9 - j) * 0.05)
                    
                        
            if self.__alien_list[i][0].getx() < 0.06: #limite au bord gauche
                self.__direction_alien = 1
                
                for j in range(10):
                    self.__alien_list[i][j].move_y()
                    self.__alien_list[i][j].setx(j * 0.05 + 0.01)
                     

        for i in range(5):
            for j in range(10):
                self.__alien_list[i][j].move_x( self.__direction_alien )
                self.__game.coords(self.__rec_alien_list[i][j], self.__alien_list[i][j].getx() * 820, self.__alien_list[i][j].gety() * 620, self.__alien_list[i][j].getx() * 820 + 30, self.__alien_list[i][j].gety() * 620 + 30)
                if self.__alien_list[i][j].getlife() == 1:
                    lower_alien = (i,j)
        
        if self.__alien_list[lower_alien[0]][lower_alien[1]].gety() > 0.95:
            self.__gameover = 1
            self.you_lose()
        
        else:
            self.__game.after(self.__speed, self.move_alien)
        
    
    
    # Méthode gérant les tirs du vaisseau et les déplacements du vaisseau
    # entree : objet et event 
    # sortie : déplacement et apparition de la balle, déplacement du vaisseau
    def key_pressed(self, event):    
        
        #Sous-méthode gérant 

        def spaceship_shoot():
            new_bullet = Bullet(self.__spaceship1.getx(), 0.9)
            rec_bullet = self.__game.create_rectangle(new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10, fill = 'white', outline = "white")
            
            def move_bullet():
                if new_bullet.getlife() == 1:
                    new_bullet.move_y(-1)
                    self.__game.coords(rec_bullet, new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10)
                    if new_bullet.gety() <= 0:
                        new_bullet.setlife(0)
                        self.__game.delete(rec_bullet)
                    else:
                        self.collision(new_bullet, rec_bullet, "spaceship")
                        self.__game.after(10, move_bullet)
            
            move_bullet()

        def move_spaceship1():
            self.__spaceship1.move(direction)
            self.__game.coords(self.__bottom_spaceship1, self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645)
            self.__game.coords(self.__top_spaceship1, self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635)


        if self.__gameover == 0:
            touche = event.keysym
            direction = 0
            if touche == "space":
                if self.__bullet_cooldown > 0:
                    spaceship_shoot()
                    self.__bullet_cooldown -= 1
            # print("We love M.Trouillot")
            elif touche == "Right" and self.__spaceship1.getx() < 0.98:
                direction = 1
                move_spaceship1()
            elif touche == "Left" and self.__spaceship1.getx() > 0.02:
                direction = -1
                move_spaceship1()
    
    
    # Méthode gérant la destruction des murs
    # entrée : objet, sortie: disparition d'un bloc du mur 
    
    def collision(self, bullet, rec_bullet, source):
        if self.__gameover == 0:
            (x1,y1,x2,y2) = self.__game.coords(rec_bullet) 
            x = (x2 + x1)/2
            y = (y2 + y1)/2
            
            for j in range(3):
                for k in range(3):
                    for l in range(6):
                        if self.__wall_list[j].get_state()[k][l] == 1:
                            coords = self.__game.coords(self.__rec_wall_list[j][k][l])
                            if x > coords[0] and y > coords[1] and x < coords[2] and y < coords[3]:
                                self.__wall_list[j].destroy(k, l)
                                self.__game.delete(self.__rec_wall_list[j][k][l])
                                self.__game.delete(rec_bullet)
                                bullet.setlife(0)


            if source == "spaceship":
                for i in range(5):
                    for j in range(10):
                        if self.__alien_list[i][j].getlife() == 1:
                            coords_alien = self.__game.coords(self.__rec_alien_list[i][j])
                            if (x1 > coords_alien[0] and y > coords_alien[1] and x1 < coords_alien[2] and y < coords_alien[3]) or (x2 > coords_alien[0] and y > coords_alien[1] and x2 < coords_alien[2] and y < coords_alien[3]):
                                self.__alien_list[i][j].setlife(0)
                                self.__game.delete(self.__rec_alien_list[i][j])
                                self.__game.delete(rec_bullet)
                                bullet.setlife(0)
                                self.__score += 20
                                self.__score_var.set("Score : " + str(self.__score))
                                self.__dead_alien += 1
                                print(self.__dead_alien)
                            
                        
            elif source == "alien":
                coords_spaceship = self.__game.coords(self.__bottom_spaceship1)
                if (x1 > coords_spaceship[0] and y > coords_spaceship[1] and x1 < coords_spaceship[2] and y < coords_spaceship[3]) or (x2 > coords_spaceship[0] and y > coords_spaceship[1] and x2 < coords_spaceship[2] and y < coords_spaceship[3]):
                    self.__spaceship1.damage()
                    self.__game.delete(rec_bullet)
                    bullet.setlife(0)
                    self.__life_var.set("Life : " + str(self.__spaceship1.getlife()))
                    if self.__spaceship1.getlife() == 0:
                        self.__gameover = 1
                        self.you_lose()
        

            if self.__dead_alien == 50:
                self.__speed -= 100
                self.__dead_alien = 0
                print(self.__rec_alien_list)
                self.create_alien()
        


    def tir_alien(self):
        if self.__gameover == 0:
            nbr = randint(1,4)
            if nbr == 1:
                i,j = randint(0,4),randint(0,9)
                if self.__alien_list[i][j].getlife() == 1:
                    new_bullet = Bullet(self.__alien_list[i][j].getx(), self.__alien_list[i][j].gety())
                    rec_bullet = self.__game.create_rectangle(new_bullet.getx() * 820, new_bullet.gety() * 650 + 30, new_bullet.getx() * 820 + 5, new_bullet.gety() * 650 + 40, fill = 'white', outline = "white")
                    
                    def move_bullet():
                        if new_bullet.getlife() == 1:
                            new_bullet.move_y(1)
                            self.__game.coords(rec_bullet, new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10)
                            if new_bullet.gety() <= 0:
                                new_bullet.setlife(0)
                                self.__game.delete(rec_bullet)
                            else:
                                self.collision(new_bullet, rec_bullet, "alien")
                                self.__game.after(10, move_bullet)
                    
                    move_bullet()
            
            self.__game.after(int(self.__speed/4), self.tir_alien)


    def you_lose(self):
        self.__game.delete('all')
        self.__game.create_text(425, 100, text = "GAME OVER !", font  = ("Times New Roman", 15, "bold"), fill = "white")
        self.__game.create_text(425, 200, text = "Score : " + str(self.__score), font  = ("Times New Roman", 15, "bold"), fill = "white")
    
