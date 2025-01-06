print("Veuillez entrer 3 noms pour savoir s'il sont dans l'ordre alphabétique, dans le cas contraire ils seront trié")
util1 = input("Veuillez entrer le premier nom :")
util2 = input("Veuillez entrer le deuxième nom :")
util3 = input("Veuillez entrer le troisième nom :")

if util1 < util2 and util2 < util3 :
    print(f"{util1}, {util2} et {util3} sont dans l'ordre alphabétique")

else:
    noms_tries = sorted([util1, util2, util3])
    print(f"{util1}, {util2} et {util3} ne sont pas dans l'ordre alphabétique mais les voici triés : {noms_tries}")