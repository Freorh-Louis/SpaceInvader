"""
Louis Vincent-Hugo Prigent
9/11/2023
script de l'objet mur

"""


class wall:
    
    # a l'initialisation, l'état du mur est complet, donc on remplit le tableau de tableau avec que des 1
    def __init__(self): 
        self.__state = [[1,1,1,1,1,1] , [1,1,1,1,1,1] , [1,1,1,1,1,1]]
    

    #fonction permettant de modifier le mur
    #quand une case du mur est touchee, son etat passe a 0, entree : position dans un tableau de tableau (int)
    #sortie : tableau de tableau (tableau)
    
    def destroy(self, row, column):
        self.__state[row][column] = 0
        return (self.__state)


    
