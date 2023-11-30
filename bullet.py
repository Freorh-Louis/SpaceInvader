"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet tir projet space invaders
to do : fini
"""

# Définie un objet bullet
class Bullet:
    def __init__(self, x, y):
        # Crée les variables de postion x et y, et de l'état de vie de bullet
        self.__x = x
        self.__y = y
        self.__life = 1
    
    # Fonction permettant de déplacer de 1% la position selon x de bullet dans un direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_y(self, direction):
        self.__y += direction*0.01
        return self.__y
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y