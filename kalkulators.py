from argparse import MetavarTypeHelpFormatter
from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
#mansLogs.geometry("300x400")

def vienads():
    global num2
    num2=(int(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    return 0

def notirit():
    e.delet(0, END)
    num1=0
    mathop=""
    return 0


btn0 = Button(mansLogs, text="0", padx="40", pady="20", command=lambda:btnClick(0),bg="grey", fg="blue")
btn1 = Button(mansLogs, text="1", padx="40", pady="20", command=lambda:btnClick(1),bg="grey", fg="blue")
btn2 = Button(mansLogs, text="2", padx="40", pady="20", command=lambda:btnClick(2),bg="grey", fg="blue")
btn3 = Button(mansLogs, text="3", padx="40", pady="20", command=lambda:btnClick(3),bg="grey", fg="blue")
btn4 = Button(mansLogs, text="4", padx="40", pady="20", command=lambda:btnClick(4),bg="grey", fg="blue")
btn5 = Button(mansLogs, text="5", padx="40", pady="20", command=lambda:btnClick(5),bg="grey", fg="blue")
btn6 = Button(mansLogs, text="6", padx="40", pady="20", command=lambda:btnClick(6),bg="grey", fg="blue")
btn7 = Button(mansLogs, text="7", padx="40", pady="20", command=lambda:btnClick(7),bg="grey", fg="blue")
btn8 = Button(mansLogs, text="8", padx="40", pady="20", command=lambda:btnClick(8),bg="grey", fg="blue")
btn9 = Button(mansLogs, text="9", padx="40", pady="20", command=lambda:btnClick(9),bg="grey", fg="blue")
btn10 = Button(mansLogs, text="+", padx="40", pady="20", command=lambda:btnClick("+"),bg="grey", fg="white")
btn11 = Button(mansLogs, text="-", padx="40", pady="20", command=lambda:btnClick("-"),bg="grey", fg="white")
btn12 = Button(mansLogs, text="/", padx="40", pady="20", command=lambda:btnClick("/"),bg="grey", fg="white")
btn13 = Button(mansLogs, text="*", padx="40", pady="20", command=lambda:btnClick("*"),bg="grey", fg="white")
btn14 = Button(mansLogs, text="=", padx="40", pady="20", command=vienads, bg="grey", fg="white")
btn15 = Button(mansLogs, text="C", padx="40", pady="20", command=notirit, bg="grey", fg="red")

btn0.grid(row=4, column=2)
btn1.grid(row=3, column=1)  
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)
btn10.grid(row=2, column=4)
btn11.grid(row=1, column=4)
btn12.grid(row=3, column=4)
btn13.grid(row=4, column=4)
btn14.grid(row=4, column=1)
btn15.grid(row=4, column=3)

def btnClick(number):
    current=e.get() #nolasa esošo skaitli
    e.delete(0, END) #nodzēš
    newNumber=str(current)+str(number)
    e.insert(0, newNumber) #ievieto displejā
    return 0


def btnCommand(command):
    global num1
    global mathOp
    mathOp = command
    num1 = float(e.get())
    e.delete(0, END)
    return 0


    

e=Entry(mansLogs, width=15, font=("Arial Black", 20))
e.grid(row=0, column=0, columnspan=5)




#poga.pack()

mansLogs.mainloop()