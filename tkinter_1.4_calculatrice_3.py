from tkinter import *


def creer_boutons(fenetre, champ_saisie):
    boutons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0)
    ]

    for (texte, ligne, colonne) in boutons:
        bouton = Button(fenetre, text=texte, padx=20, pady=20, command=lambda t=texte: gerer_clic(t, champ_saisie))
        bouton.grid(row=ligne, column=colonne, padx=5, pady=5)


def gerer_clic(valeur,champ_saisie):
    if valeur == 'C':
        champ_saisie.delete(0, END)
    elif valeur == '=':
        try:
            resultat = eval(champ_saisie.get())
            champ_saisie.delete(0, END)
            champ_saisie.insert(END, str(resultat))
        except Exception as e:
            champ_saisie.delete(0, END)
            champ_saisie.insert(END, "Erreur")
    else:
        champ_saisie.insert(END, valeur)


fenetre = Tk()
fenetre.title("Calculatrice")

champ_saisie = Entry(fenetre, width=30, borderwidth=5)
champ_saisie.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

creer_boutons(fenetre, champ_saisie)

fenetre.mainloop()
