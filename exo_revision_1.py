# Un magasin de photocopies facture 0,05 € les 10 premières photocopies,
# 0,04 € les vingt suivantes et 0,03 € au-delà.
# Écrivez un algorithme qui demande à
# l’utilisateur le nombre de photocopies effectuées et qui affiche la facture
# correspondante.

copie1 = 0.05
copie2 = 0.04
copie3 = 0.03

print("Voici la liste des tarifs en fonction du nombres de copies:\n"
      "10 premieres : 0.05€\n"
      "De 10 à 20 : 0.04€\n"
      "Les suivantes sont toutes à : 0.03€")

util = int(input("Appuyer sur ENTER pour continuer"))

nbr = int(input("Veuillez entré le nombre de copie que vous avez faites"))