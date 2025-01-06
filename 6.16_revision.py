while True:
    try:
        nombre = int(input("Veuillez entrer un nombre pour que les 10 suivants soient afficher :"))
        compteur = 0
        while compteur < 10:
            print(f"{nombre}", end= " ")
            #end c'est qu'il n'affiche pas a la ligne mais l'un a coté de l'autre0
            nombre += 1
            compteur += 1

    except ValueError:
        print("Valeur incorrecte, reesayer")


#while True:
        #   try:
        #nombre = int(input("Veuillez entrer un nombre pour que les 10 suivants soient afficher :"))
        #for i in range(nombre+1, nombre + 11):
    #   print(i)

        #except ValueError:
        #print("Valeur incorrecte, reesayer")