from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct

class errpopup:
    def __init__(self,msg) -> None:
        r=Tk()
        warn=ImageTk.PhotoImage(Image.open('warning icon.png').resize((80,80)))
        down=ImageTk.PhotoImage(Image.open('down.png'))
        left=ImageTk.PhotoImage(Image.open('left.png'))
        r.overrideredirect(True)
        def moveapp(e):
            global height
            r.geometry('300x'+str(height)+f'+{e.x_root}+{e.y_root}')
        r.bind('<B1-Motion>',moveapp)
        global height,status,fheight
        height=250
        fheight=0
        status='forward'
        def show(e):
            global height,status,fheight
            if status == 'forward':
                height+=2
                fheight+=3
                errdetails.configure(image=left)
                if height<=300:
                    r.update()
                    r.geometry('300x'+str(height))
                    detframe.configure(height=fheight)
                    r.after(5,show(e))
                status='backward'
            elif status=='backward':
                height-=2
                fheight-=3
                errdetails.configure(image=down)
                if height>=250:
                    r.update()
                    r.geometry('300x'+str(height))
                    detframe.configure(height=fheight)
                    r.after(5,show(e))
                status = 'forward'

        def resize():
            r.destroy()
        r.geometry('300x'+str(height)+'+100+100')
        redf=customtkinter.CTkFrame(r,height=100,fg_color='#f65656',corner_radius=0)
        redf.pack(fill=X)
        warnicon=customtkinter.CTkLabel(redf,text='',image=warn).place(relx=.5,rely=.5,anchor=CENTER)

        errheading=customtkinter.CTkLabel(r,text="ERROR!",text_color='black',font=('Century Gothic', 25,'bold'))
        errheading.pack(pady=25)

        errdetails=customtkinter.CTkLabel(r,text="Details",image=down,compound=RIGHT,text_color='black',font=('Century Gothic', 13))
        errdetails.place(relx=.5,y=165,anchor=CENTER)
        errdetails.bind('<Button-1>',show)

        detframe=customtkinter.CTkFrame(r,width=200,height=fheight,fg_color='transparent',corner_radius=0)
        detframe.place(x=50,y=175)

        errmsg=customtkinter.CTkLabel(detframe,
                                    text=msg,
                                    text_color='red',fg_color='transparent',font=('Century Gothic', 12),anchor='w',wraplength=200)
        errmsg.place(x=0,y=0)

        customtkinter.CTkButton(r,text='CLOSE',command=resize,width=100,corner_radius=30,fg_color='#f65656',
                                font=('Century Gothic', 12,'bold')).place(relx=.5,rely=.88,anchor=CENTER)

        r.mainloop()

errpopup('Given image is not CTkImage but. Image can not be scaled on HighDPI displays, use CTkImage instead.')