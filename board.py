"""
Hugo PRIGENT, Louis VINCENT
09/11/2023
Objet board projet space invaders
to do : 
- affichage et destruction des murs
- hitbox de tout les objets (à finir)
- collisions des bullets
- gestion de fin de partie
"""

import tkinter as tk
from alien import Alien
from spaceship import Spaceship
from wall import Wall
from bullet import Bullet

direction_alien = 1

# Cet objet gère la postion, l'apparence et l'état de vie de tout les autres objets du jeu
class Board:

    # méthode d'initialisation, crée les murs (objets), le vaisseau(objets), les aliens (liste)  
    # , game (=la fenetre), les rectangles (affichage graphique des objets)
    # comme des attributs pour l'objet Board
      
    def __init__(self, game):
        self.__game = game
        self.__spaceship1 = Spaceship()
        self.__wall1 = Wall()
        self.__wall2 = Wall()
        self.__wall3 = Wall()
        
        self.__alien_list = []
        self.__bottom_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645, fill = 'green', outline = "green")
        self.__top_spaceship1 = self.__game.create_rectangle(self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635, fill = 'green', outline = "green")
        
        self.__rec_list = []
        
        for i in range(12):
            if i <= 5:
                self.__alien_list.append( Alien( 0.12 + i * 0.05, 0.1 + 0.05))
            
            if i > 5 :
                self.__alien_list.append( Alien( 0.12 + (i-6) * 0.05, 0.22))
            
            self.__rec_list.append(self.__game.create_rectangle(self.__alien_list[i].getx() * 820, self.__alien_list[i].gety() * 620, self.__alien_list[i].getx() * 820 + 30, self.__alien_list[i].gety() * 620 + 30, fill = 'green', outline = 'green'))
    



    # méthode donnant le centre de gravité de l'objet, en vue de gérer les collisions
    # entrée : un objet, sortie: centre de gravité( tableau de valeurs réelles)
    def hitbox(self, objet):
        (x1,y1,x2,y2) = self.__game.coords(objet) 
        return [(x2-x1)/2,(y1-y2)/2]
    


    # méthode permettant la gestion des déplacements des aliens, 
    # cette méthode utilise d'autres méthodes (getx, move_x, move_y) propre à l'objet  
    # entrée:l'objet, sortie: un déplacement des alien (déplacement d'objets)

    def move_alien(self):
        global direction_alien
        
        n = len(self.__alien_list)

        if self.__alien_list[n -1].getx() > 0.9:
            direction_alien = -1
            
            for i in range(n):
                
                self.__alien_list[i].move_y()
            
            for i in range(n-1, -1 ,-1):
                print(i)
                if i >= 6:
                    self.__alien_list[i].setx(0.90 - (n-i-1) * 0.05)
                    print(0.90 - ((n -i )* 0.05))
            
                else:
                    self.__alien_list[i].setx(0.90 - (n -(i + 5)) * 0.05)
        
        elif self.__alien_list[0].getx() < 0.1:
            direction_alien = 1
            

            for i in range(n):
                self.__alien_list[i].move_y()
            

                
        
        for i in range(n):
            self.__alien_list[i].move_x(direction_alien)
            self.__game.coords(self.__rec_list[i], self.__alien_list[i].getx() * 820, self.__alien_list[i].gety() * 620, self.__alien_list[i].getx() * 820 + 30, self.__alien_list[i].gety() * 620 + 30)
        
        self.__game.after(1000, self.move_alien)
        
        





    # Méthode permettant la gestion du déplacement du vaisseau
    # elle aussi utilise d'autres méthodes (getx, gety) propre à l'objet (spaceship)
    # entrée: l'objet, "sortie": déplacement de l'objet 

    def move_spaceship1(self, event):
        direction = 0
        touche = event.keysym
        # print("We love M.Trouillot")
        if touche == "Right":
            direction = 1
        elif touche == "Left":
            direction = -1
        self.__spaceship1.move(direction)
        self.__game.coords(self.__bottom_spaceship1, self.__spaceship1.getx() * 820, 635, self.__spaceship1.getx() * 820 + 30, 645)
        self.__game.coords(self.__top_spaceship1, self.__spaceship1.getx() * 820 + 12, 629, self.__spaceship1.getx() * 820 + 18, 635)
    

    # Méthode permettant d'actualiser la fenetre
    # entrée: l'objet, "sortie": actualisation de la fenetre. 
    def get_game(self):
        return self.__game
    
