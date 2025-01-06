

from tkinter import *
def pizza():
    #Label.destroy()
    Label1 = Label(root, text="Ingredients :\nPâte à pizza\nTomates\nJambon\nMozzarella\nChampignons")
    Label1.pack()
    print("Ingredients :\nPâte à pizza\nTomates\nJambon\nMozzarella\nChampignons")
def burger():
    #Label.deletecommand(0, END)
    Label2 = Label(root, text="Ingredients :\nPain à burger\nViande haché\nFromage\nCrudités")
    Label2.pack()
    print("Ingredients :\nPain à burger\nViande haché\nFromage\nCrudités")
def salade():
    #Label.destroy(0, END)
    Label3 = Label(root, text="Ingredients :\nSalade verte\nTomates\nPoulet\nOlives")
    Label3.pack()
    print("Ingredients :\nSalade verte\nTomates\nPoulet\nOlives")

root = Tk()
root.geometry("300x250")
frame = Frame(root)
frame.pack()
MenuBttn = Menubutton(frame, text="Favourite food", relief=RAISED)
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Menu1 = Menu(MenuBttn, tearoff=0)
Menu1.add_checkbutton(label="Pizza", variable=Var1, command=pizza)
Menu1.add_checkbutton(label="Cheese Burger", variable=Var2, command=burger)
Menu1.add_checkbutton(label="Salad", variable=Var3, command=salade)
MenuBttn["menu"] = Menu1
MenuBttn.pack()
root.mainloop()