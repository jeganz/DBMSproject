# Import module
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct
import mysql.connector
import adminpage
import empframe

#connection to mysql
def create_connection():
    #Used to connect Python with MySQL
    con = mysql.connector.connect(\
          host = "localhost",\
          user = "root",
          password = "alexsqlMY_10")
    cur = con.cursor()
    strSQL = "show databases"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("mkmartdb",) in r:
        pass
    else:  #Till here
        strSQL = "create database mkmartdb;"
        cur.execute(strSQL)
    strSQL = "select database();"
    cur.execute(strSQL)
    r = cur.fetchall()
    if r in ("mkmartdb",):
        pass
    else:
        strSQL = "use mkmartdb;"
        cur.execute(strSQL)
    strSQL = "show tables;"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("employee",) in r:
        pass
    else:
        strSQL = "create table employee("\
                "empid int(5) primary key,name varchar(20),pass varchar(20),"\
                "admin varchar(10) default 'no',salary float(20),"\
                "phone_no varchar(50),city varchar(20),department varchar(20));"
        cur.execute(strSQL)
        strSQL="insert into employee values(007,null,'000','yes',null,null,null,null);"
        cur.execute(strSQL)
        con.commit()
    if ("item",) in r:
        pass
    else:
        strSQL = "create table item("\
                "barcode varchar(20) primary key,name varchar(20),"\
                "category varchar(20),price float(20),"\
                "stock int);"
        cur.execute(strSQL)
    return con, cur

#con,cur=create_connection()
customtkinter.set_appearance_mode("light")

def CustomerChange():
    Customer.place(x = 525, y = 25)
    Main.place_forget()

def EmpChange():
    Employee.place(x = 525, y = 25)
    Main.place_forget()

def AdminChange():
    Admin.place(x = 525, y = 25)
    Main.place_forget()

def MainChange():
    clearTF()
    Main.place(x = 525, y = 25)
    Customer.place_forget()
    Employee.place_forget()
    Admin.place_forget()

def AdminLogin():
    InvPass.place_forget()
    InvUser.place_forget()
    NotAdmin.place_forget()
    L = [entryAdmin.get(), entryPassA.get()]
    con,cur=create_connection()
    cur.execute("select * from employee where empid=%s;",(int(L[0]),))
    r=cur.fetchone()
    if r is None:
        entryAdmin.configure(border_color='red')
        LoginAdmin.focus_set()
        entryAdmin.bind('<FocusIn>',lambda e:entryAdmin.configure(border_color='gray'))
        InvUser.place(relx = 0.5, y = 300,anchor=CENTER)
    elif r[2] == L[1] and r[3]=="yes":
       MainChange()
       adminpage.adminpage(root,L[0],create_connection)
    elif r[2] == L[1] and r[3]=="no":
       NotAdmin.place(relx = 0.5, y = 300,anchor=CENTER)
    else:
        entryPassA.configure(border_color='red')
        LoginAdmin.focus_set()
        entryPassA.bind('<FocusIn>',lambda e:entryPassA.configure(border_color='gray'))
        InvPass.place(relx = 0.5, y = 300,anchor=CENTER)
    con.close()


def EmployeeLogin():
    InvUserE.place_forget()
    InvPassE.place_forget()
    L = [entryEmp.get(), entryPasse.get()]
    con,cur=create_connection()
    cur.execute("select * from employee where empid=%s;",(int(L[0]),))
    r=cur.fetchone()
    if r is None:
        entryEmp.configure(border_color='red')
        LoginEmp.focus_set()
        entryEmp.bind('<FocusIn>',lambda e:entryEmp.configure(border_color='gray'))
        InvUserE.place(relx = 0.5, y = 300,anchor=CENTER)
    elif r[2] == L[1]:
       MainChange()
       empframe.empframe(root,create_connection)
    else:
        entryPasse.configure(border_color='red')
        LoginEmp.focus_set()
        entryPasse.bind('<FocusIn>',lambda e:entryPasse.configure(border_color='gray'))
        InvPassE.place(relx = 0.5, y = 300,anchor=CENTER)
    con.close()  

def clearTF():
    entryAdmin.delete(0,END)
    entryPassA.delete(0,END)
    entryEmp.delete(0,END)
    entryPasse.delete(0,END)
    InvUserE.place_forget()
    InvPassE.place_forget()
    InvPass.place_forget()
    InvUser.place_forget()
    NotAdmin.place_forget()

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
root = Tk()
con,cor=create_connection()
con.close()

# Adjust size
root.geometry("1000x500+100+100")
root.resizable(False, False)
root.title("MK Mart")

BgLogin = customtkinter.CTkFrame(root, height= 510, width=1020, fg_color="#000000")
Main = customtkinter.CTkFrame(root, corner_radius= 20, height= 450, width=425, bg_color="#000000")
Customer = customtkinter.CTkFrame(root, corner_radius= 20, height= 450, width=425, bg_color="#000000")
Employee = customtkinter.CTkFrame(root, corner_radius= 20, height= 450, width=425, bg_color="#000000")
Admin = customtkinter.CTkFrame(root, corner_radius= 20, height= 450, width=425, bg_color="#000000")

BgLogin.place(x = -10, y = -10)
Main.place(x = 525, y = 25)


# Create Frame Main

# Add image file
bg = ImageTk.PhotoImage(Image.open("MKMart2.png"))
back = ImageTk.PhotoImage(Image.open("Back.png").resize((30,30)))


canvas = Canvas( BgLogin, width = 1020,
				height = 520)
canvas.place(x = -5, y = -5)
canvas.configure(background="#000000", bg="#000000")

canvas.create_image( 0, 0, image = bg, anchor = "nw")



# Add Text
label = customtkinter.CTkLabel(master=Main, text="SELECT USER", width=250, height=50,
                               font=("Arial", 25, "bold"), corner_radius=8)
    
# Create Buttons
button1 = customtkinter.CTkButton(master=Main, text_color="#000000", fg_color="lightgray",
                                  height=32.5, width=150,
                                  font=("Bahnschrift SemiBold", 18), text="Customer", command=CustomerChange)
button2 = customtkinter.CTkButton(master=Main, text_color="#000000", fg_color="lightgray",
                                  height=32.5, width=150, 
                                  font=("Bahnschrift SemiBold", 18), text="Employee", command=EmpChange)
button3 = customtkinter.CTkButton(master=Main, text_color="#000000", fg_color="lightgray", 
                                  height=32.5, width=150,
                                  font=("Bahnschrift SemiBold", 18), text="Admin", command=AdminChange)


button1.place(x = 137.5, y = 150)
button2.place(x = 137.5, y = 250)
button3.place(x = 137.5, y = 350)
label.place(x = 90, y = 50)



# # Create Frame Customer

# #Login label
# label2 = customtkinter.CTkLabel(master=Customer, text="Log into your account", width=350, height=50,
#                                 font=("Century Gothic", 25, "bold"), corner_radius=8)
# label2.place(relx = 0.5, y = 50, anchor=CENTER)

# #Customer Username and textfield
# CusUser = customtkinter.CTkLabel(master=Customer, text="USERNAME:", width=120, height=50, 
#                                 font=("Century Gothic", 16), corner_radius=8)
# CusUser.place(x = 35, y = 125)
# entryUser = customtkinter.CTkEntry(master=Customer,
#                                width=200, height=25, corner_radius=10)
# entryUser.place(x = 170, y = 135)

# #Customer Password and textfield
# CusPass = customtkinter.CTkLabel(master=Customer, text="PASSWORD:", width=120, height=50, 
#                                 font=("Century Gothic", 16), corner_radius=8)
# CusPass.place(x = 35, y = 200)
# entryPass = customtkinter.CTkEntry(master=Customer,
#                                width=200, height=25, corner_radius=10)
# entryPass.place(x = 170, y = 210)

# #login Button
# Login = customtkinter.CTkButton(master=Customer, text="LOGIN")
# Login.place(x = 150, y = 275)

# # Register
# RegisterLabel = customtkinter.CTkLabel(master=Customer, text="Not a User?", width=165, height=50,
#                                 corner_radius=8)
# RegisterLabel.place(x = 125, y = 350)
# Register = customtkinter.CTkButton(master=Customer,
#                                 fg_color="lightblue", text="Register")
# Register.place(x = 150, y = 400)

# #Back button
# Back = customtkinter.CTkButton(master=Customer, fg_color="transparent", text="", image=back, corner_radius =20,
#                                width=30,command=MainChange)
# Back.place(x = 10, y = 10)




# Create Frame Employee

#Login label
label3 = customtkinter.CTkLabel(master=Employee, text="Log into your account", width=350, height=50,
                                font=("Century Gothic", 25, "bold"), corner_radius=8)
label3.place(relx = 0.5, rely = 0.2, anchor=CENTER)

#Customer Username and textfield
EmpUser = customtkinter.CTkLabel(master=Employee, text="EMPLOYEE ID:", width=120, height=50,
                                font=("Century Gothic", 16), corner_radius=8)
EmpUser.place(x = 35, y = 150)
entryEmp = customtkinter.CTkEntry(master=Employee,
                               width=200, height=25, corner_radius=10)
entryEmp.place(x = 170, y = 165)

#Customer Password and textfield
EmpPass = customtkinter.CTkLabel(master=Employee, text="PASSWORD:", width=120, height=50,
                                font=("Century Gothic", 16), corner_radius=8)
EmpPass.place(x = 35, y = 225)
entryPasse = customtkinter.CTkEntry(master=Employee, show = "*",
                               width=200, height=25, corner_radius=10)
entryPasse.place(x = 170, y = 240)

#login Button
LoginEmp = customtkinter.CTkButton(master=Employee, text="LOGIN", fg_color="#ed6d31", command=EmployeeLogin,
                                     font=("Century Gothic", 16, "bold"))
LoginEmp.place(relx = 0.5, y = 350, anchor=CENTER)

#Back button
Back = customtkinter.CTkButton(master=Employee, fg_color="transparent", text="", image=back,
                                corner_radius =20,width=30,command=MainChange)
Back.place(x = 10, y = 10)

warn = ImageTk.PhotoImage(Image.open("warningicon.png").resize((25,25)))
InvPassE = customtkinter.CTkLabel(master=Employee, text=" INVALID PASSWORD", width=150,image=warn,compound='left',
                                  height=30, font=("Century Gothic", 16, "bold"), corner_radius=8,
                                  text_color="red", fg_color="transparent", bg_color="transparent")
InvUserE = customtkinter.CTkLabel(master=Employee, text=" USER NOT FOUND", width=150,image=warn,compound='left',
                                  height=30, font=("Century Gothic", 16,'bold'), corner_radius=8,
                                  text_color="red", fg_color="transparent", bg_color="transparent")



# Create Frame Admin

#Login label
label4 = customtkinter.CTkLabel(master=Admin, text="Log into your account", width=350, height=50,
                                font=("Century Gothic", 25, "bold"), corner_radius=8)
label4.place(relx = 0.5, rely = 0.2, anchor=CENTER)
#Customer Username and textfield
AdminUser = customtkinter.CTkLabel(master=Admin, text="ADMIN ID:", width=150, height=50,
                                font=("Century Gothic", 16), corner_radius=8)
AdminUser.place(x = 35, y = 150)
entryAdmin = customtkinter.CTkEntry(master=Admin, width=200,
                                    height=25, corner_radius=10)
entryAdmin.place(x = 170, y = 165)

#Customer Password and textfield
AdminPass = customtkinter.CTkLabel(master=Admin, text="PASSWORD:", width=150,
                                    height=50, font=("Century Gothic", 16), corner_radius=8)
AdminPass.place(x = 35, y = 225)
entryPassA = customtkinter.CTkEntry(master=Admin, width=200, height=25, corner_radius=10, show = "*")
entryPassA.place(x = 170, y = 240)

#login Button
LoginAdmin = customtkinter.CTkButton(master=Admin, text="LOGIN", fg_color="#ed6d31",
                                     font=("Century Gothic", 16, "bold"), command=AdminLogin)
LoginAdmin.place(relx = 0.5, y = 350, anchor=CENTER)

#Back button
Back = customtkinter.CTkButton(master=Admin, fg_color="transparent", text="", image=back,
                                corner_radius =20, width=30,command=MainChange)
Back.place(x = 10, y = 10)

InvPass = customtkinter.CTkLabel(master=Admin, text=" INVALID PASSWORD", width=150,image=warn,compound='left', 
                                height=30, font=("Century Gothic", 16, "bold"), corner_radius=8,
                                text_color="red", fg_color="transparent", bg_color="transparent")
InvUser = customtkinter.CTkLabel(master=Admin, text=" USER NOT FOUND", width=150,image=warn,compound='left',
                                height=30, font=("Century Gothic", 16, "bold"), corner_radius=8,
                                text_color="red", fg_color="transparent", bg_color="transparent")
NotAdmin = customtkinter.CTkLabel(master=Admin, text=" NOT AN ADMIN ID", width=150,image=warn,compound='left',
                                height=30, font=("Century Gothic", 16, "bold"), corner_radius=8,
                                text_color="red", fg_color="transparent", bg_color="transparent")




# Execute tkinter
dark_title_bar(root)
root.mainloop()