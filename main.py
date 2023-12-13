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
import function
from launch_game import Launch_game



#creation de la fenetre du jeu : 

window = tk.Tk()
window.title("Space Invaders")
window.geometry("1000x700")

#page menu :
difficulty_disp = tk.Label(window, text ="Choose your difficulty :")

difficulty = Launch_game(window)

button_dif1 = tk.Button(window, text = "Low", command =  difficulty.set_difficulty1)
button_dif2 = tk.Button(window, text = "Medium", command = difficulty.set_difficulty2)
button_dif3 = tk.Button(window, text = "Hard", command = difficulty.set_difficulty3)

difficulty_disp.grid(row = 2, column = 1, sticky = "N")
button_dif1.grid(row = 2, column = 1, sticky = "W", padx = 75)
button_dif2.grid(row = 2, column = 1, padx = 300)
button_dif3.grid(row = 2, column = 1, sticky = "E", padx = 200)



window.mainloop()

