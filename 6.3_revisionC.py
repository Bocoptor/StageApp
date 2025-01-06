noms = []

print("Veuillez entrer 3 noms pour savoir s'il sont dans l'ordre alphabétique, dans le cas contraire ils seront trié")

for k in range(3):
    if k == 0:
        utilisateur = input("Veuillez saisir votre 1er nom :")

    else:
        utilisateur = input(f"Veuillez sais0ir votre {k + 1}ème nom :")

    noms.append(utilisateur)

noms_trié = sorted(noms)

if noms == noms_trié:
    print("Ils sont dans l'ordre")

else:
    print(f"Ils ne sont pas l'ordre mais les voici trié : {noms_trié}")