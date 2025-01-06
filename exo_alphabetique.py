print("Veuillez entré 3 noms à la suite et savoir s'ils sont par ordre alphabetique")
n1 = str(input())
n2 = str(input())
n3 = str(input())

if n1 < n2 and n1 < n3:
    print(n1, n2, n3, "sont rangés par ordre alphabetique")

else:
    print(n1, n2, n3, "ne sont pas rangés par ordre alphabetique")