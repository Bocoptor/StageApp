print("Veuillez saisir 10 nombres pour afficher le plus grand")

n1 = input()
n2 = input()
n3 = input()
n4 = input()
n5 = input()
n6 = input()
n7 = input()
n8 = input()
n9 = input()
n10 = input()


plusgrandnombre = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]

def maximum(liste):
    for valeur in plusgrandnombre:
        max = plusgrandnombre[0]
        if valeur >= max:
            max = valeur
    return max