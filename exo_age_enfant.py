#algo qui demande l'age 1 enfant et l'informe de sa categorie

#"poussin" 6 à 7 ans
#"pupille" 8 a 9 ans
#"minime" 10 a 11 ans
#"cadet" apres 12 ans

print("Veuillez entré l'age de votre enfant pour connaitre sa categorie")

age = int(input())

while age >= 6 and age <=12 :
    if age == 6 or age == 7 :
        print("Votre enfant sera dans la catégorie poussin")

    elif age == 8 or age == 9 :
        print("Votre enfant sera dans la catégorie pupille")

    elif age == 10 or age == 11 :
        print("Votre enfant sera dans la catégorie minime")

    else :
        print("Votre enfant sera dans la catégorie cadet")