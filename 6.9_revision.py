print("Il s'agit d'un calculateur de facture par rapport aux nombres de copies")
print("Les 10 premieres sont facturés 0.05€")
print("Les 20 suivantes 0.04€")
print("Et au delà 0.03€")

while True:
    try:
        nombre_copie = int(input("Veuillez entrer le nombre de photocopie faite :"))
        photocopie1 = 0.05

        photocopie2 = nombre_copie - 10
        photocopie22 = (photocopie2*0.04)+0.5

        photocopie3 = nombre_copie -30
        photocopie33 = (photocopie3*0.03)+1.26

        if nombre_copie <= 10:
            print(f"Ca vous coutera {nombre_copie*photocopie1}€")

        elif nombre_copie > 10 and nombre_copie <= 30:
            print(f"Ca vous coutera {photocopie22}€")

        else:
            print(f"ca vous coutera {photocopie33}€")

        break

    except ValueError:
        print("Ce n'est pas un chiffre, reesayer")