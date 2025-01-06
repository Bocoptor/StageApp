while True:
    try:
        tableM = int(input("Veuillez taper un nombre et la table de multiplication jusqu'a 10 s'affichera :"))
        for i in range(0,10):
            i += 1
            print(f"{tableM} X {i} = {tableM*i}")
        break
    except ValueError:
        print("Valeur incorrect, reesayer")