tableau = []

utilsateur1 = int(input("Veuillez saisir le nombres de valeurs pour le tableau :"))

for k in range(0,utilsateur1):
    utilisateur2 = int(input("Veuillez saisir vos valeurs qui seront incrémenté de 1 :"))

    tableau.append(utilisateur2)
    tableau[k] += 1

print(tableau)