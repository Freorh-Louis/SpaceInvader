"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : 
- affichage(image) et mvt des aliens (à finir)
- afficher une liste d'alien complete
- affichage et destruction des murs
- hitbox de tout les objets (à finir)
- affichage, mvt et collisions des bullets
- gestion de fin de partie
"""

import tkinter as tk
from alien import Alien
from spaceship import Spaceship
from wall import Wall
from bullet import Bullet



# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:
    def __init__(self, game):
        self.__game = game
        self.__spaceship1 = Spaceship()
        self.__wall_list = [Wall(), Wall(), Wall()]
        self.__alien1 = Alien(0.5,0.1)   # position en pourcentage d'ecran
        self.__direction_alien = 1

        self.__bottom_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645, fill = 'green', outline = "green")
        self.__top_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635, fill = 'green', outline = "green")
        self.__rec_alien = self.__game.create_rectangle(self.__alien1.getx() * 820, self.__alien1.gety() * 620, self.__alien1.getx() * 820 + 30, self.__alien1.gety() * 620 +30, fill = 'green', outline = "green")
        self.__rec_wall_list = []
        for j in range(3):
            self.__rec_wall_list.append([])
            for k in range(3):
                self.__rec_wall_list[j].append([])
                for l in range(6):
                    self.__rec_wall_list[j][k].append(self.__game.create_rectangle(170 + j*200 + l*20, 450 + k*20, 180 + j*200 + l*20, 460 + k*20, fill = 'green', outline = "green"))
    

    def hitbox(self, objet):
        (x1,y1,x2,y2) = self.__game.coords(objet) 
        return [(x2-x1)/2,(y1-y2)/2]
    
    def move_alien(self):
        if self.__alien1.getx() > 0.9:
            self.__direction_alien = -1
            self.__alien1.move_y()
            self.__alien1.setx(0.9)
        elif self.__alien1.getx() < 0.1:
            self.__direction_alien = 1
            self.__alien1.move_y()
            self.__alien1.setx(0.1)
        else:
            self.__alien1.move_x(self.__direction_alien)

        
        self.__game.coords(self.__rec_alien, self.__alien1.getx() * 820, self.__alien1.gety() * 620, self.__alien1.getx() * 820 + 30,self.__alien1.gety() * 620 +30)
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
                        