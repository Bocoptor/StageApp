tableau = []

utilisateur1 = int(input("Veuillez saisir la taille de votre tableau :"))

for k in range(0,utilisateur1):
    utilisateur2 = int(input("Veuillez saisir vos nombres :"))

    tableau.append(int(utilisateur2))

print(f"La valeur la plus grande est :{max(tableau)}")

