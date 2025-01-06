from tkinter import *
import sqlite3


def reinitialiser():
    My_entry1.delete(0,END)
    My_entry2.delete(0,END)
    My_entry3.delete(0,END)

def delete_donnees(Nom, Prenom, Ville):
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM SaisieIdentification 
        WHERE Nom = ? AND Prenom = ? AND Ville = ?""",
                   (Nom, Prenom, Ville))
    conn.commit()
    conn.close()

def delete():
    Nom = My_entry1.get()
    Prenom = My_entry2.get()
    Ville = My_entry3.get()
    delete_donnees(Nom, Prenom, Ville)

def insert_donnees(Nom, Prenom, Ville):
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")
    cur = conn.cursor()
    try:
        cur.execute("""
                INSERT INTO SaisieIdentification (Nom, Prenom, Ville)
                VALUES (?, ?, ?)""",
                (Nom, Prenom, Ville))
        conn.commit()
        conn.close()
        return True
    except Exception as x:
        print("Erreur d'ajout des données")

def inserer():
    Nom = My_entry1.get()
    Prenom = My_entry2.get()
    Ville = My_entry3.get()
    #insert_donnees(Nom, Prenom, Ville)
    if insert_donnees(Nom, Prenom, Ville):
        reinitialiser()
    #Creer une nvelle fenetre qui s'ouvre
    #My_label1 = My_entry1.get()
    #My_label2 = My_entry2.get()
    #My_label3 = My_entry3.get()

def filtre_donnees(Nom, Prenom, Ville):
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")
    cur = conn.cursor()
    requete = """SELECT *
                 FROM SaisieIdentification
                 WHERE 1=1""" # 1=1 car en dessous on lui met des conditions
                              # pour chaque champs et celà permet que les requetes
                              # soient toujours vrai
    liste_param = []
    if Nom:
        requete += " AND Nom = ?"
        liste_param.append(Nom)
    if Prenom:
        requete += " AND Prenom = ?"
        liste_param.append(Prenom)
    if Ville:
        requete += " AND Ville = ?"
        liste_param.append(Ville)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    affichage = cur.fetchall()

    conn.commit()
    conn.close()
    return affichage

def lire_filtre_donnees():
    Nom = My_entry1.get()
    Prenom = My_entry2.get()
    Ville = My_entry3.get()
    entre_util = filtre_donnees(Nom, Prenom, Ville)
    new_window(entre_util)

def new_window(entre_util):
    # Toplevel permet de creer des fenetres supplementaires
    window = Toplevel()
    window.geometry("300x250")
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(window, yscrollcommand=scrollbar.set)
    for row in entre_util:
        listbox.insert(END, row)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar.config(command=listbox.yview)

My_fenetre = Tk()
My_fenetre.geometry("550x300")
My_fenetre.title("Exercice 1.1")

#Creation d'un label pour afficher l'image.
#les labels sont des widgets polyvalents qui peuvent
#contenir du texte, des images et d'autres éléments visuels.
My_image = PhotoImage(file="ex1_1.png")
My_image_label = Label(My_fenetre, image=My_image)
My_image_label.grid(row=0, column=5, padx=10, pady=10)

left_frame = Frame(My_fenetre)
left_frame.grid(row=0, column=0, padx=10, pady=10)
text_a_afficher = Frame(My_fenetre)
text_a_afficher.grid()
bottom_frame = Frame(My_fenetre)
bottom_frame.grid(row=1, column=0, columnspan=4, pady=20)
Label_text = Label(text_a_afficher, text="")
Label_text.grid()

#sticky = emplacement (est, ouest, nord, sud)
#columnspan = occupation de colonne qu'il prend
My_text1 = Label(left_frame, text="Nom")
My_text1.grid(row=0, column=0)
My_entry1 = Entry(left_frame)
My_entry1.grid(row=0, column=1)

My_text2 = Label(left_frame, text="Prenom")
My_text2.grid(row=1, column=0)
My_entry2 = Entry(left_frame)
My_entry2.grid(row=1, column=1)

My_text3 = Label(left_frame, text="Ville")
My_text3.grid(row=2, column=0)
My_entry3 = Entry(left_frame)
My_entry3.grid(row=2, column=1)


My_bouton1 = Button(bottom_frame, text="Insérer", command=inserer)
My_bouton1.grid(row=0, column=0, padx=5)

My_bouton2 = Button(bottom_frame, text="Lire", command=lire_filtre_donnees)
My_bouton2.grid(row=0, column=1, padx=5)

My_bouton3 = Button(bottom_frame, text="Supprimer", command=delete)
My_bouton3.grid(row=0, column=2, padx=5)

My_bouton4 = Button(bottom_frame, text="Reinitialiser", command=reinitialiser)
My_bouton4.grid(row=0, column=3, padx=5)

My_bouton5 = Button(bottom_frame, text="Quitter", command=My_fenetre.destroy)
My_bouton5.grid(row=0, column=4, padx=5)
#My_bouton3.place(x=500, y=100)

My_fenetre.mainloop()

conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\fichierDonnees.db")
cur = conn.cursor()

#cur.execute("CREATE TABLE SaisieIdentification (ID INTEGER PRIMARY KEY AUTOINCREMENT, Prenom TEXT, Nom TEXT, Ville TEXT)")
#conn.commit()