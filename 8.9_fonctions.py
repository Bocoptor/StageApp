import random

# compteur allumettes
compteur_allumettes = 20
print("Bienvenue sur le jeu des allumettes")
print(f"Il y a {compteur_allumettes} allumettes au depart")
# joueur 1
joueur1 = input("Veuillez entré le premier nom du joueur :")
# joueur 2
joueur2 = input("Veuillez entré le deuxieme nom du joueur :")

# allumettes 1-3
while True:
    try:
        joueur_joue = random.choice([joueur1, joueur2])
        print(f"Le joueur qui doit joué est : {joueur_joue}")
        print("Vous pouvez retirer 1, 2 ou 3 allumettes")

        if compteur_allumettes > 0:
            tirage_allumette = int(input("Combien voulez-vous retiré d'allumette(s):"))

            if tirage_allumette >= 1 and tirage_allumette <= 3:
                compteur_allumettes -= tirage_allumette
            else:
                print("Choix invalide. Veuillez entrer 1, 2 ou 3 allumettes.")

            print(f"Il reste {compteur_allumettes} allumettes")

        else:
            print(f"C'est le joueur {joueur_joue} qui à perdu")
            break
    except ValueError:
        print("Veuillez entré des chiffres")