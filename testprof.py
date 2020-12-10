# coding: latin-1
# script cible.py

from tkinter import *
import random
Mafenetre = Tk()
Mafenetre.title('IMG')

def affichImg (nbfautes) :

    # Création de la fenÃªtre principale (main window)
    # img = "bonhomme" + str(1 + nbfautes) +".gif"
    img = "bonhomme1.gif"

    # Image de fond
    photo = PhotoImage(file = img )
    return photo
    
# Création d'un widget Canvas (zone graphique)
Largeur = 550
Hauteur = 550
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0, anchor = NW, image = affichImg (2))
print ("Image de fond (item",item,")")
Canevas.pack()

# Création d'un widget Button (bouton Quitter)


BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 10, pady = 10)

Mafenetre.mainloop()
