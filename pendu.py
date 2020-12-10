"--utf8--"
'''
Header
par Romain GALMIER / Delio COLAS
en nov/dec 2020 
projet :  pendu avec interface graphique
TODO : reafficher l'image supprimmer (tout marche sauf l'affichage)
'''

from random import randint
from fonctionpendu import verifLetter , ajoutLettre , concat , choixMot
from tkinter import *
from tkinter import messagebox

MaFenetre = Tk()
MaFenetre.title("Jeu du Pendu")
MaFenetre.geometry('1500x500' )




mot = choixMot()       #Mot à deviner
motdev = [" _"]* (len(mot))
motdev[0] = mot [0]
motdevc = concat(motdev)
lfausse = []
nbfaute = 0 
photos = []

def main() : 
    '''
entree : /
sortie  :/
partie qui gere la partie fonctionnelle du pendu
'''
    global mot , var2
    global motdev
    global motdevc
    global lfausse
    global nbfaute
    
    var4.set("")
    lettre = Lettrein.get()
    Lettrein.delete(0)

    if  lettre.isdigit() or len(lettre) != 1 or lettre in lfausse :
        if lettre in lfausse :
            var4.set("lettre déjà entrée")
        else :
            var4.set("Il faut mettre une seule lettre")
        Lettrein.delete(0,len(lettre))
     
            
    elif verifLetter(mot,lettre) == False : 
        lfausse.append(lettre)
        nbfaute += 1
    else : 
        motdev = ajoutLettre(mot , lettre, motdev)
        motdevc = concat(motdev)
    
    var2.set(motdevc)
    var3.set(lfausse)
    delImg()
    affichImg (nbfaute)
    if len(lfausse)==8 :
        perdu()
    if mot == motdevc :
        gagner()

    
def perdu() :

# action de fin de partie lorqu'elle est perdu
    ButtonReset.destroy()
    Lettrein.destroy()
    var4.set("perdu")
    messagebox.showinfo("perdu" , "perdu dommage ")

def gagner() : 
    
#  action de fin de partie lorqu'elle est gagner
    ButtonReset.destroy()
    Lettrein.destroy()
    var4.set("Gagner")
    messagebox.showinfo("Gagner" , "Gagner Bravo ! ! ") 

def reset() :


#  action ddu bouton reset

    global mot 
    global motdev
    global motdevc
    global lfausse
    global nbfaute

    mot = choixMot()       
    motdev = [" _"]* (len(mot))
    motdev[0] = mot [0]
    motdevc = concat(motdev)
    lfausse = []
    nbfaute = 0 
    var3.set(lfausse)
    var2.set(motdevc)

def affichImg (nbfaute) :
    ###Permet d'afficher l'image en fonction du nombre de faute

    global photos
    # Création de la fenÃªtre principale (main window)
    img = "bonhomme"+ str(1+nbfaute) +".gif"

    # Image de fond
    photo = PhotoImage(file = img )
    photos.append(photo)
    
    
    return photo


def delImg():
    ###Permet de delete l'image 
    global Canevas, item
    Canevas.delete(item)
    return

# Création d'un widget Canvas (zone graphique)
Largeur = 550
Hauteur = 550
Canevas = Canvas(MaFenetre,width = Largeur, height =Hauteur)


item = Canevas.create_image(0,0, anchor = NW, image = affichImg (nbfaute) )
Canevas.pack(side = 'right' , padx = 10, pady = 10)

labelHello = Label(MaFenetre, text = "Pendu ! ", fg = 'blue')
labelHello.pack()

Label1 = Label(MaFenetre, text = 'Entrez une lettre ')
Label1.pack(side = 'left', padx = 5, pady = 5)

var2 = StringVar()
var2.set(motdevc)
Label2 = Label(MaFenetre, textvariable = var2)
Label2.pack(side = 'left', padx = 5, pady = 5)

var3 = StringVar()
var3.set(lfausse)
Label3 = Label(MaFenetre, textvariable = var3)
Label3.pack(side = 'left', padx = 5, pady = 5)

var4 = StringVar()
var4.set(lfausse)
Label4 = Label(MaFenetre, textvariable = var4)
Label4.pack(side = 'left', padx = 5, pady = 5)

Lettre = StringVar()
Lettrein = Entry(MaFenetre, textvariable = Lettre ,bg = 'bisque', fg = 'maroon')
Lettrein.focus_set()

Lettrein.pack(side = 'left', padx = 5, pady = 6)

ButtonSubmit = Button(MaFenetre, text ='Submit', command = main )
ButtonSubmit.pack(side = 'left', padx = 5, pady = 5)

ButtonReset = Button(MaFenetre, text ='Recommencer', command = reset )
ButtonReset.pack(side= "bottom")

buttonQuitt = Button (MaFenetre, text = "QUITTER", fg = 'red', command = MaFenetre.destroy)
buttonQuitt.pack(side= "bottom",padx = 5, pady = 5)

MaFenetre.mainloop()





