from tkinter import *
from tkinter import messagebox  # pour les messages de succes ou erreur
from tkinter import ttk  # pour la creation des treeview c'est plus facile
import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
import sqlite3
from flask import Flask

from app import app

'''
1. Table Livre :
    a. Titre
    b. Auteur
    c. Année
    d. Isbn
2. Table membre :
    a. Nom
    b. Prenom
    c. Email
    d. telephone
3. Table emprunt :
    a. Date_emprunt
    b. Date_retour

1. Gestion des livres :
    a. Ajouter un nouveau livre.
    b. Modifier les informations d'un livre.
    c. Supprimer un livre.
    d. Afficher la liste des livres disponibles.

2. Gestion des membres :
    a. Ajouter un nouveau membre.
    b. Modifier les informations d'un membre.
    c. Supprimer un membre.
    d. Afficher la liste des membres.

3. Gestion des emprunts :
    a. Enregistrer un nouvel emprunt.
    b. Retourner un livre.
    c. Afficher la liste des emprunts en cours.
'''

conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Login"
            "(Login INTEGER, Mdp INTEGER)")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS Livre"
            "(ISBN INTEGER PRIMARY KEY,"
            "Titre INTEGER,"
            "Auteur INTEGER,"
            "Annee INTEGER)")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS Membre"
            "(ID_Membre INTEGER PRIMARY KEY AUTOINCREMENT,"
            "Nom TEXT,"
            "Prenom TEXT,"
            "Email INTEGER,"
            "Telephone INTEGER)")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS Emprunt"
            "(ID_Emprunt INTEGER PRIMARY KEY,"
            "ISBN INTEGER,"
            "ID_Membre INTEGER,"
            "Date_emprunt DATE,"
            "Date_retour DATE,"
            "FOREIGN KEY (ISBN) REFERENCES Livre(ISBN),"
            "FOREIGN KEY (ID_Membre) REFERENCES Membre(ID_Membre))")
conn.commit()

My_fenetre_main = ctk.CTk()
My_fenetre_main.geometry("1280x710")
My_fenetre_main.title("BibliEtterbeek")
bg = PhotoImage(file="Fenetre_main_edited3.png")

canvas_for_image = Canvas(My_fenetre_main, width=1280, height=710)
canvas_for_image.pack(fill="both", expand=True)
# Afficher l'image sur le canvas
canvas_for_image.create_image(0, 0, image=bg, anchor="nw")


# Fonction utilitaire pour afficher les messages d'erreur
def show_error(message):
    error_window = Toplevel()
    error_window.geometry("400x150")
    error_window.title("Erreur")
    Label(error_window, text=message, width=40, font=('Helvetica', 12)).pack(pady=20)


# Gestion des Livres
def clic_btn_livre():
    My_fenetre_clic_btn_livre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_livre.geometry("1000x562")
    My_fenetre_clic_btn_livre.title("Gestion des livres")

    bg = PhotoImage(file="livre_main.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_livre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_livre.bg = bg

    ajouter_button = ctk.CTkButton(My_fenetre_clic_btn_livre,
                                   text="Ajouter un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_ajout_livre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 100, window=ajouter_button, anchor="nw")

    modifier_button = ctk.CTkButton(My_fenetre_clic_btn_livre,
                                   text="Modifier un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_modifier_livre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(560, 100, window=modifier_button, anchor="nw")

    supprimer_button = ctk.CTkButton(My_fenetre_clic_btn_livre,
                                   text="Supprimer un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_supprimer_livre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 350, window=supprimer_button, anchor="nw")

    disponibilite_button = ctk.CTkButton(My_fenetre_clic_btn_livre,
                                   text="Afficher les livres",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=afficher_livres_disponibles,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(560, 350, window=disponibilite_button, anchor="nw")

    retour_livre_button = ctk.CTkButton(My_fenetre_clic_btn_livre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_livre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="silver",
                                   corner_radius=5,
                                   border_width=2,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(450, 500, window=retour_livre_button, anchor="nw")


def clic_entrer_ajout_livre(event):
    if event.widget.get() in ["Titre", "Auteur", "Année", "ISBN"]:
        event.widget.delete(0, "end")  # Supprime le texte au click
        event.widget.config(fg='black')

def clic_sortie_ajout_livre(event):
    default_texts = {
        My_entry1_ajout_livre: 'Titre',
        My_entry2_ajout_livre: 'Auteur',
        My_entry3_ajout_livre: 'Année',
        My_entry4_ajout_livre: 'ISBN'
    }
    if event.widget.get() == '':
        event.widget.insert(0, default_texts[event.widget])
        event.widget.config(fg='grey')

def clic_btn_ajout_livre():
    My_fenetre_clic_btn_ajout_livre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_ajout_livre.geometry("400x534")
    My_fenetre_clic_btn_ajout_livre.title("Ajouter un Livre")

    bg = PhotoImage(file="ajout_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_ajout_livre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_ajout_livre.bg = bg

    global My_entry1_ajout_livre, My_entry2_ajout_livre, My_entry3_ajout_livre, My_entry4_ajout_livre

    My_entry1_ajout_livre = Entry(My_fenetre_clic_btn_ajout_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_ajout_livre.insert(0, 'Titre')
    My_entry1_ajout_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    My_entry1_ajout_livre.bind("<FocusOut>", clic_sortie_ajout_livre)
    canvas_for_image.create_window(90, 50, window=My_entry1_ajout_livre, anchor="nw")

    My_entry2_ajout_livre = Entry(My_fenetre_clic_btn_ajout_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='sunken',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_ajout_livre.insert(0, 'Auteur')
    My_entry2_ajout_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    My_entry2_ajout_livre.bind("<FocusOut>", clic_sortie_ajout_livre)
    canvas_for_image.create_window(90, 100, window=My_entry2_ajout_livre, anchor="nw")

    My_entry3_ajout_livre = Entry(My_fenetre_clic_btn_ajout_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='ridge',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_ajout_livre.insert(0, 'Année')
    My_entry3_ajout_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    My_entry3_ajout_livre.bind("<FocusOut>", clic_sortie_ajout_livre)
    canvas_for_image.create_window(90, 150, window=My_entry3_ajout_livre, anchor="nw")

    My_entry4_ajout_livre = Entry(My_fenetre_clic_btn_ajout_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='raised',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_ajout_livre.insert(0, 'ISBN')
    My_entry4_ajout_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    My_entry4_ajout_livre.bind("<FocusOut>", clic_sortie_ajout_livre)
    canvas_for_image.create_window(90, 200, window=My_entry4_ajout_livre, anchor="nw")

    valider_ajout_livre_button = ctk.CTkButton(My_fenetre_clic_btn_ajout_livre,
                                   text="Ajouter un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_ajout_livre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 300, window=valider_ajout_livre_button, anchor="nw")

    retour_ajout_livre_button = ctk.CTkButton(My_fenetre_clic_btn_ajout_livre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_ajout_livre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 480, window=retour_ajout_livre_button, anchor="nw")


def fonction_ajout_livre():
    Titre = My_entry1_ajout_livre.get()
    Auteur = My_entry2_ajout_livre.get()
    Annee = My_entry3_ajout_livre.get()
    ISBN = My_entry4_ajout_livre.get()

    try:
        Annee = int(Annee)
        ISBN = int(ISBN)
    except ValueError:
        show_error("Année et ISBN doivent être des nombres entiers")
        return False

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO Livre (Titre, Auteur, Annee, ISBN) "
                    "VALUES (?, ?, ?, ?)",
                    (Titre, Auteur, Annee, ISBN))
        conn.commit()
        conn.close()
        print("Ajout livre reussi")
        messagebox.showinfo("Ajout done",
                            "Ajout du livre reussi \n\n"
                            f"Titre : {Titre}\n"
                            f"Auteur : {Auteur}\n"
                            f"Année : {Annee}\n"
                            f"ISBN : {ISBN}\n")
        return True
    except Exception as e:
        print("Erreur d'ajout des données", e)
        show_error("Erreur d'ajout des données")
        return False
    # Permet de vraiment fermer la connexion a la base de donnée
    # en cas d'erreur d'ajout de donnée, elle ne se fermait plus
    # donc impossibilité de rajouté un livre je devais redemarré l'appli
    finally:
        if conn:
            conn.close()


def clic_btn_modifier_livre():
    My_fenetre_clic_btn_modifier_livre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_modifier_livre.geometry("400x517")
    My_fenetre_clic_btn_modifier_livre.title("Rechercher un Livre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_modifier_livre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_modifier_livre.bg = bg

    global My_entry1_recher_livre, My_entry2_recher_livre, My_entry3_recher_livre, My_entry4_recher_livre

    My_entry1_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_livre.insert(0, 'Titre')
    My_entry1_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_livre, anchor="nw")

    My_entry2_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_livre.insert(0, 'Auteur')
    My_entry2_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_livre, anchor="nw")

    My_entry3_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_livre.insert(0, 'Année')
    My_entry3_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_livre, anchor="nw")

    My_entry4_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_livre.insert(0, 'ISBN')
    My_entry4_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_livre, anchor="nw")

    recherch_modif_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_livre,
                                   text="Rechercher un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_rechercher_modifier_livre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 300, window=recherch_modif_livre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_livre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_modifier_livre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")



def fonction_rechercher_modifier_livre():
    Titre = My_entry1_recher_livre.get()
    Auteur = My_entry2_recher_livre.get()
    Annee = My_entry3_recher_livre.get()
    ISBN = My_entry4_recher_livre.get()

    if Annee and not Annee.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "L'année doit être un nombre entier.")
        return
    if ISBN and not ISBN.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "L'ISBN doit être un nombre entier.")
        return
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    # Obligation de mettre les colonnes une à une au lieu de SELECT * car pour l'affichage de la
    # recherche avec la boucle il parcours les colonnes mais pas forcement dans l'ordre par
    # defaut, ici il a surement prit l'ISBN en premier car clef primaire, du coup c'était plus le
    # titre en premier mais l'ISBN et tout etait decallé
    requete = """SELECT Titre, Auteur, Annee, ISBN
                 FROM Livre
                 WHERE 1=1"""  # 1=1 car en dessous on lui met des conditions  pour chaque
    # champs et celà permet que les requetes soient toujours vrai
    liste_param = []
    if Titre:
        requete += " AND Titre = ?"
        liste_param.append(Titre)
    if Auteur:
        requete += " AND Auteur = ?"
        liste_param.append(Auteur)
    if Annee:
        requete += " AND Annee = ?"
        liste_param.append(Annee)
    if ISBN:
        requete += " AND ISBN = ?"
        liste_param.append(ISBN)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # fetchone récupère seulement un resultat
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    livre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if livre_trouver:
        afficher_details_livre_modifier(livre_trouver)
    else:
        messagebox.showinfo("Aucun livre trouvé",
                            "Aucun livre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_livre_modifier(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    style = ttk.Style()

    # Personnalisation des couleurs du Treeview
    style.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    style.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("Titre", "Auteur", "Année", "ISBN"),
                        show="headings", style="Custom.Treeview")
    tree.heading("Titre", text="Titre")
    tree.heading("Auteur", text="Auteur")
    tree.heading("Année", text="Année")
    tree.heading("ISBN", text="ISBN")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_modifier = ctk.CTkButton(details_fenetre,
                                   text="Modifier",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=lambda: modifier_livre_selectionne(tree),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_modifier.pack(pady=10) #utilisation ici de pack pour toplevel


def modifier_livre_selectionne(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur",
                             "Veuillez sélectionner un livre à modifier.")
        return

    livre = tree.item(selected_item, "values")
    titre, auteur, annee, isbn = livre

    fenetre_modif = Toplevel()
    fenetre_modif.title("Modifier le Livre")
    fenetre_modif.geometry("870x320")

    #fenetre_modif.config(bg="silver")

    label_font = ('comic sans ms', 15, "normal")

    Label(fenetre_modif, text="Titre actuel", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    titre_entry1 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    titre_entry1.grid(row=0, column=1, padx=10, pady=5)
    titre_entry1.insert(0, titre)

    Label(fenetre_modif, text="Nouveau titre", font=label_font).grid(row=0, column=2, padx=10, pady=5, sticky='w')
    titre_entry2 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    titre_entry2.grid(row=0, column=3, padx=10, pady=5)
    titre_entry2.insert(0, titre)

    Label(fenetre_modif, text="Auteur actuel", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    auteur_entry1 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    auteur_entry1.grid(row=1, column=1, padx=10, pady=5)
    auteur_entry1.insert(0, auteur)

    Label(fenetre_modif, text="Nouvel auteur", font=label_font).grid(row=1, column=2, padx=10, pady=5, sticky='w')
    auteur_entry2 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    auteur_entry2.grid(row=1, column=3, padx=10, pady=5)
    auteur_entry2.insert(0, auteur)

    Label(fenetre_modif, text="Année actuelle", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    annee_entry1 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    annee_entry1.grid(row=2, column=1, padx=10, pady=5)
    annee_entry1.insert(0, annee)

    Label(fenetre_modif, text="Nouvelle année", font=label_font).grid(row=2, column=2, padx=10, pady=5, sticky='w')
    annee_entry2 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    annee_entry2.grid(row=2, column=3, padx=10, pady=5)
    annee_entry2.insert(0, annee)

    Label(fenetre_modif, text="ISBN actuel", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
    isbn_entry1 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    isbn_entry1.grid(row=3, column=1, padx=10, pady=5)
    isbn_entry1.insert(0, isbn)

    Label(fenetre_modif, text="Nouvel ISBN", font=label_font).grid(row=3, column=2, padx=10, pady=5, sticky='w')
    isbn_entry2 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    isbn_entry2.grid(row=3, column=3, padx=10, pady=5)
    isbn_entry2.insert(0, isbn)

    def valider_modification():
        nouveau_titre = titre_entry2.get()
        nouvel_auteur = auteur_entry2.get()
        nouvelle_annee = annee_entry2.get()
        nouveau_isbn = isbn_entry2.get()

        if not nouvelle_annee.isdigit() or not nouveau_isbn.isdigit():
            messagebox.showerror("Erreur de saisie",
                                 "L'année et l'ISBN doivent être des nombres entiers.")
            return

        conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
        cur = conn.cursor()
        cur.execute("""UPDATE Livre
                       SET Titre = ?, Auteur = ?, Annee = ?, ISBN = ?
                       WHERE ISBN = ?""",
                    (nouveau_titre, nouvel_auteur, nouvelle_annee, nouveau_isbn, isbn))
        conn.commit()
        conn.close()

        messagebox.showinfo("Modification réussie",
                            "Le livre a été modifié avec succès.")
        fenetre_modif.destroy()

    bouton_valider = ctk.CTkButton(fenetre_modif,
                                   text="Valider modification",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=valider_modification,
                                   height=50,
                                   width=450,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=5,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_valider.grid(row=4, columnspan=20, pady=20)

    retour_button = ctk.CTkButton(fenetre_modif,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fenetre_modif.destroy,
                                   height=25,
                                   width=60,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=2,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    retour_button.grid(row=5, columnspan=20, pady=0)

def clic_btn_supprimer_livre():
    My_fenetre_clic_btn_supprimer_livre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_supprimer_livre.geometry("400x517")
    My_fenetre_clic_btn_supprimer_livre.title("Rechercher un Livre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_supprimer_livre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_supprimer_livre.bg = bg

    global My_entry1_recher_livre, My_entry2_recher_livre, My_entry3_recher_livre, My_entry4_recher_livre

    My_entry1_recher_livre = Entry(My_fenetre_clic_btn_supprimer_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_livre.insert(0, 'Titre')
    My_entry1_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_livre, anchor="nw")

    My_entry2_recher_livre = Entry(My_fenetre_clic_btn_supprimer_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_livre.insert(0, 'Auteur')
    My_entry2_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_livre, anchor="nw")

    My_entry3_recher_livre = Entry(My_fenetre_clic_btn_supprimer_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_livre.insert(0, 'Année')
    My_entry3_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_livre, anchor="nw")

    My_entry4_recher_livre = Entry(My_fenetre_clic_btn_supprimer_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_livre.insert(0, 'ISBN')
    My_entry4_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_livre, anchor="nw")

    recherch_supr_livre_button = ctk.CTkButton(My_fenetre_clic_btn_supprimer_livre,
                                   text="Rechercher un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_rechercher_supprimer_livre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 300, window=recherch_supr_livre_button, anchor="nw")

    retour_supprimer_livre_button = ctk.CTkButton(My_fenetre_clic_btn_supprimer_livre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_supprimer_livre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_supprimer_livre_button, anchor="nw")


def fonction_rechercher_supprimer_livre():
    Titre = My_entry1_recher_livre.get()
    Auteur = My_entry2_recher_livre.get()
    Annee = My_entry3_recher_livre.get()
    ISBN = My_entry4_recher_livre.get()

    if Annee and not Annee.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "L'année doit être un nombre entier.")
        return
    if ISBN and not ISBN.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "L'ISBN doit être un nombre entier.")
        return
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    # Obligation de mettre les colonnes une à une au lieu de SELECT * car pour l'affichage de la
    # recherche avec la boucle il parcours les colonnes mais pas forcement dans l'ordre par
    # defaut, ici il a surement prit l'ISBN en premier car clef primaire, du coup c'était plus le
    # titre en premier mais l'ISBN et tout etait decallé
    requete = """SELECT Titre, Auteur, Annee, ISBN
                 FROM Livre
                 WHERE 1=1"""  # 1=1 car en dessous on lui met des conditions  pour chaque
    # champs et celà permet que les requetes soient toujours vrai
    liste_param = []
    if Titre:
        requete += " AND Titre = ?"
        liste_param.append(Titre)
    if Auteur:
        requete += " AND Auteur = ?"
        liste_param.append(Auteur)
    if Annee:
        requete += " AND Annee = ?"
        liste_param.append(Annee)
    if ISBN:
        requete += " AND ISBN = ?"
        liste_param.append(ISBN)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # fetchone récupère seulement un resultat
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    livre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if livre_trouver:
        afficher_details_livre_supprimer(livre_trouver)
    else:
        messagebox.showinfo("Aucun livre trouvé",
                            "Aucun livre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_livre_supprimer(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    style = ttk.Style()

    # Personnalisation des couleurs du Treeview
    style.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    style.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("Titre", "Auteur", "Année", "ISBN"), show="headings", style="Custom.Treeview")
    tree.heading("Titre", text="Titre")
    tree.heading("Auteur", text="Auteur")
    tree.heading("Année", text="Année")
    tree.heading("ISBN", text="ISBN")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_supprimer = ctk.CTkButton(details_fenetre,
                                   text="Supprimer",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=lambda: fonction_supprimer_livre(tree),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#FF1100'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_supprimer.pack(pady=10) #utilisation ici de pack pour toplevel


def fonction_supprimer_livre(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur",
                             "Veuillez sélectionner un livre à supprimer.")
        return

    livre = tree.item(selected_item, "values")
    Titre, Auteur, Annee, ISBN = livre

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Livre "
                    "WHERE Titre = ? AND Auteur = ? AND Annee = ? AND ISBN = ?",
                    (Titre, Auteur, Annee, ISBN))
        conn.commit()
        conn.close()
        print("Suppression livre reussi")
        messagebox.showinfo("Delete done",
                            "Suppression du livre reussi \n\n"
                            f"Titre : {Titre}\n"
                            f"Auteur : {Auteur}\n"
                            f"Année : {Annee}\n"
                            f"ISBN : {ISBN}\n")
        tree.delete(selected_item)

    except Exception as e:
        print("Erreur de suppression des données", e)
        show_error("Erreur de suppression des données")
        return False
    # Permet de vraiment fermer la connexion a la base de donnée
    # en cas d'erreur de suppression, elle ne se fermait plus
    # donc impossibilité de rajouté un livre je devais redemarré l'appli
    finally:
        conn.close()
        if conn:
            pass


def afficher_livres_disponibles():
    # Sélectionner tous les livres qui ne sont pas dans la table Emprunt
    cur.execute("""SELECT L.ISBN, L.Titre, L.Auteur, L.Annee,
               CASE WHEN E.ISBN IS NULL THEN 'Oui' ELSE 'Non' END AS Disponibilite
               FROM Livre L
               LEFT JOIN Emprunt E ON L.ISBN = E.ISBN""")

    # Récupération de tous les résultats de la requête
    livres_disponibles = cur.fetchall()

    # Création de la fenêtre pour afficher les détails des livres disponibles
    details_fenetre = Toplevel()
    details_fenetre.title("Livres Disponibles")

    style = ttk.Style()

    # Personnalisation des couleurs du Treeview
    style.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    style.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("ISBN", "Titre", "Auteur", "Annee", "Disponibilite"), show="headings", style="Custom.Treeview")
    tree.heading("ISBN", text="ISBN")
    tree.heading("Titre", text="Titre")
    tree.heading("Auteur", text="Auteur")
    tree.heading("Annee", text="Année")
    tree.heading("Disponibilite", text="Disponibilité")

    for resultat in livres_disponibles:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)


def clic_btn_membre():
    My_fenetre_clic_btn_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_membre.geometry("1000x560")
    My_fenetre_clic_btn_membre.title("Gestion des membres")

    bg = PhotoImage(file="membre_main.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_membre.bg = bg


    ajouter_button = ctk.CTkButton(My_fenetre_clic_btn_membre,
                                   text="Ajouter un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_ajout_membre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 100, window=ajouter_button, anchor="nw")

    modifier_button = ctk.CTkButton(My_fenetre_clic_btn_membre,
                                   text="Modifier un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_modifier_membre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(560, 100, window=modifier_button, anchor="nw")

    supprimer_button = ctk.CTkButton(My_fenetre_clic_btn_membre,
                                   text="Supprimer un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_supprimer_membre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 350, window=supprimer_button, anchor="nw")

    disponibilite_button = ctk.CTkButton(My_fenetre_clic_btn_membre,
                                   text="Afficher les membres",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_afficher_membre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(560, 350, window=disponibilite_button, anchor="nw")

    retour_membre_button = ctk.CTkButton(My_fenetre_clic_btn_membre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_membre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="silver",
                                   corner_radius=5,
                                   border_width=2,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(450, 500, window=retour_membre_button, anchor="nw")

def clic_entrer_ajout_membre(event):
    if event.widget.get() in ["Nom", "Prenom", "Email", "Telephone", "ID_Membre"]:
        event.widget.delete(0, "end")  # Supprime le texte au click
        event.widget.config(fg='black')

def clic_sortie_ajout_membre(event):
    default_texts = {
        My_entry1_ajout_membre: 'Nom',
        My_entry2_ajout_membre: 'Prenom',
        My_entry3_ajout_membre: 'Email',
        My_entry4_ajout_membre: 'Telephone'
    }
    if event.widget.get() == '':
        event.widget.insert(0, default_texts[event.widget])
        event.widget.config(fg='grey')
def clic_btn_ajout_membre():
    My_fenetre_clic_btn_ajout_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_ajout_membre.geometry("400x534")
    My_fenetre_clic_btn_ajout_membre.title("Ajouter un Membre")

    bg = PhotoImage(file="membre_ajout.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_ajout_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_ajout_membre.bg = bg

    global My_entry1_ajout_membre, My_entry2_ajout_membre, My_entry3_ajout_membre, My_entry4_ajout_membre

    My_entry1_ajout_membre = Entry(My_fenetre_clic_btn_ajout_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='groove',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_ajout_membre.insert(0, 'Nom')
    My_entry1_ajout_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    My_entry1_ajout_membre.bind("<FocusOut>", clic_sortie_ajout_membre)
    canvas_for_image.create_window(90, 50, window=My_entry1_ajout_membre, anchor="nw")

    My_entry2_ajout_membre = Entry(My_fenetre_clic_btn_ajout_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='groove',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_ajout_membre.insert(0, 'Prenom')
    My_entry2_ajout_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    My_entry2_ajout_membre.bind("<FocusOut>", clic_sortie_ajout_membre)
    canvas_for_image.create_window(90, 100, window=My_entry2_ajout_membre, anchor="nw")

    My_entry3_ajout_membre = Entry(My_fenetre_clic_btn_ajout_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='groove',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_ajout_membre.insert(0, 'Email')
    My_entry3_ajout_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    My_entry3_ajout_membre.bind("<FocusOut>", clic_sortie_ajout_membre)
    canvas_for_image.create_window(90, 150, window=My_entry3_ajout_membre, anchor="nw")

    My_entry4_ajout_membre = Entry(My_fenetre_clic_btn_ajout_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='groove',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_ajout_membre.insert(0, 'Telephone')
    My_entry4_ajout_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    My_entry4_ajout_membre.bind("<FocusOut>", clic_sortie_ajout_membre)
    canvas_for_image.create_window(90, 200, window=My_entry4_ajout_membre, anchor="nw")

    valider_ajout_membre_button = ctk.CTkButton(My_fenetre_clic_btn_ajout_membre,
                                   text="Ajouter un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_ajout_membre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 300, window=valider_ajout_membre_button, anchor="nw")

    retour_ajout_membre_button = ctk.CTkButton(My_fenetre_clic_btn_ajout_membre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_ajout_membre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 480, window=retour_ajout_membre_button, anchor="nw")


def fonction_ajout_membre():
    Nom = My_entry1_ajout_membre.get()
    Prenom = My_entry2_ajout_membre.get()
    Email = My_entry3_ajout_membre.get()
    Telephone = My_entry4_ajout_membre.get()

    try:
        Telephone = int(Telephone)
    except ValueError:
        messagebox.showinfo("Erreur",
                            "Le numéro de téléphone doit être des nombres entiers\n\n"
                            f"Telephone : {Telephone}\n")
        return False

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO Membre (Nom, Prenom, Email, Telephone)"
                    "VALUES (?, ?, ?, ?)",
                    (Nom, Prenom, Email, Telephone))
        conn.commit()
        conn.close()
        print("Ajout membre reussi")
        messagebox.showinfo("Ajout done",
                            "Ajout du membre reussi \n\n"
                            f"Nom : {Nom}\n"
                            f"Prenom : {Prenom}\n"
                            f"Email : {Email}\n"
                            f"Telephone : {Telephone}\n")
        return True
    except Exception as e:
        print("Erreur d'ajout des données", e)
        show_error("Erreur d'ajout des données")
        return False
    # Permet de vraiment fermer la connexion a la base de donnée
    # en cas d'erreur d'ajout de donnée, elle ne se fermait plus
    # donc impossibilité de rajouté un livre je devais redemarré l'appli
    finally:
        if conn:
            conn.close()


def clic_btn_modifier_membre():
    My_fenetre_clic_btn_modifier_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_modifier_membre.geometry("400x517")
    My_fenetre_clic_btn_modifier_membre.title("Rechercher un membre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_modifier_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_modifier_membre.bg = bg

    global My_entry1_recher_membre, My_entry2_recher_membre, My_entry3_recher_membre, \
        My_entry4_recher_membre, My_entry5_recher_membre

    My_entry1_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_membre.insert(0, 'Nom')
    My_entry1_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_membre, anchor="nw")

    My_entry2_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_membre.insert(0, 'Prenom')
    My_entry2_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_membre, anchor="nw")

    My_entry3_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_membre.insert(0, 'Email')
    My_entry3_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_membre, anchor="nw")

    My_entry4_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_membre.insert(0, 'Telephone')
    My_entry4_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_membre, anchor="nw")

    My_entry5_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry5_recher_membre.insert(0, 'ID_Membre')
    My_entry5_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 250, window=My_entry5_recher_membre, anchor="nw")

    recherch_modif_membre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_membre,
                                   text="Rechercher un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_rechercher_modifier_membre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 350, window=recherch_modif_membre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_membre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_modifier_membre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")


def fonction_rechercher_modifier_membre():
    Nom = My_entry1_recher_membre.get()
    Prenom = My_entry2_recher_membre.get()
    Email = My_entry3_recher_membre.get()
    Telephone = My_entry4_recher_membre.get()
    ID_Membre = My_entry5_recher_membre.get()

    if Telephone and not Telephone.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro de téléphone doit être en nombre entier.")
        return
    if ID_Membre and not ID_Membre.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro ID_Membre doit être en nombre entier.")
        return

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    # Obligation de mettre les colonnes une à une au lieu de SELECT * car pour l'affichage de la
    # recherche avec la boucle il parcours les colonnes mais pas forcement dans l'ordre par
    # defaut, ici il a surement prit l'ISBN en premier car clef primaire, du coup c'était plus le
    # titre en premier mais l'ISBN et tout etait decallé
    requete = """SELECT ID_Membre, Nom, Prenom, Email, Telephone
                 FROM Membre
                 WHERE 1=1"""  # 1=1 car en dessous on lui met des conditions  pour chaque
    # champs et celà permet que les requetes soient toujours vrai
    liste_param = []
    if ID_Membre:
        requete += " AND ID_Membre = ?"
        liste_param.append(ID_Membre)
    if Nom:
        requete += " AND Nom = ?"
        liste_param.append(Nom)
    if Prenom:
        requete += " AND Prenom = ?"
        liste_param.append(Prenom)
    if Email:
        requete += " AND Email = ?"
        liste_param.append(Email)
    if Telephone:
        requete += " AND Telephone = ?"
        liste_param.append(Telephone)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # fetchone récupère seulement un resultat
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    membre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if membre_trouver:
        afficher_details_membre_modifier(membre_trouver)
    else:
        messagebox.showinfo("Aucun membre trouvé",
                            "Aucun membre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_membre_modifier(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    stylemembre = ttk.Style()

    # Personnalisation des couleurs du Treeview
    stylemembre.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    stylemembre.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("ID_Membre", "Nom", "Prenom", "Email", "Telephone"),
                        show="headings", style="Custom.Treeview")
    tree.heading("ID_Membre", text="ID Membre")
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prenom")
    tree.heading("Email", text="Email")
    tree.heading("Telephone", text="Telephone")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_modifier = ctk.CTkButton(details_fenetre,
                                   text="Modifier",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=lambda: modifier_membre_selectionne(tree),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol
                                   )
    bouton_modifier.pack(pady=10) #utilisation ici de pack pour toplevel


def modifier_membre_selectionne(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur",
                             "Veuillez sélectionner un membre à modifier.")
        return

    membre = tree.item(selected_item, "values")
    id_membre, nom, prenom, email, telephone = membre

    fenetre_modif = Toplevel()
    fenetre_modif.title("Modifier le Livre")
    fenetre_modif.geometry("870x320")

    label_font = ('comic sans ms', 15, "normal")

    Label(fenetre_modif, text="Nom actuel", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    nom_entry1 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    nom_entry1.grid(row=0, column=1, padx=10, pady=5)
    nom_entry1.insert(0, nom)

    Label(fenetre_modif, text="Nouveau nom", font=label_font).grid(row=0, column=2, padx=10, pady=5, sticky='w')
    nom_entry2 = Entry(fenetre_modif,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    nom_entry2.grid(row=0, column=3, padx=10, pady=5)
    nom_entry2.insert(0, nom)

    Label(fenetre_modif, text="Prenom actuel", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    prenom_entry1 = Entry(fenetre_modif,
                       fg='grey',
                       bg='white',
                       font=('Arial', 15, 'italic'),
                       bd=2,
                       relief='flat',
                       insertbackground='black',
                       selectbackground='blue',
                       selectforeground='white',
                       width=20,
                       justify='center')
    prenom_entry1.grid(row=1, column=1, padx=10, pady=5)
    prenom_entry1.insert(0, prenom)

    Label(fenetre_modif, text="Nouveau prenom", font=label_font).grid(row=1, column=2, padx=10, pady=5, sticky='w')
    prenom_entry2 = Entry(fenetre_modif,
                          fg='grey',
                          bg='white',
                          font=('Arial', 15, 'italic'),
                          bd=2,
                          relief='flat',
                          insertbackground='black',
                          selectbackground='blue',
                          selectforeground='white',
                          width=20,
                          justify='center')
    prenom_entry2.grid(row=1, column=3, padx=10, pady=5)
    prenom_entry2.insert(0, prenom)

    Label(fenetre_modif, text="Email actuel", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    email_entry1 = Entry(fenetre_modif,
                          fg='grey',
                          bg='white',
                          font=('Arial', 15, 'italic'),
                          bd=2,
                          relief='flat',
                          insertbackground='black',
                          selectbackground='blue',
                          selectforeground='white',
                          width=20,
                          justify='center')
    email_entry1.grid(row=2, column=1, padx=10, pady=5)
    email_entry1.insert(0, email)

    Label(fenetre_modif, text="Nouvel email", font=label_font).grid(row=2, column=2, padx=10, pady=5, sticky='w')
    email_entry2 = Entry(fenetre_modif,
                         fg='grey',
                         bg='white',
                         font=('Arial', 15, 'italic'),
                         bd=2,
                         relief='flat',
                         insertbackground='black',
                         selectbackground='blue',
                         selectforeground='white',
                         width=20,
                         justify='center')
    email_entry2.grid(row=2, column=3, padx=10, pady=5)
    email_entry2.insert(0, email)

    Label(fenetre_modif, text="Telephone actuel", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='w')
    telephone_entry1 = Entry(fenetre_modif,
                         fg='grey',
                         bg='white',
                         font=('Arial', 15, 'italic'),
                         bd=2,
                         relief='flat',
                         insertbackground='black',
                         selectbackground='blue',
                         selectforeground='white',
                         width=20,
                         justify='center')
    telephone_entry1.grid(row=3, column=1, padx=10, pady=5)
    telephone_entry1.insert(0, telephone)

    Label(fenetre_modif, text="Nouveau telephone", font=label_font).grid(row=3, column=2, padx=10, pady=5, sticky='w')
    telephone_entry2 = Entry(fenetre_modif,
                             fg='grey',
                             bg='white',
                             font=('Arial', 15, 'italic'),
                             bd=2,
                             relief='flat',
                             insertbackground='black',
                             selectbackground='blue',
                             selectforeground='white',
                             width=20,
                             justify='center')
    telephone_entry2.grid(row=3, column=3, padx=10, pady=5)
    telephone_entry2.insert(0, telephone)

    def valider_modification():
        nouveau_nom = nom_entry2.get()
        nouveau_prenom = prenom_entry2.get()
        nouvel_email = email_entry2.get()
        nouveau_telephone = telephone_entry2.get()

        if not nouveau_telephone.isdigit():
            messagebox.showerror("Erreur de saisie",
                                 "Le téléphone doit être des nombres entiers.")
            return

        conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
        cur = conn.cursor()
        cur.execute("""UPDATE Membre
                       SET Nom = ?, Prenom = ?, Email = ?, Telephone = ?
                       WHERE ID_Membre = ?""",
                    (nouveau_nom, nouveau_prenom, nouvel_email, nouveau_telephone, id_membre))
        conn.commit()
        conn.close()

        messagebox.showinfo("Modification réussie",
                            "Le membre a été modifié avec succès.")
        fenetre_modif.destroy()

    bouton_valider = ctk.CTkButton(fenetre_modif,
                                   text="Valider modification",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=valider_modification,
                                   height=50,
                                   width=450,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=5,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_valider.grid(row=4, columnspan=20, pady=20)

    retour_button = ctk.CTkButton(fenetre_modif,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fenetre_modif.destroy,
                                   height=25,
                                   width=60,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=2,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    retour_button.grid(row=5, columnspan=20, pady=0)


def clic_btn_supprimer_membre():
    My_fenetre_clic_btn_supprimer_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_supprimer_membre.geometry("400x517")
    My_fenetre_clic_btn_supprimer_membre.title("Rechercher un Membre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_supprimer_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_supprimer_membre.bg = bg

    global My_entry1_recher_membre, My_entry2_recher_membre, My_entry3_recher_membre, \
        My_entry4_recher_membre, My_entry5_recher_membre

    My_entry1_recher_membre = Entry(My_fenetre_clic_btn_supprimer_membre,
                                    fg='grey',
                                    bg='white',
                                    font=('Arial', 15, 'italic'),
                                    bd=2,
                                    relief='flat',
                                    insertbackground='black',
                                    selectbackground='blue',
                                    selectforeground='white',
                                    width=20,
                                    justify='center')
    My_entry1_recher_membre.insert(0, 'Nom')
    My_entry1_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_membre, anchor="nw")

    My_entry2_recher_membre = Entry(My_fenetre_clic_btn_supprimer_membre,
                                    fg='grey',
                                    bg='white',
                                    font=('Arial', 15, 'italic'),
                                    bd=2,
                                    relief='flat',
                                    insertbackground='black',
                                    selectbackground='blue',
                                    selectforeground='white',
                                    width=20,
                                    justify='center')
    My_entry2_recher_membre.insert(0, 'Prenom')
    My_entry2_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_membre, anchor="nw")

    My_entry3_recher_membre = Entry(My_fenetre_clic_btn_supprimer_membre,
                                    fg='grey',
                                    bg='white',
                                    font=('Arial', 15, 'italic'),
                                    bd=2,
                                    relief='flat',
                                    insertbackground='black',
                                    selectbackground='blue',
                                    selectforeground='white',
                                    width=20,
                                    justify='center')
    My_entry3_recher_membre.insert(0, 'Email')
    My_entry3_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_membre, anchor="nw")

    My_entry4_recher_membre = Entry(My_fenetre_clic_btn_supprimer_membre,
                                    fg='grey',
                                    bg='white',
                                    font=('Arial', 15, 'italic'),
                                    bd=2,
                                    relief='flat',
                                    insertbackground='black',
                                    selectbackground='blue',
                                    selectforeground='white',
                                    width=20,
                                    justify='center')
    My_entry4_recher_membre.insert(0, 'Telephone')
    My_entry4_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_membre, anchor="nw")

    My_entry5_recher_membre = Entry(My_fenetre_clic_btn_supprimer_membre,
                                    fg='grey',
                                    bg='white',
                                    font=('Arial', 15, 'italic'),
                                    bd=2,
                                    relief='flat',
                                    insertbackground='black',
                                    selectbackground='blue',
                                    selectforeground='white',
                                    width=20,
                                    justify='center')
    My_entry5_recher_membre.insert(0, 'ID_Membre')
    My_entry5_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 250, window=My_entry5_recher_membre, anchor="nw")

    recherch_modif_membre_button = ctk.CTkButton(My_fenetre_clic_btn_supprimer_membre,
                                                 text="Rechercher un membre",
                                                 font=("Arial", 22, "bold"),
                                                 text_color='white',
                                                 command=fonction_rechercher_supprimer_membre,
                                                 height=50,
                                                 width=150,
                                                 bg_color='black',
                                                 fg_color="gray",
                                                 corner_radius=4,
                                                 border_width=1,
                                                 border_color='white',  # Bordure blanche
                                                 hover=True,
                                                 hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                                 )
    canvas_for_image.create_window(100, 350, window=recherch_modif_membre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_supprimer_membre,
                                                 text="Retour",
                                                 font=("Arial", 22, "bold"),
                                                 text_color='white',
                                                 command=My_fenetre_clic_btn_supprimer_membre.destroy,
                                                 height=25,
                                                 width=50,
                                                 bg_color='black',
                                                 fg_color="gray",
                                                 corner_radius=4,
                                                 border_width=1,
                                                 border_color='white',  # Bordure blanche
                                                 hover=True,
                                                 hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                                 )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")


def fonction_rechercher_supprimer_membre():
    Nom = My_entry1_recher_membre.get()
    Prenom = My_entry2_recher_membre.get()
    Email = My_entry3_recher_membre.get()
    Telephone = My_entry4_recher_membre.get()
    ID_Membre = My_entry5_recher_membre.get()

    if Telephone and not Telephone.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro de téléphone doit être en nombre entier.")
        return
    if ID_Membre and not ID_Membre.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro ID_Membre doit être en nombre entier.")
        return

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    # Obligation de mettre les colonnes une à une au lieu de SELECT * car pour l'affichage de la
    # recherche avec la boucle il parcours les colonnes mais pas forcement dans l'ordre par
    # defaut, ici il a surement prit l'ISBN en premier car clef primaire, du coup c'était plus le
    # titre en premier mais l'ISBN et tout etait decallé
    requete = """SELECT ID_Membre, Nom, Prenom, Email, Telephone
                 FROM Membre
                 WHERE 1=1"""  # 1=1 car en dessous on lui met des conditions  pour chaque
    # champs et celà permet que les requetes soient toujours vrai
    liste_param = []
    if ID_Membre:
        requete += " AND ID_Membre = ?"
        liste_param.append(ID_Membre)
    if Nom:
        requete += " AND Nom = ?"
        liste_param.append(Nom)
    if Prenom:
        requete += " AND Prenom = ?"
        liste_param.append(Prenom)
    if Email:
        requete += " AND Email = ?"
        liste_param.append(Email)
    if Telephone:
        requete += " AND Telephone = ?"
        liste_param.append(Telephone)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # fetchone récupère seulement un resultat
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    membre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if membre_trouver:
        afficher_details_membre_supprimer(membre_trouver)
    else:
        messagebox.showinfo("Aucun membre trouvé",
                            "Aucun membre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_membre_supprimer(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    tree = ttk.Treeview(details_fenetre, columns=("ID_Membre", "Nom", "Prenom", "Email", "Telephone"), show="headings")
    tree.heading("ID_Membre", text="ID Membre")
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prenom")
    tree.heading("Email", text="Email")
    tree.heading("Telephone", text="Telephone")

    for resultat in resultats:
        print(resultat)
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_supprimer = Button(details_fenetre, text="Supprimer", command=lambda: fonction_supprimer_membre(tree))
    bouton_supprimer.pack(pady=10)


def fonction_supprimer_membre(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur",
                             "Veuillez sélectionner un membre à supprimer.")
        return

    membre = tree.item(selected_item, "values")
    ID_Membre, Nom, Prenom, Email, Telephone = membre

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Membre "
                    "WHERE ID_Membre = ? AND Nom = ? AND Prenom = ? AND Email = ? AND Telephone = ?",
                    (ID_Membre, Nom, Prenom, Email, Telephone))
        conn.commit()
        conn.close()
        print("Suppression membre reussi")
        messagebox.showinfo("Delete done",
                            "Suppression du membre reussi \n\n"
                            f"Nom : {Nom}\n"
                            f"Prenom : {Prenom}\n"
                            f"Email : {Email}\n"
                            f"Telephone : {Telephone}\n"
                            f"ID_Membre : {ID_Membre}\n")
        tree.delete(selected_item)

    except Exception as e:
        print("Erreur de suppression des données", e)
        show_error("Erreur de suppression des données")
        return False
    # Permet de vraiment fermer la connexion a la base de donnée
    # en cas d'erreur de suppression, elle ne se fermait plus
    # donc impossibilité de rajouté un livre je devais redemarré l'appli
    finally:
        conn.close()
        if conn:
            pass


def clic_btn_afficher_membre():
    My_fenetre_clic_btn_afficher_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_afficher_membre.geometry("400x550")
    My_fenetre_clic_btn_afficher_membre.title("Affichage de Membre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_afficher_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_afficher_membre.bg = bg

    global My_entry1_recher_membre, My_entry2_recher_membre, My_entry3_recher_membre, \
        My_entry4_recher_membre, My_entry5_recher_membre

    My_entry1_recher_membre = Entry(My_fenetre_clic_btn_afficher_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_membre.insert(0, 'Nom')
    My_entry1_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 30, window=My_entry1_recher_membre, anchor="nw")

    My_entry2_recher_membre = Entry(My_fenetre_clic_btn_afficher_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_membre.insert(0, 'Prenom')
    My_entry2_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 80, window=My_entry2_recher_membre, anchor="nw")

    My_entry3_recher_membre = Entry(My_fenetre_clic_btn_afficher_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_membre.insert(0, 'Email')
    My_entry3_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 130, window=My_entry3_recher_membre, anchor="nw")

    My_entry4_recher_membre = Entry(My_fenetre_clic_btn_afficher_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_membre.insert(0, 'Telephone')
    My_entry4_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 180, window=My_entry4_recher_membre, anchor="nw")

    My_entry5_recher_membre = Entry(My_fenetre_clic_btn_afficher_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry5_recher_membre.insert(0, 'ID_Membre')
    My_entry5_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 230, window=My_entry5_recher_membre, anchor="nw")

    recherch_modif_membre_button = ctk.CTkButton(My_fenetre_clic_btn_afficher_membre,
                                   text="Rechercher un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_rechercher_modifier_membre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(80, 310, window=recherch_modif_membre_button, anchor="nw")

    recherch_tout_afficher_membre_button = ctk.CTkButton(My_fenetre_clic_btn_afficher_membre,
                                   text="Aficher tous les membres",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_recherche_tout_afficher_membre,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(70, 390, window=recherch_tout_afficher_membre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_afficher_membre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_afficher_membre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")





def fonction_recherche_tout_afficher_membre():
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()
    requete = """SELECT ID_Membre, Nom, Prenom, Email, Telephone
                 FROM Membre"""
    cur.execute(requete)
    membre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if membre_trouver:
        afficher_details_membre_afficher(membre_trouver)
    else:
        messagebox.showinfo("Aucun membre trouvé",
                            "Aucun membre correspondant aux critères de recherche n'a été trouvé.")


def fonction_rechercher_afficher_membre():
    Nom = My_entry1_recher_membre.get()
    Prenom = My_entry2_recher_membre.get()
    Email = My_entry3_recher_membre.get()
    Telephone = My_entry4_recher_membre.get()
    ID_Membre = My_entry5_recher_membre.get()

    if Telephone and not Telephone.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro de téléphone doit être en nombre entier.")
        return
    if ID_Membre and not ID_Membre.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro ID_Membre doit être en nombre entier.")
        return

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    # Obligation de mettre les colonnes une à une au lieu de SELECT * car pour l'affichage de la
    # recherche avec la boucle il parcours les colonnes mais pas forcement dans l'ordre par
    # defaut, ici il a surement prit l'ISBN en premier car clef primaire, du coup c'était plus le
    # titre en premier mais l'ISBN et tout etait decallé
    requete = """SELECT ID_Membre, Nom, Prenom, Email, Telephone
                 FROM Membre
                 WHERE 1=1"""  # 1=1 car en dessous on lui met des conditions  pour chaque
    # champs et celà permet que les requetes soient toujours vrai
    liste_param = []
    if ID_Membre:
        requete += " AND ID_Membre = ?"
        liste_param.append(ID_Membre)
    if Nom:
        requete += " AND Nom = ?"
        liste_param.append(Nom)
    if Prenom:
        requete += " AND Prenom = ?"
        liste_param.append(Prenom)
    if Email:
        requete += " AND Email = ?"
        liste_param.append(Email)
    if Telephone:
        requete += " AND Telephone = ?"
        liste_param.append(Telephone)

    # tuple est utilisé pour convertir la liste liste_param en un tuple
    # Cette conversion est souvent nécessaire car la méthode execute()
    # attend en général un tuple de paramètres comme deuxième argument.
    cur.execute(requete, tuple(liste_param))

    # creation d'une variable pour stocker les resultats des requetes.
    # fetchall() récupère tous les résultats de la requête
    # fetchone récupère seulement un resultat
    # et les retourne sous forme d'une liste de tuples,
    # où chaque tuple représente une ligne de résultat de la requête.
    # bien pour une question d'affichage.
    membre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if membre_trouver:
        afficher_details_membre_afficher(membre_trouver)
    else:
        messagebox.showinfo("Aucun membre trouvé",
                            "Aucun membre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_membre_afficher(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    stylemembre = ttk.Style()

    # Personnalisation des couleurs du Treeview
    stylemembre.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    stylemembre.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("ID_Membre", "Nom", "Prenom", "Email", "Telephone"),
                        show="headings", style="Custom.Treeview")
    tree.heading("ID_Membre", text="ID Membre")
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prenom")
    tree.heading("Email", text="Email")
    tree.heading("Telephone", text="Telephone")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)


def clic_btn_emprunt():
    My_fenetre_clic_btn_emprunt = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_emprunt.geometry("1000x560")
    My_fenetre_clic_btn_emprunt.title("Gestion des emprunts")

    bg = PhotoImage(file="emprunt_main.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_emprunt, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_emprunt.bg = bg


    enregistrer_button = ctk.CTkButton(My_fenetre_clic_btn_emprunt,
                                   text="Ajouter un emprunt",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=clic_btn_enregistrer_emprunt,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(120, 120, window=enregistrer_button, anchor="nw")

    retourner_button = ctk.CTkButton(My_fenetre_clic_btn_emprunt,
                                   text="Retourner un emprunt",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=ouvrir_fenetre_retourner_livre,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(560, 120, window=retourner_button, anchor="nw")

    afficher_button = ctk.CTkButton(My_fenetre_clic_btn_emprunt,
                                   text="Afficher les emprunts",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=afficher_emprunts_en_cours,
                                   height=80,
                                   width=300,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(350, 320, window=afficher_button, anchor="nw")

    retour_emprunt_button = ctk.CTkButton(My_fenetre_clic_btn_emprunt,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_emprunt.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="silver",
                                   corner_radius=5,
                                   border_width=2,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(450, 500, window=retour_emprunt_button, anchor="nw")


def clic_btn_enregistrer_emprunt():
    My_fenetre_clic_btn_modifier_livre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_modifier_livre.geometry("400x550")
    My_fenetre_clic_btn_modifier_livre.title("Rechercher un Livre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_modifier_livre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_modifier_livre.bg = bg

    global My_entry1_recher_livre, My_entry2_recher_livre, My_entry3_recher_livre, My_entry4_recher_livre

    My_entry1_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_livre.insert(0, 'Titre')
    My_entry1_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_livre, anchor="nw")

    My_entry2_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_livre.insert(0, 'Auteur')
    My_entry2_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_livre, anchor="nw")

    My_entry3_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_livre.insert(0, 'Année')
    My_entry3_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_livre, anchor="nw")

    My_entry4_recher_livre = Entry(My_fenetre_clic_btn_modifier_livre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_livre.insert(0, 'ISBN')
    My_entry4_recher_livre.bind("<FocusIn>", clic_entrer_ajout_livre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_livre, anchor="nw")

    recherch_modif_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_livre,
                                   text="Rechercher un livre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_recher_livre_enregistrer_emprunt,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 300, window=recherch_modif_livre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_livre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_modifier_livre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")


def fonction_recher_livre_enregistrer_emprunt():
    Titre = My_entry1_recher_livre.get()
    Auteur = My_entry2_recher_livre.get()
    Annee = My_entry3_recher_livre.get()
    ISBN = My_entry4_recher_livre.get()

    if Annee and not Annee.isdigit():
        messagebox.showerror("Erreur de saisie", "L'année doit être un nombre entier.")
        return
    if ISBN and not ISBN.isdigit():
        messagebox.showerror("Erreur de saisie", "L'ISBN doit être un nombre entier.")
        return
    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    requete = """SELECT ISBN, Titre, Auteur, Annee
                 FROM Livre
                 WHERE 1=1"""
    liste_param = []
    if Titre:
        requete += " AND Titre = ?"
        liste_param.append(Titre)
    if Auteur:
        requete += " AND Auteur = ?"
        liste_param.append(Auteur)
    if Annee:
        requete += " AND Annee = ?"
        liste_param.append(Annee)
    if ISBN:
        requete += " AND ISBN = ?"
        liste_param.append(ISBN)

    cur.execute(requete, tuple(liste_param))
    livre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if livre_trouver:
        afficher_details_enregistrer_livre_emprunt(livre_trouver)
    else:
        messagebox.showinfo("Aucun livre trouvé", "Aucun livre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_enregistrer_livre_emprunt(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    style = ttk.Style()

    # Personnalisation des couleurs du Treeview
    style.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    style.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("Titre", "Auteur", "Année", "ISBN"),
                        show="headings", style="Custom.Treeview")
    tree.heading("Titre", text="Titre")
    tree.heading("Auteur", text="Auteur")
    tree.heading("Année", text="Année")
    tree.heading("ISBN", text="ISBN")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_rech_membr = ctk.CTkButton(details_fenetre,
                                   text="Rechercher un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=lambda: clic_btn_rech_membre_emprunt(tree),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_rech_membr.pack(pady=10) #utilisation ici de pack pour toplevel



def clic_btn_rech_membre_emprunt(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aucun livre sélectionné", "Veuillez sélectionner un livre avant de continuer.")
        return

    livre_selectionne = tree.item(selected_item)["values"]

    My_fenetre_clic_btn_modifier_membre = Toplevel(My_fenetre_main)
    My_fenetre_clic_btn_modifier_membre.geometry("400x517")
    My_fenetre_clic_btn_modifier_membre.title("Rechercher un Membre")

    bg = PhotoImage(file="recherche_livre.png")
    canvas_for_image = Canvas(My_fenetre_clic_btn_modifier_membre, width=400, height=650)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_clic_btn_modifier_membre.bg = bg


    global My_entry1_recher_membre, My_entry2_recher_membre, My_entry3_recher_membre, \
        My_entry4_recher_membre, My_entry5_recher_membre, livre_a_emprunter

    livre_a_emprunter = livre_selectionne

    My_entry1_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry1_recher_membre.insert(0, 'Nom')
    My_entry1_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 50, window=My_entry1_recher_membre, anchor="nw")

    My_entry2_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry2_recher_membre.insert(0, 'Prenom')
    My_entry2_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 100, window=My_entry2_recher_membre, anchor="nw")

    My_entry3_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry3_recher_membre.insert(0, 'Email')
    My_entry3_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 150, window=My_entry3_recher_membre, anchor="nw")

    My_entry4_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry4_recher_membre.insert(0, 'Telephone')
    My_entry4_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 200, window=My_entry4_recher_membre, anchor="nw")

    My_entry5_recher_membre = Entry(My_fenetre_clic_btn_modifier_membre,
                      fg='grey',
                      bg='white',
                      font=('Arial', 15, 'italic'),
                      bd=2,
                      relief='flat',
                      insertbackground='black',
                      selectbackground='blue',
                      selectforeground='white',
                      width=20,
                      justify='center')
    My_entry5_recher_membre.insert(0, 'ID_Membre')
    My_entry5_recher_membre.bind("<FocusIn>", clic_entrer_ajout_membre)
    canvas_for_image.create_window(90, 250, window=My_entry5_recher_membre, anchor="nw")

    recherch_modif_membre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_membre,
                                   text="Rechercher un membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=fonction_recher_membre_enregistrer_emprunt,
                                   height=50,
                                   width=200,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(80, 350, window=recherch_modif_membre_button, anchor="nw")

    retour_modifier_livre_button = ctk.CTkButton(My_fenetre_clic_btn_modifier_membre,
                                   text="Retour",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=My_fenetre_clic_btn_modifier_membre.destroy,
                                   height=25,
                                   width=50,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=4,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#CD6155'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(160, 460, window=retour_modifier_livre_button, anchor="nw")


def fonction_recher_membre_enregistrer_emprunt():
    Nom = My_entry1_recher_membre.get()
    Prenom = My_entry2_recher_membre.get()
    Email = My_entry3_recher_membre.get()
    Telephone = My_entry4_recher_membre.get()
    ID_Membre = My_entry5_recher_membre.get()

    if Telephone and not Telephone.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro de téléphone doit être un nombre entier.")
        return
    if ID_Membre and not ID_Membre.isdigit():
        messagebox.showerror("Erreur de saisie",
                             )
        return

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    requete = """SELECT ID_Membre, Nom, Prenom, Email, Telephone
                 FROM Membre
                 WHERE 1=1"""
    liste_param = []
    if Nom:
        requete += " AND Nom = ?"
        liste_param.append(Nom)
    if Prenom:
        requete += " AND Prenom = ?"
        liste_param.append(Prenom)
    if Email:
        requete += " AND Email = ?"
        liste_param.append(Email)
    if Telephone:
        requete += " AND Telephone = ?"
        liste_param.append(Telephone)
    if ID_Membre:
        requete += " AND ID_Membre = ?"
        liste_param.append(ID_Membre)

    cur.execute(requete, tuple(liste_param))
    membre_trouver = cur.fetchall()

    conn.commit()
    conn.close()

    if membre_trouver:
        afficher_details_enregistrer_membre_emprunt(membre_trouver)
    else:
        messagebox.showinfo("Aucun membre trouvé",
                            "Aucun membre correspondant aux critères de recherche n'a été trouvé.")


def afficher_details_enregistrer_membre_emprunt(resultats):
    details_fenetre = Toplevel()
    details_fenetre.title("Résultats de la Recherche")

    stylemembre = ttk.Style()

    # Personnalisation des couleurs du Treeview
    stylemembre.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    stylemembre.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Application du style personnalisé au Treeview
    tree = ttk.Treeview(details_fenetre, columns=("ID_Membre", "Nom", "Prenom", "Email", "Telephone"),
                        show="headings", style="Custom.Treeview")
    tree.heading("ID_Membre", text="ID Membre")
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prenom")
    tree.heading("Email", text="Email")
    tree.heading("Telephone", text="Telephone")

    for resultat in resultats:
        tree.insert("", "end", values=resultat)

    tree.pack(fill="both", expand=True)

    bouton_confirmer_emprunt = ctk.CTkButton(details_fenetre,
                                   text="Selectioner membre",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=lambda: clic_btn_confirmer_emprunt(tree),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="gray",
                                   corner_radius=0,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='#0B5345'  # Couleur de survol
                                   )
    bouton_confirmer_emprunt.pack(pady=10) #utilisation ici de pack pour toplevel


def clic_btn_confirmer_emprunt(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aucun membre sélectionné",
                               "Veuillez sélectionner un membre avant de continuer.")
        return

    membre_selectionne = tree.item(selected_item)["values"]

    My_fenetre_confirmer_emprunt = Toplevel(My_fenetre_main)
    My_fenetre_confirmer_emprunt.geometry("1000x560")
    My_fenetre_confirmer_emprunt.title("Confirmer Emprunt")

    bg = PhotoImage(file="emprunt_main.png")

    canvas_for_image = Canvas(My_fenetre_confirmer_emprunt, width=400, height=400)
    canvas_for_image.pack(fill="both", expand=True)
    canvas_for_image.create_image(0, 0, image=bg, anchor="nw")
    My_fenetre_confirmer_emprunt.bg = bg

    style = ttk.Style()
    style.theme_use('default')

    style.configure("DateEntry",
                    fieldbackground="white",
                    background="black",
                    foreground="black",
                    arrowcolor="black",
                    arrowsize=14,
                    font=("comic sans ms", 12, "bold"))

    global My_entry_date_emprunt, My_entry_date_retour, livre_a_emprunter, membre_a_emprunter

    membre_a_emprunter = membre_selectionne

    canvas_for_image.create_text(100, 50, text=f"Livre Sélectionné: {livre_a_emprunter[1]} ecrit par {livre_a_emprunter[2]}",
                                 anchor="nw", fill="white", font=("Helvetica", 17, "bold"))

    canvas_for_image.create_text(310, 80, text=f"ISBN: {livre_a_emprunter[0]}", anchor="nw", fill="white",
                                 font=("Helvetica", 17, "bold"))

    canvas_for_image.create_text(100, 120, text=f"Membre Sélectionné: {membre_a_emprunter[1]} {membre_a_emprunter[2]}",
                                 anchor="nw", fill="white", font=("Helvetica", 17, "bold"))
    canvas_for_image.create_text(340, 150, text=f"ID Membre: {membre_a_emprunter[0]}", anchor="nw", fill="white",
                                 font=("Helvetica", 17, "bold"))

    canvas_for_image.create_text(100, 220, text="Date d'emprunt", anchor="nw", fill="white", font=("Helvetica", 17, "underline"))
    My_entry_date_emprunt = DateEntry(My_fenetre_confirmer_emprunt, date_pattern='yyyy-mm-dd', style="DateEntry")
    canvas_for_image.create_window(100, 250, window=My_entry_date_emprunt, anchor="nw")

    canvas_for_image.create_text(100, 300, text="Date de retour", anchor="nw", fill="white",font=("Helvetica", 17, "underline"))
    My_entry_date_retour = DateEntry(My_fenetre_confirmer_emprunt, date_pattern='yyyy-mm-dd', style="DateEntry")
    canvas_for_image.create_window(100, 330, window=My_entry_date_retour, anchor="nw")

    bouton_enregistrer_emprunt = ctk.CTkButton(My_fenetre_confirmer_emprunt,
                                   text="Enregistrer l'emprunt",
                                   font=("Arial", 22, "bold"),
                                   text_color='white',
                                   command=enregistrer_emprunt,
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    canvas_for_image.create_window(100, 400, window=bouton_enregistrer_emprunt, anchor="nw")

    My_fenetre_confirmer_emprunt.mainloop()


def enregistrer_emprunt():
    date_emprunt = My_entry_date_emprunt.get()
    date_retour = My_entry_date_retour.get()
    print(f"Date Emprunt: {date_emprunt}, Date Retour: {date_retour}")

    if not date_emprunt or not date_retour:
        messagebox.showerror("Erreur de saisie",
                             "Veuillez entrer les dates d'emprunt et de retour.")
        return

    conn = sqlite3.connect(r"C:\Program Files (x86)\SQLite3\db\Bibliotheque.db")
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Emprunt (ID_Membre, ISBN, Date_emprunt, Date_retour)"
                    " VALUES (?, ?, ?, ?)",
                    (membre_a_emprunter[0], livre_a_emprunter[0], date_emprunt, date_retour))
        conn.commit()
        messagebox.showinfo("Succès",
                            "Emprunt enregistré avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur",
                             f"Une erreur s'est produite : {e}")
    finally:
        conn.close()


def ouvrir_fenetre_retourner_livre():
    global fenetre_retourner
    fenetre_retourner = Toplevel(My_fenetre_main)
    fenetre_retourner.geometry("350x150")
    fenetre_retourner.title("Retourner un livre")

    Label = tk.Label(fenetre_retourner,
             text="Veuillez saisir l'ISBN du livre à retourner :",
             font=("Helvetica", 12, "bold"),
             fg="black",
             padx=10,
             pady=10)

    Label.pack(pady=10)

    entry_isbn_retour = Entry(fenetre_retourner)
    entry_isbn_retour.pack(pady=10)

    bouton_enregistrer_retour = ctk.CTkButton(fenetre_retourner,
                                   text="Confirmer le retour",
                                   font=("Arial", 17, "bold"),
                                   text_color='white',
                                   command=lambda: retourner_livre(entry_isbn_retour.get()),
                                   height=50,
                                   width=150,
                                   bg_color='black',
                                   fg_color="#34495E",
                                   corner_radius=7,
                                   border_width=1,
                                   border_color='white',  # Bordure blanche
                                   hover=True,
                                   hover_color='gray'  # Couleur de survol légèrement plus foncée
                                   )
    bouton_enregistrer_retour.pack(pady=10)


def retourner_livre(isbn):
    if isbn and not isbn.isdigit():
        messagebox.showerror("Erreur de saisie",
                             "Le numéro ISBN doit être un nombre entier.")
        return
    if not isbn:
        messagebox.showerror("Erreur",
                             "Veuillez entrer un ISBN.")
        return

    cur.execute("SELECT * "
                "FROM Emprunt "
                "WHERE ISBN = ?",
                (isbn,))
    emprunt = cur.fetchone()  # récupère la première ligne de résultat de la requête.
    # Si aucune ligne n'est trouvée (emprunt est None),
    # cela signifie que le livre n'est pas emprunté

    if emprunt is None:
        messagebox.showerror("Livre non emprunté",
                             f"Le livre avec l'ISBN {isbn} n'est pas emprunté.")
    else:
        cur.execute("DELETE FROM Emprunt WHERE ISBN = ?",
                    (isbn,))
        conn.commit()
        messagebox.showinfo("Livre retourné",
                            f"Le livre avec l'ISBN {isbn} a été retourné avec succès.")

    fenetre_retourner.destroy()


def afficher_emprunts_en_cours():
    cur.execute("SELECT E.ID_Emprunt, L.ISBN, M.ID_Membre, L.Titre, M.Nom, M.Prenom, E.Date_emprunt, E.Date_retour "
                "FROM Emprunt E "
                "JOIN Livre L ON E.ISBN = L.ISBN "
                "JOIN Membre M ON E.ID_Membre = M.ID_Membre")

    # Récupération de tous les résultats de la requête
    emprunts = cur.fetchall()

    # Création de la fenêtre pour afficher les détails des emprunts
    details_fenetre = Toplevel()
    details_fenetre.title("Emprunts en Cours")

    style = ttk.Style()

    # Personnalisation des couleurs du Treeview
    style.configure("Custom.Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="with",
                    font=("Helvetica", 13,"bold"),
                    rowheight=30)

    # Personnalisation des en-têtes du Treeview
    style.configure("Custom.Treeview.Heading",
                    background="black",
                    foreground="#839192",
                    font=("comic sans ms", 12, "bold"))

    # Création du Treeview pour afficher les détails des emprunts
    tree = ttk.Treeview(details_fenetre,
                        columns=(
                        "ID_Emprunt", "ISBN", "ID_Membre", "Titre", "Nom", "Prenom", "Date_emprunt", "Date_retour"),
                        show="headings", style="Custom.Treeview")
    tree.heading("ID_Emprunt", text="ID Emprunt")
    tree.heading("ISBN", text="ISBN")
    tree.heading("Titre", text="Titre")
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prénom")
    tree.heading("Date_emprunt", text="Date Emprunt")
    tree.heading("Date_retour", text="Date Retour")

    # Ajout des données au Treeview
    for emprunt in emprunts:
        tree.insert("", END, values=emprunt)

    tree.pack(fill="both", expand=True)


# Fenetre principale


#Bouton Livre
livre_button = ctk.CTkButton(My_fenetre_main,
                                text="Gestion des livres",
                                font=("Arial", 22, "bold"),
                                text_color='white',
                                command=clic_btn_livre,
                                height=80,
                                width=300,
                                bg_color='black',
                                fg_color="#34495E",
                                corner_radius=7,
                                border_width=1,
                                border_color='white',  # Bordure blanche
                                hover=True,
                                hover_color='gray'  # Couleur de survol légèrement plus foncée
                            )
canvas_for_image.create_window(640, 160, window=livre_button)

#Bouton membre
membre_button = ctk.CTkButton(My_fenetre_main,
                                text="Gestion des membres",
                                font=("Arial", 22, "bold"),
                                text_color='white',
                                command=clic_btn_membre,
                                height=80,
                                width=300,
                                bg_color='black',
                                fg_color="#34495E",
                                corner_radius=7,
                                border_width=1,
                                border_color='white',  # Bordure blanche
                                hover=True,
                                hover_color='gray'  # Couleur de survol légèrement plus foncée
                            )
canvas_for_image.create_window(635, 340, window=membre_button, anchor="center")

#Bouton emprunt
emprunt_button = ctk.CTkButton(My_fenetre_main,
                                text="Gestion des emprunts",
                                font=("Arial", 22, "bold"),
                                text_color='white',
                                command=clic_btn_emprunt,
                                height=80,
                                width=300,
                                bg_color='black',
                                fg_color="#34495E",
                                corner_radius=7,
                                border_width=1,
                                border_color='white',  # Bordure blanche
                                hover=True,
                                hover_color='gray'  # Couleur de survol légèrement plus foncée
                            )
canvas_for_image.create_window(640, 540, window=emprunt_button, anchor="center")

My_fenetre_main.mainloop()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
