# 15. 8.5 Dames
# Écrivez un algorithme de jeu de dames très simplifié.
# L’ordinateur demande à l’utilisateur dans quelle case se trouve son pion (ligne,
# colonne). On met en place un contrôle de saisie afin de vérifier la validité des
# valeurs entrées.
# Ensuite, on demande à l’utilisateur quel mouvement il veut effectuer : 7 (en haut
# à gauche), 9 (en haut à droite), 1 (en bas à gauche), 3 (en bas à droite).
# Si le mouvement est impossible (on sort du damier), on le signale à l’utilisateur
# et on s’arrête là. Sinon, on déplace le pion et on affiche le damier résultant, en
# affichant un "O" pour une case vide et un "X" pour la case où se trouve le pion.
# ===================================================================================
# 1) Intialiser le tableau
damier = [0] * 10
print(damier)
for i in range(0,len(damier)) :
    damier[i] = [0] * 10
    print(f"{damier[i]}")
# print(damier)

#2) Demander au joueur la position intiale de son pion
OK = 0
while True :
    if OK == 1 :
        break
    pos_i = int(input("Tapez la ligne du pion, svp : "))
    print(f"pos_i = {pos_i}")
    if pos_i > 0 and pos_i <= 10 :
        while True :
            pos_j = int(input("Tapez la colonne du pion, svp : "))
            print(f"pos_j = {pos_j}")
            if pos_j > 0 and pos_j <= 10 :
                OK = 1
                damier[pos_i - 1][pos_j - 1] = 'X'
                print(f"pos_i devient pos_i - 1 = {pos_i - 1}")
                print(f"pos_j devient pos_j - 1 = {pos_j - 1}")
                for i in range(0, len(damier)):
                    print(f"{damier[i]}")
                damier[pos_i - 1][pos_j - 1] = 0
                break
            else :
                print("Donner une valeur entre 1 eT 10")
    else:
        print("Donner une valeur entre 1 eT 10")
# print(f"ligne : {pos_i} ; colonne : {pos_j} ")

# 3) Faire bouger le pion
while True:
    dir = int(input("Dans quelle direction voulez-vous faire avancer votre pion ? \n 7' : à gauche, en haut \n '9' : à droite, en haut \n '1' : à gauche, en bas \n '3' : à droite, en bas \n Direction : "))
    # print("'7' : à gauche, en haut \n '9' : à droite, en haut \n '1' : à gauche, en bas \n '3' : à droite, en bas")
    if dir == 7 :
        if pos_i == 1 :
            print("Mouvement interdit !")
        elif pos_j == 1 :
            print("Mouvement interdit !")
        else :
            pos_i = pos_i - 2
            pos_j = pos_j - 2
            damier[pos_i][pos_j] = 'X'
            for i in range(0, len(damier)):
                print(f"{damier[i]}")
            break
    elif dir == 9 :
        if pos_i == 1 :
            print("Mouvement interdit !")
        elif pos_j == 10 :
            print("Mouvement interdit !")
        else :
            pos_i = pos_i - 2
            # pos_j = pos_j
            damier[pos_i][pos_j] = 'X'
            for i in range(0, len(damier)):
                print(f"{damier[i]}")
            break
    elif dir == 1:
        if pos_i == 10 :
            print("Mouvement interdit !")
        elif pos_j == 1 :
            print("Mouvement interdit !")
        else :
            # pos_i = pos_i + 1
            pos_j = pos_j - 2
            damier[pos_i][pos_j] = 'X'
            for i in range(0, len(damier)):
                print(f"{damier[i]}")
            break
    elif dir == 3:
        if pos_i == 10 :
            print("Mouvement interdit !")
        elif pos_j == 10 :
            print("Mouvement interdit !")
        else :
            # pos_i = pos_i - 1
            # pos_j = pos_j - 1
            damier[pos_i][pos_j] = 'X'
            for i in range(0, len(damier)):
                print(f"{damier[i]}")
            break
# 4) Vérifier que le pion se trouve bien dans le tableau

# 5) Afficher le résultat