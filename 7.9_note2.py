note = []


for k in range (0,9):
    if k == 0 :
        utilisateur = int(input("Veuillez saisir votre 1 ère note :"))

    else :
        utilisateur = int(input(f"Veuillez saisir votre {k+1} éme notes :"))

    note.append(utilisateur)

moy = sum(note) / len(note)

print(note)
print(f"La moyenne des notes est : {moy}")

#on doit specifié ici que l'utilisateur entre des int sinon il ne peut pas faire la moyenne