util = int(input("Entrez un nombre pour savoir s'il est pair ou divisible par 5 :" ))

if (util % 5) == 0 and (util % 2) == 0 :

    print(f"{util} l'est")

else :

    print(f"{util} ne l'est pas")
