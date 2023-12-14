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

image_menu = tk.PhotoImage(file = 'images\menu2.png')

difficulty_disp = tk.Label(window, text ="Choose your difficulty :")
canva_img = tk.Canvas(window, width = 500, height = 700, bg = 'black' )

image1 = canva_img.create_image(250,350, image = image_menu)
background_label = tk.Label(image = image_menu)
background_label.place(x = 220, y = 0, relwidth = 1, relheight = 1)

difficulty = Launch_game(window)
button_dif1 = tk.Button(window, text = "Low", command =  difficulty.set_difficulty1)
button_dif2 = tk.Button(window, text = "Medium", command = difficulty.set_difficulty2)
button_dif3 = tk.Button(window, text = "Hard", command = difficulty.set_difficulty3)



difficulty_disp.place(x = 100, y = 0)
button_dif1.place(x = 100, y = 100)
button_dif2.place(x = 160, y = 100) 
button_dif3.place(x = 220 , y = 100)



window.mainloop()

