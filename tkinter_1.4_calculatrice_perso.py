from tkinter import *


def ajouter_chiffre(chiffre):
    display.insert(END, chiffre)


def effacer():
    display.delete(1.0, END)


button_style = {
    "font": ("Arial", 12),
    "width": 8,
    "height": 4,
    "activebackground": "#ccc",
    "highlightbackground": "#999", }


def calculer():
    try:
        #eval est une fonction native de Python qui evalue des expressions mathematiques.
        resultat = eval(display.get(1.0, END))
        effacer()
        display.insert(END, str(resultat))
        #'e' est simplement une variable à laquelle vous assignez l'objet exception pour pouvoir
        #y accéder et examiner ses propriétés dans le bloc except. Cela permet de fournir des
        #informations plus détaillées sur l'erreur qui s'est produite, ce qui peut être
        #utile pour le débogage ou pour fournir des messages d'erreur significatifs à l'utilisateur.
    except Exception as e:
        effacer()
        display.insert(END, "Erreur")

def handle_enter(event):
    if event.keysym == "Return":
        calculer()


root = Tk()
root.title("Calculatrice")
root.geometry("325x450")
root.configure(bg="#DCDCDC")
#Permet de gerer le redimentionnement de la fenetre
#Le premier argument (False) correspond à la possibilité de redimensionner la fenêtre en largeur.
#Le deuxième argument (False) correspond à la possibilité de redimensionner la fenêtre en hauteur.
root.resizable(False, False)

root.bind("<KeyPress>", handle_enter)

# Display ne fonctionne pas avec height
#display = Entry(root, width=25, font=("Arial", 16), justify="right")
display = Text(root, width=25, height=3, font=("Arial", 15))
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


Button(root, text="7", command=lambda: ajouter_chiffre("7"), **button_style).grid(row=1, column=0)
Button(root, text="8", command=lambda: ajouter_chiffre("8"), **button_style).grid(row=1, column=1)
Button(root, text="9", command=lambda: ajouter_chiffre("9"), **button_style).grid(row=1, column=2)

Button(root, text="4", command=lambda: ajouter_chiffre("4"), **button_style).grid(row=2, column=0)
Button(root, text="5", command=lambda: ajouter_chiffre("5"), **button_style).grid(row=2, column=1)
Button(root, text="6", command=lambda: ajouter_chiffre("6"), **button_style).grid(row=2, column=2)

Button(root, text="1", command=lambda: ajouter_chiffre("1"), **button_style).grid(row=3, column=0)
Button(root, text="2", command=lambda: ajouter_chiffre("2"), **button_style).grid(row=3, column=1)
Button(root, text="3", command=lambda: ajouter_chiffre("3"), **button_style).grid(row=3, column=2)

Button(root, text="0", command=lambda: ajouter_chiffre("0"), **button_style).grid(row=4, column=1)
Button(root, text="C", bg="#CB4335", command=effacer, **button_style).grid(row=4, column=0)
Button(root, text="=", bg="#7DCEA0", command=calculer, **button_style).grid(row=4, column=2)

Button(root, text="+", bg="#CCEEFF", command=lambda: ajouter_chiffre("+"), **button_style).grid(row=1, column=3)
Button(root, text="-", bg="#CCEEFF", command=lambda: ajouter_chiffre("-"), **button_style).grid(row=2, column=3)
Button(root, text="*", bg="#CCEEFF", command=lambda: ajouter_chiffre("*"), **button_style).grid(row=3, column=3)
Button(root, text="/", bg="#CCEEFF", command=lambda: ajouter_chiffre("/"), **button_style).grid(row=4, column=3)

root.mainloop()
