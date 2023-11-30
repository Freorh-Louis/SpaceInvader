"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : 
- affichage et destruction des murs
- hitbox de tout les objets (à finir)
- collisions des bullets
- gestion de fin de partie
"""

import tkinter as tk
from alien import Alien
from spaceship import Spaceship
from wall import Wall
from bullet import Bullet



# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:

    # méthode d'initialisation, crée les murs (objets), le vaisseau(objets), les aliens (liste)  
    # , game (=la fenetre), les rectangles (affichage graphique des objets)
    # comme des attributs pour l'objet Board
      
    def __init__(self, game):
        self.__game = game
        self.__spaceship1 = Spaceship()
        self.__wall_list = [Wall(), Wall(), Wall()]
        self.__direction_alien = 1
        self.__alien_list = []
        self.__bottom_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645, fill = 'green', outline = "green")
        self.__top_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635, fill = 'green', outline = "green")
        
        self.__rec_list = []
        
        for i in range(12):
            if i <= 5:
                self.__alien_list.append( Alien( 0.12 + i * 0.05, 0.1 + 0.05))
            
            if i > 5 :
                self.__alien_list.append( Alien( 0.12 + (i-6) * 0.05, 0.22))
            
            self.__rec_list.append(self.__game.create_rectangle(self.__alien_list[i].getx() * 820, self.__alien_list[i].gety() * 620, self.__alien_list[i].getx() * 820 + 30, self.__alien_list[i].gety() * 620 + 30, fill = 'green', outline = 'green'))
    
        self.__rec_wall_list = []
        for j in range(3):
            self.__rec_wall_list.append([])
            for k in range(3):
                self.__rec_wall_list[j].append([])
                for l in range(6):
                    self.__rec_wall_list[j][k].append(self.__game.create_rectangle(170 + j*200 + l*20, 450 + k*20, 180 + j*200 + l*20, 460 + k*20, fill = 'green', outline = "green"))


    # méthode donnant le centre de gravité de l'objet, en vue de gérer les collisions
    # entrée : un objet, sortie: centre de gravité( tableau de valeurs réelles)
    def hitbox(self, objet):
        (x1,y1,x2,y2) = self.__game.coords(objet) 
        return [(x2-x1)/2,(y1-y2)/2]
    


    # méthode permettant la gestion des déplacements des aliens, 
    # cette méthode utilise d'autres méthodes (getx, move_x, move_y) propre à l'objet  
    # entrée:l'objet, sortie: un déplacement des alien (déplacement d'objets)

    def move_alien(self):
        global direction_alien
        
        n = len(self.__alien_list)

        if self.__alien_list[n -1].getx() > 0.9:
            direction_alien = -1
            
            for i in range(n):
                
                self.__alien_list[i].move_y()
            
            for i in range(n-1, -1 ,-1):
                print(i)
                if i >= 6:
                    self.__alien_list[i].setx(0.90 - (n-i-1) * 0.05)
                    print(0.90 - ((n -i )* 0.05))
            
                else:
                    self.__alien_list[i].setx(0.90 - (n -(i + 5)) * 0.05)
        
        elif self.__alien_list[0].getx() < 0.1:
            direction_alien = 1
            

            for i in range(n):
                self.__alien_list[i].move_y()
            

                
        
        for i in range(n):
            self.__alien_list[i].move_x(direction_alien)
            self.__game.coords(self.__rec_list[i], self.__alien_list[i].getx() * 820, self.__alien_list[i].gety() * 620, self.__alien_list[i].getx() * 820 + 30, self.__alien_list[i].gety() * 620 + 30)
        
        self.__game.after(1000, self.move_alien)
        
    
    def get_game(self):
        return self.__game
    
    def key_pressed(self, event):    
        def spaceship_shoot():
            new_bullet = Bullet(self.__spaceship1.getx(), 0.9)
            rec_bullet = self.__game.create_rectangle(new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10, fill = 'green', outline = "green")
            
            def move_bullet():
                new_bullet.move_y(-1)
                self.__game.coords(rec_bullet, new_bullet.getx() * 820 + 12, new_bullet.gety() * 650, new_bullet.getx() * 820 + 17, new_bullet.gety() * 650 + 10)
                if new_bullet.gety() <= 0:
                    self.__game.delete(rec_bullet)
                else:
                    self.__game.after(10, move_bullet)
                    self.destroy_wall(rec_bullet)

                
            move_bullet()

        def move_spaceship1():
            self.__spaceship1.move(direction)
            self.__game.coords(self.__bottom_spaceship1, self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645)
            self.__game.coords(self.__top_spaceship1, self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635)

        touche = event.keysym
        direction = 0
        if touche == "space":
            spaceship_shoot()
        # print("We love M.Trouillot")
        elif touche == "Right" and self.__spaceship1.getx() < 0.98:
            direction = 1
            move_spaceship1()
        elif touche == "Left" and self.__spaceship1.getx() > 0.02:
            direction = -1
            move_spaceship1()
    
    def destroy_wall(self, bullet):
        (x1,y1,x2,y2) = self.__game.coords(bullet) 
        hitbox = (x2 + x1)/2
        for j in range(3):
            for k in range(3):
                for l in range(6):
                    coords = self.__game.coords(self.__rec_wall_list[j][k][l])
                    if coords[0] > hitbox and coords[1] > hitbox and coords[2] < hitbox and coords[3] < hitbox:
                        # self.__rec_wall_list[j][k][l].destroy(j, k)
                        self.__game.delete(self.__rec_wall_list[j][k][l])
                        self.__game.delete(bullet)
                        