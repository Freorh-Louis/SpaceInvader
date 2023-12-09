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

    #fonction permettant au vaisseau de se déplacer
    #son entree est direction valant 1 ou -1, elle ajoute ou retire 0.05 a x stockee dans self 
    def move(self, direction):
        self.__x  = self.__x  + direction * 0.02       #quand on tape sur une fleche, il se déplace de 0.05% de l'ecran
        return(self.__x)

    def getx(self):
        return self.__x

    def damage(self):
        self.__life -=1
        return self.__life
    
    def getlife(self):
        return self.__life