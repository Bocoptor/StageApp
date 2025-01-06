# algo qui demande a l'utilisateur un nombre compris entre 1 et 3
# jusqu'a ce que la réponse convienne.

print("Veuillez trouvé le nombre qui est compris entre 1 et 3")


n1 = int(input())


if n1 >= 1 and n1 <= 3:
    print("c'est bon !")

else:
    print("reessayer !")
