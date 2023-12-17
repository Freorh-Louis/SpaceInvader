"""
Louis Vincent-Hugo Prigent
9/11/2023
script de l'objet mur

To do: fini
"""


class Wall:
    
    # Méthode d'initialisation
    # a l'initialisation, l'état du mur est complet, donc on remplit le tableau de tableau avec que des 1
    
    def __init__(self): 
        self.__state = [[1,1,1,1,1,1] , [1,1,1,1,1,1] , [1,1,1,1,1,1]]
    

    # Méthode permettant de modifier le mur, quand une case du mur est touchee, son etat passe a 0
    # entree : position dans un tableau de tableau en colone et ligne (entiers)
    # sortie : tableau de tableau (tableau)
    
    def destroy(self, row, column):
        self.__state[row][column] = 0
        return (self.__state)
    
    # Méthode permettant d'accéder à létat du mur
    # entrée: l'objet
    # sortie: tableau de tableau indiquant l'état du mur
    
    def get_state(self):
        return self.__state


    
