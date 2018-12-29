from tkinter import *
import random
win=Tk()
win.title("Hang-Man")
menubar=Menu(win)
win.config(menu=menubar)
filemenu=(Menu(menubar,tearoff=0))
def showlist():
    
    window = Toplevel(win)
    l1=Label(window,text ="Choose a Word From The list Below")
    l1.pack()
    l=Label(window,text="dog','cat','cow','sheep','rabbit','duck','hen','horse','pig','squirrel',snail','mouse','chameleon','deer','raccoon','moose','snake','bat','tiger','turtle",fg="red")
    l.pack()
def listsearch():
    global i
    global str1
    global l5
    e.delete(0, END)
    i=3
    list1=['dog','cat','cow','sheep','rabbit','duck','hen','horse','pig','squirrel','snail','mouse','chameleon','deer','raccoon','moose','snake','bat','tiger','turtle']
    str1=random.choice(list1)
    ln=len(str1)
    l5=Label(text="Tedad Horof : "+str(ln),bg='red',fg='blue')
    l5.pack()
    l1.config(text="Welcome to Hangman(Animal Words)")
    l2.config(text="")
    #print("random =",str1)

def submit():
    global i
    global str1
    global str2
    global w
    global l5
    if(i>0):
        str2=e.get()
        str2.lower()
        w.forget()
        l5.forget()
        if i==3:
            photo=PhotoImage(file ="h6.png")
            w=Label(win,image=photo)
            w.photo=photo
            w.pack()
        elif i==2:
            photo=PhotoImage(file ="h2.png")
            w=Label(win,image=photo)
            w.photo=photo
            w.pack()
        if str1 == str2:
            l1.config(text="You Win")
        else:
            i-=1
            l1.config(text=" Try = "+str(i))
    if i==0:
        photo=PhotoImage(file ="h1.png")
        w=Label(win,image=photo)
        w.photo=photo
        w.pack()
        l1.config(text="You Lose")
        l5.forget()
    e.delete(0, END)


str1='' #global
str2='' #global
i=3 #global
global w #global
global x
global l5
v=StringVar()
e = Entry(win,textvariable=v)
e.pack()
l1=Label(win,text="Click NewGame")
l1.pack()
l2=Label(win,text="")
l2.pack()
b1=Button(win,text="New Game",command=listsearch)
b1.pack()
b2=Button(win,text="Submit",command=submit)
b2.pack()
b3=Button(win,text="Help",command=showlist)
b3.pack()
b4=Button(win,text="Exit",command=win.destroy)
b4.pack()
filemenu.add_command(label='New',command=listsearch)
filemenu.add_command(label='Exit',command=win.destroy)
photo=PhotoImage(file ="h0.png")
w=Label(win,image=photo)
w.photo=photo
w.pack()
menubar.add_cascade(label='File',menu=filemenu)
