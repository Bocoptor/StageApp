nombre = []

while True:
    try:
        for i in range(0,20):
            util = int(input("Saisir 20 nombres pour connaitre le + grand :"))
            nombre.append(util)
        plus_grand = max(nombre)
        print(f"Le + grand est {plus_grand}")
        break
    except ValueError:
        print("Valeurs incorrect, reesayer")

