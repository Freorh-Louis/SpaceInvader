"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet alien projet space invaders
to do : fini
"""

# Définie un objet alien
class Alien:
    
    # Méthode d'initialisation
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
    
    # Ces deux méthodes donnent la position en x ou y de l'ogjet 
    # entrée : l'objet 
    # sortie : x/y attributs (réels). 
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    # Méthode permettant de changer la position en x de l'objet
    # entrée: l'objet, la nouvelle valeur de x (réel)
    # sortie: mise a la valeur voulue de la position en x
    def setx(self, new_x):
        self.__x = new_x

    # Méthode permettant de changer la vie l'objet
    # entrée: l'objet, la nouvelle valeur de vie (entier)
    # sortie: mise a la valeur voulue de la vie
   
    def setlife(self,value):
        self.__life = value

    # Méthodes donnant la vie de l'ogjet 
    # entrée : l'objet 
    # sortie : vie (entier).
    def getlife(self):
        return(self.__life)
        