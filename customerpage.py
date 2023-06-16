# Import module
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct



class empframe:
     def __init__(self,root,create_connection):
        root = Tk()

        # Adjust size
        root.geometry("1000x500+100+100")
        root.resizable(False, False)
        root.title("MK Mart")
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
        
        def enter1(e):
            button1.configure(text_color='#ed6d31')
        def leave1(e):
            button1.configure(text_color='white')
        def enter3(e):
            button3.configure(text_color='#ed6d31')
        def leave3(e):
            button3.configure(text_color='white')
        def enter(e):
            logoutbutton.configure(image=logouticon2)
        def leave(e):
            logoutbutton.configure(image=logouticon)


        #button functions 
        def profileclick():
            button1.configure(state='disabled')
            button3.configure(state='normal')
            profileframe.place(x=230,y=27.5)
            itemframe.place_forget()

        def itemclick():
            button1.configure(state='normal')
            button3.configure(state='disabled')
            itemframe.place(x=230,y=27.5)
            profileframe.place_forget()
            

        #admin login page

        employpage = Frame(root)
        employpage.pack(fill=BOTH,expand=1)

        #sidebar of admin login page

        sidebar = Canvas(master=employpage,width=1000,height=500,background='#000000')
        sidebar.place(x=-2,y=-2)

        mkmart =ImageTk.PhotoImage(Image.open("MKMart2.png").resize((249,249)))

        martbg=customtkinter.CTkLabel(sidebar,width=250,height=250,fg_color='black',image=mkmart,text='')
        martbg.place(x=-10,y=0)

        sidebar.create_image( -10, -15, image = mkmart,anchor = "nw")
        button3 = customtkinter.CTkButton(master=sidebar,state=DISABLED,width=220,corner_radius=0,height=50,text_color='white',
                                          fg_color="transparent", text="All Items",font=('Century Gothic',20,'bold'),
                                          command=itemclick,text_color_disabled='#ed6d31')
        button3.place(x=1,y=210)
        button3.bind('<Enter>',enter3)
        button3.bind('<Leave>',leave3)

        # button2 = customtkinter.CTkButton(master=sidebar,width=220,corner_radius=0,height=50,text_color='white',fg_color="transparent", text="Employee",font=('Century Gothic',20,'bold'),command=employeeclick,text_color_disabled='#ed6d31')
        # button2.place(x=1,y=251)
        # button2.bind('<Enter>',enter2)
        # button2.bind('<Leave>',leave2)

        button1 = customtkinter.CTkButton(master=sidebar,width=220,corner_radius=0,height=50,text_color='white',
                                          fg_color="transparent", text="By Category",font=('Century Gothic',20,'bold'),
                                          command=profileclick,text_color_disabled='#ed6d31')
        button1.place(x=1,y=261)
        button1.bind('<Enter>',enter1)
        button1.bind('<Leave>',leave1)

        def empLogout():
            employpage.pack_forget()

        logouticon =ImageTk.PhotoImage(Image.open("logouticon.png"))
        logouticon2 =ImageTk.PhotoImage(Image.open("logouticon2.png"))
        logoutbutton = customtkinter.CTkButton(master=sidebar,image=logouticon,text='',corner_radius=10,hover_color='#000000',fg_color='transparent',width=35,font=('Century Gothic',15), command=empLogout)
        logoutbutton.place(x=1,y=462)
        logoutbutton.bind('<Enter>',enter)
        logoutbutton.bind('<Leave>',leave)

        #profile page

        profileframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        profilepic =ImageTk.PhotoImage(Image.open("profileicon.png").resize((100,100)))
        customtkinter.CTkLabel(profileframe,image=profilepic,text="").place(x=620,y=30)
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
        #itempage
        itemframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        itemframe.place(x=230,y=27.5)

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
        mytree.place(x=10,y=45)
        search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((20,20)))
        nameentry=customtkinter.CTkEntry(itemframe,width=305,height=30,font=('Century Gothic',12),fg_color='#E5E5E5',placeholder_text='ENTER NAME OR CODE',
                                        bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
        nameentry.place(x=75+230,y=9)
        l1=customtkinter.CTkLabel(itemframe,text=' SEARCH ',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 10),height=15)
        l1.place(x=83+230,y=1)

        def refresh(e):
            for x in mytree.get_children():
                mytree.delete(x)
            count=0
            for i in data:
                if nameentry.get().isnumeric() and nameentry.get() in str(i[1]):
                    mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[1],i[0],i[2],i[3],i[4]))
                    count+=1
                elif nameentry.get() in i[0]:
                    mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[1],i[0],i[2],i[3],i[4]))
                    count+=1

        nameentry.bind('<KeyRelease>',refresh)

        def searchemp():
            pass

        searchbut=customtkinter.CTkButton(itemframe,text='',font=('Century Gothic', 15,'bold'),
                                            fg_color='#ed6d31',text_color='black',image=search,width=35,
                                            height=30,hover_color='#f7a681',bg_color='#E5E5E5',command=searchemp)
        searchbut.place(x=385+230,y=9)
        def enter(e):
            nameentry.configure(border_color='#ed6d31')
            l1.configure(text_color='#ed6d31')
        def leave(e):
            nameentry.configure(border_color='black')
            l1.configure(text_color='black')
        nameentry.bind('<FocusIn>',enter)
        nameentry.bind('<FocusOut>',leave)

        root.mainloop()


empframe(None,None)
