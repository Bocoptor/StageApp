tableau = []

while True:
    utilisateur1 = input("Veuillez saisir les notes :")

    if utilisateur1 == "stop":
        break

    else:
        try:
            conversion = int(utilisateur1)
            tableau.append(conversion)
        except ValueError:
            print("Pas correct")

print(tableau)

moy = sum(tableau) / len(tableau)

sup_moye = [x for x in tableau if x > moy]

print(f"La moyenne etant de :{moy}")
print(f"Les notes supérieurs sont : {sup_moye}")


