from tkinter import *
from PIL import Image, ImageTk

top=Tk()
top.geometry('1350x1000')
top.title('TRUE ARTICLE')


a=Label(top,text='ARTICLE ON PLASMODIUM.',bg='yellow',fg='black',
        font=('comicsansms',20,'bold')).pack(fill=X)

original_image = Image.open('images/Plasmodium.png')
resized_image = original_image.resize((320, 265))
photo1 = ImageTk.PhotoImage(resized_image)
label1 = Label(top, image=photo1,bg="pink")

label1.pack(fill=X)


p1=Label(top,text='\n\nPlasmodium falciparum (Malaria Parasite):',fg='black',
font=('comicsansms',23,'bold'),bg="pink")

p1.pack(fill=X)

p2=Label(top,text='''
Plasmodium falciparum is a protozoan parasite responsible for causing the most
severe form of malaria in humans.Transmitted through the bite of infected Anopheles
mosquitoes, this parasite infects red blood cells, leading to symptoms such as fever,
anemia, and, in severe cases, organ failure. Malaria remains a major global health
concern, particularly in tropical and subtropical regions.''',fg='black',
font=('comicsansms',22,),bg="pink")

p2.pack(fill=X)

c=Canvas(top,bg='pink',height='1000',width='1350').pack()
top.mainloop()