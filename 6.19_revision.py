while True:
    try:
        nombre = int(input("Veuillez saisir un nombre pour lequel la somme à partir de 1 sera calculé jusqu'a y arriver :"))
        compteur = 1
        somme = 0
        for i in range(1, nombre):
            somme += i
            compteur += 1
        print(f"{compteur} + {compteur} = {somme}")
        break
    except ValueError:
        print("Valeur incorrect, reesayer")


#pas complet