"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : 
- finir print_starship1
- gerer mvt du startship1
- affichage(image) et mvt des aliens
- affichage et destruction des murs
- hitbox de tout les objets
- affichage, mvt et collisions des bullets
- gestion de fin de partie
"""

import time
import tkinter as tk
from main import window, game
from alien import alien
from spaceship import spaceship
from wall import wall
from bullet import bullet


# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class board:
    def __init__(self):
        self.__spaceship1 = spaceship
        self.__wall1 = wall
        self.__wall2 = wall
        self.__wall3 = wall
        self.__alien1 = alien

        self.__bottom_spaceship1 = game.create_rectangle(self.__spaceship1.x * 820, 635, self.__spaceship1.x * 820 + 30, 645)
        self.__top_spaceship = game.create_rectangle(self.__spaceship1.x * 820 + 12, 629, self.__spaceship1.x * 820 + 18, 635)
    
    def init_board(self, difficulty):
        game.delete(all)
        

    #ef create_bullet(self):

    def hitbox(self, objet):
        (x1,y1,x2,y2) = game.coords(objet) 
        return [(x2-x1)/2,(y2-y1)/2]
    
    #def colision(self,objet1, objet2):
        

    def move_spaceship1(self, direction):
        self.__spaceship1.move(direction)
        game.coords(self.__bottom_spaceship1, self.__spaceship1.x * 820, 635, self.__spaceship1.x * 820 + 30, 645)
        game.coords(self.__top_spaceship, self.__spaceship1.x * 820 + 12, 629, self.__spaceship1.x * 820 + 18, 635)
        