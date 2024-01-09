"""----------------------- < PYTHON TKINTER BUTTON > -------------------------"""


'''-----> Basics BUTTON '''

# from tkinter import *
# top = Tk()
# top.geometry('200x100')
# b = Button(top,text = 'Simple',fg = 'black').pack()
# top.mainloop()



'''-----> Image_Label '''

from tkinter import *
top=Tk()
top.geometry('900x850')
top.minsize(200,150)
top.maxsize(1100,1050)
photo=PhotoImage(file='images\youtube.png')
label1=Label(top,image=photo)
label1.pack()
top.mainloop()



'''-----> BUTTON_WITH_OPTIONS '''

# from tkinter import *
# from tkinter import messagebox
# top = Tk()
# top.geometry('200x100')
# def fun():
#     messagebox.showinfo('hello','Red Button Clicked !!')
# b1=Button(top,text = "Red",command = fun,activeforeground ='red',activebackground = 'pink',pady = 10)
# b2=Button(top,text = 'Green',activeforeground = 'green',activebackground = "pink",pady = 10)
# b3=Button(top,text = 'blue',activeforeground = 'blue',activebackground = "pink",pady = 10)
# b4=Button(top,text = 'Yellow',activeforeground = 'yellow',activebackground = "pink",pady = 10)
# b1.pack(side=LEFT)
# b2.pack(side=TOP)
# b3.pack(side=RIGHT)
# b4.pack(side=BOTTOM)
# top.mainloop()

'''


............  BUTTON IS END NOW  ................



'''