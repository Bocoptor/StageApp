tableau = []

nombres = input("Veuillez saisir des nombres pour savoir s'ils se suivent consecutivement et terminer par 'ok' :")

while True:
    if nombres == 'ok':
        break
    else:
        consecutif = int(nombres)
        tableau.append(consecutif)

print(tableau)