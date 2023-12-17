"""
Hugo PRIGENT, Louis VINCENT
13/12/2023

Classe permettant de lancer le jeu en choisissant la difficulté et de relancer une nouvelle partie

to do : fini
"""

from board import Board

class Launch_game:
    
    #méthode d'initialisation
    def __init__(self, window, score, life):
        self.__difficulty = 0
        self.__window = window
        self.__score = score
        self.__life = life
        self.__board1 = None
        
    # Méthode permettant d'effacer le menu.
    # entrée: l'objet 
    # sortie: effacement des éléments enfant de la fenentre en fonction de si le jeu a été lancé ou non
    
    def clear_window(self):
        if self.__board1 != None:
            self.__board1.set_gameover(1)
        widget_list = []
        # on répertorit les éléments dans une liste
        for e in self.__window.children:
            widget_list.append(e)
        
        for e in widget_list:
            # si le jeu à commencé, alors on efface le menu
            if self.__difficulty != 0:
                self.__window.children[e].place_forget()
            # si le jeu est déjà lancé, on efface le jeu
            else: 
                self.__window.children[e].grid_forget()



    # Méthode permettant de choisir le nivau 1:
    # entrée : l'objet  
    # sortie : valeur 1 attribuée pour la difficulté
    
    def set_difficulty1(self):
        self.__difficulty = 1
        self.clear_window()
        self.launch_game()
        
    
    # Cette méthode marche comme celle ci-dessus mais pour le niveau 2
    def set_difficulty2(self):
        self.__difficulty = 2
        self.clear_window()
        self.launch_game()

    # De même pour le niveau 3
    def set_difficulty3(self):
        self.__difficulty = 3
        self.clear_window()
        self.launch_game()

    # Méthode permettant de lancer une nouvelle partie, elle est associée au bouton new_game
    # entrée: l'ojet
    # sortie: effacement de la fenetre, lancement du menu, mise à 0 de la difficulté
    
    def meth_new_game(self):
        self.__difficulty = 0
        self.clear_window()
        self.launch_menu()
    
    # méthode permettant d'afficher le menu
    # entrée: l'objet
    # sortie: affichage des éléments du menu
    
    def launch_menu(self):
        menu_list = []
        # on répertorit les éléments du menu
        for e in self.__window.children:
            menu_list.append(e)
        # on les affiche dans l'ordre voulu, a des positions voulues
        self.__window.children[menu_list[0]].place(x = 100, y = 50)
        self.__window.children[menu_list[1]].place(x = 220, y = 0, relwidth = 1, relheight = 1)
        self.__window.children[menu_list[2]].place(x = 100, y = 100)
        self.__window.children[menu_list[3]].place(x = 160, y = 100) 
        self.__window.children[menu_list[4]].place(x = 240 , y = 100)


    # méthode permettant de lancer le jeu, d'afficher le jeu de façon a ce qu'il soit dynamique
    # entrée : l'ojet 
    # sortie : lancement et actualisation du jeu
    
    def launch_game(self):
        game_list = []
        for e in self.__window.children:
            game_list.append(e)

        self.__window.children[game_list[5]].grid(row = 2, column = 1, sticky = 'SW', padx = 5, pady = 5)
        self.__window.children[game_list[6]].grid(row = 2, column = 2, sticky ='N', pady = 200, padx = 30)
        self.__window.children[game_list[7]].grid(row = 2, column = 2, pady = 200, padx = 30)
        self.__window.children[game_list[8]].grid(row = 1, column = 1, sticky= "W")
        self.__window.children[game_list[9]].grid(row = 1, column = 1, sticky = "E")

        self.__score.set("Score : 0")
        self.__life.set("Life : 3")

        self.__window.children[game_list[5]].delete('all')
        self.__board1 = Board(self.__window.children[game_list[5]], self.__score, self.__life, self.__difficulty)
        self.__board1.create_alien()
        self.__board1.create_wall()
        self.__board1.move_alien()
        self.__board1.tir_alien()
        self.__window.bind("<Key>", self.__board1.key_pressed)
        
        

    
    # methode permettant d'acceder a la difficulté 
    # entrée : l'objet 
    # sortie : la difficulté (entier)
    def get_difficulty(self):
        return self.__difficulty
    
    

    