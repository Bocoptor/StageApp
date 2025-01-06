while True:
    try:
        nombre = int(input("Taper un nombre pour afficher les 10 suivants :"))
        for i in range(0,10):
            nombre += 1
            print(f"{nombre}", end=" ")
    except ValueError:
        print("Valeur incorrect, reesayer")

    # for i in range(nombre+1, nombre + 11):
    #   print(i)