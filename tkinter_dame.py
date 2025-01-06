from tkinter import *

root = Tk()
root.title("Damier")
root.geometry("900x900")

frame = Frame(root)
frame.pack()
frame.config(highlightbackground="#79E8FE", highlightthickness=15)

canvas = Canvas(frame, bg="white", width=800, height=800)

#(x= debut de la forme de gauche à droite,y= debut de la forme du haut vers le bas, largeur, hauteur)
carre1 = canvas.create_rectangle(0, 0, 100, 100, fill="black")
carre2 = canvas.create_rectangle(200, 0, 300, 100, fill="black")
carre3 = canvas.create_rectangle(400, 0, 500, 100, fill="black")
carre4 = canvas.create_rectangle(600, 0, 700, 100, fill="black")

carre9 = canvas.create_rectangle(0, 300, 100, 200, fill="black")
carre10 = canvas.create_rectangle(200, 300, 300, 200, fill="black")
carre11 = canvas.create_rectangle(400, 300, 500, 200, fill="black")
carre12 = canvas.create_rectangle(600, 300, 700, 200, fill="black")

carre17 = canvas.create_rectangle(0, 500, 100, 400, fill="black")
carre18 = canvas.create_rectangle(200, 500, 300, 400, fill="black")
carre19 = canvas.create_rectangle(400, 500, 500, 400, fill="black")
carre20 = canvas.create_rectangle(600, 500, 700, 400, fill="black")

carre25 = canvas.create_rectangle(0, 700, 100, 600, fill="black")
carre26 = canvas.create_rectangle(200, 700, 300, 600, fill="black")
carre27 = canvas.create_rectangle(400, 700, 500, 600, fill="black")
carre28 = canvas.create_rectangle(600, 700, 700, 600, fill="black")


carre5 = canvas.create_rectangle(100, 100, 200, 200, fill="black")
carre6 = canvas.create_rectangle(300, 100, 400, 200, fill="black")
carre7 = canvas.create_rectangle(500, 100, 600, 200, fill="black")
carre8 = canvas.create_rectangle(700, 100, 800, 200, fill="black")

carre13 = canvas.create_rectangle(100, 400, 200, 300, fill="black")
carre14 = canvas.create_rectangle(300, 400, 400, 300, fill="black")
carre15 = canvas.create_rectangle(500, 400, 600, 300, fill="black")
carre16 = canvas.create_rectangle(700, 400, 800, 300, fill="black")

carre21 = canvas.create_rectangle(100, 600, 200, 500, fill="black")
carre22 = canvas.create_rectangle(300, 600, 400, 500, fill="black")
carre23 = canvas.create_rectangle(500, 600, 600, 500, fill="black")
carre24 = canvas.create_rectangle(700, 600, 800, 500, fill="black")

carre29 = canvas.create_rectangle(100, 700, 200, 800, fill="black")
carre30 = canvas.create_rectangle(300, 700, 400, 800, fill="black")
carre31 = canvas.create_rectangle(500, 700, 600, 800, fill="black")
carre32 = canvas.create_rectangle(700, 700, 800, 800, fill="black")

canvas.pack()

btn = Button(root, text="Quitter", command=root.destroy, width=80, height=2)
btn.pack()

root.mainloop()
