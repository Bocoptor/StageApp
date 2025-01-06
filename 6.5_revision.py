print("Veuillez entrer 2 nombres pour savoir si le produit de ceux ci sont positif, negatif ou nul")

while True :
    try :
        nombre1 = int(input("Veuillez entrer votre 1er nombre :"))
        nombre2 = int(input("Veuillez entrer votre 2ème nombre :"))

        if nombre1 == 0 or nombre2 == 0 :
            print(f"Le produit de {nombre1} et {nombre2} est nul")

        elif (nombre1 < 0 and nombre2 < 0) or (nombre1 > 0 and nombre2 > 0) :
            print(f"Le produit de {nombre1} et {nombre2} est positif")

        else:
            print(f"Le produit de {nombre1} et {nombre2} est negatif")

    except ValueError :
        print("Ce n'est pas un nombre, veuillez reesayer")