"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet alien projet space invaders
"""

# Définie un objet alien
class alien:
    def __init__(self,x,y):
        # Crée les variables de postion x et y, et de l'état de vie de l'alien
        self.__x = x
        self.__y = y
        self.__life = 1    # Si life = 1 l'alien est en vie, si life = 0 l'alien est mort
    
    # Fonction permettant de déplacer de 5% la position selon x de l'alien dans un direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_x(self, direction):
        self.__x += direction*0.05
        return self.__x
    
    # Fonction permettant de déplacer de 10% la position selon y de l'alien dans une direction donnée
    # direction = 1 : déplacement vers la droite / direction = -1 : déplacement vers la gauche
    def move_y(self, direction):
        self.__y += direction*0.1
        return self.__y
    