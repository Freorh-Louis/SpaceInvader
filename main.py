"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Main projet space invaders
To do :  
mettre en lien avec les objets,
(afficher les vies),
gestion du score

"""
#importation des librairies
import tkinter as tk
from board import Board



#creation de la fenetre du jeu : 

window = tk.Tk()
window.title("Space Invaders")
window.geometry("1000x700")


#pour les elements de la fentre on les organise en grid, en "tableau" au sens graphique
game = tk.Canvas(window, width = 850, height = 650, bg = "black")
game.grid(row = 2, column = 1, sticky = 'SW', padx = 5, pady = 5)

new_game = tk.Button(window, text = "New Game")
new_game.grid(row = 2, column = 2, sticky ='N', pady = 200, padx = 30)

score = tk.StringVar()
life = tk.StringVar()
score.set("Score : 0")
life.set("Life : 3")
board1 = Board(game, score, life)

quit = tk.Button(window, text = "Quit game", command = game.destroy)
quit.grid(row = 2, column = 2, pady = 200, padx = 30)
 
score = tk.Label(window, textvariable = score , font  = ("Times New Roman", 15, "bold"))
score.grid(row = 1, column = 1, sticky= "W")

lives = tk.Label(window, textvariable = life, font = ("Times New Roman", 15, "bold"))
lives.grid(row = 1, column = 1, sticky = "E")


board1.move_alien()
board1.tir_alien()
window.bind("<Key>", board1.key_pressed)


""""
#page menu :
difficulty = tk.Label(window, text ="Choose your difficulty :")

button_dif1 = tk.Button(window, text = "Low")
button_dif2 = tk.Button(window, text = "Medium")
button_dif3 = tk.Button(window, text = "Hard")

difficulty.grid(row = 2, column = 1, sticky = "N", pady = 150)
button_dif1.grid(row = 2, column =1, sticky = "W", padx = 75)
button_dif2.grid(row = 2, column = 1)
button_dif3.grid(row = 2, column = 1, sticky = "E", padx = 75)
"""


window.mainloop()

 