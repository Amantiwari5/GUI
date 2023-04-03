#imports
from tkinter import *
from tkinter import ttk
import os
from  PIL import ImageTk, Image

def Reg():
    main.destroy()
    reg=Tk()
    reg.title("Fuck management system")
    reg.geometry("1500x1500")
    reg.configure(bg="white")
    # frame1 = ttk.Frame(reg)
    
    #image
    img1 = Image.open('logo.png')
    img1 = img1.resize((550,400))
    img1 = ImageTk.PhotoImage(img1)
    Label(reg, image=img1,bg='white').place(x=0,y=-100,relwidth=1)
    l1 = Label(reg, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="white",font=("bold"))
    l1.place(x=0,y=110,relwidth=1)
    
    #buttons and entries
    Entry(reg,)
    
    
    
    
    
    
    
    
    
    
    reg.mainloop()












#Main
main=Tk()
main.title("Fuck management system")
main.geometry("1500x1500")
main.configure(bg="white")


#Image import
img = Image.open('fst.png')
img = img.resize((900,900))
img = ImageTk.PhotoImage(img)
Label(main, image=img,bg='white').place(x=0,y=80)

img1 = Image.open('logo.png')
img1 = img1.resize((550,400))
img1 = ImageTk.PhotoImage(img1)
Label(main, image=img1,bg='white').place(x=910,y=250)

# Label
Label(main, text = " India's Most Secure Bank ", font=('Calibri',16,"bold"),bg="white").place(x=1080,y=480)

#Buttons
Button(main, text="Register", font=('Calibri',12),width=40,height=2,command=Reg,bg='white',border=1,activebackground="light blue",relief="groove").place(x=1030,y=600)
Button(main, text="Log In", font=('Calibri',12),width=40,height=2,command="Login",bg='white',border=1,activebackground="light blue",relief="groove").place(x=1030,y=680)

#bar
my = Menu(main)
m=Menu(my)
m.add_command(label="Registeration",command='')
m.add_command(label="Login",command='')
m.add_command(label="setting",command=set)
main.config(menu=my)
my.add_cascade(label="Menu",menu=m)
help=Menu(my)
help.add_command(label="Report Problem",command='')
help.add_command(label="Feedback",command='')
help.add_command(label="About",command='')
my.add_cascade(label="Help",menu=help)
my.add_command(label="Exit",command='')

main.mainloop()