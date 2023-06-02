from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct

class profileframe:
    def __init__(self,profileframe):
        # profilepic =ImageTk.PhotoImage(Image.open("profileicon.png").resize((100,100)))
        # customtkinter.CTkLabel(profileframe,image=profilepic,text="").place(x=620,y=30)
        namel=customtkinter.CTkLabel(profileframe,text='JAMES BOND',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 18,'bold'))
        namel.place(x=250,y=50)
        namel1=customtkinter.CTkLabel(profileframe,text='ID',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        namel1.place(x=105,y=150)
        namel2=customtkinter.CTkLabel(profileframe,text='Department',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        namel2.place(x=105,y=200)
        namel3=customtkinter.CTkLabel(profileframe,text='Salary',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        namel3.place(x=105,y=250)
        namel4=customtkinter.CTkLabel(profileframe,text='Phone No',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        namel4.place(x=105,y=300)
        named1=customtkinter.CTkLabel(profileframe,text=':',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        named1.place(x=275,y=150)
        named2=customtkinter.CTkLabel(profileframe,text=':',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        named2.place(x=275,y=200)
        named3=customtkinter.CTkLabel(profileframe,text=':',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        named3.place(x=275,y=250)
        named4=customtkinter.CTkLabel(profileframe,text=':',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 15,'bold'))
        named4.place(x=275,y=300)
        named1=customtkinter.CTkLabel(profileframe,text='007',text_color='black',fg_color='#E5E5E5')
        named1.place(x=290,y=150)
        named2=customtkinter.CTkLabel(profileframe,text='MI6',text_color='black',fg_color='#E5E5E5')
        named2.place(x=290,y=200)
        named3=customtkinter.CTkLabel(profileframe,text='12',text_color='black',fg_color='#E5E5E5')
        named3.place(x=290,y=250)
        named4=customtkinter.CTkLabel(profileframe,text='85877587575',text_color='black',fg_color='#E5E5E5')
        named4.place(x=290,y=300)
