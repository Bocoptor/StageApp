nombre = int(input("Veuillez entrer un nombre pour savoir si il est positif, negatif ou egal à zero :"))

if nombre == 0 :
    print(f"{nombre} est egal à zero")

elif nombre > 0 :
    print(f"{nombre} est positif")

else :
    print(f"{nombre} est negatif")