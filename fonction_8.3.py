def voyellesfonc():

    util = input("Entrez une phrase pour connaitre le nombre de voyelle(s) qu'elle contient :")

    voyelle = ["a","e","i","o","u","y"]

    compteur_voy = 0

    for mot in util :

        if mot in voyelle:

            compteur_voy += 1

    print(f"Il y a {compteur_voy} voyelle(s) dans votre phrase")

voyellesfonc()