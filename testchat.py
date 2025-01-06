print("Veuillez entrez l'argent que vous avez ?")
somme = int(input())

print("Pour combien en avez vous eu ?")
achat = int(input())

monnaie_a_rendre = somme-achat

print("Vous allez être remboursé de\n",monnaie_a_rendre)

# Liste des valeurs des billets et pièces disponibles
billets_et_pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Affichage du rendu de monnaie
if monnaie_a_rendre > 0:
    print(f"Monnaie à rendre : {monnaie_a_rendre} euros")
    for valeur in billets_et_pieces:
        nombre = monnaie_a_rendre // valeur
        if nombre > 0:
            if valeur >= 5:
                print(f"{nombre} billet(s) de {valeur}€")
            else:
                print(f"{nombre} pièce(s) de {valeur}€")
            monnaie_a_rendre %= valeur
else:
    print("Pas de monnaie à rendre. Le montant est payé intégralement.")