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

def getLettre() :
    return (Lettrein.get())
# création de la fenêtre graphique
MaFenetre = Tk()
MaFenetre.title("Jeu du Pendu")
MaFenetre.geometry('300x100' )

labelHello = Label(MaFenetre, text = "Pendu ! ", fg = 'blue')
labelHello.pack()

Label1 = Label(MaFenetre, text = 'Mot de passe ')
Label1.pack(side = 'left', padx = 5, pady = 5)

Lettre= StringVar()

Lettrein = Entry(MaFenetre, textvariable = Lettre ,bg = 'bisque', fg = 'maroon')
Lettrein.focus_set()

Lettrein.pack(side = 'left', padx = 5, pady = 5)


BoutonSubmit = Button(MaFenetre, text ='Submit', command = getLettre)
BoutonSubmit.pack(side = 'top', padx = 5, pady = 5)

buttonQuitt = Button (MaFenetre, text = "QUITTER", fg = 'red', command = MaFenetre.destroy)
buttonQuitt.pack()


Mafenetre.mainloop()



while (motdevc != mot) and len(lfausse) < 8  :
    print("----------------------------------------------------------------------------------")
    print(motdevc)
    lettre = getLettre()

    if  lettre.isdigit() or len(lettre) != 1  : 
        print("La valeur entree est un nombre remet une lettre")
        continue

    if verifLetter(mot,lettre) == False : 
        if lettre in lfausse : 
            print("lettre deja entée")
            continue
        lettre = lettre.upper()
        lfausse.append(lettre)
        nbfaute += 1
        print(lfausse)

    else : 
        motdev = ajoutLettre(mot , lettre, motdev)
        motdevc = concat(motdev)
        print("bien ouej continue  " )
        # print(motdevc)

print ("finito avec ",nbfaute )




