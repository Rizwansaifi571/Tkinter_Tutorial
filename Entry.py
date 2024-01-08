"""----------------------- < PYTHON TKINTER ENTRY > -------------------------"""


'''-----> Simple Example '''

# from tkinter import *
# top=Tk()
# top.geometry("400x250")
# name=Label(top,text="Name").place(x=30,y=50)
# email=Label(top,text="E-Mail").place(x=30,y=90)
# password=Label(top,text="Password").place(x=30,y=130)
# sbmitbtn=Button(top,text="Submit",fg='green',activebackground='pink',
#          activeforeground='blue').place(x=30,y=170)
# e1=Entry(top).place(x=80,y=50)
# e2=Entry(top).place(x=80,y=90)
# e3=Entry(top).place(x=90,y=130)
# top.mainloop()


'''-----> A Simple calculator '''

import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 + num2
    label_result.config(text='Result = %d' % result)

top = tk.Tk()
top.geometry('400x200+100+200')
top.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

label_num1 = tk.Label(top, text='A').grid(row=1, column=0)
label_num2 = tk.Label(top, text='B').grid(row=2, column=0)

# The labelresult variable should be defined separately from the grid method
label_result = tk.Label(top)
label_result.grid(row=7, column=2)

entry_num1 = tk.Entry(top, textvariable=number1).grid(row=1, column=2)
entry_num2 = tk.Entry(top, textvariable=number2).grid(row=2, column=2)

# Adjusted the function call to remove partial
btn_cal = tk.Button(top, text="Calculate", command=lambda: call_result(label_result, number1, number2)).grid(row=3, column=0)

top.mainloop()

'''


............  ENTRY IS END NOW  ................



'''




