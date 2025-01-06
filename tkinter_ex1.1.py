from tkinter import *

def reinitialiser():
    My_entry1.delete(0,END)
    My_entry2.delete(0,END)
    My_entry3.delete(0,END)

def valider():
    My_label1 = My_entry1.get()
    My_label2 = My_entry2.get()
    My_label3 = My_entry3.get()
    entre_util = f"Nom : {My_label1}\n Prenom : {My_label2}\n Ville : {My_label3}"
    new_window(entre_util)

def new_window(entre_util):
    window = Toplevel()
    window.geometry("300x250")
    newlabel = Label(window, text=entre_util)
    newlabel.grid()

My_fenetre = Tk()
My_fenetre.geometry("500x300")
My_fenetre.title("Exercice 1.1")

#Creation d'un label pour afficher l'image.
#les labels sont des widgets polyvalents qui peuvent
#contenir du texte, des images et d'autres éléments visuels.
My_image = PhotoImage(file="ex1_1.png")
My_image_label = Label(My_fenetre, image=My_image)
My_image_label.grid(row=0, column=5, padx=10, pady=10)

left_frame = Frame(My_fenetre)
left_frame.grid(row=0, column=0, padx=10, pady=10)
text_a_afficher = Frame(My_fenetre)
text_a_afficher.grid()
bottom_frame = Frame(My_fenetre)
bottom_frame.grid(row=1, column=0, columnspan=3, pady=10)
Label_text = Label(text_a_afficher, text="")
Label_text.grid()

#sticky = emplacement (est, ouest, nord, sud)
#columnspan = occupation de colonne qu'il prend
My_text1 = Label(left_frame, text="Nom")
My_text1.grid(row=0, column=0)
My_entry1 = Entry(left_frame)
My_entry1.grid(row=0, column=1)

My_text2 = Label(left_frame, text="Prenom")
My_text2.grid(row=1, column=0)
My_entry2 = Entry(left_frame)
My_entry2.grid(row=1, column=1)

My_text3 = Label(left_frame, text="Ville")
My_text3.grid(row=2, column=0)
My_entry3 = Entry(left_frame)
My_entry3.grid(row=2, column=1)


My_bouton1 = Button(bottom_frame, text="Valider", command=valider)
My_bouton1.grid(row=0, column=0, padx=5)

My_bouton2 = Button(bottom_frame, text="Reinitialiser", command=reinitialiser)
My_bouton2.grid(row=0, column=1, padx=5)

My_bouton3 = Button(bottom_frame, text="Quitter", command=My_fenetre.destroy)
My_bouton3.grid(row=0, column=2, padx=20)
#My_bouton3.place(x=500, y=100)

My_fenetre.mainloop()