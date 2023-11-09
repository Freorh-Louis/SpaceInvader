"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
"""
import time
from alien import alien
from spaceship import spaceship
from wall import wall
from bullet import bullet


# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class board:
    def __init__(self):
        self.__spaceship1 = 0