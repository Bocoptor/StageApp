nombre = int(input("Entrer nombre :"))

for i in range(0, nombre):
    if i < nombre:
        i += 1
    print(f"{i} X", end=" ")
