util = int(input("Entrez un nombre pour savoir s'il est impair ou divisible par 5 :" ))

if (util % 5) == 0 or (util % 2) == 1 :

    print(f"{util} l'est")

else :

    print(f"{util} ne l'est pas")
