# Import module
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct

class itempage:
    def __init__(self,itemframe):
         
        def dark_title_bar(window):
            window.update()
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
            get_parent = ct.windll.user32.GetParent
            hwnd = get_parent(window.winfo_id())
            rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
            value = 2
            value = ct.c_int(value)
            set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                                ct.sizeof(value))

        # itemframe=Tk()
        # itemframe.geometry('750x450')
        # itemframe.title('Add new employee')

        heading=customtkinter.CTkLabel(itemframe,text='Item Details',font=('Century Gothic', 18,'bold','underline'),width=100,text_color='black')
        heading.place(x=14,y=10)

        data=[['abc',1,'stationary',12,87],['bcd',2,'vegtable',5,75],['drf',3,'vegetable',7,120]
            ]

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Century Gothic', 11),background='#E5E5E5',rowheight=30,) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Century Gothic', 13,'bold underline'),background='#E5E5E5') # Modify the font of the headings
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        style.map('Treeview', background=[('selected', '#ed6d31')])

        mytree = ttk.Treeview(itemframe,columns=("id","name",'Category','Stock','Price'))
        mytree.column("#0",width=50,minwidth=50)
        mytree.column('id',width=90,anchor=W)
        mytree.column('name',width=140,anchor=W)
        mytree.column('Category',width=120,anchor=W)
        mytree.column('Stock',width=120,anchor=W)
        mytree.column('Price',width=120,anchor=W)

        mytree.heading('#0',text='Sl.no')
        mytree.heading('name',text='Product Name',anchor=W)
        mytree.heading('id',text='Code',anchor=W)
        mytree.heading('Category',text='Category',anchor=W)
        mytree.heading('Stock',text='Stock',anchor=W)
        mytree.heading('Price',text='MRP',anchor=W)

        def updatelist():
            for x in mytree.get_children():
                mytree.delete(x)
            count=0
            for i in data:
                mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[1],i[0],i[2],i[3],i[4]))
                count+=1
        updatelist()
        mytree.place(x=10,y=40)

        def additem():
            r=Toplevel()
            r.geometry('500x500')
            r.title('Add new item')

            bgimg=ImageTk.PhotoImage(Image.open('additemform.png'))

            bg=customtkinter.CTkLabel(r,text='',image=bgimg)
            bg.place(x=0,y=0)
            # bg=Frame(r,bg='#d9d9d9')
            # bg.pack(fill=BOTH,expand=1)
            

            def enter(e):
                nameentry.configure(border_color='#ed6d31')
                l1.configure(text_color='#ed6d31')
            def leave(e):
                nameentry.configure(border_color='black')
                l1.configure(text_color='black')


            nameentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            nameentry.place(x=75,y=210)
            l1=customtkinter.CTkLabel(bg,text=' NAME ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l1.place(x=83,y=202)

            nameentry.bind('<FocusIn>',enter)
            nameentry.bind('<FocusOut>',leave)

            def enter(e):
                codeentry.configure(border_color='#ed6d31')
                l5.configure(text_color='#ed6d31')
            def leave(e):
                codeentry.configure(border_color='black')
                l5.configure(text_color='black')


            codeentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            codeentry.place(x=75,y=255)
            l5=customtkinter.CTkLabel(bg,text=' CODE ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l5.place(x=83,y=247)

            codeentry.bind('<FocusIn>',enter)
            codeentry.bind('<FocusOut>',leave)

            def enter(e):
                qtyentry.configure(border_color='#ed6d31')
                l2.configure(text_color='#ed6d31')
            def leave(e):
                qtyentry.configure(border_color='black')
                l2.configure(text_color='black')


            qtyentry=customtkinter.CTkEntry(bg,width=170,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            qtyentry.place(x=75,y=300)
            l2=customtkinter.CTkLabel(bg,text=' STOCK ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l2.place(x=83,y=292)

            qtyentry.bind('<FocusIn>',enter)
            qtyentry.bind('<FocusOut>',leave)

            def enter(e):
                mrpentry.configure(border_color='#ed6d31')
                l3.configure(text_color='#ed6d31')
            def leave(e):
                mrpentry.configure(border_color='black')
                l3.configure(text_color='black')


            mrpentry=customtkinter.CTkEntry(bg,width=175,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            mrpentry.place(x=250,y=300)
            l3=customtkinter.CTkLabel(bg,text=' PRICE ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l3.place(x=258,y=292)

            mrpentry.bind('<FocusIn>',enter)
            mrpentry.bind('<FocusOut>',leave)

            def enter(e):
                catentry.configure(border_color='#ed6d31')
                l4.configure(text_color='#ed6d31')
            def leave(e):
                catentry.configure(border_color='black')
                l4.configure(text_color='black')

            catentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            catentry.place(x=75,y=345)
            l4=customtkinter.CTkLabel(bg,text=' CATEGORY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l4.place(x=83,y=337)

            catentry.bind('<FocusIn>',enter)
            catentry.bind('<FocusOut>',leave)
            def addempsubmit():
                data.append([nameentry.get(),int(codeentry.get()),catentry.get(),qtyentry.get(),mrpentry.get()])
                updatelist()
                r.destroy()
            addempbut=customtkinter.CTkButton(bg,text='SUBMIT',font=('Century Gothic', 15,'bold'),
                                            fg_color='#ed6d31',text_color='black',bg_color='#d9d9d9',
                                            height=35,hover_color='#f7a681',command=addempsubmit)
            addempbut.place(relx=.5,y=450,anchor=CENTER)

            dark_title_bar(r)
            r.mainloop()
        def delitem():
            r=Toplevel()
            r.geometry('500x500')
            r.title('Add new employee')

            img=ImageTk.PhotoImage(Image.open('delitemform.png'))
            search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((25,25)))
            tick=ImageTk.PhotoImage(Image.open('tickicon.png').resize((25,25)))
            eks=ImageTk.PhotoImage(Image.open('eksicon.png').resize((25,25)))
            warning=ImageTk.PhotoImage(Image.open('warningicon.png'))

            bg=customtkinter.CTkLabel(r,text='',image=img)
            bg.place(x=0,y=0)

            infoemp=customtkinter.CTkFrame(bg,width=350,height=210,bg_color='#d9d9d9',fg_color='#d9d9d9')


            def labels(text,x,y,content):
                namel=customtkinter.CTkLabel(infoemp,text=text,text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
                l=customtkinter.CTkLabel(infoemp,text=':',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
                namel.place(x=x,y=y)
                l.place(x=80,y=y-.5)
                dl=customtkinter.CTkLabel(infoemp,text=content,text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15))
                dl.place(x=90,y=y)
            rl=customtkinter.CTkLabel(infoemp,text='REMOVE THIS ITEM ?',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
            
            def delconfirm():
                id=int(nameentry.get())
                for i in data:
                    if id in i:
                        data.remove(i)
                updatelist()
                r.destroy()
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
                l1.configure(text_color='#ed6d31')
            def leave(e):
                nameentry.configure(border_color='black')
                l1.configure(text_color='black')


            nameentry=customtkinter.CTkEntry(bg,width=305,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',placeholder_text='ENTER PRODUCT CODE',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
            nameentry.place(x=75,y=190)
            l1=customtkinter.CTkLabel(bg,text=' SEARCH ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l1.place(x=83,y=182)

            def searchemp():
                for i in infoemp.winfo_children():
                    i.place_forget()
                id=int(nameentry.get())
                flag=0
                for i in data:
                    if id in i:
                        labels('NAME',1,6,i[0])
                        labels('CODE',1,36,i[1])
                        labels('PRICE',1,66,i[3])
                        labels('CATEG',1,96,i[2])
                        eksbut.place(x=310,y=122)
                        tickbut.place(x=260,y=122)
                        rl.place(x=1,y=126)
                        flag=1
                if flag==0:
                    notfound.place(x=80,y=10)

                
                infoemp.place(x=75,y=270)

            searchbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                                fg_color='#ed6d31',text_color='black',image=search,width=40,
                                                height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=searchemp)
            searchbut.place(x=385,y=190)

            nameentry.bind('<FocusIn>',enter)
            nameentry.bind('<FocusOut>',leave)

            dark_title_bar(r)
            r.mainloop()
        def moditem():
            r=Toplevel()
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
                id=int(searchentry.get())
                for i in data:
                    if id in i:
                        data.remove(i)
                updatelist()
                r.destroy()
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
                searchentry.configure(border_color='#ed6d31')
                l.configure(text_color='#ed6d31')
            def leave(e):
                searchentry.configure(border_color='black')
                l.configure(text_color='black')


            searchentry=customtkinter.CTkEntry(bg,width=305,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',placeholder_text='ENTER PRODUCT CODE',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
            searchentry.place(x=75,y=190)
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

            def searchitem():
                for i in infoemp.winfo_children():
                    i.place_forget()
                id=int(searchentry.get())
                flag=0
                for i in data:
                    if id == i[1]:
                        placeall()
                        inameentry.insert(0,i[0])
                        codeentry.insert(0,i[1])
                        qtyentry.insert(0,i[3])
                        mrpentry.insert(0,i[4])
                        catentry.insert(0,i[2])
                        codeentry.configure(state=DISABLED)
                        flag=1
                

            searchbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                                fg_color='#ed6d31',text_color='black',image=search,width=40,
                                                height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=searchitem)
            searchbut.place(x=385,y=190)

            searchentry.bind('<FocusIn>',enter)
            searchentry.bind('<FocusOut>',leave)

            dark_title_bar(r)
            r.mainloop()
        def buttons(text,x,y,img1,img2,command):
            def enter(e):
                addempbut.configure(text_color='#ed6d31',border_color='#ed6d31',image=img2)
            def leave(e):
                addempbut.configure(text_color='black',border_color='black',image=img1)
            
            addempbut=customtkinter.CTkButton(itemframe,text=text,font=('Century Gothic', 13),
                                            fg_color='#d1d1d1',text_color='black',border_color='black',width=140,
                                            border_width=2,image=img1,command=command)
            addempbut.place(x=x,y=y)
            addempbut.bind('<Enter>',enter)
            addempbut.bind('<Leave>',leave)

        additemicon=ImageTk.PhotoImage(Image.open("additemicon.png").resize((30,30)))
        additemicon2=ImageTk.PhotoImage(Image.open("additemicon2.png").resize((30,30)))
        buttons('Add Product',10,405,additemicon,additemicon2,additem)

        delitemicon=ImageTk.PhotoImage(Image.open("delitemicon.png").resize((30,30)))
        delitemicon2=ImageTk.PhotoImage(Image.open("delitemicon2.png").resize((30,30)))
        buttons('Delete Product',160,405,delitemicon,delitemicon2,delitem)

        moditemicon=ImageTk.PhotoImage(Image.open("moditemicon.png").resize((30,30)))
        moditemicon2=ImageTk.PhotoImage(Image.open("moditemicon2.png").resize((30,30)))
        buttons('Modify Product',320,405,moditemicon,moditemicon2,moditem)

        outofstock=ImageTk.PhotoImage(Image.open("outofstock.png").resize((30,30)))
        outofstock2=ImageTk.PhotoImage(Image.open("outofstock2.png").resize((30,30)))
        buttons('Out of Stock',480,405,outofstock,outofstock2,delitem)

        # delitemicon=ImageTk.PhotoImage(Image.open("delitemicon.png").resize((30,30)))
        # delitemicon2=ImageTk.PhotoImage(Image.open("delitemicon2.png").resize((30,30)))
        # buttons('Delete Product',610,405,delitemicon,delitemicon2,delitem)


        # itemframe.mainloop()


