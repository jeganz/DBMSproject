from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct

r=Tk()
r.geometry('500x500')
r.title('Add new employee')

img=ImageTk.PhotoImage(Image.open('delitemform.png'))
search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((25,25)))
tick=ImageTk.PhotoImage(Image.open('tickicon.png').resize((25,25)))
eks=ImageTk.PhotoImage(Image.open('eksicon.png').resize((25,25)))
warning=ImageTk.PhotoImage(Image.open('warningicon.png'))

bg=customtkinter.CTkLabel(r,text='',image=img)
bg.place(x=0,y=0)

infoemp=customtkinter.CTkFrame(bg,width=370,height=230,bg_color='#d9d9d9',fg_color='#d9d9d9')

def enter(e):
    inameentry.configure(border_color='#ed6d31')
    l1.configure(text_color='#ed6d31')
def leave(e):
    inameentry.configure(border_color='black')
    l1.configure(text_color='black')


inameentry=customtkinter.CTkEntry(infoemp,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')

l1=customtkinter.CTkLabel(infoemp,text=' NAME ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)


inameentry.bind('<FocusIn>',enter)
inameentry.bind('<FocusOut>',leave)

def enter(e):
    codeentry.configure(border_color='#ed6d31')
    l5.configure(text_color='#ed6d31')
def leave(e):
    codeentry.configure(border_color='black')
    l5.configure(text_color='black')


codeentry=customtkinter.CTkEntry(infoemp,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')

l5=customtkinter.CTkLabel(infoemp,text=' CODE ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)


codeentry.bind('<FocusIn>',enter)
codeentry.bind('<FocusOut>',leave)

def enter(e):
    qtyentry.configure(border_color='#ed6d31')
    l2.configure(text_color='#ed6d31')
def leave(e):
    qtyentry.configure(border_color='black')
    l2.configure(text_color='black')


qtyentry=customtkinter.CTkEntry(infoemp,width=170,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')

l2=customtkinter.CTkLabel(infoemp,text=' STOCK ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)


qtyentry.bind('<FocusIn>',enter)
qtyentry.bind('<FocusOut>',leave)

def enter(e):
    mrpentry.configure(border_color='#ed6d31')
    l3.configure(text_color='#ed6d31')
def leave(e):
    mrpentry.configure(border_color='black')
    l3.configure(text_color='black')


mrpentry=customtkinter.CTkEntry(infoemp,width=175,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')

l3=customtkinter.CTkLabel(infoemp,text=' PRICE ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)


mrpentry.bind('<FocusIn>',enter)
mrpentry.bind('<FocusOut>',leave)

def enter(e):
    catentry.configure(border_color='#ed6d31')
    l4.configure(text_color='#ed6d31')
def leave(e):
    catentry.configure(border_color='black')
    l4.configure(text_color='black')

catentry=customtkinter.CTkEntry(infoemp,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')

l4=customtkinter.CTkLabel(infoemp,text=' CATEGORY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)


catentry.bind('<FocusIn>',enter)
catentry.bind('<FocusOut>',leave)


rl=customtkinter.CTkLabel(infoemp,text='SAVE THE CHANGES ?',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))

def delconfirm():
    # id=int(nameentry.get())
    # for i in data:
    #     if id in i:
    #         data.remove(i)
    # updatelist()
    # r.destroy()
    pass
def delcancel():
    for i in infoemp.winfo_children():
        i.place_forget()
tickbut=customtkinter.CTkButton(infoemp,text='',font=('Century Gothic', 15,'bold'),
                                    fg_color='#ed6d31',text_color='black',image=tick,width=40,
                                    height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=delconfirm)

eksbut=customtkinter.CTkButton(infoemp,text='',font=('Century Gothic', 15,'bold'),
                                    fg_color='black',image=eks,width=40,
                                    height=35,hover_color='gray',bg_color='#d9d9d9',command=delcancel)


notfound=customtkinter.CTkLabel(infoemp,image=warning,compound=TOP,text='Employee not Found',text_color='red',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))

def enter(e):
    nameentry.configure(border_color='#ed6d31')
    l.configure(text_color='#ed6d31')
def leave(e):
    nameentry.configure(border_color='black')
    l.configure(text_color='black')


nameentry=customtkinter.CTkEntry(bg,width=305,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',placeholder_text='ENTER PRODUCT CODE',
                                bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
nameentry.place(x=75,y=190)
l=customtkinter.CTkLabel(bg,text=' SEARCH ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
l.place(x=83,y=182)
def placeall():
    
    inameentry.place(x=10,y=10)
    l1.place(x=19,y=2)
    codeentry.place(x=11,y=55)
    l5.place(x=19,y=47)
    qtyentry.place(x=11,y=100)
    l2.place(x=19,y=92)
    mrpentry.place(x=185,y=100)
    l3.place(x=193,y=92)
    catentry.place(x=11,y=145)
    l4.place(x=19,y=137)
    rl.place(x=12,y=190)
    eksbut.place(x=320,y=190)
    tickbut.place(x=270,y=190)
    
    infoemp.place(x=65,y=230)

def searchemp():
    for i in infoemp.winfo_children():
        i.place_forget()
    placeall()
    

    
    

searchbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                    fg_color='#ed6d31',text_color='black',image=search,width=40,
                                    height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=searchemp)
searchbut.place(x=385,y=190)

nameentry.bind('<FocusIn>',enter)
nameentry.bind('<FocusOut>',leave)

dark_title_bar(r)
r.mainloop()