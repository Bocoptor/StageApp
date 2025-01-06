
while True :
    try :
        age_enfant = int(input("Veuillez entrer l'age de votre enfant pour savoir dans quelle categorie il sera :"))

        if age_enfant < 6 :
            print("Votre enfant sera dans la categorie 'Bébé'")

        elif age_enfant == 6 or age_enfant == 7 :
            print("Votre enfant sera dans la categorie 'Poussin'")

        elif age_enfant == 8 or age_enfant == 9:
            print("Votre enfant sera dans la categorie 'Pupille'")

        elif age_enfant == 10 or age_enfant == 11:
            print("Votre enfant sera dans la categorie 'Minime'")

        elif age_enfant >= 12:
            print("Votre enfant sera dans la categorie 'Cadet'")

        break

    except ValueError:
        print("Ce n'est pas un age, veuillez reesayer")