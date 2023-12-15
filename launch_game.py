"""
Hugo PRIGENT, Louis VINCENT
13/12/2023

Classe permettant de lancer le jeu 
en choisissant la difficulté

to do :
"""

import tkinter as tk
from board import Board

class Launch_game:
    
    #méthode d'initialiastion
    def __init__(self, window):
        self.__difficulty = 0
        self.__window = window
        
    
    def clear_window(self):
        widget_list = []
        for e in self.__window.children:
            widget_list.append(e)
        for e in widget_list:
            if self.__difficulty != 0:
                self.__window.children[e].place_forget()
            else: 
                self.__window.children[e].grid_forget()



    #méthode permettant de choisir le nivau 1:
    #entrée : l'objet , sortie : valeur 1 attribuée pour la difficulté
    def set_difficulty1(self):
        self.__difficulty = 1
        print(self.__difficulty)
        self.clear_window()
        
    
    #cette méthode marche comme celle ci-dessus mais pour le niveau 2
    def set_difficulty2(self):
        self.__difficulty = 2
        self.launch_game()

    #de même pour le niveau 3
    def set_difficulty3(self):
        self.__difficulty = 3
        self.launch_game()

    
    def meth_new_game(self):
        self.__difficulty = 0
        self.clear_window()
    

    def launch_menu(self):
        image_menu = tk.PhotoImage(file = 'images\menu2.png')

        difficulty_disp = tk.Label(self.__window, text ="Choose your difficulty :")
        canva_img = tk.Canvas(self.__window, width = 500, height = 700, bg = 'black' )

        image1 = canva_img.create_image(250,350, image = image_menu)
        background_label = tk.Label(image = image_menu)
        background_label.place(x = 220, y = 0, relwidth = 1, relheight = 1)

        button_dif1 = tk.Button(self.__window, text = "Low", command =  self.set_difficulty1)
        button_dif2 = tk.Button(self.__window, text = "Medium", command = self.set_difficulty2)
        button_dif3 = tk.Button(self.__window, text = "Hard", command = self.set_difficulty3)

        difficulty_disp.place(x = 100, y = 0)
        button_dif1.place(x = 100, y = 100)
        button_dif2.place(x = 160, y = 100) 
        button_dif3.place(x = 220 , y = 100)


    #méthode permettant de lancer le jeu, d'afficher le jeu de façon a ce qu'il soit dynamique
    #entrée : l'ojet, sortie : lancement et actualisation du jeu
    def launch_game(self):
        game = tk.Canvas(self.__window, width = 850, height = 650, bg = "black")
        game.grid(row = 2, column = 1, sticky = 'SW', padx = 5, pady = 5)

        new_game = tk.Button(self.__window, text = "New Game", command =  self.meth_new_game())
        new_game.grid(row = 2, column = 2, sticky ='N', pady = 200, padx = 30)

        score = tk.StringVar()
        life = tk.StringVar()
        score.set("Score : 0")
        life.set("Life : 3")


        board1 = Board(game, score, life, self.__difficulty)

        quit = tk.Button(self.__window, text = "Quit game", command = lambda: self.__window.destroy() )
        quit.grid(row = 2, column = 2, pady = 200, padx = 30)
        
        score = tk.Label(self.__window, textvariable = score , font  = ("Times New Roman", 15, "bold"))
        score.grid(row = 1, column = 1, sticky= "W")

        lives = tk.Label(self.__window, textvariable = life, font = ("Times New Roman", 15, "bold"))
        lives.grid(row = 1, column = 1, sticky = "E")

        
        board1.move_alien()
        board1.tir_alien()
        self.__window.bind("<Key>", board1.key_pressed)

    
    #methode permettant d'acceder a la difficulté 
    #entrée : l'objet, sortie : la difficulté
    def get_difficulty(self):
        return self.__difficulty
    
    

    