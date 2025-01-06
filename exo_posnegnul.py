#demander 2 nombres et l'informe si le produit est positif negatif ou nul sans calculer

print("veuillez entré 2 nombres pour savoir s'ils sont positif, negatif ou nul")

n1 = int(input())
n2 = int(input())

if n1 < 0 or n2 < 0 :
    print("le produit de",n1,"et",n2,"est negatif")

elif n1 == 0 and n2 == 0 :
    print("le produit de",n1,"et",n2,"est nul")

else :
    print("le produit de",n1,"et",n2,"est positif")
