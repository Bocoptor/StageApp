from tkinter import *

pwet = Tk()
pwet.geometry("400x400")
pwet.maxsize(1280, 720)
pwet.minsize(200, 400)

#texte1 = Label (pwet, text = "RIGHT", fg="blue")
#texte1.pack(side=RIGHT) #Side pour l'emplacement (left, right, top, bottom)

texte1 = Label (pwet, text="Bonjour tout le monde", bg="ivory", fg="red",
                cursor = "heart", font=("arial",25))
texte1.pack()

text2 = Label(pwet, text="FLAT", cursor = "tcross")
text2.pack()

logo = PhotoImage(file="Exit.png") #jpeg ico fonctionne pas
bouton = Button(text="Quitter", bg="#8671CD", command=pwet.destroy,
                image=logo, height=75, width=250)
bouton.pack()

frame = Frame(pwet)
frame.pack()

my_entry = Entry(frame, width=15)
my_entry.insert(0,'Username')
my_entry.pack(padx=5, pady=5)
my_entry.delete(0,"end")

my_entry2 = Entry(frame, width=15)
my_entry2.insert(0,'')
my_entry2.pack(padx=5, pady=5)



pwet.mainloop()