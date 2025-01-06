from tkinter import *

windows = Tk()
windows.title("Morpion")
windows.geometry("455x550")

# Création du canevas
canvas = Canvas(windows, width=450, height=450)
canvas.grid(row=1, column=0, columnspan=2, pady=10)

# Dessiner les lignes du Morpion sur le canevas
canvas.create_line(0, 3, 450, 3, fill="#556B2F", width=3)  #haut
canvas.create_line(0, 450, 450, 450, fill="#556B2F", width=3)  #bas
canvas.create_line(3, 0, 3, 450, fill="#556B2F", width=3)  #gauche
canvas.create_line(450, 0, 450, 450, fill="#556B2F", width=3)  #droite
canvas.create_line(150, 0, 150, 450, fill="#556B2F", width=3)
canvas.create_line(300, 0, 300, 450, fill="#556B2F", width=3)
canvas.create_line(0, 150, 450, 150, fill="#556B2F", width=3)
canvas.create_line(0, 300, 450, 300, fill="#556B2F", width=3)

#underline pour souligner le texte et bold pour le mettre en gras
My_text1 = Label(windows, text="Bienvenue sur le jeu du Morpion", font=("Arial", 12, "underline bold"))
My_text1.grid(row=0, column=0, columnspan=2, pady=10)

My_bouton1 = Button(windows, text="Recommencer")
My_bouton1.grid(row=2, column=0, sticky="ew")

My_bouton2 = Button(windows, text="Quitter", command=windows.destroy)
My_bouton2.grid(row=2, column=1, sticky="ew")

windows.mainloop()
