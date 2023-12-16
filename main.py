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
from launch_game import Launch_game


#creation de la fenetre du jeu : 

window = tk.Tk()
window.title("Space Invaders")
window.geometry("1000x700+100+0")


score = tk.StringVar()
life = tk.StringVar()
score.set("Score : 0")
life.set("Life : 3")

launcher = Launch_game(window, score, life)

image_menu = tk.PhotoImage(file = 'images\menu2.png')
difficulty_disp = tk.Label(window, text ="Choose your difficulty :")
background_label = tk.Label(image = image_menu)
button_dif1 = tk.Button(window, text = "Low", command =  launcher.set_difficulty1)
button_dif2 = tk.Button(window, text = "Medium", command = launcher.set_difficulty2)
button_dif3 = tk.Button(window, text = "Hard", command = launcher.set_difficulty3)


game = tk.Canvas(window, width = 850, height = 650, bg = "black")
new_game = tk.Button(window, text = "New Game", command =  launcher.meth_new_game)
quit = tk.Button(window, text = "Quit game", command = window.destroy )
score = tk.Label(window, textvariable = score , font  = ("Times New Roman", 15, "bold"))
lives = tk.Label(window, textvariable = life, font = ("Times New Roman", 15, "bold"))


launcher.launch_menu()
launcher.clear_window()



window.mainloop()

