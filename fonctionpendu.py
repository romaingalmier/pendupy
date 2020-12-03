"--utf8--"

from random import randint
def verifLetter (mot,lettre) :
    '''
    entee//sortie : le mot a deviner et la lettre donné // True or False
    sert a verifer que la lettre proposer est dans le mot a deviner
    '''
    if lettre in mot:
        return True
    else : 
        return False

def ajoutLettre(mot,lettre,motdev) : 
    '''
    entree : le mot a deviné / la lettre proposé / le mot deviné jusque là
    sortie : le mot deviné jusque là
    si une lettre est juste l'ajoute au  mot deviné jusque là
    '''
    c = 0
    for i in mot :
        if i == lettre and i !=0 : 
            lettre = lettre.lower()
            motdev[c] = lettre
        c += 1
    return motdev

def concat (motdev):
    '''
    concatene les differend element str d'une liste
    '''
    x = ""
    for i in range(len(motdev)):
        x=  x + motdev[i]
    return x

def choixMot() :
    '''
    entree : /
    sortie  :mot à deviner
    prend un mot dans la liste eproposé 
    '''
    fichier = open( file= "motspendu.txt", mode="rt" ,encoding="utf-8")
    while True :
        text=fichier.readlines()
        print(len(text))
        mot=text[randint(0,len(text)-1)]
        mot = mot.strip()
        if len(mot) >= 5 :
            fichier.close()
            return mot