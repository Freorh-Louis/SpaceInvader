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

direction_alien = 1

# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:
    def __init__(self, game):
        self.__game = game
        self.__spaceship1 = Spaceship()
        self.__wall1 = Wall()
        self.__wall2 = Wall()
        self.__wall3 = Wall()
        self.__alien1 = Alien(0.5,0.1)   # position en pourcentage d'ecran

        self.__bottom_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645, fill = 'green', outline = "green")
        self.__top_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635, fill = 'green', outline = "green")
        self.__rec_alien = self.__game.create_rectangle(self.__alien1.getx() * 820, self.__alien1.gety() * 620, self.__alien1.getx() * 820 + 30, self.__alien1.gety() * 620 +30, fill = 'green', outline = "green") 
    

    def hitbox(self, objet):
        (x1,y1,x2,y2) = self.__game.coords(objet) 
        return [(x2-x1)/2,(y1-y2)/2]
    
    def move_alien(self):
        global direction_alien
        if self.__alien1.getx() > 0.9:
            direction_alien = -1
            self.__alien1.move_y()
        elif self.__alien1.getx() < 0.1:
            direction_alien = 1
            self.__alien1.move_y()
        
        self.__alien1.move_x(direction_alien)
        self.__game.coords(self.__rec_alien, self.__alien1.getx() * 820, self.__alien1.gety() * 620, self.__alien1.getx() * 820 + 30,self.__alien1.gety() * 620 +30)
        self.__game.after(1000, self.move_alien)
        

    def move_spaceship1(self, event):
        direction = 0
        touche = event.keysym
        # print("We love M.Trouillot")
        if touche == "Right":
            direction = 1
        elif touche == "Left":
            direction = -1
        self.__spaceship1.move(direction)
        self.__game.coords(self.__bottom_spaceship1, self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645)
        self.__game.coords(self.__top_spaceship1, self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635)
    
    def get_game(self):
        return self.__game