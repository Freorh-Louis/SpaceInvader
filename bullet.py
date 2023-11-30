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
    
    # Méthode permettant de déplacer de 1% la position selon x de bullet dans un direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_x(self, direction):
        self.__x += direction*0.01
        return self.__x
    


    # Ces méthodes permettent d'obtenir la postion en x/y  de l'objet
    # entrée: l'objet sortie: postion en x/y (valeurs réelles)
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y