note = []

for k in range (0,9):
    if k == 0 :
        utilisateur = input("Veuillez saisir votre 1 ère note :")

    else :
        utilisateur = input(f"Veuillez saisir votre {k+1} éme notes :")

    note.append(utilisateur)

print(note)