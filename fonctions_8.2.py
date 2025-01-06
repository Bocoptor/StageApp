def phrase ():

    util = input("Entrez une phrase pour connaitre le nombre de mot(s) :")

    espace = util.split()

    nbr_mot = len(espace)

    print(f"Le nombre de mot(s) qu'il y a dans votre phrase est : {nbr_mot}")

phrase()