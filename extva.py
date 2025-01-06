print("Veuillez saisir le nom d'un article :")
art = input()
print("Veuillez saisir son prix HT :")
HT = float(input())
print("Veuillez saisir le nombre d'exemplaires :")
ex = int(input())
print("Veuillez saisir le taux de TVA :")
TVA = float(input())

rep1 = TVA/100
rep2 = HT * ex
rep3 = rep2 * rep1
rep4 = rep3 + rep2

print("Le nom de l'article est :",art)
print("Le prix hors TVA est de :",HT, "€")
print("Le nombre d'exemplaires est de :",ex)
print("Le taux de TVA est de :",TVA)
print("Le prix total revient à :",rep4)






