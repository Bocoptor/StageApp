from tkinter import *

def reinitialiser():
    My_entry1.delete(0, END)
    My_entry2.delete(0, END)
    My_entry3.delete(0, END)

def valider():
    My_label1 = Label(My_fenetre, text='Merci')
    My_label1.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centre le label "Merci" dans la fenêtre

My_fenetre = Tk()
My_fenetre.title("Exercice 1.1")

def on_resize(event):
    # Mettre à jour la disposition lors du redimensionnement de la fenêtre
    w = My_fenetre.winfo_width()
    h = My_fenetre.winfo_height()

    left_frame.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)  # Positionne le frame à gauche
    My_image_label.place(relx=0.45, rely=0.1, relwidth=0.4, relheight=0.8)  # Positionne l'image dans la fenêtre
    bottom_frame.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)  # Positionne le frame en bas

My_fenetre.bind("<Configure>", on_resize)

My_image = PhotoImage(file="ex1_1.png")
My_image_label = Label(My_fenetre, image=My_image)

left_frame = Frame(My_fenetre)
My_text1 = Label(left_frame, text="Nom")
My_entry1 = Entry(left_frame)
My_text2 = Label(left_frame, text="Prenom")
My_entry2 = Entry(left_frame)
My_text3 = Label(left_frame, text="Ville")
My_entry3 = Entry(left_frame)

bottom_frame = Frame(My_fenetre)
My_bouton1 = Button(bottom_frame, text="Valider", command=valider)
My_bouton2 = Button(bottom_frame, text="Reinitialiser", command=reinitialiser)
My_bouton3 = Button(bottom_frame, text="Quitter", command=My_fenetre.destroy)

My_fenetre.mainloop()
