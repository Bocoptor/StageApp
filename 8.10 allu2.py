import random

# compteur allumettes
compteur_allumettes = 20
print("Bienvenue sur le jeu des allumettes")
print(f"Il y a {compteur_allumettes} allumettes au depart")
print("Vous pouvez retirer 1, 2 ou 3 allumettes")
while True:
    joueur_joue = input("Voulez vous joué seul contre l'ordinateur ou à 2 joueurs ?")

    if joueur_joue == "2":
        # joueur 1
        joueur1 = input("Veuillez entré le premier nom du joueur :")
        # joueur 2
        joueur2 = input("Veuillez entré le deuxieme nom du joueur :")

        # allumettes 1-3
        while True:
            try:
                joueur_joue = random.choice([joueur1, joueur2])
                print(f"Le joueur qui doit joué est : {joueur_joue}")

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

    elif joueur_joue == 'seul':
        joueur1 = input("Veuillez entré le nom du joueur :")
        joueur2 = 'Ordinateur'
        while True:
            try:
                joueur_joue = random.choice([joueur1, joueur2])
                print(f"Le joueur qui doit joué est : {joueur_joue}")
                if joueur_joue == joueur2:
                    tirage_allumette = random.choice ([1,2,3])
                    if tirage_allumette >= 1 and tirage_allumette <= 3:
                        compteur_allumettes -= tirage_allumette
                        print(f"{joueur2} à retiré {tirage_allumette} allumettes")
                        print(f"Il reste {compteur_allumettes} allumettes")


                elif compteur_allumettes > 0:
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

    else:
        print("Veuillez entré '2' ou 'seul'")