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
    
    #méthode permettant de choisir le nivau 1:
    #entrée : l'objet , sortie : valeur 1 attribuée pour la difficulté
    def set_difficulty1(self):
        self.__difficulty = 1
        self.launch_game()
        
    #cette méthode marche comme celle ci-dessus mais pour le niveau 2
    def set_difficulty2(self):
        self.__difficulty = 2
        self.launch_game()

    #de même pour le niveau 3
    def set_difficulty3(self):
        self.__difficulty = 3
        self.launch_game()


    #méthode permettant de lancer le jeu, d'afficher le jeu de façon a ce qu'il soit dynamique
    #entrée : l'ojet, sortie : lancement et actualisation du jeu
    def launch_game(self):
        game = tk.Canvas(self.__window, width = 850, height = 650, bg = "black")
        game.grid(row = 2, column = 1, sticky = 'SW', padx = 5, pady = 5)

        new_game = tk.Button(self.__window, text = "New Game")
        new_game.grid(row = 2, column = 2, sticky ='N', pady = 200, padx = 30)

        score = tk.StringVar()
        life = tk.StringVar()
        score.set("Score : 0")
        life.set("Life : 3")


        board1 = Board(game, score, life, self.__difficulty)

        quit = tk.Button(self.__window, text = "Quit game", command = game.destroy)
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
    
    

    