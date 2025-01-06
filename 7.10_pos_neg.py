tableau = []

utilisateur1 = int(input("Veuillez saisir le nombre de valeur qu'il y aura dans votre tableau :"))

#len(tableau) == utilisateur1

for k in range(0,utilisateur1):

    utilisateur2 = int(input("Veuillez entré vos valeurs negatives ou positives :"))

    tableau.append(utilisateur2)

print(tableau)

nbrpos = 0
nbrneg = 0
nbrnul = 0

for valeur in tableau :

    if valeur > 0 :
        nbrpos += 1

    elif valeur < 0 :
        nbrneg += 1

    else :
        nbrnul += 1

print(f"Vous avez {nbrpos} nombre(s) positif")
print(f"Vous avez {nbrneg} nombre(s) negatif")
print(f"Il y a {nbrnul} fois le zero")




