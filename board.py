"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
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
    
    def print_spaceship1(self):
        bottom_spaceship1 = game.create_rectangle(self.__spaceship1.x, 635, self.__spaceship1.x + 30, 645)
        top_spaceship = game.create_rectangle(self.__spaceship1.x + 10, 625, self.__spaceship1.x + 20, 635)