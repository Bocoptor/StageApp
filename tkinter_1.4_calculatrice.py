from tkinter import *

calculation=""

def add_to_calculation(symbol):
    #global permet de pouvoir modifier les variables en dehors de la fonction
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

root=Tk()
root.geometry("400x375")

text_result=Text(root,height=2,width=16,font=('Arial',24))
text_result.grid(columnspan=5)

btn_1=Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2=Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3=Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4=Button(root,text="4",command=lambda:add_to_calculation(4),width=5,font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5=Button(root,text="5",command=lambda:add_to_calculation(5),width=5,font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6=Button(root,text="6",command=lambda:add_to_calculation(6),width=5,font=('Arial',14))
btn_6.grid(row=3,column=3)

btn_7=Button(root,text="7",command=lambda:add_to_calculation(7),width=5,font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8=Button(root,text="8",command=lambda:add_to_calculation(8),width=5,font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9=Button(root,text="9",command=lambda:add_to_calculation(9),width=5,font=('Arial',14))
btn_9.grid(row=4,column=3)

btn_0=Button(root,text="0",command=lambda:add_to_calculation(0),width=5,font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_plus=Button(root,text="+",command=lambda:add_to_calculation("+"),width=5,font=('Arial',14))
btn_plus.grid(row=2,column=5)

btn_sous=Button(root,text="-",command=lambda:add_to_calculation("-"),width=5,font=('Arial',14))
btn_sous.grid(row=3,column=5)

btn_div=Button(root,text="/",command=lambda:add_to_calculation("/"),width=5,font=('Arial',14))
btn_div.grid(row=4,column=5)

btn_mul=Button(root,text="x",command=lambda:add_to_calculation("*"),width=5,font=('Arial',14))
btn_mul.grid(row=5,column=5)

btn_open=Button(root,text="(",command=lambda:add_to_calculation("("),width=5,font=('Arial',14))
btn_open.grid(row=5,column=1)

btn_clos=Button(root,text=")",command=lambda:add_to_calculation(")"),width=5,font=('Arial',14))
btn_clos.grid(row=5,column=3)

btn_equal=Button(root,text="=",command=evaluate_calculation,width=10,font=('Arial',14))
btn_equal.grid(row=6,column=3,columnspan=2)

btn_clear=Button(root,text="C",command=clear_field,width=10,font=('Arial',14))
btn_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()