import sqlite3

conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")

cur = conn.cursor()

#nom = input("Saisir votre nom :")
#age = input("Saisir votre age :")
#taille = input("Saisir votre taille :")

#cur.execute("INSERT INTO membres(age,nom,taille) VALUES(?,?,?)", (age,nom,taille))
#conn.commit()

cur.execute("""UPDATE membres_new 
            SET nom='Dupont_update'
            WHERE id = 1 AND nom='Dupont1'""")
conn.commit()

#Les triples guillemets (""") en Python sont utilisés
#pour créer des chaînes de caractères multi-lignes.
#cur.execute("""SELECT id, nom, age, taille
#            FROM membres_new
#            WHERE id = 1 AND nom = 'Dupont1' AND age = 21 AND taille = 1.95""")

for k in cur :
    print(k)