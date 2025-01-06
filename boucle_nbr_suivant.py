# Écrivez un algorithme qui demande un nombre de départ, et qui affiche
# ensuite les dix nombres suivants.
# Par exemple, si l’utilisateur entre le nombre 33, l’algorithme affichera les
# nombres

print("Veuillez entré un nombre et il y affichera les 10 suivants")

n = int(input())

while True:
    if n < (n + 10):
        n += n

    else:
        print(n)
        break
