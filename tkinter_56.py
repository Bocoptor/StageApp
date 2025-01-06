#1.Importation de la bibliotheque tkinter
from tkinter import *

#2.On creé ensuite un objet(une instance) de la classe tk.
#La plupart du temps, cet objet sera la fenetre principale de notre interface
pwet = Tk()
#pwet.Tk()   pour l'utilisation de from tkinter from *

#4.Customization de l'interface
#Titre de la fenetre
pwet.title("Fenetre de test")

#Taille d'ouverture
pwet.geometry("400x600")
#Taille maximum
pwet.maxsize(1280, 720)
#Taille minimum
pwet.minsize(200, 400)

#Changer l'icone a coté du titre
pwet.iconbitmap("pacman.ico")

# Ajout d'un texte dans la fenêtre
texte1 = Label (pwet, text = "Ceci est un texte")
texte1.pack()
#Ajouter un bouton
bouton1 = Button(pwet, text = "Cliquez ici")
bouton1.pack()
#creation d'un cadre dans la fenetre
cadre1 = Frame(pwet)
cadre1.pack()
#Ajout de boutons dans le cadre
bouton2 = Button (cadre1, text="Bouton 1")
bouton3 = Button (cadre1, text="Bouton 2")
bouton2.pack()
bouton3.pack()

#Creation d'un champ de saisie de l'utilisateur
entrée1 = Entry(pwet)
entrée1.pack()

#Creation de cases à cocher
case_cocher1 = Checkbutton(pwet, text="oui")
case_cocher2 = Checkbutton(pwet, text="non")
case_cocher1.pack()
case_cocher2.pack()
#Creation de cases à cocher unique
case_unique1 = Radiobutton(pwet,text="Choix 1")
case_unique2 = Radiobutton(pwet,text="Choix 2")
case_unique3 = Radiobutton(pwet,text="Choix 3")
case_unique1.pack()
case_unique2.pack()
case_unique3.pack()

#Creation d'une liste
liste1 = Listbox(pwet)
liste1.insert(1, "Valeur 1")
liste1.insert(2, "Valeur 2")
liste1.insert(3, "Valeur 3")
liste1.insert(4, "Valeur 4")
liste1.pack()

#changer la couler de fond avec code couleur ou ecrit (blue, white, ect)
pwet.config(background='#8671CD')

#3.On appelle la methode mainloop de notre fenetre racine.
#Cette methode ne retourne que lorsqu'on ferme la fenetre
pwet.mainloop()

