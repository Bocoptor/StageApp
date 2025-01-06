print("Veuillez entré deux nombres pour savoir si il est positif ou negatif :")
n1 = int(input())
n2 = int(input())

if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
     print("le produit de",n1,"et",n2,"sera positif")

else:
     print("le produit de",n1,"et",n2,"sera negatif")
