# algo qui demande a l'utilisateur un nombre compris entre 1 et 3
# jusqu'a ce que la réponse convienne.



n = 27

while True:
    print("Veuillez trouvé le nombre qui est compris entre 1 et 50")

    n_util = int(input())

    if n_util < n :
        print("c'est plus grand !")


    elif n_util > n :
        print("c'est plus petit !")


    else:
        print("c'est bon !")
        break
