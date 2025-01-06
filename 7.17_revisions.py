tableau = []

while True:
    try:
        utilisateur1 = int(input("Veuillez saisir le nombres de chiffres à placer :"))

        for k in range(0, utilisateur1):
            while True:
                try:
                    if k == 0:
                        utilisateur2 = int(input("Veuillez saisir votre 1er chiffre :"))

                    else:
                        utilisateur2 = int(input(f"Veuillez saisir vos {k + 1} éme chiffres :"))

                    tableau.append(utilisateur2)
                    break
                except ValueError:
                    print("Veuillez entré des chiffres")
        break
    except ValueError:
        print("Veuillez entré des chiffres")

tableau_trie = sorted(tableau, reverse=True)

print(f"Tableau original : {tableau}")
print(f"Tableau trié : {tableau_trie}")