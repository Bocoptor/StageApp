print("Veuillez entrer une heure avec les secondes pour qu'il y affiche 1 seconde apreès :")

while True:
    try:
        heure = int(input("Entrer l'heure :"))
        minute = int(input("Entrer les minutes :"))
        seconde = int(input("Entrer les secondes :"))

        if heure > 23 or minute > 59 or seconde > 59:
            print("Format pas valide, reesayer")
            continue

        elif heure == 23 and minute == 59 and seconde == 59:
            print("Il sera 00:00:00")

        elif minute == 59 and seconde == 59:
            print(f"{heure+1}:00:00")

        elif seconde == 59:
            print(f"{heure}:{minute+1}:00")

        else:
            print(f"Il sera {heure}:{minute}:{seconde+1}")
            break

    except ValueError:
        print("Ce ne sont pas des chiffres, reesayer")