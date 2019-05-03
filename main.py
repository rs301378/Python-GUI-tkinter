import pymysql
import tkinter
from tkinter import messagebox

def search():
    try:
        con=pymysql.connect(user='root',password='',\
                            host='localhost',database='student_db')
        cur=con.cursor()
        sql="Select * from student where UID='%s'"%UID.get()
        cur.execute(sql)
        result=cur.fetchone()
        Name.set(result[1])
        CGPA.set(result[2])
        e1.configure(state='disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data found...')
        clear()
def clear():
    UID.set('')
    Name.set('')
    CGPA.set('')
    e1.configure(state='normal')

def add():
    try:
        con=pymysql.connect(user='root',password='',\
                            host='localhost',database='student_db')
        cur=con.cursor()
        sql="insert into student values('%s','%s','%s')"\
             %(UID.get(),Name.get(), CGPA.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record Inserted...')
    except:
        messagebox.showinfo('Error','Error in data...')
    finally:
        clear()

def update():
    try:
        con=pymysql.connect(user='root',password='',\
                            host='localhost',database='student_db')
        cur=con.cursor()
        sql="update student set Name='%s', CGPA='%s' where UID='%s'"\
             %(Name.get(),CGPA.get(), UID.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record update...')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()

def delete():
    try:
        con=pymysql.connect(user='root',password='',\
                            host='localhost',database='student_db')
        cur=con.cursor()
        sql="delete from student where UID='%s'"\
             %(UID.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Record deleted....')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()

w1=tkinter.Tk()
w1.title('USER INTERFACE')
ptitle=tkinter.Label(w1, text='User Interface',font=('Helvetica',20,'bold'),padx=2, pady=2,bg="Grey",fg="White")
ptitle.grid(row=0, column=0, columnspan=2)

UID=tkinter.StringVar()
Name=tkinter.StringVar()
CGPA=tkinter.StringVar()

l1=tkinter.Label(w1, text='Student UID',font=('arial',15,'bold'),padx=2, pady=2)
e1=tkinter.Entry(w1, textvariable=UID,font=('arial',10),width=20)
l2=tkinter.Label(w1, text='Student Name',font=('arial',15,'bold'),padx=2, pady=2)
e2=tkinter.Entry(w1, textvariable=Name,font=('arial',10),width=20)
l3=tkinter.Label(w1, text='CGPA',font=('arial',15,'bold'),padx=2, pady=2)
e3=tkinter.Entry(w1, textvariable=CGPA,font=('arial',10),width=20)

bu=tkinter.Button(w1, text='Search', command=search,font=('arial',10),height=1, width=15, bd=4)
but=tkinter.Button(w1, text='Add', command=add,font=('arial',10),height=1, width=15, bd=4)
butt=tkinter.Button(w1, text='Update', command=update,font=('arial',10),height=1, width=15, bd=4)
butto=tkinter.Button(w1, text='Delete', command=delete,font=('arial',10),height=1, width=15, bd=4)
button=tkinter.Button(w1, text='Clear', command=clear,font=('arial',10),height=1, width=5, bd=4)
    
l1.grid(row=1, column=0)
e1.grid(row=1, column=1)
bu.grid(row=5, column=1)

l2.grid(row=2, column=0)
e2.grid(row=2, column=1)
l3.grid(row=3, column=0)
e3.grid(row=3, column=1)
but.grid(row=4, column=0)
butt.grid(row=4, column=1)
butto.grid(row=5, column=0)
button.grid(row=6, column=0)
w1.mainloop()




























