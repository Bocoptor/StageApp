#Algo qui lit une suite de prix en euro entiers
#terminée par un 0 et qui correspond aux achats d'un client
#calculer la somme que le client doit payer
#lire ce que le client donne
#simuler la remise de la monnaie en affichant les textes billet de 10€, 20€, 50€ ect et pieces 1€, 2€ ect
#autant de fois qu'il y a de monnaie à rendre

#

print("Veuillez entrez l'argent que vous avez ?")
somme = int(input())

print("Pour combien en avez vous eu ?")
achat = int(input())

rembours = somme-achat

print("Vous allez être remboursé de\n",rembours)

billetpiece = [500,200,100,50,20,10,5,2,1]

if rembours > 0 :
    for calcul in billetpiece:
        var = rembours // calcul
        if var % 0 :
            print(var)
else :
    print("pas de monnaie à rendre")

