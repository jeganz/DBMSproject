# Import module
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct



class custframe:
     def __init__(self,root,create_connection):
        # root = Tk()

        # Adjust size
        # root.geometry("1000x500+100+100")
        # root.resizable(False, False)
        # root.title("MK Mart")
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
            categframe.place(x=230,y=27.5)
            itemframe.place_forget()

        def itemclick():
            button1.configure(state='normal')
            button3.configure(state='disabled')
            itemframe.place(x=230,y=27.5)
            categframe.place_forget()
            

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

        categframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        categframe.place(x=230,y=27.5)

        heading=customtkinter.CTkLabel(categframe,text='Item Details',font=('Century Gothic', 18,'bold','underline'),width=100,text_color='black')
        heading.place(x=14,y=10)
        deptlist=list()
        con,cur=create_connection()
        strsql="select distinct category  from item"
        cur.execute(strsql)
        r=cur.fetchall()
        con.commit()
        con.close()
        for i in r:
            deptlist.append(i)
        depdata=list()
        def fetchdeptdata(dept):
            depdata.clear()
            con,cur=create_connection()
            strsql="select * from item where category='"+dept+"';"
            cur.execute(strsql)
            r=cur.fetchall()
            con.commit()
            con.close()
            for i in r:
                depdata.append(i)
        # fetchdata()

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Century Gothic', 11),background='#E5E5E5',rowheight=30,) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Century Gothic', 13,'bold underline'),background='#E5E5E5') # Modify the font of the headings
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        style.map('Treeview', background=[('selected', '#ed6d31')])

        mytr = ttk.Treeview(categframe,columns=("id","name",'Category','Stock','Price'),height=12)
        mytr.column("#0",width=50,minwidth=50)
        mytr.column('id',width=90,anchor=W)
        mytr.column('name',width=140,anchor=W)
        mytr.column('Category',width=120,anchor=W)
        mytr.column('Stock',width=120,anchor=W)
        mytr.column('Price',width=120,anchor=W)

        mytr.heading('#0',text='Sl.no')
        mytr.heading('name',text='Product Name',anchor=W)
        mytr.heading('id',text='Code',anchor=W)
        mytr.heading('Category',text='Category',anchor=W)
        mytr.heading('Stock',text='Stock',anchor=W)
        mytr.heading('Price',text='MRP',anchor=W)

        def updatedeptlist(e):
            fetchdeptdata(deptbox.get())
            for x in mytr.get_children():
                mytr.delete(x)
            count=0
            for i in depdata:
                mytr.insert(parent='',iid=count,text=count+1,index=END,values=(i[0],i[1],i[2],i[4],i[3]))
                count+=1
        mytr.place(x=10,y=45)
        search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((20,20)))
        searchentry=customtkinter.CTkEntry(categframe,width=305,height=30,font=('Century Gothic',12),fg_color='#E5E5E5',placeholder_text='ENTER NAME OR CODE',
                                        bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
        searchentry.place(x=75+230,y=9)
        l2=customtkinter.CTkLabel(categframe,text=' SEARCH ',text_color='black',fg_color='#E5E5E5',font=('Century Gothic', 10),height=15)
        l2.place(x=83+230,y=1)

        def refresh(e):
            for x in mytr.get_children():
                mytr.delete(x)
            count=0
            con,cur=create_connection()
            strsql=''
            if searchentry.get().isnumeric():
                strsql="select * from item where barcode like '"+searchentry.get()+"%' and category='"+deptbox.get()+"';"
            else:
                strsql="select * from item where name like '"+searchentry.get()+"%'and category='"+deptbox.get()+"';"
            cur.execute(strsql)
            r=cur.fetchall()
            count=0
            for i in r:
                mytr.insert(parent='',iid=count,text=count+1,index=END,values=(i[0],i[1],i[2],i[4],i[3]))
                count+=1
            con.commit()
            con.close()

        searchentry.bind('<KeyRelease>',refresh)

        def searchemp():
            pass

        searchbut=customtkinter.CTkButton(categframe,text='',font=('Century Gothic', 15,'bold'),
                                            fg_color='#ed6d31',text_color='black',image=search,width=35,
                                            height=30,hover_color='#f7a681',bg_color='#E5E5E5',command=searchemp)
        searchbut.place(x=385+230,y=9)
        def enter(e):
            searchentry.configure(border_color='#ed6d31')
            l2.configure(text_color='#ed6d31')
        def leave(e):
            searchentry.configure(border_color='black')
            l2.configure(text_color='black')
        searchentry.bind('<FocusIn>',enter)
        searchentry.bind('<FocusOut>',leave)


        deptbox=ttk.Combobox(categframe,width=25,font=('Century Gothic', 8),values=deptlist)
        deptbox.place(x=120,y=15)
        deptbox.bind('<<ComboboxSelected>>',updatedeptlist)

        #itempage
        itemframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        itemframe.place(x=230,y=27.5)

        heading=customtkinter.CTkLabel(itemframe,text='Item Details',font=('Century Gothic', 18,'bold','underline'),width=100,text_color='black')
        heading.place(x=14,y=10)

        data=list()
        def fetchdata():
            data.clear()
            con,cur=create_connection()
            strsql="select * from item"
            cur.execute(strsql)
            r=cur.fetchall()
            con.commit()
            con.close()
            for i in r:
                data.append(i)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Century Gothic', 11),background='#E5E5E5',rowheight=30,) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Century Gothic', 13,'bold underline'),background='#E5E5E5') # Modify the font of the headings
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        style.map('Treeview', background=[('selected', '#ed6d31')])

        mytree = ttk.Treeview(itemframe,columns=("id","name",'Category','Stock','Price'),height=12)
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
            fetchdata()
            for x in mytree.get_children():
                mytree.delete(x)
            count=0
            for i in data:
                mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[0],i[1],i[2],i[4],i[3]))
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
            con,cur=create_connection()
            strsql=''
            if nameentry.get().isnumeric():
                strsql="select * from item where barcode like '"+nameentry.get()+"%';"
            else:
                strsql="select * from item where name like '"+nameentry.get()+"%';"
            cur.execute(strsql)
            r=cur.fetchall()
            count=0
            for i in r:
                mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[0],i[1],i[2],i[4],i[3]))
                count+=1
            con.commit()
            con.close()

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

        # root.mainloop()


# empframe(None,None)
