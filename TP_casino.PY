import pandas as pd
import random

#on déclare les cartes dans une liste :
deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

#on fait notre premier tirage de 5 cartes :
def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
	#on supprime les cartes tirées du reste:
        deck.remove(i)
    return tirage, deck
	
	
def choix_carte(tirage):
    nouvelles_cartes_choisies = []
    count = 0
#on boucle sur la liste des cartes du 1er tirage afin de choisir les cartes a conserver :
    for carte in tirage:
        print('voulez-vous garder la carte ? o/n ?:' + carte)
        reponse_utilisateur = input()
        if reponse_utilisateur == 'o':
            nouvelles_cartes_choisies.append(carte)
        elif reponse_utilisateur == "n":
            pass
        else:
            return "erreur de saisie"
#on retourne la liste des cartes conservées :
    return nouvelles_cartes_choisies
	
	
	
def deuxieme_tirage(nouvelles_cartes_choisies, deck):
    nb_carte = len(nouvelles_cartes_choisies)
    carte_a_tirer = 5 - nb_carte
#après avoir vérifier le nbr de cartes manquantes on tire au hasard ces cartes :
    nouvelle_carte = random.sample(deck, carte_a_tirer)
    for i in nouvelle_carte:
        nouvelles_cartes_choisies.append(i)
    return nouvelles_cartes_choisies
	
	
def machine():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
# on stocke le resultat de la fonction premier_tirage    
    tirage1, deck = premier_tirage(deck)
    print(tirage1)
# on stocke le resultat de la fonction choix_carte
    nouvelles_cartes_choisies = choix_carte(tirage1)
# on stocke le resultat de la fonction deuxieme_tirage
    tirage_final = deuxieme_tirage(nouvelles_cartes_choisies, deck)
    print(tirage_final)
    return tirage_final
	
def decompose_jeu(tirage):
#on déclare un dictionnaire
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    famille = []
#on boucle sur 2 colonnes
    for i,j in zip(tirage, keys):
#on partage la valeur de notre carte afin d'avoir d'un coté la valeur et de l'autre coté la famille
        dic[j] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0])
        famille.append(dic[key][1])
    return valeur, famille
	
	
def convert_carte(liste):
#Permettant de convertir les valeur K,Q,A,J en valeur numérique 
    for e,i in zip(liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J' :
                liste[i] = 11
            elif e == 'Q' :
                liste[i] = 12
            elif e == 'K' :
                liste[i] = 13
            elif e == 'A' :
                liste[i] = 1
            else:
                continue
    return liste
	
	
def quinte_flush_royale(tirage):
    valeur_gagnante = ['10','J','Q','K','A']
#on stock le résultat de la fonction decompose_jeu
    valeur, famille = decompose_jeu(tirage)
#on test si on a une suite de 10 à A de la meme famille
	#valeur_gagnante = sorted(valeur_gagnante)
	#valeur = sorted(valeur)
    if  sorted(valeur_gagnante) == sorted(valeur) and famille.count(famille[0]) == 5:
        return True
    else:
        return False
		
		
def quinte_flush(tirage):
#on stock le résultat de la fonction decompose_jeu et la fonction convert_carte
    valeur, famille = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
#si le count de la premiere valeur de la colonne famille = 5 alors c'est la même famille
    if suite.count('True') == 4 and famille.count(famille[0]) == 5:
        return True
    else:
        return False
		
		
def carre(tirage):
    valeur, famille = decompose_jeu(tirage)
#on utilise series de la librairie pandas
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else:
        return False
		
		
def full(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur1 =pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) ==[2, 3]:
        return True
    else:
        return False
		
		
def flush(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    if famille.count(famille[0]) == 5:
#si le count de la premiere valeur de la colonne famille = 5 alors c'est la même famille
        return True
    else:
        return False
		
		
def quinte(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('true') == 4 or valeur == [1, 10, 11, 12, 13]:
        return True
    else:
        return False
		
		
		
def brelan(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False
		
		
def double_paire(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
        return True
    else:
        return False
		
		
		
def paire(tirage):
    valeur, famille = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        return False
		
#la fonction gain permet d'utiliser les fonctions de test des differentes combinaisons possibles en se basant sur le retour (false ou true)
def gain(tirage_final, mise):
#on récupère les cartes de l'utilisateurs afin de connaitre son gain
    if quinte_flush_royale(tirage_final) == True:
        g = mise*250
        resultat = "Quinte Flush Royale !! Vous gagnez " + str(g) + " euros!"
        return g, resultat
    elif quinte_flush(tirage_final) == True:
        g = mise*50
        resultat = "Quinte Flush !!! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif carre(tirage_final) == True:
        g = mise*25
        resultat = "Carré! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif full(tirage_final) == True:
        g = mise*9
        resultat = " Full! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif flush(tirage_final) == True:
        g = mise*6
        resultat = "Flush! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif quinte(tirage_final) == True:
        g = mise*4
        resultat = "Quinte! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif brelan(tirage_final) == True:
        g = mise*3
        resultat = "Brelan! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif double_paire(tirage_final) == True:
        g = mise*2
        resultat = "Double paire! Vous gagnez " + str(g) + " euros !"
        return g, resultat
    elif paire(tirage_final) == True:
        g = mise*1
        resultat = "Paire !! Vous conservez votre mise !"
        return g, resultat
    else:
        g = 0
        resultat = "Perdu!
		"
        return g, resultat
		

def partie(mise, bankroll):
#On stock le résultat de la fonction machine et de la fonction gain afin d'avoir le jeu et le gain gagné
    main = machine()
    g, resultat = gain(main, mise)
    bankroll = bankroll - mise
    bankroll += g
    return resultat, bankroll
	
	
	
def video_pocker():
    bankroll = int(input("Veuillez saisir votre argent disponible: "))
    mise_joueur = int(input("Veuillez faire vos jeux:"))
    
    while bankroll - mise_joueur >=0:
        resultat, bankroll = partie(mise_joueur, bankroll)
        print(resultat)
        print("Solde compte: "+ str(bankroll))
        if bankroll == 0:
            print("Partie terminée")
            break
        else:
            mise_joueur = int(input("Veuillez refaire vos jeux: "))
            if bankroll - mise_joueur < 0:
                print("mise trop elevée")
                mise_joueur = int(input("Veuillez refaire vos jeux: "))
				
 #Menu main du programme				
				
if __name__ == "__main__":
   video_pocker()
