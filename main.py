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

launcher = Launch_game(window)

print(launcher.get_difficulty())
launcher.launch_menu()
launcher.launch_game()
launcher.clear_window()



window.mainloop()

