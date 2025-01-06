"""
Exercice 4 - V2 :
    Lie, comprendre et expliquer le code suivant
===================================================================================
"""
# -*- coding: utf-8 -*-
# 1) -  Importation des modules nécessaires

from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('300x200')

def action(event):
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    #print("Vous avez sélectionné : '", select,"'")
    text_box.insert("1.0", f"Vous avez sélectionné : {select}\n")

labelChoix = Label(root, text = "Veuillez faire un choix !")
labelChoix.pack()

# 2) - créer la liste Python contenant les éléments de la liste Combobox
listeProduits=["Laptop", "Imprimante","Tablette","SmartPhone"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = Combobox(root, values=listeProduits)
listeCombo.set("Choisissez un appareil")

# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

# Création d'une zone de texte pour afficher le contenu du fichier
text_box = Text(root, wrap="word", width=40, height=10)
text_box.pack(padx=10, pady=10)

root.mainloop()