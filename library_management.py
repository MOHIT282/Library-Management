from tkinter import *
import tkinter.messagebox as tm
t=Tk()
t.config(bg='orange')
a=IntVar()
t.geometry('400x400+300+150')
t.title('Member Login')

def addbook():
    k=Toplevel(t)
    k.title("Add a Book")
    k.geometry("400x400+400+200")
    k.config(bg='orange')

    def res():
        b_name.set("")
        b_id.set("")

    b_name=StringVar(k)
    b_id=StringVar(k)

    lb0=Label(k,text="Add A Book",fg='yellow',bg='blue',font=('arial',16,'bold','underline'))
    lb0.place(x=150,y=10)
    lb1=Label(k,text="Book Name", fg='blue',width=9,anchor='w')
    lb1.place(x=50,y=80)
    lb1 = Label(k, text="Book Id", fg='blue', width=9, anchor='w')
    lb1.place(x=50, y=120)

    tb1=Entry(k,textvariable=b_name,fg='blue')
    tb1.place(x=150,y=80)
    tb2=Entry(k, textvariable=b_id,fg='blue')
    tb2.place(x=150, y=120)

    bt1=Button(k,text="Add",fg='blue',bg='red',activebackground='orange',font=30)
    bt1.place(x=150,y=160)
    bt2=Button(k,text="Cancel",fg='blue',bg='red',activebackground='orange',font=30,command=res)
    bt2.place(x=210, y=162)

    k.mainloop()

def openpage():
    import tkinter.messagebox
    x = Toplevel(t)
    x.config(bg='orange')
    a = IntVar()
    x.geometry('400x400+350+150')
    x.title('Library Management System')

    def mship():
        n = Toplevel(t)
        n.config(bg='orange')
        n.title('Membership Form')
        n.geometry("470x400+350+200")

        f1 = Frame(n, bd=2, bg='black')
        f1.place(x=270, y=50)
        text1 = Text(f1, bd=2, bg='pink', font=('arial', 10, 'italic'), height=17, width=25)
        text1.pack()

        def submit():
            text1.delete("1.0", END)
            text1.insert(END, "\tAccount Details\n\n")
            text1.insert(END, "Name :\t" + name.get() + "\n\n")
            text1.insert(END, "Course :\t" + course.get() + "\n\n")
            text1.insert(END, "Branch :\t" + e.get() + "\n\n")
            text1.insert(END, "Year :\t" + year.get() + "\n\n")
            text1.insert(END, "Gender :\t" + val.get() + "\n\n")
            text1.insert(END, "Roll No :\t" + rollno.get() + "\n\n")
            text1.insert(END, "Email-Id :\t" + email.get() + "\n\n")
            text1.insert(END, "Col Name :\t" + col.get() + "\n\n")

        def reset():
            name.set("")
            course.set("")
            e.set(b[0])
            year.set("")
            rollno.set("")
            email.set("")
            col.set("")
            val.set(0)

        e = StringVar(n)
        b = ['--Select Branch--', 'IT', 'CS', 'EC', 'EN', 'ME', 'CE']
        e.set(b[0])

        name = StringVar(n)
        course = StringVar(n)
        year = StringVar(n)
        rollno = StringVar(n)
        email = StringVar(n)
        col = StringVar(n)
        val = StringVar(n)

        la = Label(n, text='Membership Form', bg='blue', fg='Yellow', font=('arial', 16, 'bold', 'underline'))
        la.place(x=126, y=5)
        l0 = Label(n, text='Name', fg='blue', font=10, width=8, anchor='w')
        l0.place(x=25, y=45)
        l1 = Label(n, text='Course', fg='blue', font=10, width=8, anchor='w')
        l1.place(x=25, y=70)
        l2 = Label(n, text='Branch', fg='blue', font=10, width=8, anchor='w')
        l2.place(x=25, y=95)
        l3 = Label(n, text='Year', fg='blue', font=10, width=8, anchor='w')
        l3.place(x=25, y=120)
        l4 = Label(n, text='Gender', fg='blue', font=10, width=8, anchor='w')
        l4.place(x=25, y=145)
        l5 = Label(n, text='Roll No', fg='blue', font=10, width=8, anchor='w')
        l5.place(x=25, y=170)
        l6 = Label(n, text='Email-ID', fg='blue', font=10, width=8, anchor='w')
        l6.place(x=25, y=195)
        l7 = Label(n, text='Col. Name', fg='blue', font=10, width=8, anchor='w')
        l7.place(x=25, y=220)

        r1 = Radiobutton(n, text='Male', activeforeground='red', value='Male',
                         variable=val, fg='blue', anchor='w')
        r1.place(x=130, y=142)
        r2 = Radiobutton(n, text='Female', activeforeground='red', value='Female', variable=val, fg='blue', anchor='w')
        r2.place(x=187, y=142)

        tb1 = Entry(n, textvariable=name, fg='blue')
        tb1.place(x=130, y=45)
        tb2 = Entry(n, textvariable=course, fg='blue')
        tb2.place(x=130, y=70)
        tb3 = OptionMenu(n, e, *b)
        tb3.place(x=130, y=93, height=22, width=125)
        tb4 = Entry(n, textvariable=year, fg='blue')
        tb4.place(x=130, y=120)
        tb5 = Entry(n, textvariable=rollno, fg='blue')
        tb5.place(x=130, y=170)
        tb6 = Entry(n, textvariable=email, fg='blue')
        tb6.place(x=130, y=195)
        tb7 = Entry(n, textvariable=col, fg='blue')
        tb7.place(x=130, y=220)

        btn1 = Button(n, text='Submit', fg='blue', bg='red', activebackground='orange', font=30, command=submit)
        btn1.place(x=130, y=265)
        btn2 = Button(n, text='Cancel', fg='blue', bg='red', activebackground='orange', font=30, command=reset)
        btn2.place(x=200, y=265)

        # n.resizable(False, False)

        n.mainloop()

    def issue():
        z = Toplevel(t)
        z.config(bg='orange')
        a = IntVar(z)
        z.geometry('400x400+350+200')
        z.title('Issue A Book')

        def re():
            book.set("")

        l1 = Label(z, text='Issue/Return A Book', fg='yellow', bg='blue', font=('arial', 16, 'bold', 'underline'))
        l1.place(x=130, y=10)
        l2 = Label(z, text='Book ID', fg='blue', width=10, font=24, anchor='w')
        l2.place(x=25, y=70)
        l3 = Label(z, text='Action', fg='blue', width=10, font=24, anchor='w')
        l3.place(x=25, y=120)

        book = StringVar(z)

        tb1 = Entry(z, textvariable=book, fg='blue', bg='pink', width=33)
        tb1.place(x=140, y=70)

        r1 = Radiobutton(z, text='Issue', fg='blue', variable=a, value=1)
        r1.place(x=140, y=120)
        r2 = Radiobutton(z, text='Reissue', fg='blue', variable=a, value=2)
        r2.place(x=204, y=120)
        r3 = Radiobutton(z, text='Return', fg='blue', variable=a, value=3)
        r3.place(x=280, y=120)

        bt1 = Button(z, text='Submit', fg='blue', bg='red', font=30, activebackground='orange')
        bt1.place(x=150, y=180)
        bt2 = Button(z, text='Cancel', fg='blue', bg='red', font=30, activebackground='orange', command=re)
        bt2.place(x=250, y=180)

        z.resizable(False, False)
        z.mainloop()

    def view():
        k = Toplevel(t)
        k.title('Book Inquiry')
        k.geometry("400x400+350+200")
        k.config(bg='orange')

        t1 = Label(k, text='Book Inquiry', bg='blue', font=('arial', 24, 'bold', 'underline'), fg='Yellow')
        t1.place(x=100, y=10)
        t2 = Label(k, text='Book Name', fg='blue', font=20, width=9, anchor='w')
        t2.place(x=25, y=80)
        t3 = Label(k, text='Book Id', fg='blue', font=20, width=9, anchor='w')
        t3.place(x=25, y=110)
        t4 = Label(k, text='Status', fg='blue', font=20, width=9, anchor='w')
        t4.place(x=25, y=140)
        t5 = Label(k, text='Return', fg='blue', font=20, width=9, anchor='w')
        t5.place(x=25, y=170)

        def res():
            name.set("")
            ide.set("")
            status.set("")
            ret.set("")

        name = StringVar(k)
        ide = StringVar(k)
        status = StringVar(k)
        ret = StringVar(k)

        tb1 = Entry(k, textvariable=name, fg='blue')
        tb1.place(x=150, y=80)
        tb2 = Entry(k, textvariable=ide, fg='blue')
        tb2.place(x=150, y=110)
        tb3 = Entry(k, textvariable=status, fg='blue')
        tb3.place(x=150, y=140)
        tb4 = Entry(k, textvariable=ret, fg='blue')
        tb4.place(x=150, y=170)

        btn1 = Button(k, text='Submit', fg='blue', bg='red', activebackground='green', font=30)
        btn1.place(x=140, y=220)
        btn2 = Button(k, text='Cancel', fg='blue', bg='red', activebackground='green', font=30, command=res)
        btn2.place(x=210, y=220)

        t.resizable(False, False)

        t.mainloop()

    def exit0():
        exit = tkinter.messagebox.askokcancel("info", 'Do you want to Exit ?')
        if exit > 0:
            x.destroy()


    la1 = Label(x,text='LIBRARY MANAGEMENT SYSTEM', fg='yellow', bg='blue', font=('arial', 16, 'bold', 'underline'))
    la1.place(x=30, y=20)

    but1 = Button(x,text='Membership Form', fg='blue', bg='red', width=15, activebackground='green', font=30,
                 command=mship)
    but1.place(x=140, y=100)
    but2 = Button(x,text='Add a Book',fg='blue',bg='red',width=15,activebackground='green',font=30,command=addbook)
    but2.place(x=140,y=150)
    but3 = Button(x,text='Issue/Return Book', fg='blue', bg='red', width=15, activebackground='green', font=30,
                 command=issue)
    but3.place(x=140, y=200)
    but4 = Button(x,text='View Book Status', fg='blue', bg='red', width=15, activebackground='green', font=30,
                 command=view)
    but4.place(x=140, y=250)
    but5 = Button(x,text='Exit', fg='blue', bg='red', width=15, activebackground='green', font=30, command=exit0)
    but5.place(x=140, y=300)

    x.resizable(False, False)

    x.mainloop()

def reset():
    reg.set("")
    pas.set("")

def sho():
    p=pas.get()
    print(p)

def login():
    username=tb1.get()
    password=tb2.get()

    if username=='root' and password=='root': 
        tm.showinfo("Login Info", "Welcome ")
        openpage()
    elif username=='root1' and password=='root1':
        tm.showinfo("Login Info", "Welcome ")
        openpage()
    else:
        tm.showinfo("Login Error", "Incorrect Username/Password")


l1=Label(text='Member Login',fg='yellow',width=15,bg='blue',font=('arial',16,'bold','underline'))
l1.place(x=140,y=10)
l2=Label(text='User Id',fg='blue',width=10,font=24,anchor='w')
l2.place(x=25,y=70)
l3=Label(text='Password',fg='blue',width=10,font=24,anchor='w')
l3.place(x=25,y=130)

reg=StringVar()
pas=StringVar()

tb1=Entry(textvariable=reg,fg='blue',bd=3,bg='pink',width=30)
tb1.place(x=150,y=70)
tb2=Entry(textvariable=pas,show='*',fg='blue',bd=3,bg='pink',width=30)
tb2.place(x=150,y=130)

bt1=Button(text='Login',fg='blue',bg='red',font=30,activebackground='orange',command=login)
bt1.place(x=150,y=200)
bt2=Button(text='Cancel',fg='blue',bg='red',font=30,activebackground='orange',command=reset)
bt2.place(x=250,y=200)
bt3=Button(text='Show',fg='blue',bg='orange',activebackground='orange',command=sho)
bt3.place(x=338,y=127)

t.resizable(False,False)

t.mainloop()
