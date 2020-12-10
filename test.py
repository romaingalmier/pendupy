"--utf8--"
'''
Header
par Romain GALMIER
en nov/dec 2020 
projet :  pendu avec interface grafique
'''

from random import randint
from fonctionpendu import verifLetter , ajoutLettre , concat , choixMot
from tkinter import Tk, Label, Button ,StringVar, Entry


mot = choixMot()       #Mot à deviner
motdev = [" _"]* (len(mot))
motdev[0] = mot [0]
motdevc = concat(motdev)
lfausse = []
nbfaute = 0 

# création de la fenêtre graphique

def main() : 
    global mot
    global motdev
    global motdevc
    global lfausse
    global nbfaute

    # while (motdevc != mot) and len(lfausse) < 8  :
    print("----------------------------------------------------------------------------------")
    print(mot)
    
    lettre = Lettrein.get()
    Lettrein.delete(0)
    print(lettre)

    if  lettre.isdigit() or len(lettre) != 1  : 
        print("La valeur entree est un nombre remet une lettre")
        Lettrein.delete(0,len(lettre))
    if lettre in lfausse : 
        print("lettre deja entée")    
    elif verifLetter(mot,lettre) == False : 
        
        
        lettre = lettre.upper()
        lfausse.append(lettre)
        nbfaute += 1
        print(lfausse)
    else : 
        motdev = ajoutLettre(mot , lettre, motdev)
        motdevc = concat(motdev)
        print("bien ouej continue  " )
        print(motdevc)
    
    print(nbfaute)

    # print ("finitdo avec ",nbfaute )
MaFenetre = Tk()
MaFenetre.title("Jeu du Pendu")
MaFenetre.geometry('500x200' )

labelHello = Label(MaFenetre, text = "Pendu ! ", fg = 'blue')
labelHello.pack()

Label1 = Label(MaFenetre, text = 'Entrez une lettre ')
Label1.pack(side = 'left', padx = 5, pady = 5)

motdevc = StringVar()
Label2 = Label(MaFenetre, textvariable = motdevc)
Label2.pack(side = 'left', padx = 5, pady = 5)

Label3 = Label(MaFenetre, textvariable = lfausse)
Label3.pack(side = 'left', padx = 5, pady = 5)

Lettre = StringVar()
Lettrein = Entry(MaFenetre, textvariable = Lettre ,bg = 'bisque', fg = 'maroon')
Lettrein.focus_set()

Lettrein.pack(side = 'left', padx = 5, pady = 5)


ButtonSubmit = Button(MaFenetre, text ='Submit', command = main )
ButtonSubmit.pack(side = 'top', padx = 5, pady = 5)

buttonQuitt = Button (MaFenetre, text = "QUITTER", fg = 'red', command = MaFenetre.destroy)
buttonQuitt.pack()

MaFenetre.mainloop()

























