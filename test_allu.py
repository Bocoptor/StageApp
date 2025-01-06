import random

nombre_allumettes = 20

print("Bienvenue sur le jeu des allumettes, la regle consiste à retiré 1,2 ou 3 allumettes.")
print("Il y a 20 allumettes au départ, celui qui tire la derniere allumette à perdu.")
print("Vous pouvez joué seul contre l'ordinateur ou à deux.")
nombre_joueur = input("Voulez vous joué seul ou à deux (tapez '1' ou '2') :")
if nombre_joueur == '2' :
    joueur1 = input("Veuillez saisir le 1er nom :")
    joueur2 = input("Veuillez saisir le 2ème nom :")
    joueur_joue = random.choice([joueur1,joueur2])
    print(f"C'est à {joueur_joue} de joué")
    retrait_allumette = input("Combien d'allumettes voulez vous retiré ? (tapez 1, 2 ou 3 :")
    nombre_allumettes -= retrait_allumette
    print(f"Il reste {nombre_allumettes} allumettes")