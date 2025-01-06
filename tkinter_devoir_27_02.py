from tkinter import *

def open_file():
    Label_nom.config(text="Ouvrir un fichier")
def save_file():
    Label_nom.config(text="Enregistrer le fichier")
def exit_app():
    My_fenetre.destroy()
def copy():
    Label_nom.config(text="Copier")
def cut():
    Label_nom.config(text="Couper")
def paste():
    Label_nom.config(text="Coller")

My_fenetre = Tk()
My_fenetre.geometry("300x300")
My_fenetre.title("Exercice 3")

Menu_bar = Menu(My_fenetre)
File_menu1 = Menu(Menu_bar, tearoff=0)
File_menu2 = Menu(Menu_bar, tearoff=0)

Menu_bar.add_cascade(label="Fichier", menu=File_menu1)
File_menu1.add_command(label="Nouveau", command=open_file)
File_menu1.add_command(label="Ouvrir", command=save_file)
File_menu1.add_separator()
File_menu1.add_command(label="Quitter", command=exit_app)

Menu_bar.add_cascade(label="Edition", menu=File_menu2)
File_menu2.add_command(label="Copier", command=copy)
File_menu2.add_command(label="Couper",command=cut)
File_menu2.add_command(label="Coller", command=paste)

Label_nom = Label(My_fenetre, text="", width=30, font=('Helvetica', 10))
Label_nom.pack()

My_fenetre.config(menu=Menu_bar)

My_fenetre.mainloop()