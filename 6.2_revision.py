util1 = int(input("Entrez 2 nombres pour savoir si le produit est positif ou negatif :"))
util2 = int(input())

produit = util1*util2

if produit < 0 :
    print(f"{produit} est negatif")

elif produit == 0 :
    print(f"{produit} est nul")

else :
    print(f"{produit} est positif")