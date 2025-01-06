

from tkinter import *

def open_file():
    Label_nom.config(text="Ouvrir un fichier")
def save_file():
    Label_nom.config(text="Enregistrer le fichier")
def exit_app():
    My_fenetre.destroy()

My_fenetre = Tk()
My_fenetre.geometry("300x300")
My_fenetre.title("Exercice 3")

Menu_bar = Menu(My_fenetre)

File_menu = Menu(Menu_bar, tearoff=0)
File_menu.add_command(label="Ouvrir", command=open_file)

File_menu.add_command(label="Enregistrer", command=save_file)

File_menu.add_separator()

File_menu.add_command(label="Quitter", command=exit_app)

Menu_bar.add_cascade(label="Fichier", menu=File_menu)

Label_nom = Label(My_fenetre, text="", width=30, font=('Helvetica', 10))
Label_nom.pack()

My_fenetre.config(menu=Menu_bar)

My_fenetre.mainloop()