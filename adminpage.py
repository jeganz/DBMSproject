from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct
import mysql.connector
import itempage
import profilepage

class adminpage:
    def __init__(self,root,user,create_connection,):
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

        # Create object
        # root = Tk()

        # # Adjust size
        # root.geometry("1000x500+10+10")
        # root.resizable(False,False)


        def enter1(e):
            button1.configure(text_color='#ed6d31')
        def leave1(e):
            button1.configure(text_color='white')
        def enter2(e):
            button2.configure(text_color='#ed6d31')
        def leave2(e):
            button2.configure(text_color='white')
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
            button3.configure(state='disabled')
            button2.configure(state='normal')
            button1.configure(state='normal')
            profileframe.place(x=230,y=27.5)
            itemframe.place_forget()
            employeeframe.place_forget()

        def itemclick():
            button3.configure(state='normal')
            button2.configure(state='normal')
            button1.configure(state='disabled')
            itemframe.place(x=230,y=27.5)
            profileframe.place_forget()
            employeeframe.place_forget()
            
        def employeeclick():
            button3.configure(state='normal')
            button2.configure(state='disabled')
            button1.configure(state='normal')
            employeeframe.place(x=230,y=27.5)
            itemframe.place_forget()
            profileframe.place_forget()
            

        #admin login page

        adminpage = Frame(root)
        adminpage.pack(fill=BOTH,expand=1)

        #sidebar of admin login page
        def adminlogout():
            adminpage.pack_forget()
        sidebar = Canvas(master=adminpage,width=1000,height=500,background='#000000')
        sidebar.place(x=-2,y=-2)
        
        mkmart =ImageTk.PhotoImage(Image.open("MKMart2.png").resize((249,249)))
        
        martbg=customtkinter.CTkLabel(sidebar,width=250,height=250,fg_color='black',image=mkmart,text='')
        martbg.place(x=-10,y=0)
        button3 = customtkinter.CTkButton(sidebar,state=DISABLED,width=220,corner_radius=0,height=50,text_color='white',fg_color="transparent", text="Profile",font=('Century Gothic',20,'bold'),command=profileclick,text_color_disabled='#ed6d31')
        button3.place(x=1,y=200)
        button3.bind('<Enter>',enter3)
        button3.bind('<Leave>',leave3)

        button2 = customtkinter.CTkButton(master=sidebar,width=220,corner_radius=0,height=50,text_color='white',fg_color="transparent", text="Employee",font=('Century Gothic',20,'bold'),command=employeeclick,text_color_disabled='#ed6d31')
        button2.place(x=1,y=251)
        button2.bind('<Enter>',enter2)
        button2.bind('<Leave>',leave2)

        button1 = customtkinter.CTkButton(master=sidebar,width=220,corner_radius=0,height=50,text_color='white',fg_color="transparent", text="Item",font=('Century Gothic',20,'bold'),command=itemclick,text_color_disabled='#ed6d31')
        button1.place(x=1,y=301)
        button1.bind('<Enter>',enter1)
        button1.bind('<Leave>',leave1)

        logouticon =ImageTk.PhotoImage(Image.open("logouticon.png"))
        logouticon2 =ImageTk.PhotoImage(Image.open("logouticon2.png"))
        logoutbutton = customtkinter.CTkButton(master=sidebar,image=logouticon,text='',corner_radius=10,command=adminlogout,
                                        hover_color='#000000',fg_color='transparent',width=35,font=('Century Gothic',15))
        logoutbutton.place(x=1,y=462)
        logoutbutton.bind('<Enter>',enter)
        logoutbutton.bind('<Leave>',leave)

        #profile page

        profileframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        profileframe.place(x=230,y=27.5)
        profilepage.profileframe(profileframe,user)

        #itempage
        itemframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')
        itempage.itempage(itemframe,create_connection)

        #employeepage
        

        employeeframe=customtkinter.CTkFrame(sidebar,width=750,height=450,corner_radius=10,fg_color='#E5E5E5')

        heading=customtkinter.CTkLabel(employeeframe,text='Employee Details',font=('Century Gothic', 18,'bold','underline'),width=150,text_color='black')
        heading.place(x=14,y=10)

        data=list()
        def fetchdata():
            data.clear()
            con,cur=create_connection()
            strsql="select * from employee"
            cur.execute(strsql)
            r=cur.fetchall()
            con.commit()
            con.close()
            for i in r:
                data.append(i)
        # fetchdata()
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Century Gothic', 11),background='#E5E5E5',rowheight=30,) # Modify the font of the body
        style.configure("Treeview.Heading", font=('Century Gothic', 13,'bold underline'),background='#E5E5E5') # Modify the font of the headings
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        style.map('Treeview', background=[('selected', '#ed6d31')])

        mytree = ttk.Treeview(employeeframe,columns=("name","id",'department','salary','city','phno'))
        mytree.column("#0",width=50,minwidth=50)
        mytree.column('name',width=120,anchor=W)
        mytree.column('id',width=50,anchor=CENTER)
        mytree.column('department',width=120,anchor=W)
        mytree.column('salary',width=100,anchor=W)
        mytree.column('city',width=140,anchor=W)
        mytree.column('phno',width=140,anchor=W)


        mytree.heading('#0',text='Sl.no')
        mytree.heading('name',text='Name',anchor=W)
        mytree.heading('id',text='ID')
        mytree.heading('department',text='Department',anchor=W)
        mytree.heading('salary',text='Salary',anchor=W)
        mytree.heading('city',text='City',anchor=W)
        mytree.heading('phno',text='PH.NO',anchor=W)

        def updatelist():
            fetchdata()
            for x in mytree.get_children():
                mytree.delete(x)
            count=0
            for i in data:
                mytree.insert(parent='',iid=count,text=count+1,index=END,values=(i[1],i[0],i[7],i[4],i[6],i[5]))
                count+=1
        updatelist()
        mytree.place(x=10,y=40)

        def addemp():
            r=Toplevel()
            r.geometry('500x500')
            r.title('Add new employee')

            bgimg=ImageTk.PhotoImage(Image.open('addempform.png'))

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
            nameentry.place(x=75,y=210-15)
            l1=customtkinter.CTkLabel(bg,text=' NAME ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l1.place(x=83,y=202-15)

            nameentry.bind('<FocusIn>',enter)
            nameentry.bind('<FocusOut>',leave)

            def enter(e):
                identry.configure(border_color='#ed6d31')
                l2.configure(text_color='#ed6d31')
            def leave(e):
                identry.configure(border_color='black')
                l2.configure(text_color='black')


            identry=customtkinter.CTkEntry(bg,width=170,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            identry.place(x=75,y=255-15)
            l2=customtkinter.CTkLabel(bg,text=' ID ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l2.place(x=83,y=247-15)

            identry.bind('<FocusIn>',enter)
            identry.bind('<FocusOut>',leave)

            def enter(e):
                salentry.configure(border_color='#ed6d31')
                l3.configure(text_color='#ed6d31')
            def leave(e):
                salentry.configure(border_color='black')
                l3.configure(text_color='black')


            salentry=customtkinter.CTkEntry(bg,width=175,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            salentry.place(x=250,y=255-15)
            l3=customtkinter.CTkLabel(bg,text=' SALARY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l3.place(x=258,y=247-15)

            salentry.bind('<FocusIn>',enter)
            salentry.bind('<FocusOut>',leave)

            def enter(e):
                deptentry.configure(border_color='#ed6d31')
                l4.configure(text_color='#ed6d31')
            def leave(e):
                deptentry.configure(border_color='black')
                l4.configure(text_color='black')


            deptentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            deptentry.place(x=75,y=300-15)
            l4=customtkinter.CTkLabel(bg,text=' DEPARTMENT ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l4.place(x=83,y=292-15)

            deptentry.bind('<FocusIn>',enter)
            deptentry.bind('<FocusOut>',leave)

            def enter(e):
                cityentry.configure(border_color='#ed6d31')
                l5.configure(text_color='#ed6d31')
            def leave(e):
                cityentry.configure(border_color='black')
                l5.configure(text_color='black')


            cityentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            cityentry.place(x=75,y=345-15)
            l5=customtkinter.CTkLabel(bg,text=' CITY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l5.place(x=83,y=337-15)

            cityentry.bind('<FocusIn>',enter)
            cityentry.bind('<FocusOut>',leave)

            def enter(e):
                phnoentry.configure(border_color='#ed6d31')
                l6.configure(text_color='#ed6d31')
            def leave(e):
                phnoentry.configure(border_color='black')
                l6.configure(text_color='black')


            phnoentry=customtkinter.CTkEntry(bg,width=250,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            phnoentry.place(x=75,y=390-15)
            l6=customtkinter.CTkLabel(bg,text=' PH NO ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l6.place(x=83,y=382-15)

            phnoentry.bind('<FocusIn>',enter)
            phnoentry.bind('<FocusOut>',leave)

            adminbut=customtkinter.CTkCheckBox(bg,text='ADMIN',height=35,width=50,text_color='black',font=('Century Gothic', 15),
                                            bg_color='#d9d9d9',checkbox_height=30,checkbox_width=30,border_color='black',checkmark_color='black',
                                            hover_color='#d9d9d9', onvalue="yes", offvalue="no")
            adminbut.place(x=335,y=390-15)

            def enter(e):
                passentry.configure(border_color='#ed6d31')
                l7.configure(text_color='#ed6d31')
            def leave(e):
                passentry.configure(border_color='black')
                l7.configure(text_color='black')


            passentry=customtkinter.CTkEntry(bg,width=200,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            passentry.place(x=75,y=435-15)
            l7=customtkinter.CTkLabel(bg,text=' PASSWORD ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l7.place(x=83,y=427-15)

            passentry.bind('<FocusIn>',enter)
            passentry.bind('<FocusOut>',leave)

            def addempsubmit():
                # data.append([nameentry.get(),int(identry.get()),deptentry.get()])
                L = (int(identry.get()),nameentry.get(), passentry.get(),adminbut.get(),float(salentry.get()),phnoentry.get()
                     ,cityentry.get(),deptentry.get())
                con,cur=create_connection()
                strsql="insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(strsql,L)
                con.commit()
                con.close()
                updatelist()
                r.destroy()
            addempbut=customtkinter.CTkButton(bg,text='SUBMIT',font=('Century Gothic', 15,'bold'),
                                            fg_color='#ed6d31',text_color='black',bg_color='#d9d9d9',
                                            height=35,hover_color='#f7a681',command=addempsubmit)
            addempbut.place(x=285,y=420)

            dark_title_bar(r)
            r.mainloop()
        def delemp():
            r=Toplevel()
            r.geometry('500x500')
            r.title('Add new employee')

            img=ImageTk.PhotoImage(Image.open('delempform.png'))
            search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((25,25)))
            tick=ImageTk.PhotoImage(Image.open('tickicon.png').resize((25,25)))
            eks=ImageTk.PhotoImage(Image.open('eksicon.png').resize((25,25)))
            warning=ImageTk.PhotoImage(Image.open('warningicon.png'))

            bg=customtkinter.CTkLabel(r,text='',image=img)
            bg.place(x=0,y=0)
            # bg=Canvas(r,width= 500,height= 500)
            # bg.place(x=0,y=0)
            # img=bg.create_image(0,0,image=img,anchor=NW)

            infoemp=customtkinter.CTkFrame(bg,width=350,height=210,bg_color='#d9d9d9',fg_color='#d9d9d9')


            def labels(text,x,y,content):
                namel=customtkinter.CTkLabel(infoemp,text=text,text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
                l=customtkinter.CTkLabel(infoemp,text=':',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
                namel.place(x=x,y=y)
                l.place(x=80,y=y-.5)
                dl=customtkinter.CTkLabel(infoemp,text=content,text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15))
                dl.place(x=90,y=y)
            rl=customtkinter.CTkLabel(infoemp,text='REMOVE THIS EMPLOYEE ?',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))
            
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


            nameentry=customtkinter.CTkEntry(bg,width=305,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',placeholder_text='ENTER EMPLOYEE ID',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
            nameentry.place(x=75,y=210)
            l1=customtkinter.CTkLabel(bg,text=' SEARCH ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l1.place(x=83,y=202)

            def searchemp():
                for i in infoemp.winfo_children():
                    i.place_forget()
                id=int(nameentry.get())
                flag=0
                for i in data:
                    if id in i:
                        labels('NAME',1,6,i[0])
                        labels('ID',1,36,i[1])
                        labels('SALARY',1,66,'')
                        labels('DEPT',1,96,i[2])
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
            searchbut.place(x=385,y=210)

            nameentry.bind('<FocusIn>',enter)
            nameentry.bind('<FocusOut>',leave)

            dark_title_bar(r)
            r.mainloop()
        def modemp():
            r=Toplevel()
            r.geometry('500x500')
            r.title('Modify an item')

            img=ImageTk.PhotoImage(Image.open('modempform.png'))
            search=ImageTk.PhotoImage(Image.open('searchicon.png').resize((25,25)))
            tick=ImageTk.PhotoImage(Image.open('tickicon.png').resize((25,25)))
            eks=ImageTk.PhotoImage(Image.open('eksicon.png').resize((25,25)))
            warning=ImageTk.PhotoImage(Image.open('warningicon.png'))

            bg=customtkinter.CTkLabel(r,text='',image=img)
            bg.place(x=0,y=0)

            infoemp=customtkinter.CTkFrame(bg,width=370,height=250,bg_color='#d9d9d9',fg_color='#d9d9d9')

            def enter(e):
                nameentry.configure(border_color='#ed6d31')
                l1.configure(text_color='#ed6d31')
            def leave(e):
                nameentry.configure(border_color='black')
                l1.configure(text_color='black')


            nameentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l1=customtkinter.CTkLabel(bg,text=' NAME ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            nameentry.bind('<FocusIn>',enter)
            nameentry.bind('<FocusOut>',leave)

            def enter(e):
                identry.configure(border_color='#ed6d31')
                l2.configure(text_color='#ed6d31')
            def leave(e):
                identry.configure(border_color='black')
                l2.configure(text_color='black')


            identry=customtkinter.CTkEntry(bg,width=170,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l2=customtkinter.CTkLabel(bg,text=' ID ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            identry.bind('<FocusIn>',enter)
            identry.bind('<FocusOut>',leave)

            def enter(e):
                salentry.configure(border_color='#ed6d31')
                l3.configure(text_color='#ed6d31')
            def leave(e):
                salentry.configure(border_color='black')
                l3.configure(text_color='black')


            salentry=customtkinter.CTkEntry(bg,width=175,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l3=customtkinter.CTkLabel(bg,text=' SALARY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            salentry.bind('<FocusIn>',enter)
            salentry.bind('<FocusOut>',leave)

            def enter(e):
                deptentry.configure(border_color='#ed6d31')
                l4.configure(text_color='#ed6d31')
            def leave(e):
                deptentry.configure(border_color='black')
                l4.configure(text_color='black')


            deptentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l4=customtkinter.CTkLabel(bg,text=' DEPARTMENT ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            deptentry.bind('<FocusIn>',enter)
            deptentry.bind('<FocusOut>',leave)

            def enter(e):
                cityentry.configure(border_color='#ed6d31')
                l5.configure(text_color='#ed6d31')
            def leave(e):
                cityentry.configure(border_color='black')
                l5.configure(text_color='black')


            cityentry=customtkinter.CTkEntry(bg,width=350,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l5=customtkinter.CTkLabel(bg,text=' CITY ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            cityentry.bind('<FocusIn>',enter)
            cityentry.bind('<FocusOut>',leave)

            def enter(e):
                phnoentry.configure(border_color='#ed6d31')
                l6.configure(text_color='#ed6d31')
            def leave(e):
                phnoentry.configure(border_color='black')
                l6.configure(text_color='black')


            phnoentry=customtkinter.CTkEntry(bg,width=250,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l6=customtkinter.CTkLabel(bg,text=' PH NO ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            phnoentry.bind('<FocusIn>',enter)
            phnoentry.bind('<FocusOut>',leave)

            adminbut=customtkinter.CTkCheckBox(bg,text='ADMIN',height=35,width=50,text_color='black',font=('Century Gothic', 15),
                                            bg_color='#d9d9d9',checkbox_height=30,checkbox_width=30,border_color='black',checkmark_color='black',
                                            hover_color='#d9d9d9', onvalue="yes", offvalue="no")
            

            def enter(e):
                passentry.configure(border_color='#ed6d31')
                l7.configure(text_color='#ed6d31')
            def leave(e):
                passentry.configure(border_color='black')
                l7.configure(text_color='black')


            passentry=customtkinter.CTkEntry(bg,width=200,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black')
            
            l7=customtkinter.CTkLabel(bg,text=' PASSWORD ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            

            passentry.bind('<FocusIn>',enter)
            passentry.bind('<FocusOut>',leave)

            rl=customtkinter.CTkLabel(infoemp,text='SAVE THE CHANGES ?',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))

            def delconfirm():
                id=searchentry.get()
                con,cur=create_connection()
                strsql=f"update employee set  empid={identry.get()},name='{nameentry.get()}',pass='{passentry.get()}',"\
                    f"admin='{adminbut.get()}',salary={salentry.get()},phone_no='{phnoentry.get()}',city='{cityentry.get()}',department='{deptentry.get()}' where empid='"+id+"';"
                cur.execute(strsql)
                con.commit()
                con.close()
                updatelist()
                r.destroy()
            def delcancel():
                for i in bg.winfo_children():
                    if i not in (searchentry,l,searchbut):
                        i.place_forget()
            tickbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                                fg_color='#ed6d31',text_color='black',image=tick,width=40,
                                                height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=delconfirm)

            eksbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                                fg_color='black',image=eks,width=40,
                                                height=35,hover_color='gray',bg_color='#d9d9d9',command=delcancel)


            notfound=customtkinter.CTkLabel(infoemp,image=warning,compound=TOP,text='Item not Found',text_color='red',fg_color='#D9D9D9',font=('Century Gothic', 15,'bold'))

            def enter(e):
                searchentry.configure(border_color='#ed6d31')
                l.configure(text_color='#ed6d31')
            def leave(e):
                searchentry.configure(border_color='black')
                l.configure(text_color='black')


            searchentry=customtkinter.CTkEntry(bg,width=305,height=35,font=('Century Gothic',12),fg_color='#D9D9D9',placeholder_text='ENTER EMPLOYEE ID',
                                            bg_color='#D9D9D9',text_color='black',border_width=2,border_color='black',)
            searchentry.place(x=75,y=175)
            l=customtkinter.CTkLabel(bg,text=' SEARCH ',text_color='black',fg_color='#D9D9D9',font=('Century Gothic', 10),height=20)
            l.place(x=83,y=167)
            def placeall():
                
                nameentry.place(x=75,y=210+5)
                l1.place(x=83,y=202+5)
                identry.place(x=75,y=255+5)
                l2.place(x=83,y=247+5)
                salentry.place(x=250,y=255+5)
                l3.place(x=258,y=247+5)
                deptentry.place(x=75,y=300+5)
                cityentry.place(x=75,y=345+5)
                l5.place(x=83,y=337+5)
                phnoentry.place(x=75,y=390+5)
                l6.place(x=83,y=382+5)
                passentry.place(x=75,y=435+5)
                l7.place(x=83,y=427+5)
                l4.place(x=83,y=292+5)
                # rl.place(x=12,y=190)
                adminbut.place(x=335,y=390+5)

                eksbut.place(x=380,y=440)
                tickbut.place(x=330,y=440)
                

            def searchitem():
                nameentry.delete(0,END)
                identry.delete(0,END)
                salentry.delete(0,END)
                deptentry.delete(0,END)
                cityentry.delete(0,END)
                phnoentry.delete(0,END)
                passentry.delete(0,END)
                for i in infoemp.winfo_children():
                    i.place_forget()
                id=searchentry.get()
                con,cur=create_connection()
                strsql="select * from employee where empid='"+id+"';"
                cur.execute(strsql)
                r=cur.fetchone()
                con.close()
                if r != None:
                    placeall()
                    nameentry.insert(0,r[1])
                    identry.insert(0,r[0])
                    salentry.insert(0,r[4])
                    deptentry.insert(0,r[7])
                    cityentry.insert(0,r[6])
                    phnoentry.insert(0,r[5])
                    passentry.insert(0,r[2])
                    if r[3] == 'yes':
                        adminbut.select()
                    identry.configure(state=DISABLED)
                else:
                    notfound.place(relx=.5,y=70,anchor=CENTER)
            infoemp.place(x=65,y=230)    

            searchbut=customtkinter.CTkButton(bg,text='',font=('Century Gothic', 15,'bold'),
                                                fg_color='#ed6d31',text_color='black',image=search,width=40,
                                                height=35,hover_color='#f7a681',bg_color='#d9d9d9',command=searchitem)
            searchbut.place(x=385,y=175)

            searchentry.bind('<FocusIn>',enter)
            searchentry.bind('<FocusOut>',leave)

            dark_title_bar(r)
            r.mainloop()
        def buttons(text,x,y,img1,img2,command):
            def enter(e):
                addempbut.configure(text_color='#ed6d31',border_color='#ed6d31',image=img2)
            def leave(e):
                addempbut.configure(text_color='black',border_color='black',image=img1)
            
            addempbut=customtkinter.CTkButton(employeeframe,text=text,font=('Century Gothic', 13),
                                            fg_color='#d1d1d1',text_color='black',border_color='black',
                                            border_width=2,image=img1,command=command)
            addempbut.place(x=x,y=y)
            addempbut.bind('<Enter>',enter)
            addempbut.bind('<Leave>',leave)

        addempicon=ImageTk.PhotoImage(Image.open("addempicon.png").resize((30,30)))
        addempicon2=ImageTk.PhotoImage(Image.open("addempicon2.png").resize((30,30)))
        buttons('Add Employee',10,405,addempicon,addempicon2,addemp)

        delempicon=ImageTk.PhotoImage(Image.open("delempicon.png").resize((30,30)))
        delempicon2=ImageTk.PhotoImage(Image.open("delempicon2.png").resize((30,30)))
        buttons('Delete Employee',180,405,delempicon,delempicon2,delemp)

        modempicon=ImageTk.PhotoImage(Image.open("moditemicon.png").resize((30,30)))
        modempicon2=ImageTk.PhotoImage(Image.open("moditemicon2.png").resize((30,30)))
        buttons('Modify Employee',360,405,modempicon,modempicon2,modemp)


        dark_title_bar(root)
        # root.mainloop()
            