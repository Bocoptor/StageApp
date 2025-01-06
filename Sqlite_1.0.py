import sqlite3

# r devant les " pour qu'ils prennent en compte le chemin d'acces
conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")

cur = conn.cursor()

#creation informations en demandant a l'utilisateur

#age = input("Saisir votre age :")
#nom = input("Saisir votre nom :")
#taille = input("Saisir votre taille :")

#cur.execute("CREATE TABLE membres_new (id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER, nom TEXT, taille REAL)")
#for i in range(4):
#      cur.execute("INSERT INTO membres_new(age,nom,taille) VALUES(?,?,?)", (id,age,nom,taille))
#conn.commit()

#copier données table vers une autre
#cur.execute('''
#   INSERT INTO membres_new (nom, age, taille)
#    SELECT nom, age, taille FROM membres
#''')
#conn.commit()

#affichage des informations dans la console
#cur.execute("SELECT * FROM membres")

#1 methode
#for l in cur:
#print(l)

#2 methode
#listeMembres = list(cur)
#i = 0
#while i < 3 :
# print(f"Les membres sont : {listeMembres[i]}")
# i += 1