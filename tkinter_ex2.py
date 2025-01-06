from tkinter import *

#En cliquant sur le button
def afficher_text():
    My_text_saisi = My_entry.get()
    Label_text.config(text='Bonjour'+ My_text_saisi)

My_fenetre = Tk()
My_fenetre.geometry("500x400")

My_frame = Frame(My_fenetre)
My_frame.pack()

My_entry = Entry(My_frame, width=15)
My_entry.pack(padx=5, pady=5)

My_bouton = Button(My_frame,text="Afficher ", command=afficher_text)
My_bouton.pack(pady=5)

Label_text = Label(My_frame, text="")
Label_text.pack()

#En appuyant sur ENTER mais ca affiche sur pycharm pas sur tkinter
#def push_enter(event):
   # My_text_saisi = My_entry.get()
    #print("Bonjour ", My_text_saisi)

#My_fenetre = Tk()
#My_fenetre.geometry("500x400")

#My_frame = Frame(My_fenetre)
#My_frame.pack()

#My_entry = Entry(My_frame, width=15)
#My_entry.pack(padx=5, pady=5)

# Lier le gestionnaire d'événements à la touche "Enter"
#My_entry.bind("<Return>", push_enter)

My_fenetre.mainloop()