from tkinter import *

root = Tk()
root.title = "Damier"
root.geometry("900x800")
frame = Frame(root)
frame.pack()


def damier():
    "Trace le damier"
    y = 0
    while y < 10:
        if y % 2 == 0:  # Décale une fois sur deux
            x = 0  # la position du premier carré noir
        else:
            x = 1
        carre_noir(x * taille_carre, y * taille_carre)
        y += 1


def carre_noir(x, y):
    "Trace les carrés noirs"
    i = 0
    while i < 5:
        can.create_rectangle(x, y, x + taille_carre, y + taille_carre, fill="black")
        i += 1
        x += taille_carre * 2


taille_carre = 60

can = Canvas(frame, bg="white", width=taille_carre * 10, height=taille_carre * 10)

can.pack()

btn = Button(root, text="Quitter", command=root.destroy)
btn.pack()

root.mainloop()
