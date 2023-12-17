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
    def move_y(self, direction):
        self.__y += direction * 0.01
        return self.__y
    


    # Ces méthodes permettent d'obtenir la postion en x/y  de l'objet
    # entrée: l'objet 
    # sortie: postion en x/y (réels)
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    # Méthode permettant d'obtenir la vie de l'objet 
    # entrée: l'objet 
    # sortie: état de la vie de l'objet (entier 0 ou 1)
    def getlife(self):
        return self.__life
    
    # Méthode permettant d'obtenir la vie de l'objet 
    # entrée: l'objet, newlife (entier)
    # sortie: changement de l'état de la vie de l'objet (entier)
    def setlife(self, newlife):
        self.__life = newlife
        return self.__life