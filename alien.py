"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet alien projet space invaders
to do : fini
"""

# Définie un objet alien
class Alien:
    def __init__(self,x,y):
        # Crée les variables de postion x et y, et de l'état de vie de l'alien
        self.__x = x
        self.__y = y
        self.__life = 1    # Si life = 1 l'alien est en vie, si life = 0 l'alien est mort
        
    # Méthode permettant de déplacer de 5% la position selon x de l'alien dans un direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_x(self, direction):
        self.__x += direction*0.05
    
    # Méthode permettant de déplacer de 10% la position selon y de l'alien dans une direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_y(self):
        self.__y += 0.1
    
    #Ces méthodes donnent la position en x ou y de l'ogjet entrée : self, objet sortie : x/y attribut. 
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def setx(self, new_x):
        self.__x = new_x