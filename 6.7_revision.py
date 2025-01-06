print("Veuillez entrer une heure pour qu'elle s'y affiche avec 1 minute de + :")

while True:
    try:
        heure = int(input("Entrez l'heure :"))
        minute = int(input("Entrez les minutes :"))

        if minute > 59 or heure > 24:
            print("Ce n'est pas une heure valide")
            continue

        elif heure == 23 and minute == 59:
            print("Il sera 00:00")

        elif minute == 59:
            print(f"Il sera {heure+1}:00")

        else:
            print(f"Il sera {heure}:{minute+1}")

        break

    except ValueError:
        print("Ce ne sont pas des chiffres")