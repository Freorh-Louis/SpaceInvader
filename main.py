"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Main projet space invaders
To do : menu, 
mettre en lien avec les objets,
(afficher les vies),
gestion du score

"""
#importation des librairies
import tkinter as tk



#creation de la fenetre: 

window = tk.Tk()
window.title("Space Invaders")
window.geometry("1000x700")


#pour les elements de la fentre on les organise en grid, en "tableau" au sens graphique
game = tk.Canvas(window, width = 850, height = 650, bg = "black")
game.grid(row = 2, column = 1, sticky = 'SW', padx = 5, pady = 5)

new_game = tk.Button(window, text = "New Game")
new_game.grid(row = 2, column = 2, sticky ='N', pady = 200, padx = 30)


quit = tk.Button(window, text = "Quit game")
quit.grid(row = 2, column = 2, pady = 200, padx = 30)

 
score = tk.Label(window, text = "Score : ", font  = ("Times New Roman", 15, "bold"))
score.grid(row = 1, column = 1, sticky= "W")

lives = tk.Label(window, text = "Live : ", font = ("Times New Roman", 15, "bold"))
lives.grid(row = 1, column = 1, sticky = "E")

window.mainloop()

