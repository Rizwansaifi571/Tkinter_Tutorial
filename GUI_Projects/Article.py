from tkinter import *
from PIL import Image, ImageTk

top=Tk()
top.geometry('1350x1000')
top.title('TRUE ARTICLE')


a=Label(top,text='ARTICLE ON PLASMODIUM.',bg='yellow',fg='black',
        font=('comicsansms',20,'bold')).pack(fill=X)

original_image = Image.open('images/Plasmodium.png')
resized_image = original_image.resize((300, 250))
photo1 = ImageTk.PhotoImage(resized_image)
label1 = Label(top, image=photo1)

label1.pack()


p1=Label(top,text='Plasmodium falciparum (Malaria Parasite):',fg='black',
font=('comicsansms',23,'bold'))

p1.pack()

p2=Label(top,text='''
Plasmodium falciparum is a protozoan parasite responsible for causing the most
severe form of malaria in humans.Transmitted through the bite of infected Anopheles
mosquitoes, this parasite infects red blood cells, leading to symptoms such as fever,
anemia, and, in severe cases, organ failure. Malaria remains a major global health
concern, particularly in tropical and subtropical regions.''',fg='black',
font=('comicsansms',22,))

p2.pack()














# c=Canvas(top,bg='pink',height='1000',width='900').pack()
top.mainloop()