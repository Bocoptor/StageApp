from tkinter import *

windows = Tk()
windows.title("Lignes de couleurs")
windows.geometry("500x450")

canvas = Canvas(windows, width=500, height=450)
canvas.pack()

#"Le premier nombre est la coordonnée x du point de départ de la ligne."
#"Le deuxième nombre est la coordonnée y du point de départ de la ligne."
#"Le troisième nombre est la coordonnée x du point d'arrivée de la ligne."
#"Le quatrième nombre est la coordonnée y du point d'arrivée de la ligne."

canvas.create_line(0, 10, 500, 10, fill="blue", width=20) #haut
canvas.create_line(0, 440, 500, 440, fill="yellow", width=20) #bas
canvas.create_line(10, 0, 10, 450, fill="turquoise", width=20) #gauche
canvas.create_line(490, 0, 490, 450, fill="green", width=20) #droite
canvas.create_line(10, 10, 490, 440, fill="pink", width=20)
canvas.create_line(10, 440, 490, 10, fill="brown", width=20)
canvas.create_line(250, 440, 250, 10, fill="red", width=20)
canvas.create_line(490, 225, 10, 225, fill="sky blue", width=20)

windows.mainloop()