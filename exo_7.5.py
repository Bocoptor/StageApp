#print("veuillez entré la table de multiplication à afficher")
#n = int(input())

#multi = range(1,10)
#for x in multi:
#    result = n * x
#    print(n,"*",x,"=",result)


print("veuillez entré la table de multiplication à afficher")
n = int(input())

temp = 1

while temp < 9:
    result = n * temp
    print(n,"*",temp,"=",result)
    temp += 1

print(list(range(9,99,9)))