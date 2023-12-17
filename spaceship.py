"""""
Louis Vincent-Hugo Prigent
9/11/2023
script de l'objet vaisseau
to do : fini
"""

class Spaceship:

    def __init__(self):
        self.__x = 0.5      #Quand on lance le jeu le vaisseau est centré au milieu de l'ecran
        self.__life = 3     #nombre de vies au lancement 

    # Méthode permettant au vaisseau de se déplacer
    # entree:  l'objet, direction (entier)
    # sortie: déplacement de l'objet dans la direction choisie
    def move(self, direction):
        # il se déplace de 0.05% de l'ecran
        self.__x  = self.__x  + direction * 0.02       
        return(self.__x)

    # Méthode permettant d'accéder à la position en x de l'objet
    # entrée: l'objet
    # sortie: la position en x (réel)
    def getx(self):
        return self.__x

    # Méthode gérant une collision avec une balle tirée
    # entrée: l'objet
    # sortie: nouveau nombre de vie (entier)
    def damage(self):
        self.__life -= 1
        return self.__life
    
    # Méthode permettant d'accéder au nombre de vie de l'objet
    # entrée: l'objet
    # sortie: le nombre de vie de l'objet (entier)
    def getlife(self):
        return self.__life