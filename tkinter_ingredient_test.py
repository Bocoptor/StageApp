from tkinter import *

def afficher_chckbutton():
    text = ingredients.get("text")
    Label_text.config(text=" "+ text)

root = Tk()
root.geometry("800x700")
root.title("Pizza")

framelabel = Frame(root)
framelabel.pack()
frameckbttn = Frame(root)
frameckbttn.pack()
framebttn = Frame(root)
framebttn.pack()
framemenuvalider = Frame(root)
framemenuvalider.pack()

Label_text = Label(framemenuvalider, text="")
Label_text.pack()

Labeldepart = Label(framelabel, text="Veuillez choisir vos ingredients pour votre pizza puis valider svp")
Labeldepart.pack()

ingredients = ["Mozzarela", "Champigon", "Olive", "Pepperoni", "Poulet",
               "Lardon", "Oignon", "Aubergine", "Roquette", "Thon",
               "Ananas", "Fromage de chevre", "Gorgonzola", "Poivron",
               "Chorizo", "Merguez", "Jambon", "Basilic"]

# Liste pour stocker les instances de Checkbutton
liste_checkbuttons = []

for garniture in ingredients:
    var = StringVar()
    chck_bttn = Checkbutton(frameckbttn, text=garniture, variable=var)
    chck_bttn.pack()
    #stocker la variable associé au Checkbutton
    chck_bttn.var = var
    #stocker le texte du Checkbutton
    chck_bttn.text = garniture
    #ajoute le Checkbutton à la liste
    liste_checkbuttons.append(chck_bttn)


My_bouton = Button(frameckbttn,text="Valider", command=afficher_chckbutton)
My_bouton.pack(pady=5)

root.mainloop()