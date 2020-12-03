"--utf8--"
'''
Header

par Romain GALMIER
en nov/dec 2020 
projet :  pendu sans interface grafique
'''
from random import randint
from fonctionpendu import verifLetter , ajoutLettre , concat , choixMot

mot = choixMot()       #Mot à deviner
motdev = [" _"]* (len(mot))
motdev[0] = mot [0]
motdevc = concat(motdev)
lfausse = []
nbfaute = 0 

while (motdevc != mot) and len(lfausse) < 8  :
    print("----------------------------------------------------------------------------------")
    print(motdevc)
    lettre = input("devine : ") 

    if  lettre.isdigit() or len(lettre) != 1  : 
        print("La valeur entree est un nombre remet une lettre")
        continue

    if verifLetter(mot,lettre) == False : 
        lettre = lettre.upper()
        lfausse.append(lettre)
        nbfaute+=1
        print(lfausse)

    else : 
        motdev = ajoutLettre(mot , lettre, motdev)
        motdevc = concat(motdev)
        print("bien ouej continue  " )
        # print(motdevc)

print ("finito avec ",nbfaute )





