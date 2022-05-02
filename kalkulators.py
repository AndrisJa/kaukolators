from argparse import MetavarTypeHelpFormatter
from ast import operator
from tkinter import*
from math import*
mansLogs=Tk()
mansLogs.title("Kalkulators")

mansLogs.configure(bg="grey")
#mansLogs.geometry("300x400")

#======================================================================================================================

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
    elif mathOp=="%":
        result=num1*0.01*num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

#======================================================================================================================

def notirit():
    e.delete(0, END)
    num1=0
    mathop=""
    return 0

def sq_rt():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

def kvadrats():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=num1**2
    e.delete(0,END)
    e.insert(0,num1)
    return 0

def logaritms():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=log10(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

#======================================================================================================================

btn0 = Button(mansLogs, text="0", padx="40", bd=5, pady="20", command=lambda:btnClick(0),bg="black", fg="white")
btn1 = Button(mansLogs, text="1", padx="40", bd=5, pady="20", command=lambda:btnClick(1),bg="black", fg="white")
btn2 = Button(mansLogs, text="2", padx="40", bd=5, pady="20", command=lambda:btnClick(2),bg="black", fg="white")
btn3 = Button(mansLogs, text="3", padx="40", bd=5, pady="20", command=lambda:btnClick(3),bg="black", fg="white")
btn4 = Button(mansLogs, text="4", padx="40", bd=5, pady="20", command=lambda:btnClick(4),bg="black", fg="white")
btn5 = Button(mansLogs, text="5", padx="40", bd=5, pady="20", command=lambda:btnClick(5),bg="black", fg="white")
btn6 = Button(mansLogs, text="6", padx="40", bd=5, pady="20", command=lambda:btnClick(6),bg="black", fg="white")
btn7 = Button(mansLogs, text="7", padx="40", bd=5, pady="20", command=lambda:btnClick(7),bg="black", fg="white")
btn8 = Button(mansLogs, text="8", padx="40", bd=5, pady="20", command=lambda:btnClick(8),bg="black", fg="white")
btn9 = Button(mansLogs, text="9", padx="40", bd=5, pady="20", command=lambda:btnClick(9),bg="black", fg="white")
btn10 = Button(mansLogs, text="+", padx="40", bd=5, pady="20", command=lambda:btnCommand("+"),bg="black", fg="green")
btn11 = Button(mansLogs, text="-", padx="40", bd=5, pady="20", command=lambda:btnCommand("-"),bg="black", fg="green")
btn12 = Button(mansLogs, text="/", padx="40", bd=5, pady="20", command=lambda:btnCommand("/"),bg="black", fg="green")
btn13 = Button(mansLogs, text="*", padx="40", bd=5, pady="20", command=lambda:btnCommand("*"),bg="black", fg="green")
btn14 = Button(mansLogs, text="sqrt", padx="35", bd=5, pady="20", command=sq_rt, bg="black", fg="green")
btn15 = Button(mansLogs, text="x2", padx="40", bd=5, pady="20", command=kvadrats, bg="black", fg="green")
btn16 = Button(mansLogs, text="log", padx="35", bd=5, pady="20", command=logaritms, bg="black", fg="green")
btn17 = Button(mansLogs, text="=", padx="40", bd=5, pady="20", command=vienads, bg="green", fg="black")
btn18 = Button(mansLogs, text="C", padx="40", bd=5, pady="20", command=notirit, bg="black", fg="red")
btn19 = Button(mansLogs, text="%", padx="40", bd=5, pady="20", command=lambda:btnCommand("%"),bg="black", fg="green")
 
#======================================================================================================================

btn0.grid(row=5, column=2)
btn1.grid(row=4, column=1)  
btn2.grid(row=4, column=2)
btn3.grid(row=4, column=3)
btn4.grid(row=3, column=1)
btn5.grid(row=3, column=2)
btn6.grid(row=3, column=3)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)
btn9.grid(row=2, column=3)
btn10.grid(row=2, column=4)
btn11.grid(row=1, column=4)
btn12.grid(row=3, column=4)
btn13.grid(row=4, column=4)
btn14.grid(row=1, column=3)
btn15.grid(row=5, column=3)
btn16.grid(row=1, column=2)
btn17.grid(row=5, column=4)
btn18.grid(row=1, column=1)
btn19.grid(row=5, column=1)

#======================================================================================================================

def btnClick(number):
    current=e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displejā
    return 0


def btnCommand(command):
    global num1 #jāiegaumē skatlis un darbība
    global mathOp #matemātisks operators
    mathOp = command #+, -, /, *
    num1 = float(e.get())
    e.delete(0,END)
    return 0

#======================================================================================================================
    
e=Entry(mansLogs, width=15, bd=10, bg="black", fg="white", font=("Comic Sans MS", 20))
e.grid(row=0, column=0, columnspan=5)




#poga.pack()

mansLogs.mainloop()