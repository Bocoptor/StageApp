util1 = input("Veuillez entré 3 noms pour savoir s'ils sont rangé par ordre alphabetique ou non :")
util2 = input("2ème nom :")
util3 = input("3ème nom :")

if util1 < util2 and util1 < util3 and util2 < util3 :
    print("oui")

elif util2 < util1 and util2 < util3 and util1 < util3 :
    print(f"non mais les voici dans l'ordre : {util2} {util1} {util3}")

elif util3 < util1 and util3 < util2 and util1 < util2 :
    print(f"non mais les voici dans l'ordre : {util3} {util1} {util2} ")

else:
    print(f"non mais les voici dans l'ordre : {util3} {util2} {util1} ")