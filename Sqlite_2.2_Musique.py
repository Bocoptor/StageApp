from tkinter import *
import sqlite3

Mots_entrees = ['User', 'Mot de passe']


# Argument event est souvent utilisé avec TKinter qui car il est lui meme
# une requete utilisé en direct (fenetre lancé), et event est souvent
# utilisé quand on utilise une fonction qui est en standby, qui peut
# s'executé, s'arreté, s'executé a nouveau.
# Ici "User et Mot de passe" sont affiché de base donc la fonction
# est deja utilisé
def clic_d_entrer(event):
    if event.widget.get() in Mots_entrees:
        event.widget.delete(0, "end")  # Supprime le texte au click
        event.widget.config(fg='black')


# fg = foreground c'est pour la couleur de la police
# bg = background pour la couleur de fond
# Config = utilisé pour changé les proprietés du widget

def reinitialiser():
    My_entry1.delete(0, END)
    My_entry2.delete(0, END)
    My_entry3.delete(0, END)
    My_entry4.delete(0, END)
    My_entry5.delete(0, END)


def check_categorie(Login, Mdp):
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Musique.db")
    cur = conn.cursor()
    try:
        cur.execute("SELECT Categorie FROM Pwb WHERE Login = ? AND Mdp = ?",
                    (Login, Mdp))
        resultat = cur.fetchone()
        conn.close()
        if resultat:
            Categorie = resultat[0]
            if Categorie == "admin":
                ouvrir_fenetre_admin()
            else:
                ouvrir_fenetre_user()
        else:
            show_error("Login ou mot de passe incorrect")
    except Exception as ex:
        show_error("Erreur lors de la vérification des données")


def click_login():
    Login = My_entry1.get()
    Mdp = My_entry2.get()
    check_categorie(Login, Mdp)


def ouvrir_fenetre_admin():
    My_fenetre_admin = Toplevel(My_fenetre)
    My_fenetre_admin.geometry("400x550")
    My_fenetre_admin.title("Acces Admin")
    #My_fenetre.after(10, My_fenetre.destroy)

    bg = PhotoImage(file="938222222.png")
    canvas_for_image = Canvas(My_fenetre_admin, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    # Creation d'une variable pour stocker l'image car elle peut être
    # détruite par Python si elle n'est pas conservée dans une variable
    My_fenetre_admin.bg = bg

    rechercher_button = Button(My_fenetre_admin, text="Rechercher", command=filtre_donnee)
    canvas_for_image.create_window(150, 30, window=rechercher_button, anchor="nw")

    create_table_button = Button(My_fenetre_admin, text="Creation de table", command="")
    canvas_for_image.create_window(150, 60, window=create_table_button, anchor="nw")

    del_table_button = Button(My_fenetre_admin, text="Supprimer table", command="")
    canvas_for_image.create_window(150, 90, window=del_table_button, anchor="nw")

    del_user_button = Button(My_fenetre_admin, text="Supprimer utilisateur", command="")
    canvas_for_image.create_window(150, 120, window=del_user_button, anchor="nw")

    quitter_button = Button(My_fenetre_admin, text="Fermer", command=My_fenetre_admin.destroy)
    canvas_for_image.create_window(150, 150, window=quitter_button, anchor="nw")
    #My_fenetre.after(10, My_fenetre.destroy)

def filtre_donnee():
    My_fenetre_filtredonee = Toplevel(My_fenetre)
    My_fenetre_filtredonee.geometry("400x550")
    My_fenetre_filtredonee.title("Recherche")
    #My_fenetre.after(10, My_fenetre.destroy)

    bg = PhotoImage(file="938222222.png")
    canvas_for_image = Canvas(My_fenetre_filtredonee, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    # Creation d'une variable pour stocker l'image car elle peut être
    # détruite par Python si elle n'est pas conservée dans une variable
    My_fenetre_filtredonee.bg = bg

    global My_entry1
    My_entry1 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry1.insert(0, 'compositeur')
    My_entry1.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 20, window=My_entry1, anchor="nw")

    global My_entry2
    My_entry2 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry2.insert(0, 'titre')
    My_entry2.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 50, window=My_entry2, anchor="nw")

    global My_entry3
    My_entry3 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry3.insert(0, 'durée')
    My_entry3.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 80, window=My_entry3, anchor="nw")

    global My_entry4
    My_entry4 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry4.insert(0, 'interprète')
    My_entry4.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 110, window=My_entry4, anchor="nw")

    global My_entry5
    My_entry5 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry5.insert(0, 'annee_naissance')
    My_entry5.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 140, window=My_entry5, anchor="nw")

    global My_entry6
    My_entry5 = Entry(My_fenetre_filtredonee, fg='grey')
    My_entry5.insert(0, 'annee_mort')
    My_entry5.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 170, window=My_entry5, anchor="nw")

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
    compositeur = My_entry1.get()
    titre = My_entry2.get()
    durée = My_entry3.get()
    interprète = My_entry4.get()
    annee_naissance = My_entry5.get()
    annee_mort = My_entry6.get()
    resultats = filtre_donnees(compositeur, titre, durée, interprète, annee_naissance, annee_mort)
    new_window(entre_util)

def create_table():
    pass

def delete_table():
    pass

def delete_user():
    pass




def ouvrir_fenetre_user():
    My_fenetre_user = Toplevel(My_fenetre)
    My_fenetre_user.geometry("400x550")
    My_fenetre_user.title("Acces User")
    # My_fenetre.after(10, My_fenetre.destroy)

    bg = PhotoImage(file="938222222.png")
    canvas_for_image = Canvas(My_fenetre_user, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    # Creation d'une variable pour stocker l'image car elle peut être
    # détruite par Python si elle n'est pas conservée dans une variable
    My_fenetre_user.bg = bg


def insert_donnees(Login, Mdp, Prenom, Nom, Categorie, parent_window):
    if not Login or not Mdp or not Prenom or not Nom or not Categorie:
        show_error("Toutes les cases doivent être remplies.", parent_window)
        return False

        # Vérification de la catégorie
    if Categorie not in ["admin", "user"]:
        show_error("La catégorie doit être 'admin' ou 'user'.", parent_window)
        return False

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Musique.db")
    cur = conn.cursor()
    try:
        cur.execute("""
                INSERT INTO Pwb (Login, Mdp, Prenom, Nom, Categorie)
                VALUES (?, ?, ?, ?, ?)""",
                    (Login, Mdp, Prenom, Nom, Categorie))
        conn.commit()
        conn.close()
        show_error("Inscription réussie", parent_window)
        return True
    except Exception as x:
        print("Erreur d'ajout des données")
        show_error("Erreur d'ajout des données", parent_window)
        return False


def show_error(message, parent_window):
    error_window = Toplevel(parent_window)
    error_window.geometry("400x150")
    error_window.title("Erreur")
    Label(error_window, text=message, width=40, font=('Helvetica', 12)).pack(pady=20)

    # Configurer la fenêtre pour qu'elle soit modale(parent-enfant)
    error_window.transient(parent_window)
    error_window.grab_set()
    parent_window.wait_window(error_window)


#fonction specifique à l'ajout des entrées et ne peut etre mit avec la fonction d'insertion
#de données car les entrées doivent etre appelés avec des arguments dans le cas de verification
#et c'est plus facile a creer une autre fonction auquel on appel la fonction d'insertion de données ici
def inserer():
    Login = My_entry1.get()
    Mdp = My_entry2.get()
    Prenom = My_entry3.get()
    Nom = My_entry4.get()
    Categorie = My_entry5.get()
    insert_donnees(Login, Mdp, Prenom, Nom, Categorie, My_fenetre)
    #if insert_donnees(Login, Mdp, Prenom, Nom, Categorie):
    #   reinitialiser()


def ouvrir_fenetre_inscription():
    My_fenetre_inscription = Toplevel(My_fenetre)
    My_fenetre_inscription.geometry("400x550")
    My_fenetre_inscription.title("Inscription")

    bg = PhotoImage(file="938222222.png")
    canvas_for_image = Canvas(My_fenetre_inscription, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    # Creation d'une variable pour stocker l'image car elle peut être
    # détruite par Python si elle n'est pas conservée dans une variable
    My_fenetre_inscription.bg = bg

    global My_entry1
    My_entry1 = Entry(My_fenetre_inscription, fg='grey')
    My_entry1.insert(0, 'User')
    My_entry1.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 20, window=My_entry1, anchor="nw")

    global My_entry2
    My_entry2 = Entry(My_fenetre_inscription, fg='grey')
    My_entry2.insert(0, 'Mot de passe')
    My_entry2.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 50, window=My_entry2, anchor="nw")

    global My_entry3
    My_entry3 = Entry(My_fenetre_inscription, fg='grey')
    My_entry3.insert(0, 'Prenom')
    My_entry3.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 80, window=My_entry3, anchor="nw")

    global My_entry4
    My_entry4 = Entry(My_fenetre_inscription, fg='grey')
    My_entry4.insert(0, 'Nom')
    My_entry4.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 110, window=My_entry4, anchor="nw")

    global My_entry5
    My_entry5 = Entry(My_fenetre_inscription, fg='grey')
    My_entry5.insert(0, 'Categorie')
    My_entry5.bind('<FocusIn>', clic_d_entrer)
    canvas_for_image.create_window(150, 140, window=My_entry5, anchor="nw")

    inscription_button = Button(My_fenetre_inscription, text="Inscription", command=inserer)
    canvas_for_image.create_window(150, 170, window=inscription_button, anchor="nw")

    quitter_button = Button(My_fenetre_inscription, text="Fermer", command=My_fenetre_inscription.destroy)
    canvas_for_image.create_window(230, 200, window=quitter_button, anchor="nw")
    #My_fenetre.after(10, My_fenetre.destroy)


My_fenetre = Tk()
My_fenetre.geometry("400x650")

bg = PhotoImage(file="938222222.png")

# Creer canvas pour afficher l'image
canvas_for_image = Canvas(My_fenetre, width=400, height=650)
canvas_for_image.pack(fill="both", expand=True)

# Affiher l'image sur la canvas
canvas_for_image.create_image(0, 0, image=bg, anchor="nw")

# Entrée User
# FocusIn est declanché quand on clique dessus (my_entry1) et
# appel la fonction qui est si User est ecrit, le texte est supprimé
# et la couleur de la police passe en noir
# FocusOut est declenché quand le clic(focus) n'est plus dans (my_entry1)
# et quand il n'est plus focus il appel la fonction qui si le champ de saisie
# est vide, User est réinseré et le couleur de la police change en gris
My_entry1 = Entry(My_fenetre, fg='grey')
My_entry1.insert(0, 'User')
My_entry1.bind('<FocusIn>', clic_d_entrer)
canvas_for_image.create_window(150, 20, window=My_entry1, anchor="nw")

# Entrée Mot de passe
# Bind est une fonction tres vaste qui reagis a beaucoup d'evenements.
# Clic de souris, changement de focus, frappe au clavier ect
My_entry2 = Entry(My_fenetre, fg='grey')
My_entry2.insert(0, 'Mot de passe')
My_entry2.bind('<FocusIn>', clic_d_entrer)
canvas_for_image.create_window(150, 50, window=My_entry2, anchor="nw")

# Bouton Login
# anchor = positionnement dans le canvas (ici nw = north west)
login_button = Button(My_fenetre, text="Login", command=click_login)
canvas_for_image.create_window(150, 80, window=login_button, anchor="nw")

inscription_button = Button(My_fenetre, text="Inscription", command=ouvrir_fenetre_inscription)
canvas_for_image.create_window(200, 80, window=inscription_button, anchor="nw")

My_fenetre.mainloop()

conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Musique.db")
cur = conn.cursor()

# Creation tables Pwb (User mdp autorisations ect)
# Pas d'espace apres le nom d'une categorie sinon
# il prend ca pour un type de données
#cur.execute("CREATE TABLE Pwb (ID INTEGER PRIMARY KEY AUTOINCREMENT,"
#            "Login INTEGER, Mdp INTEGER,"
#            "Prenom TEXTE, Nom TEXTE,"
#            "Categorie INTEGER)")
#conn.commit()

#cur.execute("CREATE TABLE Oeuvres (ID INTEGER PRIMARY KEY AUTOINCREMENT,"
#            "Compositeur INTEGER, Titre INTEGER,"
#            "Durée DOUBLE, Interprète INTEGER)")
#conn.commit()

#cur.execute("CREATE TABLE Compositions (ID INTEGER PRIMARY KEY AUTOINCREMENT,"
#            "Compositeur INTEGER, Annee_naissance INTEGER,"
#            "Annee_mort INTEGER)")
#conn.commit()

# Creation Users
# Triple guillemets si insertion sur plusieurs lignes
#cur.execute("""INSERT INTO Pwb (Login, Mdp, Prenom, Nom, Categorie) VALUES
#('Administrateur', 'isfceadmin', 'Quentin', 'Alvarez', 'admin'),
#('Quentin', 'isfceuser', 'Quentin', 'Diaz', 'user')""")
#conn.commit()

#cur.execute("""INSERT INTO Compositions (Compositeur, Annee_naissance, Annee_mort) VALUES
#('Mozart', '1756', '1791'),
#('Beethoven', '1770', '1827'),
#('Haendel','1685','1759'),
#('Schubert','1797','1828'),
#('Vivaldi', '1678', '1741'),
#('Monteverdi', '1567', '1643'),
#('Chopin', '1810', '1849'),
#('Bach', '1685', '1750'),
#('Shostakovich', '1906', '1975')""")
#conn.commit()

#cur.execute("""INSERT INTO Oeuvres (Compositeur, Titre, Durée, Interprète) VALUES
#('Vivaldi', 'Les quatre saisons', '20', 'T. Pinnock'),
#('Mozart', 'Concerto piano N°12', '25', 'M. Perahia'),
#('Brahms','Concerto violon N°2','40', 'A. Grumiaux'),
#('Beethoven','Sonate "au clair de lune"','14', 'W. Kempf'),
#('Beethoven', 'Sonate "pathétique"', '17', 'W. Kempf'),
#('Schubert', 'Quintette "la truite"', '39', 'SE of London'),
#('Haydn', 'La création', '109', 'H. Von Karajan'),
#('Chopin', 'Concerto piano N°1', '42', 'M.J. Pires'),
#('Bach', 'Toccata & fugue', '9', 'P. Burmester'),
#('Beethoven', 'Concerto piano N°4', '33', 'M. Pollini'),
#('Mozart', 'Symphonie N°40', '29', 'F. Bruggen'),
#('Mozart', 'Concerto piano N°22', '35', 'S. Richter'),
#('Beethoven', 'Concerto piano N°3', '37', 'S. Richter')""")
#conn.commit()
