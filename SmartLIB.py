from tkinter import *
import os
import time
import mysql.connector as mycon
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as mt
import tkcalendar as tc
import numpy as np
import datetime


def bb():
    def quit():
        root.destroy()

    def calen():
        global cal, root1
        root1 = Toplevel()
        root1.geometry("300x300+300+200")
        root1.title("CALENDAR")
        cal = tc.Calendar(root1, date_pattern="y-mm-dd", textvariable=StringVar(), year=2021, month=2, day=3)
        cal.pack(pady=30, fill="both", expand=TRUE)
        bttno = Button(root1, text="OK", command=upg)
        bttno.pack(pady=10, ipadx=40, ipady=10)

    def upg():
        if str(cal.get_date()) == "":
            messagebox.showinfo("!!!", "SELECT THE DATE")
        else:
            bttnc.configure(text=str(cal.get_date()))
            root1.destroy()

    def calen1():
        global cal1, root2
        root2 = Toplevel()
        root2.geometry("300x300+300+200")
        root2.title("CALENDAR")
        cal1 = tc.Calendar(root2, date_pattern="y-mm-dd", textvariable=StringVar(), year=2021, month=2, day=3)
        cal1.pack(pady=30, fill="both", expand=TRUE)
        bttno = Button(root2, text="OK", command=upg1)
        bttno.pack(pady=10, ipadx=40, ipady=10)

    def upg1():
        if str(cal1.get_date()) == "":
            messagebox.showinfo("!!!", "SELECT THE DATE")
        else:
            bttnc1.configure(text=str(cal1.get_date()))
            root2.destroy()

    def book(event=NONE):
        if str.isnumeric(idd.get()) and str.isnumeric(aad.get()) and str.isnumeric(eml.get()):
            a1 = int(idd.get())
            b6 = str.upper(str(nm.get()))
            c = int(aad.get())
            d = str.upper(str(phn.get()))
            e = str.upper(str(ad.get()))
            f1 = int(eml.get())
            g = str.upper(str(ln.get()))
            h = str(cal.get_date())
            i = str(cal1.get_date())
            k = str.upper(str(opp.get()))
            if k == "   N O  ":
                k = "NO"
            else:
                k = "YES"
            import mysql.connector as mycon
            mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
            mycursor = mydb.cursor()
            mycursor.execute("select * from book where book_no=" + str(a1) + "")
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                mycursor.execute(
                    "insert into book values(" + str(a1) + ",'" + b6 + "'," + str(
                        c) + ",'" + d + "','" + e + "'," + str(
                        f1) + ",'" + g + "','" + h + "','" + i + "','" + k + "')")
                messagebox.showinfo(":-)....:-)", "Data has been saved!!!")
                idd.delete(0, END)
                nm.delete(0, END)
                aad.delete(0, END)
                phn.delete(0, END)
                ad.delete(0, END)
                eml.delete(0, END)
                ln.delete(0, END)
            else:
                messagebox.showinfo("!!!!!!", "BOOK NUMBER ALREADY PRESENT")
                return
            mydb.commit()
            mycursor.close()
            mydb.close()

        else:
            messagebox.showinfo("!!!!!", "Error with your entry")

    root = Toplevel()
    root.title("Book")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    my_img = Image.open("C:\library_management_prj\images\_bb.jpg")
    new1 = my_img.resize((1400, 800), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new1)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)
    imm1 = Image.open("C:\library_management_prj\images\_books.png")
    new1 = imm1.resize((100, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(new1)
    Label(root, image=img1, bg="#D33834").place(x=80, y=40)
    Label(root, text="Enter the Book NO.", fg="#fff", bg="#D33834", font=("Helvetica", 11, "bold")).pack(
        ipadx=5, pady=5)
    idd = Entry(root, textvariable=IntVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    idd.delete(0,END)
    idd.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the Book name", fg="#fff", bg="#D33834", font=("Helvetica", 11, "bold")).pack(ipadx=5,
                                                                                                          pady=2)
    nm = Entry(root, textvariable=StringVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    nm.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the Price of the book", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    aad = Entry(root, textvariable=IntVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    aad.delete(0,END)
    aad.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the category of the book", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    phn = Entry(root, textvariable=StringVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    phn.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the author name of the book", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    ad = Entry(root, textvariable=StringVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    ad.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the number of pages of the book", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    eml = Entry(root, textvariable=IntVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    eml.delete(0,END)
    eml.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Enter the language of the book", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    ln = Entry(root, textvariable=StringVar(), fg="#fff", bg="#FB8770", font=("Helvetica", 11))
    ln.pack(ipadx=10, pady=2, ipady=2)
    Label(root, text="Select the date of purchase of the book in YYYY-MM-DD form", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    bttnc = Button(root, text="CALENDAR", fg="#fff", font=("Helvetica", 11, "bold"), bg="#FB8770", command=calen)
    bttnc.pack(ipadx=15, ipady=3)
    Label(root, text="Select the Print Date of the book in YYYY-MM-DD form", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    bttnc1 = Button(root, text="CALENDAR", fg="#fff", font=("Helvetica", 11, "bold"), bg="#FB8770", command=calen1)
    bttnc1.pack(ipadx=15, ipady=3)
    Label(root, text="Select whether the student had issued or not", fg="#fff", bg="#D33834",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    con = {"   Y E S   ", "   N O  "}
    opp = StringVar()
    opp.set("SELECT")
    p = OptionMenu(root, opp, *con)
    p.config(bg="#FB8770", fg="#fff", font=("Helvetica", 9, "bold"))
    p.pack(ipadx=10, pady=3)
    bttn = Button(root, text="Press to load the the above data", command=book, fg="#fff", bg="#D33834",
                  font=("Helvetica", 11, "bold"))
    bttn.pack(ipadx=10, pady=2)
    root.bind('<Return>', book)
    Button(root, text="Exit The Program", command=quit, fg="#fff", bg="#D33834",
           font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    root.mainloop()


def ss():
    def calen():
        global cal, root1
        root1 = Toplevel()
        root1.geometry("300x300+300+200")
        root1.title("CALENDAR")

        cal = tc.Calendar(root1, date_pattern="y-mm-dd", textvariable=StringVar(), year=2021, month=2, date=21)
        cal.pack(pady=30, fill="both", expand=TRUE)
        bttno = Button(root1, text="OK", command=upg)
        bttno.pack(pady=10, ipadx=40, ipady=10)

    def quit():
        root.destroy()

    def upg():
        if str(cal.get_date()) == "":
            messagebox.showinfo("!!!", "SELECT THE DATE")
        else:
            bttnc.configure(text=str(cal.get_date()))
            root1.destroy()

    def dis():
        if str(opp.get()) == "YES":
            dt.configure(state=NORMAL)
            bttnc.configure(state=NORMAL)
        if str(opp.get()) == "NO":
            dt.configure(state=DISABLED)
            bttnc.configure(state=DISABLED)
        bttn.configure(state=NORMAL)

    def stud(event=None):
        if str.isnumeric(idd.get()) and str.isnumeric(phn.get()):
            a1 = int(idd.get())
            b3 = str.upper(str(nm.get()))
            c = str.upper(str(aad.get()))
            d = int(phn.get())
            e = str.upper(str(ad.get()))
            f1 = str.upper(str(opp.get()))
            g = str.upper(str(ln.get()))
            mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
            mycursor = mydb.cursor()
            mycursor.execute("select * from student where admno=" + str(1) + "")
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                if f1 == "NO":
                    mycursor.execute(
                        "insert into student(ADMNO,Name,Class_Sec,Roll_No,Address,Book_Issued,Phone,Book_No) values(" +

                        str(
                            a1) + ",'" + b3 + "','" + c + "'," + str(d) + ",'" + e + "','" + f1 + "','" + g + "',0)")
                else:
                    f1 = "YES"
                    h = str.upper(str(dt.get()))
                    i = str(cal.get_date())
                    mycursor.execute("insert into student values(" + str(a1) + ",'" + b3 + "','" + c + "'," + str(
                        d) + ",'" + e + "','" + f1 + "','" + g + "','" + h + "','" + i + "')")
                messagebox.showinfo(":-)....:-)", "Data has been saved!!!")
                idd.delete(0, END)
                nm.delete(0, END)
                aad.delete(0, END)
                phn.delete(0, END)
                ad.delete(0, END)
                dt.delete(0, END)
                ln.delete(0, END)
                dt.configure(state=DISABLED)
                bttnc.configure(state=DISABLED)
                bttn.configure(state=DISABLED)
            else:
                messagebox.showinfo("!!!!!!", "ADMISSION NUMBER ALREADY PRESENT")
                return
            mydb.commit()
            mycursor.close()
            mydb.close()
        else:
            messagebox.showinfo("!!!!!", "Error with your entry")

    root = Toplevel()
    root.title("Student")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\ss.jpg")
    new = l.resize((1400, 800), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)
    imm = Image.open("C:\library_management_prj\images\studentb.png")
    new = imm.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(new)
    Label(root, image=img, bg="#F9E7CF").place(x=80, y=40)
    imm1 = Image.open("C:\library_management_prj\images\studentg.png")
    new1 = imm1.resize((100, 85), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(new1)
    Label(root, image=img1, bg="#F9E7CF").place(x=180, y=40)
    Label(root, text="Enter the admission number", fg="black", font=("Helvetica", 11, "bold"), bg="#FDC453").pack(
        padx=30, pady=5)
    idd = Entry(root, textvariable=IntVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    idd.delete(0,END)
    idd.pack(ipadx=15, ipady=3)
    Label(root, text="Enter the Name", fg="black", font=("Helvetica", 11, "bold"), bg="#FDC453").pack(padx=30,
                                                                                                      pady=5)
    nm = Entry(root, textvariable=StringVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    nm.pack(ipadx=15, ipady=3)
    Label(root, text="Enter the Class_sec [class-section]", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDC453").pack(padx=30, pady=5)
    aad = Entry(root, textvariable=StringVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    aad.pack(ipadx=15, ipady=3)
    Label(root, text="Enter the roll number of the student", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDC453").pack(padx=30, pady=5)
    phn = Entry(root, textvariable=IntVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    phn.delete(0, END)
    phn.pack(ipadx=15, ipady=3)
    Label(root, text="Enter the Address of the student", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDC453").pack(padx=30, pady=5)
    ad = Entry(root, textvariable=StringVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    ad.pack(ipadx=15, ipady=3)
    Label(root, text="Enter the phone number of the student", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDC453").pack(padx=30, pady=5)
    ln = Entry(root, textvariable=StringVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    ln.pack(ipadx=15, ipady=3)
    Label(root, text="Select whether the student had issued or not", fg="black",
          font=("Helvetica", 11, "bold"), bg="#FDC453").pack(padx=30, pady=5)
    opp = StringVar()
    ch = Radiobutton(root, text="YES", variable=opp, value="YES", command=dis)
    ch.configure(fg="black", font=("Helvetica", 10, "italic"), bg="#FCD19C")
    ch.pack(pady=5)
    ch.deselect()
    ch1 = Radiobutton(root, text="NO", variable=opp, value="NO", command=dis)
    ch1.configure(fg="black", font=("Helvetica", 10, "italic"), bg="#FCD19C")
    ch1.pack(pady=5)
    ch1.deselect()
    Label(root, text="Enter the book number if issued else null", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDC453").pack(padx=30, pady=5)
    dt = Entry(root, textvariable=StringVar(), fg="black", bg="#FCD19C", font=("Helvetica", 11, "bold"))
    dt.configure(state=DISABLED)
    dt.pack(ipadx=15, ipady=3)
    Label(root, text="Enter book issued on if book issued else null", fg="black",
          font=("Helvetica", 11, "bold"), bg="#FDC453").pack(padx=30, pady=5)
    bttnc = Button(root, text="CALENDAR", fg="black", font=("Helvetica", 11, "bold"), bg="#FDC453", command=calen)
    bttnc.configure(state=DISABLED)
    bttnc.pack(ipadx=15, ipady=3)
    bttn = Button(root, text="Press to load the the above data", command=stud, font=("Helvetica", 11, "bold"),
                  fg="black", bg="#FDC453")
    bttn.configure(state=DISABLED)
    root.bind('<Return>', stud)
    bttn.pack(ipadx=10, pady=5)
    Button(root, text="Exit The Program", command=quit, font=("Helvetica", 11, "bold"), fg="black",
           bg="#FDC453").pack(ipadx=30, pady=0)
    root.mainloop()


def librar():
    def quit():
        root.destroy()

    def librarian(event=None):

        if str.isnumeric(idd.get()) and str.isnumeric(aad.get()) and str.isnumeric(phn.get()):
            a = int(idd.get())
            b = str.upper(str(nm.get()))
            c = int(aad.get())
            d = int(phn.get())
            e = str.upper(str(ad.get()))
            f = str(eml.get())
            g = str(pw1.get())
            h = str(sec1.get())
            mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
            mycursor = mydb.cursor()
            mycursor.execute("select * from librarian where id =" + str(a) + "")
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                mycursor.execute("insert into librarian values(" + str(a) + ",'" + b + "'," + str(c) + "," + str(d) +
                                 ",'" + e + "','" + f + "','" + g + "','" + h + "')")
                messagebox.showinfo(":-)....:-)", "Data has been saved!!!")
                idd.delete(0, END)
                nm.delete(0, END)
                aad.delete(0, END)
                phn.delete(0, END)
                ad.delete(0, END)
                eml.delete(0, END)
                pw1.delete(0, END)
                sec1.delete(0, END)
            else:
                messagebox.showinfo("!!!!!!", "LIBRARIAN ID ALREADY PRESENT")
                return
            mydb.commit()
            mycursor.close()
            mydb.close()
        else:
            messagebox.showinfo("!!!!!", "Error with your entry")

    root = Toplevel()
    root.title("Librarian")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\dispstud.jpg")
    new = l.resize((1400, 800), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)
    Label(root, bg="#fff").pack(pady=20, anchor="nw")
    Label(root, text="Enter the ID number given by institution", fg="blue", font=("Helvetica", 12, "bold"),
          bg="#fff").pack(pady=2)
    idd = Entry(root, textvariable=IntVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    idd.delete(0,END)
    idd.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your full name", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(pady=2)
    nm = Entry(root, textvariable=StringVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    nm.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your Aadhaar number", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(
        pady=2)
    aad = Entry(root, textvariable=IntVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    aad.delete(0,END)
    aad.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your Phone number", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(
        pady=2)
    phn = Entry(root, textvariable=IntVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    phn.delete(0,END)
    phn.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your address", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(pady=2)
    ad = Entry(root, textvariable=StringVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    ad.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your email", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(pady=2)
    eml = Entry(root, textvariable=StringVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    eml.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="Enter your password", fg="blue", font=("Helvetica", 12, "bold"), bg="#fff").pack(pady=2)
    pw1 = Entry(root, textvariable=StringVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    pw1.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    Label(root, text="SECURITY QUESTION:-\nENTER YOUR FIRST INSTITUTION", fg="blue",
          font=("Helvetica", 12, "bold"), bg="#fff").pack(pady=2)
    sec1 = Entry(root, textvariable=StringVar(), fg="black", font=("Helvetica", 11, "bold"), bg="#fff")
    sec1.pack(padx=70, pady=2, ipadx=30, ipady=2, anchor="center")
    bttn = Button(root, text="Press to load the the above data", command=librarian, fg="blue",
                  font=("Helvetica", 12, "bold"), bg="#fff")
    bttn.pack(pady=2)
    root.bind('<Return>', librarian)
    Button(root, text="Exit The Program", command=quit, fg="blue", font=("Helvetica", 12, "bold"),
           bg="#fff").pack(pady=2)
    root.mainloop()


def dispbook():
    root = Toplevel()
    root.title("Displaying Books ")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\dispstud.jpg")
    new = l.resize((1350,800), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)

    def quit():
        root.destroy()

    def display():
        mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
        mycursor = mydb.cursor()
        bttn.configure(state=DISABLED)
        ntm.configure(state=NORMAL)
        mv = str(opt.get())
        if mv == "       Z-A     ":
            mv = " desc"
        else:
            mv = " asc"
        if str(opp.get()) == "      BOOK  NUMBER     ":
            dd = srch.get()
            if str.isnumeric(dd):
                int(dd)
                mycursor.execute("select * from book where book_no=" + str(dd) + " order by book_name" + str(mv) + "")
            else:
                messagebox.showinfo("ERROR", "GIVE AN INTEGER VALUE")
                return
        elif str(opp.get()) == "     BOOK  NAME      ":
            dd = srch.get()
            mycursor.execute(
                "select * from book where book_name='" + str.upper(str(dd)) + "' order by book_name" + str(mv) + "")
        elif str(opp.get()) == "       EVERYTHING      ":
            mycursor.execute("select * from book order by book_name" + str(mv) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        global b
        b = Label(root, text="NUMBER OF RECORDS=" + str(gg), fg="blue", font=("Helvetica", 15, "bold"), bg="#fff")
        b.place(anchor="center", x=630, y=90)
        if gg != 0:
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def reset():
        for record in tree.get_children():
            tree.delete(record)
        b.destroy()
        bttn.configure(state=NORMAL)
        ntm.configure(state=DISABLED)
        srch.delete(0, END)

    search = StringVar()
    srch = Entry(root, textvariable=search, font=("Helvetica", 11), bg="#fff")
    con = {"      BOOK  NUMBER     ", "     BOOK  NAME      ", "       EVERYTHING      "}
    opp = StringVar()
    opp.set("             SELECT          ")
    mn = OptionMenu(root, opp, *con)
    mn.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    co = {"       A-Z      ", "       Z-A     "}
    opt = StringVar()
    opt.set("    ORDER BY    ")
    m = OptionMenu(root, opt, *co)
    m.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    imm = Image.open("C:\library_management_prj\images\search.png")
    new = imm.resize((55, 25), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(new)
    bttn = Button(root, image=img, command=display, bg="#fff")
    ntm = Button(root, text="CLEAR", command=reset, font=("Helvetica", 11, "bold"), bg="#fff")
    ntm.configure(state=DISABLED)
    srch.pack(padx=20, pady=10, anchor="nw", ipadx=15, ipady=3)
    mn.place(x=250, y=5)
    m.place(x=470, y=5)
    bttn.place(x=650, y=6)
    ntm.place(x=750, y=5)
    qt = Button(root, text="              E X I T           ", command=quit, font=("Helvetica", 11, "bold"), bg="red")
    qt.place(x=1150, y=5)
    disp_frame=LabelFrame(root)
    disp_frame.pack(pady=70)
    tree = ttk.Treeview(disp_frame)
    tree['show'] = 'headings'
    s = ttk.Style(disp_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = (
        "Book_NO", "Book_Name", "Price", "Category", "Author_Name", "No_of_Pages", "Book_Language", "date_of_purchase",
        "print_date", "Availability")
    tree.column("Book_NO", width=120, minwidth=120, anchor=CENTER)
    tree.column("Book_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("Price", width=120, minwidth=120, anchor=CENTER)
    tree.column("Category", width=120, minwidth=120, anchor=CENTER)
    tree.column("Author_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("No_of_Pages", width=120, minwidth=120, anchor=CENTER)
    tree.column("Book_Language", width=120, minwidth=120, anchor=CENTER)
    tree.column("date_of_purchase", width=125, minwidth=125, anchor=CENTER)
    tree.column("print_date", width=120, minwidth=120, anchor=CENTER)
    tree.column("Availability", width=120, minwidth=120, anchor=CENTER)
    tree.heading("Book_NO", text="BOOK NUMBER", anchor=CENTER)
    tree.heading("Book_Name", text="BOOK NAME", anchor=CENTER)
    tree.heading("Price", text="PRICE", anchor=CENTER)
    tree.heading("Category", text="CATEGORY", anchor=CENTER)
    tree.heading("Author_Name", text="AUTHOR NAME", anchor=CENTER)
    tree.heading("No_of_Pages", text="NUMBER OF PAGES", anchor=CENTER)
    tree.heading("Book_Language", text="BOOK LANGUAGE", anchor=CENTER)
    tree.heading("date_of_purchase", text="DATE OF PURCHASE", anchor=CENTER)
    tree.heading("print_date", text="PRINT DATE", anchor=CENTER)
    tree.heading("Availability", text="AVAILABILITY", anchor=CENTER)
    hsb = ttk.Scrollbar(disp_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    vsb = ttk.Scrollbar(disp_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side="right")
    tree.pack(side="bottom"
              , pady=2, ipady=150,ipadx=30)
    root.mainloop()


def displibr():
    root = Toplevel()
    root.title("Displaying Librarian ")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\dispstud.jpg")
    new = l.resize((1350, 750), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)

    def quit():
        root.destroy()

    def display():
        mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
        mycursor = mydb.cursor()
        bttn.configure(state=DISABLED)
        ntm.configure(state=NORMAL)
        mv = str(opt.get())
        if mv == "       Z-A      ":
            mv = " desc"
        else:
            mv = " asc"
        if str(opp.get()) == "         I D         ":
            dd = srch.get()
            if str.isnumeric(dd):
                mycursor.execute("select * from librarian where id=" + str(dd) + " order by name" + str(mv) + "")
            else:
                messagebox.showinfo("ERROR", "GIVE AN INTEGER VALUE")
                return
        elif str(opp.get()) == "    NAME     ":
            dd = srch.get()
            mycursor.execute(
                "select * from librarian where name='" + str.upper(str(dd)) + "' order by name" + str(mv) + "")
        elif str(opp.get()) == "  EVERYTHING   ":
            mycursor.execute("select * from librarian order by name" + str(mv) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        global b
        b = Label(root, text="NUMBER OF RECORDS=" + str(gg), fg="blue", font=("Helvetica", 15, "bold"), bg="#fff")
        b.place(anchor="center", x=630, y=70)
        if gg != 0:
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def reset():
        for record in tree.get_children():
            tree.delete(record)
        b.destroy()
        bttn.configure(state=NORMAL)
        ntm.configure(state=DISABLED)
        srch.delete(0, END)

    search = StringVar()
    srch = Entry(root, textvariable=search, bg="#fff")
    con = {"         I D         ", "    NAME     ", "  EVERYTHING   "}
    opp = StringVar()
    opp.set("      SELECT    ")
    mn = OptionMenu(root, opp, *con)
    mn.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    co = {"       A-Z      ", "       Z-A      "}
    opt = StringVar()
    opt.set("    ORDER BY    ")
    m = OptionMenu(root, opt, *co)
    m.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    imm = Image.open("C:\library_management_prj\images\search.png")
    new = imm.resize((55, 25), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(new)
    bttn = Button(root, image=img, command=display, bg="#fff")
    ntm = Button(root, text="CLEAR", command=reset, font=("Helvetica", 11, "bold"), bg="#fff")
    ntm.configure(state=DISABLED)
    srch.pack(padx=20, pady=10, anchor="nw", ipadx=15, ipady=3)
    mn.place(x=250, y=5)
    m.place(x=470, y=5)
    bttn.place(x=650, y=6)
    ntm.place(x=750, y=5)
    qt = Button(root, text="         E X I T          ", command=quit, font=("Helvetica", 11, "bold"), bg="red")
    qt.place(x=1150, y=5)
    disp_frame=LabelFrame(root)
    disp_frame.pack(pady=60)
    tree = ttk.Treeview(disp_frame)
    tree['show'] = 'headings'
    s = ttk.Style(disp_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = ("ID", "Name", "Aadhaar_No", "Phone_No", "Address", "Email")
    tree.column("ID", width=170, minwidth=170, anchor=CENTER)
    tree.column("Name", width=170, minwidth=170, anchor=CENTER)
    tree.column("Aadhaar_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Phone_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Address", width=170, minwidth=170, anchor=CENTER)
    tree.column("Email", width=170, minwidth=170, anchor=CENTER)

    tree.heading("ID", text="ID", anchor=CENTER)
    tree.heading("Name", text="  NAME  ", anchor=CENTER)
    tree.heading("Aadhaar_No", text="AADHAAR NUMBER", anchor=CENTER)
    tree.heading("Phone_No", text="PHONE NUMBER", anchor=CENTER)
    tree.heading("Address", text="ADDRESS", anchor=CENTER)
    tree.heading("Email", text="EMAIL ID", anchor=CENTER)

    hsb = ttk.Scrollbar(disp_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    vsb = ttk.Scrollbar(disp_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side="right")
    tree.pack(side="bottom", pady=5, ipady=160, ipadx=160)
    root.mainloop()


def dispstud():
    root = Toplevel()
    root.title("Displaying Student ")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\dispstud.jpg")
    new = l.resize((1350, 750), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)

    def display():
        mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
        mycursor = mydb.cursor()
        bttn.configure(state=DISABLED)
        ntm.configure(state=NORMAL)
        mv = str(opt.get())
        if mv == "       Z-A      ":
            mv = " desc"
        else:
            mv = " asc"
        if str(opp.get()) == "ADMISSION  NUMBER":
            dd = srch.get()
            if str.isnumeric(dd):
                mycursor.execute("select * from student where admno=" + str(dd) + " order by name" + str(mv) + "")
            else:
                messagebox.showinfo("ERROR", "GIVE AN INTEGER VALUE")
                return
        elif str(opp.get()) == "    NAME     ":
            dd = srch.get()
            mycursor.execute(
                "select * from student where name='" + str.upper(str(dd)) + "' order by name" + str(mv) + "")
        elif str(opp.get()) == "  EVERYTHING   ":
            mycursor.execute("select * from student order by name" + str(mv) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        global b
        b = Label(root, text="NUMBER OF RECORDS=" + str(gg), fg="blue", font=("Helvetica", 15, "bold"), bg="#fff")
        b.place(anchor="center", x=630, y=70)
        if gg != 0:
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def reset():
        for record in tree.get_children():
            tree.delete(record)
        b.destroy()
        bttn.configure(state=NORMAL)
        ntm.configure(state=DISABLED)
        srch.delete(0, END)

    def quit():
        root.destroy()

    search = StringVar()
    srch = Entry(root, textvariable=search, bg="#fff")
    con = {"ADMISSION  NUMBER", "    NAME     ", "  EVERYTHING   "}
    opp = StringVar()
    opp.set("      SELECT    ")
    mn = OptionMenu(root, opp, *con)
    mn.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    co = {"       A-Z      ", "       Z-A      "}
    opt = StringVar()
    opt.set("    ORDER BY    ")
    m = OptionMenu(root, opt, *co)
    m.configure(font=("Helvetica", 11, "bold"), bg="#fff")
    imm = Image.open("C:\library_management_prj\images\search.png")
    new = imm.resize((55, 25), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(new)
    bttn = Button(root, image=img, command=display, bg="#fff")
    ntm = Button(root, text="CLEAR", command=reset, font=("Helvetica", 11, "bold"), bg="#fff")
    ntm.configure(state=DISABLED)
    srch.pack(padx=20, pady=10, anchor="nw", ipadx=15, ipady=3)
    mn.place(x=250, y=5)
    m.place(x=470, y=5)
    bttn.place(x=650, y=6)
    ntm.place(x=750, y=5)
    qt = Button(root, text="         E X I T          ", command=quit, font=("Helvetica", 11, "bold"), bg="red")
    qt.place(x=1150, y=5)
    disp_frame=LabelFrame(root)
    disp_frame.pack(pady=70)
    tree = ttk.Treeview(disp_frame)
    tree['show'] = 'headings'
    s = ttk.Style(disp_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = (
        "ADMNO", "Name", "Class_Sec", "Roll_No", "Address", "Book_Issued", "Phone", "Book_No", "Book_issued_on")
    tree.column("ADMNO", width=170, minwidth=170, anchor=CENTER)
    tree.column("Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("Class_Sec", width=120, minwidth=120, anchor=CENTER)
    tree.column("Roll_No", width=130, minwidth=130, anchor=CENTER)
    tree.column("Address", width=120, minwidth=120, anchor=CENTER)
    tree.column("Book_Issued", width=160, minwidth=150, anchor=CENTER)
    tree.column("Phone", width=130, minwidth=130, anchor=CENTER)
    tree.column("Book_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Book_issued_on", width=170, minwidth=170, anchor=CENTER)
    tree.heading("ADMNO", text="ADMISSION NUMBER", anchor=CENTER)
    tree.heading("Name", text="  NAME  ", anchor=CENTER)
    tree.heading("Class_Sec", text="CLASS SECTION", anchor=CENTER)
    tree.heading("Roll_No", text="ROLL NUMBER", anchor=CENTER)
    tree.heading("Address", text="ADDRESS", anchor=CENTER)
    tree.heading("Book_Issued", text="BOOK ISSUED", anchor=CENTER)
    tree.heading("Phone", text="PHONE NUMBER", anchor=CENTER)
    tree.heading("Book_No", text="BOOK NUMBER", anchor=CENTER)
    tree.heading("Book_issued_on", text="BOOK ISSUED DATE", anchor=CENTER)
    hsb = ttk.Scrollbar(disp_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    vsb = ttk.Scrollbar(disp_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side="right")
    tree.pack(side="bottom", pady=5, ipady=170, ipadx=50, padx=3)
    root.mainloop()


def updbook():
    root = Toplevel()
    root.title("  UPDATING BOOK ")
    hu=root.winfo_screenwidth()
    wu=root.winfo_screenheight()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), int(wu)-50))
    root.configure(bg="#fff")
    mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
    mycursor = mydb.cursor()

    def jus():
        for record in tree.get_children():
            tree.delete(record)
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        sel.deselect()
        upd.deselect()
        ch.deselect()
        ch1.deselect()
        x2.configure(state=DISABLED)
        x3.configure(state=DISABLED)
        x4.configure(state=DISABLED)
        x5.configure(state=DISABLED)
        x6.configure(state=DISABLED)
        x7.configure(state=DISABLED)
        x8.configure(state=DISABLED)
        x9.configure(state=DISABLED)
        x10.configure(state=DISABLED)
        clear1.configure(state=DISABLED)
        btn.configure(state=DISABLED)
        lb.configure(state=DISABLED)
        ent.configure(state=DISABLED)
        xv.configure(state=DISABLED)
        sel.configure(state=NORMAL)
        upd.configure(state=NORMAL)
        ent.delete(0, END)
        xcc1.delete(0, END)

    def enabling():
        global gg
        gg = Label(root)
        gg.pack()
        lb.configure(state=NORMAL)
        ent.configure(state=NORMAL)
        btn.configure(state=NORMAL)
        if q.get() == "DELETE":
            global gg1
            gg1 = Label(frame, text="DELETE WILL COMPLETELY\nDELETE THE RECORD", font=("helvetica", "6"), fg="red")
            gg1.place(anchor="center", x=130, y=100)
            x2.configure(state=DISABLED)
            x3.configure(state=DISABLED)
            x4.configure(state=DISABLED)
            x5.configure(state=DISABLED)
            x6.configure(state=DISABLED)
            x7.configure(state=DISABLED)
            x8.configure(state=DISABLED)
            x9.configure(state=DISABLED)
            x10.configure(state=DISABLED)
        elif q.get() == "UPDATE":
            x2.configure(state=NORMAL)
            x3.configure(state=NORMAL)
            x4.configure(state=NORMAL)
            x5.configure(state=NORMAL)
            x6.configure(state=NORMAL)
            x7.configure(state=NORMAL)
            x8.configure(state=NORMAL)
            x9.configure(state=NORMAL)
            x10.configure(state=NORMAL)
            gg.destroy()
        return

    def main():
        global opt, do1
        do1 = ent.get()
        opt = q.get()
        clear1.configure(state=NORMAL)
        mycursor.execute("select * from book where book_no=" + str(do1) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        if gg != 0:
            lb.configure(state=DISABLED)
            ent.configure(state=DISABLED)
            btn.configure(state=DISABLED)
            xz.configure(state=NORMAL)
            ch.configure(state=NORMAL)
            ch1.configure(state=NORMAL)
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")

    def clear():
        try:
            xcc1.destroy()
            xc.destroy()
            jus()
        except:
            jus()

    def yesno():
        global xcc1, xc
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        if opt == "UPDATE":
            if str(y.get()) == "YES":
                if str(p.get()) == "date_of_purchase" or str(p.get()) == "print_date":
                    xc = Label(root, text="SELECT THE NEW VALUE\nCALENDAR", fg="blue", font=("Helvetica", 11, "italic"),
                               bg="#fff")
                    xc.pack(pady=10)
                    xcc1 = Button(root, text="CALENDAR", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff",
                                  command=calen)
                    xcc1.pack(pady=5)
                else:
                    xc = Label(root, text="ENTER THE NEW VALUE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                    xc.pack(pady=10)
                    xcc1 = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                    xcc1.pack(pady=5)
                xv.configure(state=NORMAL)
            elif str(y.get()) == "NO":
                clear()
                return
        elif opt == "DELETE":
            updel()

    def calen():
        global xcc, root1
        root1 = Toplevel()
        root1.geometry("300x300+300+200")
        root1.title("CALENDAR")
        xcc = tc.Calendar(root1, date_pattern="y-mm-dd", textvariable=StringVar(), year=2021, month=2, date=21)
        xcc.pack(pady=30, fill="both", expand=TRUE)
        bttno = Button(root1, text="OK", command=upg)
        bttno.pack(pady=10, ipadx=40, ipady=10)

    def upg():
        xcc1.configure(text=str(xcc.get_date()))
        root1.destroy()

    def updel():
        sel.configure(state=DISABLED)
        upd.configure(state=DISABLED)
        if not str(do1).isalpha():
            if opt == "DELETE":
                mycursor.execute("delete from book where book_no=" + str(do1) + "")
                messagebox.showinfo("DONE", "RECORD HAS BEEN DELETED")
            elif opt == "UPDATE":
                xcc1.configure(state=DISABLED)
                xc.configure(state=DISABLED)
                if str(p.get()) == "date_of_purchase" or str(p.get()) == "print_date":
                    mycursor.execute(
                        "update book set " + str(p.get()) + "='" + str(xcc.selection_get()) + "' where book_no=" + str(do1))
                else:
                    mycursor.execute(
                        "update book set " + str(p.get()) + "='" + str.upper(str(xcc1.get())) + "' where book_no=" + str(
                            do1))
                messagebox.showinfo("DONE", "RECORD HAS BEEN UPDATED")
            mydb.commit()
        else:
            messagebox.showinfo("!!!!","PLEASE ENTER ID")

    def exit1():
        mycursor.close()
        mydb.close()
        root.destroy()

    frame = LabelFrame(root, text="SELECT", padx=20, pady=60, bg="#fff")
    frame.pack(padx=10, pady=5, anchor="nw")
    Label(frame, text="WHAT DO YOU WANT TO DO", fg="blue", font=("Helvetica", 11, "bold"), bg="#fff").pack()
    q = StringVar()
    sel = Radiobutton(frame, text="UPDATE", variable=q, value="UPDATE", command=enabling)
    sel.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    sel.pack(anchor="nw", pady=10)
    sel.deselect()
    upd = Radiobutton(frame, text="DELETE", variable=q, value="DELETE", command=enabling)
    upd.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    upd.place(anchor="center", x=160, y=50)
    upd.deselect()
    frame1 = LabelFrame(root, text="", bg="#fff")
    frame1.place(y=13, x=270, width=250, height=205)
    p = StringVar()
    x2 = Radiobutton(frame1, text="BOOK NAME", variable=p, value="book_name")
    x2.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x2.pack(anchor="nw", padx=5, pady=7)
    x2.deselect()
    x3 = Radiobutton(frame1, text="PRICE", variable=p, value="price")
    x3.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x3.place(x=130, y=7)
    x3.deselect()
    x4 = Radiobutton(frame1, text="CATEGORY", variable=p, value="category")
    x4.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x4.pack(anchor="nw", padx=5, pady=5)
    x4.deselect()
    x5 = Radiobutton(frame1, text="AUTHOR NAME", variable=p, value="author_name")
    x5.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x5.place(x=130, y=43)
    x5.deselect()
    x6 = Radiobutton(frame1, text="NO_OF_PAGES", variable=p, value="no_of_pages")
    x6.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x6.pack(anchor="nw", padx=5, pady=7)
    x6.deselect()
    x7 = Radiobutton(frame1, text="BOOK LANGUAGE", variable=p, value="book_language")
    x7.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x7.pack(anchor="nw", padx=5, pady=7)
    x7.deselect()
    x8 = Radiobutton(frame1, text="PURCHASE DATE", variable=p, value="date_of_purchase")
    x8.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x8.place(x=112, y=165)
    x8.deselect()
    x9 = Radiobutton(frame1, text="PRINT DATE", variable=p, value="print_date")
    x9.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x9.place(x=130, y=82)
    x9.deselect()
    x10 = Radiobutton(frame1, text="AVAILABILITY", variable=p, value="availability")
    x10.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x10.pack(anchor="nw", padx=5, pady=15)
    x10.deselect()
    frame2 = LabelFrame(root, bg="#fff")
    frame2.place(y=13, x=522, width=400, height=205)
    lb = Label(frame2, text="ENTER THE BOOK NUMBER \nTHAT YOU WANT TO UPDATE/DELETE", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")
    lb.configure(state=DISABLED)
    lb.pack(pady=5)
    ent = Entry(frame2, textvariable=IntVar(), fg="blue", font=("Helvetica", 12, "italic"), bg="#fff")
    ent.delete(0,END)
    ent.configure(state=DISABLED)
    ent.pack(pady=10)
    btn = Button(frame2, text="ENTER", command=main, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    btn.configure(state=DISABLED)
    btn.pack(side="bottom", pady=10)
    frame4 = LabelFrame(root, bg="#fff")
    frame4.place(y=13, x=924, height=205, width=335)
    clear1 = Button(frame4, text="       C L E A R        ", command=clear, fg="blue", font=("Helvetica", 12, "italic"),
                    bg="red")
    clear1.configure(state=DISABLED)
    clear1.pack(anchor="nw", pady=65, padx=10)
    ext = Button(frame4, text="           E X I T         ", command=exit1, fg="#fff", font=("Helvetica", 12, "italic"),
                 bg="red")
    ext.place(anchor="center", x=270, y=78)
    xz = Label(root, text="ARE YOU SURE YOU WANT TO DELETE/UPDATE THIS RECORD", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")
    xz.configure(state=DISABLED)
    xz.pack()
    y = StringVar()
    ch = Radiobutton(root, text="YES", variable=y, value="YES", command=yesno)
    ch.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch.pack(anchor="nw", padx=600)
    ch.deselect()
    ch1 = Radiobutton(root, text="NO", variable=y, value="NO", command=yesno)
    ch1.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch1.place(x=700, y=245)
    ch1.deselect()
    upd_frame = LabelFrame(root,bg="#fff")
    upd_frame.pack(side="bottom", pady=25)
    xv = Button(upd_frame, text="UPDATE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    xv.configure(state=DISABLED, command=updel)
    xv.pack(pady=5)
    tree = ttk.Treeview(upd_frame)
    tree['show'] = 'headings'
    s = ttk.Style(upd_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = (
        "Book_NO", "Book_Name", "Price", "Category", "Author_Name", "No_of_Pages", "Book_Language", "date_of_purchase",
        "print_date", "Availability")
    tree.column("Book_NO", width=150, minwidth=150, anchor=CENTER)
    tree.column("Book_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("Price", width=120, minwidth=120, anchor=CENTER)
    tree.column("Category", width=120, minwidth=120, anchor=CENTER)
    tree.column("Author_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("No_of_Pages", width=160, minwidth=150, anchor=CENTER)
    tree.column("Book_Language", width=150, minwidth=150, anchor=CENTER)
    tree.column("date_of_purchase", width=170, minwidth=170, anchor=CENTER)
    tree.column("print_date", width=120, minwidth=120, anchor=CENTER)
    tree.column("Availability", width=150, minwidth=150, anchor=CENTER)
    tree.heading("Book_NO", text="BOOK NUMBER", anchor=CENTER)
    tree.heading("Book_Name", text="BOOK NAME", anchor=CENTER)
    tree.heading("Price", text="PRICE", anchor=CENTER)
    tree.heading("Category", text="CATEGORY", anchor=CENTER)
    tree.heading("Author_Name", text="AUTHOR NAME", anchor=CENTER)
    tree.heading("No_of_Pages", text="NUMBER OF PAGES", anchor=CENTER)
    tree.heading("Book_Language", text="BOOK LANGUAGE", anchor=CENTER)
    tree.heading("date_of_purchase", text="DATE OF PURCHASE", anchor=CENTER)
    tree.heading("print_date", text="PRINT DATE", anchor=CENTER)
    tree.heading("Availability", text="AVAILABILITY", anchor=CENTER)
    hsb = ttk.Scrollbar(upd_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    tree.pack(side="bottom", pady=5, ipadx=180, padx=3)
    root.mainloop()


def updlibr():
    root = Toplevel()
    root.title("  UPDATING BOOK ")
    hu = root.winfo_screenwidth()
    wu = root.winfo_screenheight()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), int(wu) - 50))
    root.configure(bg="#fff")
    mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
    mycursor = mydb.cursor()

    def enabling():
        global gg
        gg = Label(root)
        gg.pack()
        lb.configure(state=NORMAL)
        ent.configure(state=NORMAL)
        btn.configure(state=NORMAL)
        if q.get() == "DELETE":
            gg = Label(frame, text="DELETE WILL COMPLETELY\nDELETE THE RECORD", font=("helvetica", "6"), fg="red")
            gg.place(anchor="center", x=130, y=100)
            x2.configure(state=DISABLED)
            x3.configure(state=DISABLED)
            x4.configure(state=DISABLED)
            x5.configure(state=DISABLED)
            x6.configure(state=DISABLED)
            x7.configure(state=DISABLED)
            x8.configure(state=DISABLED)
        elif q.get() == "UPDATE":
            x2.configure(state=NORMAL)
            x3.configure(state=NORMAL)
            x4.configure(state=NORMAL)
            x5.configure(state=NORMAL)
            x6.configure(state=NORMAL)
            x7.configure(state=NORMAL)
            x8.configure(state=NORMAL)
            gg.destroy()
        return

    def radio():
        x2.configure(state=DISABLED)
        x3.configure(state=DISABLED)
        x4.configure(state=DISABLED)
        x5.configure(state=DISABLED)
        x6.configure(state=DISABLED)
        x7.configure(state=DISABLED)
        x8.configure(state=DISABLED)

    def radio_e():
        x2.configure(state=NORMAL)
        x3.configure(state=NORMAL)
        x4.configure(state=NORMAL)
        x5.configure(state=NORMAL)
        x6.configure(state=NORMAL)
        x7.configure(state=NORMAL)
        x8.configure(state=NORMAL)

    def main():
        global opt, do1
        radio()
        do1 = ent.get()
        opt = q.get()
        clear1.configure(state=NORMAL)
        mycursor.execute("select * from librarian where id=" + str(do1) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        if gg != 0:
            lb.configure(state=DISABLED)
            ent.configure(state=DISABLED)
            btn.configure(state=DISABLED)
            xz.configure(state=NORMAL)
            ch.configure(state=NORMAL)
            ch1.configure(state=NORMAL)
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")
            return

    def run():
        for record in tree.get_children():
            tree.delete(record)
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        sel.deselect()
        upd.deselect()
        radio()
        clear1.configure(state=DISABLED)
        btn.configure(state=DISABLED)
        lb.configure(state=DISABLED)
        ent.configure(state=DISABLED)
        xv.configure(state=DISABLED)

    def clear():
        try:
            xc.destroy()
            xcc.destroy()
            xc1.destroy()
            xcc1.destroy()
            lbl.destroy()
            run()
            radio_e()
            ent.delete(0, END)
            xcc1.delete(0, END)
        except:
            run()
            radio_e()
            ent.delete(0, END)
            xcc1.delete(0, END)

    def yesno():
        global xc, xcc, xc1, xcc1, lbl
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        if opt == "UPDATE":
            if str(p.get()) == "password":
                xc = Label(root, text="ENTER THE OLD PASSWORD", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xc.pack(pady=5)
                xcc = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xcc.pack(pady=2)
                xc1 = Label(root, text="ENTER THE NEW PASSWORD", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xc1.pack(pady=5)
                xcc1 = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xcc1.pack(pady=2)
            elif str(p.get()) == "security":
                xc = Label(root, text="ENTER YOUR PASSWORD", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xc.pack(pady=5)
                xcc = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xcc.pack(pady=2)
                lbl = Label(root, text="YOUR FIRST INSTITUTION", fg="blue", font=("Helvetica", 11, "italic"), bg="red")
                lbl.pack(pady=3)
                xc1 = Label(root, text="ENTER YOUR ANSWER", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xc1.pack(pady=5)
                xcc1 = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xcc1.pack(pady=2)
            else:
                xc = Label(root, text="ENTER THE NEW VALUE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xc.pack(pady=10)
                xcc = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                xcc.pack(pady=5)
            if str(y.get()) == "YES":
                xv.configure(state=NORMAL)
            elif str(y.get()) == "NO":
                return
        elif opt == "DELETE":
            updel()

    def updel():
        sel.configure(state=DISABLED)
        upd.configure(state=DISABLED)
        if not str(do1).isalpha():
            if opt == "DELETE":
                mycursor.execute("delete from librarian where id=" + str(do1) + "")
                messagebox.showinfo("DONE", "RECORD HAS BEEN DELETED")
            elif opt == "UPDATE":
                if str(p.get()) == "password":
                    mycursor.execute("select password from librarian where ID=" + str(do1))
                    dj = mycursor.fetchall()
                    if dj[0][0] == str(xcc.selection_get()):
                        mycursor.execute(
                            "update librarian set password='" + str(xcc1.get()) + "' where ID=" + str(do1))
                        messagebox.showinfo("DONE", "RECORD HAS BEEN UPDATED")
                    else:
                        messagebox.showinfo("!!!", "WRONG PASSWORD")
                        return
                elif str(p.get()) == "security":
                    mycursor.execute("select password from librarian where ID=" + str(do1))
                    dj = mycursor.fetchall()
                    if dj[0][0] == str(xcc.selection_get()):
                        mycursor.execute(
                            "update librarian set security='" + str(xcc1.get()) + "' where ID=" + str(do1))
                        messagebox.showinfo("DONE", "RECORD HAS BEEN UPDATED")
                    else:
                        messagebox.showinfo("!!!", "WRONG PASSWORD")
                        return
                else:
                    mycursor.execute(
                        "update librarian set " + str(p.get()) + "='" + str(xcc.get()) + "' where ID=" + str(do1))
                    messagebox.showinfo("DONE", "RECORD HAS BEEN UPDATED")
            xv.configure(state=DISABLED)
            mydb.commit()
        else:
            messagebox.showinfo("!!!","ENTER YOUR ID")

    def exit1():
        mycursor.close()
        mydb.close()
        root.destroy()

    frame = LabelFrame(root, text="SELECT", padx=20, pady=60, bg="#fff")
    frame.pack(padx=10, pady=5, anchor="nw")
    x = Label(frame, text="WHAT DO YOU WANT TO DO", fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    x.pack()
    q = StringVar()
    sel = Radiobutton(frame, text="UPDATE", variable=q, value="UPDATE", command=enabling)
    sel.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    sel.pack(anchor="nw", pady=10)
    sel.deselect()
    upd = Radiobutton(frame, text="DELETE", variable=q, value="DELETE", command=enabling)
    upd.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    upd.place(anchor="center", x=160, y=50)
    upd.deselect()
    frame1 = LabelFrame(root, text="", bg="#fff")
    frame1.place(y=13, x=270, width=250, height=205)
    p = StringVar()
    x2 = Radiobutton(frame1, text="NAME", variable=p, value="name")
    x2.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x2.pack(anchor="nw", padx=5, pady=15)
    x2.deselect()
    x3 = Radiobutton(frame1, text="AADHAAR", variable=p, value="aadhaar")
    x3.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x3.place(x=130, y=15)
    x3.deselect()
    x4 = Radiobutton(frame1, text="PHONE_NO", variable=p, value="phone_no")
    x4.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x4.pack(anchor="nw", padx=5, pady=5)
    x4.deselect()
    x5 = Radiobutton(frame1, text="ADDRESS", variable=p, value="Address")
    x5.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x5.place(x=130, y=60)
    x5.deselect()
    x6 = Radiobutton(frame1, text="EMAIL", variable=p, value="email")
    x6.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x6.pack(anchor="nw", padx=5, pady=15)
    x6.deselect()
    x7 = Radiobutton(frame1, text="PASSWORD", variable=p, value="password")
    x7.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x7.place(x=130, y=105)
    x7.deselect()
    x8 = Radiobutton(frame1, text="SECURITY QUESTION", variable=p, value="security")
    x8.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x8.pack(anchor="nw", padx=5, pady=15)
    x8.deselect()
    frame2 = LabelFrame(root, bg="#fff")
    frame2.place(y=13, x=522, width=400, height=205)
    lb = Label(frame2, text="ENTER THE ID \nTHAT YOU WANT TO UPDATE/DELETE", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")
    lb.configure(state=DISABLED)
    lb.pack(pady=5)
    ent = Entry(frame2, textvariable=IntVar(), fg="blue", font=("Helvetica", 12, "italic"), bg="#fff")
    ent.delete(0,END)
    ent.configure(state=DISABLED)
    ent.pack(pady=10)
    btn = Button(frame2, text="ENTER", command=main, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    btn.configure(state=DISABLED)
    btn.pack(side="bottom", pady=10)
    frame4 = LabelFrame(root, bg="#fff")
    frame4.place(y=13, x=924, height=205, width=360)
    clear1 = Button(frame4, text="       C L E A R        ", command=clear, fg="blue", font=("Helvetica", 12, "italic"),
                    bg="red")
    clear1.configure(state=DISABLED)
    clear1.pack(anchor="nw", pady=65, padx=10)
    ext = Button(frame4, text="           E X I T         ", command=exit1, fg="#fff", font=("Helvetica", 12, "italic"),
                 bg="red")
    ext.place(anchor="center", x=270, y=78)
    xz = Label(root, text="ARE YOU SURE YOU WANT TO DELETE/UPDATE THIS RECORD", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")

    xz.configure(state=DISABLED)
    xz.pack()
    y = StringVar()
    ch = Radiobutton(root, text="YES", variable=y, value="YES", command=yesno)
    ch.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch.pack(anchor="nw", padx=600)
    ch.deselect()
    ch1 = Radiobutton(root, text="NO", variable=y, value="NO", command=yesno)
    ch1.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch1.place(x=700, y=245)
    ch1.deselect()
    upd_frame=LabelFrame(root)
    upd_frame.pack(side="bottom",pady=15)
    xv = Button(upd_frame, text="DELETE/UPDATE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    xv.configure(state=DISABLED, command=updel)
    xv.pack(pady=8)
    tree = ttk.Treeview(upd_frame)
    tree['show'] = 'headings'
    s = ttk.Style(upd_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = ("ID", "Name", "Aadhaar_No", "Phone_No", "Address", "Email")
    tree.column("ID", width=170, minwidth=170, anchor=CENTER)
    tree.column("Name", width=170, minwidth=170, anchor=CENTER)
    tree.column("Aadhaar_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Phone_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Address", width=170, minwidth=170, anchor=CENTER)
    tree.column("Email", width=170, minwidth=170, anchor=CENTER)
    tree.heading("ID", text="ID", anchor=CENTER)
    tree.heading("Name", text="  NAME  ", anchor=CENTER)
    tree.heading("Aadhaar_No", text="AADHAAR NUMBER", anchor=CENTER)
    tree.heading("Phone_No", text="PHONE NUMBER", anchor=CENTER)
    tree.heading("Address", text="ADDRESS", anchor=CENTER)
    tree.heading("Email", text="EMAIL ID", anchor=CENTER)
    hsb = ttk.Scrollbar(upd_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    tree.pack(side="bottom", ipadx=180, padx=3)
    root.mainloop()


def updstud():
    from tkinter import ttk, messagebox
    root = Toplevel()
    root.title("  UPDATING STUDENT ")
    wu = root.winfo_screenheight()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), int(wu) - 50))
    root.configure(bg="#fff")
    mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
    mycursor = mydb.cursor()

    def jus():
        for record in tree.get_children():
            tree.delete(record)
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        sel.deselect()
        upd.deselect()
        ch.deselect()
        ch1.deselect()
        x2.configure(state=DISABLED)
        x3.configure(state=DISABLED)
        x4.configure(state=DISABLED)
        x5.configure(state=DISABLED)
        x6.configure(state=DISABLED)
        x7.configure(state=DISABLED)
        x8.configure(state=DISABLED)
        x9.configure(state=DISABLED)
        clear1.configure(state=DISABLED)
        btn.configure(state=DISABLED)
        lb.configure(state=DISABLED)
        ent.configure(state=DISABLED)
        xv.configure(state=DISABLED)
        sel.configure(state=NORMAL)
        upd.configure(state=NORMAL)
        ent.delete(0, END)
        xcc1.delete(0, END)

    def calen():
        global xcc, root1
        root1 = Toplevel()
        root1.geometry("300x300+300+200")
        root1.title("CALENDAR")
        xcc = tc.Calendar(root1, date_pattern="y-mm-dd", textvariable=StringVar(), year=2021, month=2, date=21)
        xcc.pack(pady=30, fill="both", expand=TRUE)
        bttno = Button(root1, text="OK", command=upg)
        bttno.pack(pady=10, ipadx=40, ipady=10)

    def upg():
        if str(xcc.get_date()) == "":
            messagebox.showinfo("!!!", "SELECT THE DATE")
        else:
            xcc1.configure(text=str(xcc.get_date()))
            root1.destroy()

    def enabling():
        global gg
        gg = Label(root)
        gg.pack()
        lb.configure(state=NORMAL)
        ent.configure(state=NORMAL)
        btn.configure(state=NORMAL)
        if q.get() == "DELETE":
            global gg1
            gg1 = Label(frame, text="DELETE WILL COMPLETELY\nDELETE THE RECORD", font=("helvetica", "6"), fg="red")
            gg1.place(anchor="center", x=130, y=100)
            x2.configure(state=DISABLED)
            x3.configure(state=DISABLED)
            x4.configure(state=DISABLED)
            x5.configure(state=DISABLED)
            x6.configure(state=DISABLED)
            x7.configure(state=DISABLED)
            x8.configure(state=DISABLED)
            x9.configure(state=DISABLED)
        elif q.get() == "UPDATE":
            x2.configure(state=NORMAL)
            x3.configure(state=NORMAL)
            x4.configure(state=NORMAL)
            x5.configure(state=NORMAL)
            x6.configure(state=NORMAL)
            x7.configure(state=NORMAL)
            x8.configure(state=NORMAL)
            x9.configure(state=NORMAL)
            gg.destroy()
        return

    def main():
        global opt, do1
        do1 = ent.get()
        opt = q.get()
        clear1.configure(state=NORMAL)
        mycursor.execute("select * from student where admno=" + str(do1) + "")
        zz = mycursor.fetchall()
        gg = mycursor.rowcount
        if gg != 0:
            lb.configure(state=DISABLED)
            ent.configure(state=DISABLED)
            btn.configure(state=DISABLED)
            xz.configure(state=NORMAL)
            ch.configure(state=NORMAL)
            ch1.configure(state=NORMAL)
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))
                i += 1
        else:
            messagebox.showinfo("ERROR", "NO SUCH DATA AVAILABLE")

    def clear():
        try:
            xcc1.destroy()
            xc.destroy()
            cv.destroy()
            jus()
        except:
            jus()

    def yesno():
        global xcc1, xc, z, cv
        xz.configure(state=DISABLED)
        ch.configure(state=DISABLED)
        ch1.configure(state=DISABLED)
        if opt == "UPDATE":
            if str(y.get()) == "YES":
                if str(p.get()) == "book_issued_on":
                    xc = Label(root, text="SELECT THE NEW VALUE", fg="blue", font=("Helvetica", 11, "italic"),
                               bg="#fff")
                    xc.pack(pady=10)
                    xcc1 = Button(root, text="CALENDAR", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff",
                                  command=calen)
                    xcc1.pack(pady=5)
                    z = StringVar()
                    cv = Radiobutton(root, text="NULL", variable=z, value="null")
                    cv.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
                    cv.place(x=640, y=360)
                else:
                    xc = Label(root, text="ENTER THE NEW VALUE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                    xc.pack(pady=10)
                    xcc1 = Entry(root, textvariable=StringVar(), fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
                    xcc1.pack(pady=5)
                xv.configure(state=NORMAL)
            elif str(y.get()) == "NO":
                clear()
                return
        elif opt == "DELETE":
            updel()

    def updel():
        sel.configure(state=DISABLED)
        upd.configure(state=DISABLED)
        if not str(do1).isalpha():
            if opt == "DELETE":
                mycursor.execute("delete from student where admno=" + str(do1) + "")
                messagebox.showinfo("DONE", "RECORD HAS BEEN DELETED")
            elif opt == "UPDATE":
                xcc1.configure(state=DISABLED)
                xc.configure(state=DISABLED)
                if str(p.get()) == "book_issued_on":
                    if str(z.get()) != "":
                        mycursor.execute(
                            "update student set " + str(p.get()) + "='" + str(z.get()) + "' where admno=" + str(do1))
                    else:
                        mycursor.execute(
                            "update student set " + str(p.get()) + "='" + str(xcc.get_date()) + "' where admno=" + str(do1))
                else:
                    mycursor.execute(
                        "update student set " + str(p.get()) + "='" + str.upper(str(xcc1.get())) + "' where admno=" + str(
                            do1))
                messagebox.showinfo("DONE", "RECORD HAS BEEN UPDATED")
            mydb.commit()
        else:
            messagebox.showinfo("!!!!","ENTER YOUR ID")
    def exit1():
        mycursor.close()
        mydb.close()
        root.destroy()

    frame = LabelFrame(root, text="SELECT", padx=20, pady=60, bg="#fff")
    frame.pack(padx=10, pady=5, anchor="nw")
    Label(frame, text="WHAT DO YOU WANT TO DO", fg="blue", font=("Helvetica", 11, "bold"), bg="#fff").pack()
    q = StringVar()
    sel = Radiobutton(frame, text="UPDATE", variable=q, value="UPDATE", command=enabling)
    sel.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    sel.pack(anchor="nw", pady=10)
    sel.deselect()
    upd = Radiobutton(frame, text="DELETE", variable=q, value="DELETE", command=enabling)
    upd.configure(fg="blue", font=("Helvetica", 11, "bold"), bg="#fff")
    upd.place(anchor="center", x=160, y=50)
    upd.deselect()
    frame1 = LabelFrame(root, text="", bg="#fff")
    frame1.place(y=13, x=270, width=250, height=205)
    p = StringVar()
    x2 = Radiobutton(frame1, text="NAME", variable=p, value="name")
    x2.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x2.pack(anchor="nw", padx=5, pady=15)
    x2.deselect()
    x3 = Radiobutton(frame1, text="CLASS_SEC", variable=p, value="class_sec")
    x3.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x3.place(x=130, y=15)
    x3.deselect()
    x4 = Radiobutton(frame1, text="ROLL_NO", variable=p, value="roll_no")
    x4.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x4.pack(anchor="nw", padx=5, pady=5)
    x4.deselect()
    x5 = Radiobutton(frame1, text="ADDRESS", variable=p, value="Address")
    x5.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x5.place(x=130, y=60)
    x5.deselect()
    x6 = Radiobutton(frame1, text="BOOK_ISSUED", variable=p, value="book_issued")
    x6.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x6.pack(anchor="nw", padx=5, pady=15)
    x6.deselect()
    x7 = Radiobutton(frame1, text="PHONE", variable=p, value="phone")
    x7.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x7.pack(anchor="nw", padx=5, pady=15)
    x7.deselect()
    x8 = Radiobutton(frame1, text="BOOK_NO", variable=p, value="book_no")
    x8.configure(state=DISABLED, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    x8.place(x=130, y=105)
    x8.deselect()
    x9 = Radiobutton(frame1, text="BOOK_ISSUED_DATE", variable=p, value="book_issued_on")
    x9.configure(state=DISABLED, fg="blue", font=("Helvetica", 8, "italic"), bg="#fff")
    x9.place(x=100, y=158)
    x9.deselect()
    frame2 = LabelFrame(root, bg="#fff")
    frame2.place(y=13, x=522, width=400, height=205)
    lb = Label(frame2, text="ENTER THE ADMISSION NUMBER \nTHAT YOU WANT TO UPDATE/DELETE", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")
    lb.configure(state=DISABLED)
    lb.pack(pady=5)
    ent = Entry(frame2, textvariable=IntVar(), fg="blue", font=("Helvetica", 12, "italic"), bg="#fff")
    ent.delete(0,END)
    ent.configure(state=DISABLED)
    ent.pack(pady=10)
    btn = Button(frame2, text="ENTER", command=main, fg="blue", font=("Helvetica", 9, "italic"), bg="#fff")
    btn.configure(state=DISABLED)
    btn.pack(side="bottom", pady=10)
    frame4 = LabelFrame(root, bg="#fff")
    frame4.place(y=13, x=924, height=205, width=360)
    clear1 = Button(frame4, text="       C L E A R        ", command=clear, fg="blue", font=("Helvetica", 12, "italic"),
                    bg="red")
    clear1.configure(state=DISABLED)
    clear1.pack(anchor="nw", pady=65, padx=10)
    ext = Button(frame4, text="           E X I T         ", command=exit1, fg="#fff", font=("Helvetica", 12, "italic"),
                 bg="red")
    ext.place(anchor="center", x=270, y=78)
    xz = Label(root, text="ARE YOU SURE YOU WANT TO DELETE/UPDATE THIS RECORD", fg="blue",
               font=("Helvetica", 11, "italic"), bg="#fff")
    xz.configure(state=DISABLED)
    xz.pack()
    y = StringVar()
    ch = Radiobutton(root, text="YES", variable=y, value="YES", command=yesno)
    ch.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch.pack(anchor="nw", padx=600)
    ch.deselect()
    ch1 = Radiobutton(root, text="NO", variable=y, value="NO", command=yesno)
    ch1.configure(state=DISABLED, fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    ch1.place(x=700, y=245)
    ch1.deselect()
    upd_frame=LabelFrame(root,bg="#fff")
    upd_frame.pack(pady=15,side="bottom")
    xv = Button(upd_frame, text="UPDATE", fg="blue", font=("Helvetica", 11, "italic"), bg="#fff")
    xv.configure(state=DISABLED, command=updel)
    xv.pack(pady=8)
    tree = ttk.Treeview(upd_frame)
    tree['show'] = 'headings'
    s = ttk.Style(upd_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = (
        "ADMNO", "Name", "Class_Sec", "Roll_No", "Address", "Book_Issued", "Phone", "Book_No", "Book_issued_on")
    tree.column("ADMNO", width=170, minwidth=170, anchor=CENTER)
    tree.column("Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("Class_Sec", width=120, minwidth=120, anchor=CENTER)
    tree.column("Roll_No", width=130, minwidth=130, anchor=CENTER)
    tree.column("Address", width=120, minwidth=120, anchor=CENTER)
    tree.column("Book_Issued", width=160, minwidth=150, anchor=CENTER)
    tree.column("Phone", width=130, minwidth=130, anchor=CENTER)
    tree.column("Book_No", width=170, minwidth=170, anchor=CENTER)
    tree.column("Book_issued_on", width=170, minwidth=170, anchor=CENTER)
    tree.heading("ADMNO", text="ADMISSION NUMBER", anchor=CENTER)
    tree.heading("Name", text="  NAME  ", anchor=CENTER)
    tree.heading("Class_Sec", text="CLASS SECTION", anchor=CENTER)
    tree.heading("Roll_No", text="ROLL NUMBER", anchor=CENTER)
    tree.heading("Address", text="ADDRESS", anchor=CENTER)
    tree.heading("Book_Issued", text="BOOK ISSUED", anchor=CENTER)
    tree.heading("Phone", text="PHONE NUMBER", anchor=CENTER)
    tree.heading("Book_No", text="BOOK NUMBER", anchor=CENTER)
    tree.heading("Book_issued_on", text="BOOK ISSUED DATE", anchor=CENTER)
    hsb = ttk.Scrollbar(upd_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    tree.pack(side="bottom", pady=5, ipadx=180, padx=3)
    root.mainloop()


def fine():
    lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def main(event=None):
        if str(opp.get()) == "SELECT":
            messagebox.showinfo("!!!!!!", "PLEASE SELECT A YEAR")
            return
        root.destroy()
        f = open("C:\library_management_prj\_records\_fine_record.txt", "r")
        text = f.readlines()
        if len(text) != 0:
            n = 0
            v = 1
            for i in text:
                if 6 * (v - 1) + 2 == 1 + n:
                    s = i.split()
                    x = datetime.datetime.strptime(s[0], "%Y-%m-%d")
                    yr = str(x.year).rjust(15, " ")
                    mnt = int(x.month)
                    if str(opp.get()) == str(yr):
                        lst[mnt - 1] += int(s[3])
                    v += 1
                n += 1
            mt.figure(figsize=(10, 6))
            ax = mt.axes()
            ax.set_facecolor("black")
            mon = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            ctr = np.array(lst)
            ax.plot(mon, ctr, color="red")
            mt.xlabel("MONTH")
            mt.ylabel("FINE")
            mt.show()
        else:
            messagebox.showerror("!!!", "NO DATA TO FETCH")

    root = Toplevel()
    root.geometry("400x400")
    root.title("GRPAH: FINE")
    l = Image.open("C:\library_management_prj\images\calendar.jpg")
    new = l.resize((400, 400), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)
    lbl = Label(root, text="SELECT THE YEAR THAT YOU WANT TO SEE", bg="#fff", font=("Helvetica", 11, "bold"))
    lbl.pack(pady=20, ipadx=3)
    con = []
    for i in range(2018, int(datetime.date.today().year) + 1):
        string = str(i)
        dj = string.rjust(15, " ")
        con.append(dj)
    opp = StringVar()
    opp.set("SELECT")
    p = OptionMenu(root, opp, *con)
    p.config(bg="#fff", font=("Helvetica", 11, "bold"))
    p.pack(ipadx=10, pady=10)
    button = Button(root, text="OKAY", command=main, bg="#fff", font=("Helvetica", 11, "bold"))
    button.pack(pady=5)
    root.bind('<Return>', main)
    root.mainloop()


def graph_iss():
    root1 = Toplevel()
    root1.geometry("400x400+300+200")
    root1.title("YEAR")
    root1.resizable(0, 0)
    l = Image.open("C:\library_management_prj\images\calendar.jpg")
    new = l.resize((400, 400), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root1, image=r)
    img.image = r
    img.place(x=0, y=0)

    def main(event=None):
        if str(opp.get()) == "SELECT":
            messagebox.showinfo("!!!!!!", "PLEASE SELECT A YEAR")
            return
        root1.destroy()
        f = open("C:\library_management_prj\_records\issue_books_record.txt", "r")
        text = f.readlines()
        f.close()
        n = 0
        v = 0
        lst = []
        for i in text:
            if 6 * v + 2 == 1 + n:
                z = i.rstrip(" \n")
                x = datetime.datetime.strptime(z, "%Y-%m-%d")
                yr = str(x.year).rjust(15, " ")
                if yr == str(opp.get()):
                    m = x.month
                    lst.append(m)
                v += 1
            n += 1
        lst.sort()
        ls = []
        l = []
        for i in lst:
            if i not in ls:
                ls.append(i)
                no = lst.count(i)
                l.append(no)
        ct = len(l)
        if ct != 12:
            for i in range(12 - ct):
                l.append(0)
        mt.figure(figsize=(10, 6))
        ax = mt.axes()
        ax.set_facecolor("black")
        mon = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        ctr = np.array(l)
        ax.plot(mon, ctr, color="red")
        mt.xlabel("MONTH")
        mt.ylabel("BOOKS ISSUED")
        mt.show()

    lbl = Label(root1, text="SELECT THE YEAR THAT YOU WANT TO SEE", bg="#fff", font=("Helvetica", 11, "bold"))
    lbl.pack(pady=20, ipadx=3)
    con = []
    for i in range(2018, int(datetime.date.today().year) + 1):
        string = str(i)
        dj = string.rjust(15, " ")
        con.append(dj)
    opp = StringVar()
    opp.set("SELECT")
    p = OptionMenu(root1, opp, *con)
    p.config(bg="#fff", font=("Helvetica", 11, "bold"))
    p.pack(ipadx=10, pady=10)
    button = Button(root1, text="OKAY", command=main, bg="#fff", font=("Helvetica", 11, "bold"))
    button.pack(pady=5)
    root.bind('<Return>', main)
    root1.mainloop()


def rb():
    def clear():
        try:
            hjk.destroy()
            xz.destroy()
            bttn.configure(state=NORMAL)
            ntm.configure(state=DISABLED)
            jk.deselect()
            jk1.deselect()
            e.delete(0, END)
            en.delete(0, END)
            adj1.delete(0, END)
        except:
            bttn.configure(state=NORMAL)
            ntm.configure(state=DISABLED)
            jk.deselect()
            jk1.deselect()
            e.delete(0, END)
            en.delete(0, END)
            adj1.delete(0, END)

    def quit():
        root.destroy()

    def receiving_books(event=None):
        bttn.configure(state=DISABLED)
        ntm.configure(state=NORMAL)
        mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
        mycursor = mydb.cursor()
        bkn = int(e.get())
        mycursor.execute("select * from book where Book_No=" + str(bkn) + "")
        y = "YES"
        mycursor.fetchall()
        if mycursor.rowcount == 0:
            messagebox.showinfo("!!!!!!", "WRONG BOOK NUMBER...")
            mydb.commit()
            mycursor.close()
            mydb.close()
            return
        else:
            adn = int(en.get())
            mycursor.execute("select * from student where ADMNO=" + str(adn) + "")
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                messagebox.showinfo("!!!!!!", "WRONG ADMISSION NUMBER....")
                mydb.commit()
                mycursor.close()
                mydb.close()
                return
            else:
                mycursor.execute("select Book_Issued from student where admno=" + str(adn) + "")
                x = mycursor.fetchall()
                if x[0][0] == "NO":
                    messagebox.showinfo("SOMETHING WRONG", "STUDENT HADN'T ISSUED ANY BOOK")
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    return
                mycursor.execute("select book_no from student where admno=" + str(adn))
                ll = mycursor.fetchall()
                if ll[0][0] == int(bkn):
                    mycursor.execute("select name from librarian where id=" + str(adj1.get()) + "")
                    jk2 = mycursor.fetchall()
                    jk3 = mycursor.rowcount
                    if jk3 == 0:
                        messagebox.showinfo("ERROR", "GIVE CORRECT ID")
                        mydb.commit()
                        mydb.close()
                        mycursor.close()
                        return
                    else:
                        dddd = jk2[0][0]
                        import datetime as dt
                        g = dt.datetime.now()
                        global hjk
                        ddd = "A student with admission number " + str(
                            adn) + " \nhas given a book with book number " + str(
                            bkn) + " \non " + str(g) + " \nin presence of librarian " + dddd + " \n"
                        hjk = Label(root, text=ddd, fg="#fff", bg="brown", font=("Helvetica", 11, "bold"))
                        hjk.pack()
                        if str(p.get()) == "YES":
                            import datetime
                            f = open("C:\library_management_prj\_records\_receiving_books_record.txt", "a")
                            dx = datetime.date.today()
                            f.write("\n")
                            f.write(str(dx))
                            f.write("\n")
                            f.write(ddd)
                            f.close()
                            messagebox.showinfo("........", "Report has been saved!!!")
                        elif str(p.get()) == "NO":
                            messagebox.showinfo("!!!!!!", "The report has not been saved !!!")
                        mycursor.execute("update book set  Availability='" + y + "' where Book_No=" + str(bkn) + "")
                        mycursor.execute("select Book_issued_on from student where admno=" + str(adn) + "")
                        xyz = mycursor.fetchall()
                        xyz1 = xyz[0][0]
                        mycursor.execute(
                            "update student set book_no=0, Book_issued_on=null,Book_Issued='NO' where admno=" + str(
                                adn) + "")
                        date = dt.datetime.now()
                        date1 = dt.datetime.strptime(xyz1, '%Y-%m-%d')
                        delta = date - date1
                        diff = int(delta.days)
                        diff1 = int(diff / 7)
                        money = 0
                        for i in range(diff1):
                            money += 10
                        if money != 0:
                            global xz
                            xz1 = "THE STUDENT HAS SUBMITTED THE BOOK BY " + str(
                                diff) + " DAYS\nSO HE/SHE HAS TO PAY A FINE OF RUPEES " + str(money) + ""
                            xz = Label(root, text=xz1, fg="#fff", font=("Helvetica", 13, "bold"), bg="brown")
                            xz.pack(pady=10, anchor="center")
                            f1 = open("C:\library_management_prj\_records\_fine_record.txt", "a")
                            f1.write("\n")
                            f1.write(str(date))
                            f1.write(" Rs " + str(money))
                            f1.write("\n")
                            f1.write(xz1)
                            f1.close()
                        messagebox.showinfo(":-)...:-)", "Book received......")
                else:
                    messagebox.showinfo("!!!!!!!!!", "STUDENT HAS NOT ISSUE THIS BOOK")
        mydb.commit()
        mycursor.close()
        mydb.close()

    root = Toplevel()
    root.title("RECEIVING BOOKS")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    l = Image.open("C:\library_management_prj\images\_rb.jpg")
    new = l.resize((1400, 800), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(x=0, y=0)
    Label(root, bg="#FEF6E3").pack(padx=0, pady=45, anchor="nw")
    Label(root, text="Enter the Book number       ", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDB75F").pack(padx=30, pady=5)
    e = Entry(root, textvariable=IntVar(), fg="black", bg="#FDB75F", font=("Helvetica", 10, "bold"))
    e.delete(0,END)
    e.pack(padx=70, pady=0, ipadx=30, ipady=3, anchor="center")
    Label(root, text="Enter the student admission number", fg="black", font=("Helvetica", 11, "bold"),
          bg="#FDB75F").pack(padx=30, pady=5)
    en = Entry(root, textvariable=IntVar(), fg="black", bg="#FDB75F", font=("Helvetica", 10, "bold"))
    en.delete(0,END)
    en.pack(padx=70, pady=0, ipadx=30, ipady=3)
    Label(root, text="Enter your ID(LIBRARIAN):-", fg="black", bg="#FDB75F",
          font=("Helvetica", 11, "bold")).pack(
        pady=5)
    adj1 = Entry(root, textvariable=IntVar(), fg="black", bg="#FDB75F", font=("Helvetica", 10, "bold"))
    adj1.delete(0,END)
    adj1.pack(padx=70, pady=0, ipadx=30, ipady=3)
    fj = Label(root, text="SELECT WHETHER TO SAVE REPORT OR NOT", fg="black", bg="#FDB75F",
               font=("Helvetica", 11, "bold"))
    fj.pack(pady=5)
    p = StringVar()
    jk = Radiobutton(root, text="YES", variable=p, value="YES")
    jk.configure(fg="black", font=("Helvetica", 11, "bold"), bg="#FDB75F")
    jk1 = Radiobutton(root, text="NO", variable=p, value="NO")
    jk1.configure(fg="black", font=("Helvetica", 11, "bold"), bg="#FDB75F")
    jk.pack(anchor="nw", padx=580)
    jk1.place(x=730, y=331)
    jk.deselect()
    jk1.deselect()
    bttn = Button(root, text="Press to load the the above data", command=receiving_books, fg="black",
                  font=("Helvetica", 11, "bold"), bg="#FDB75F")
    bttn.pack(padx=30, pady=10)
    root.bind('<Return>', receiving_books)
    qb = Button(root, text="             E x i t           ", command=quit, fg="black",
                font=("Helvetica", 13, "bold"), bg="red")
    qb.place(anchor="center", x=1210, y=220)
    ntm = Button(root, text="          C L E A R         ", command=clear, fg="black",
                 font=("Helvetica", 11, "bold"), bg="#FDB75F")
    ntm.configure(state=DISABLED)
    ntm.pack(pady=8, ipadx=30)
    root.mainloop()


def issbb():
    root = Toplevel()
    root.title("ISSUING BOOKS ")
    root.geometry("1350x700+0+0")
    tree = ttk.Treeview(root)
    l = Image.open("C:\library_management_prj\images\dispstud.jpg")
    new = l.resize((1400, 450), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.place(x=0, y=0)

    def quit():
        root.destroy()

    def update(event=None):
        tex.configure(state=DISABLED)
        ntm.configure(state=NORMAL)
        mydb = mycon.connect(host="localhost", user="root", password="root", database="library_management")
        mycursor = mydb.cursor()
        admno = int(adn.get())
        mycursor.execute("select Book_no from student where admno=" + str(admno))
        values = mycursor.fetchall()
        if values == []:
            messagebox.showinfo('ERROR', 'No such data in the Table')
            mydb.close()
            mycursor.close()
            return
        if not values[0][0] == 0:
            messagebox.showinfo('ERROR', 'Book already issued to the student. Instruct the student to submit the book')
            mydb.close()
            mycursor.close()
            return
        a = int(adj.get())
        mycursor.execute("select Availability from book where Book_No=" + str(a))
        records = mycursor.fetchall()
        if records == [] or records[0][0] == 'NO':
            messagebox.showinfo("ERROR", "No such Book available")
        else:
            fff = adj1.get()
            mycursor.execute("select Name from librarian where ID=" + str(fff) + "")
            dd = mycursor.fetchall()
            ddj = mycursor.rowcount
            if ddj == 0:
                messagebox.showinfo("ERROR", "GIVE CORRECT ID")
                mydb.commit()
                mydb.close()
                mycursor.close()
                return
            else:
                dddd = dd[0][0]
                import datetime as dt
                g = dt.datetime.now()
                global hjk
                ddd = "A student with admission number " + str(
                    admno) + " \nhas issued a book with book number " + str(
                    a) + " \non " + str(g) + " \nin presence of librarian " + dddd + " \n"
                hjk = Label(root, text=ddd, fg="#fff", bg="brown", font=("Helvetica", 11, "bold"))
                hjk.pack()
                if str(opp.get()) == "   Y E S   ":
                    import datetime
                    f = open("C:\library_management_prj\_records\issue_books_record.txt", "a")
                    dx = str(datetime.date.today())
                    f.write("\n")
                    f.write(dx)
                    f.write(" \n")
                    f.write(ddd)
                    f.close()
                    messagebox.showinfo("........", "Report has been saved!!!")
                elif str(opp.get()) == "   N O  ":
                    messagebox.showinfo("!!!!!!", "The report has not been saved !!!")
            global jj
            jj = Label(root, text="Book is issued successfully", bg="#fff", font=("Helvetica", 12, "bold"))
            jj.pack()
            sql = ("update book set Availability='NO' where book_no=" + str(a))
            mycursor.execute(sql)
            mycursor.execute("select date(now())")
            records = mycursor.fetchall()
            sql = ("update student set Book_No=" + str(a) + ", Book_issued_on='" + str(
                records[0][0]) + "', book_issued='YES' where admno=" + str(admno))
            mycursor.execute(sql)
            mycursor.execute("select * from book where Book_NO=" + str(a) + "")
            zz = mycursor.fetchall()
            i = 0
            for ro in zz:
                tree.insert('', i, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9]))
                i += 1
        mydb.commit()
        mydb.close()
        mycursor.close()

    def reset():
        for record in tree.get_children():
            tree.delete(record)
        ntm.configure(state=DISABLED)
        tex.configure(state=NORMAL)
        hjk.destroy()
        jj.destroy()
        adn.delete(0, END)
        adj.delete(0, END)
        adj1.delete(0, END)

    frame = LabelFrame(root, text="DATA", padx=5, pady=3, bg="#fff")
    frame.pack(padx=5, pady=4, anchor="nw", ipadx=120, ipady=20)
    Label(frame, text="ENTER YOUR ADMISSION NUMBER", fg="#fff", bg="brown", font=("Helvetica", 9, "bold")).pack(
        anchor="nw", padx=10, pady=5)
    adn = Entry(frame, textvariable=IntVar(), fg="#fff", bg="brown", font=("Helvetica", 9, "bold"))
    adn.delete(0,END)
    adn.pack(padx=25, anchor="nw", pady=3, ipady=2)
    Label(frame, text="ENTER THE BOOK NUMBER", fg="#fff", bg="brown", font=("Helvetica", 9, "bold")).place(
        anchor="nw", x=280, y=5)
    adj = Entry(frame, textvariable=IntVar(), fg="#fff", bg="brown", font=("Helvetica", 9, "bold"))
    adj.delete(0,END)
    adj.place(anchor="nw", x=280, y=37, height=23)
    Label(frame, text="Enter your ID(LIBRARIAN):-", fg="#fff", bg="brown", font=("Helvetica", 9, "bold")).pack(
        pady=3)
    adj1 = Entry(frame, textvariable=IntVar(), fg="#fff", bg="brown", font=("Helvetica", 9, "bold"))
    adj1.delete(0,END)
    adj1.pack(ipady=2)
    frame1 = LabelFrame(root, text="SELECT", bg="#fff")
    frame1.place(anchor="center", x=680, y=90, height=175, width=400)
    Label(frame1, text="Select whether you want to save the report or not", fg="#fff", bg="brown",
          font=("Helvetica", 11, "bold")).pack(ipadx=5, pady=2)
    con = {"   Y E S   ", "   N O  "}
    opp = StringVar()
    opp.set("SELECT")
    p = OptionMenu(frame1, opp, *con)
    p.config(bg="brown", fg="#fff", font=("Helvetica", 9, "bold"))
    p.pack(ipadx=10, pady=3)
    tex = Button(frame1, text="SELECT TO PROCEED", command=update, fg="#fff", bg="brown",
                 font=("Helvetica", 11, "bold"))
    tex.pack(pady=30)
    root.bind('<Return>', update)
    frame2 = LabelFrame(root, text="CLEAR/EXIT", bg="#fff")
    frame2.place(anchor="center", x=1080, y=90, height=175, width=400)
    ntm = Button(frame2, text="CLEAR", command=reset, font=("Helvetica", 11, "bold"), bg="red")
    ntm.configure(state=DISABLED)
    ntm.pack(anchor="nw", padx=10, pady=45, ipadx=50)
    qt = Button(frame2, text="     E X I T     ", command=quit, font=("Helvetica", 11, "bold"), bg="red")
    qt.place(anchor="ne", x=350, y=43, width=150)
    iss_frame=LabelFrame(root,bg="#fff")
    iss_frame.pack(side="bottom",pady=10)
    tree = ttk.Treeview(iss_frame)
    tree['show'] = 'headings'
    s = ttk.Style(iss_frame)
    s.theme_use("clam")
    s.configure(".", font=("Helvetica", 11))
    s.configure("Treeview.Heading", foreground="#fff", font=("Helvetica", 11, "bold"), background="blue")
    s.configure("Treeview", foreground="#fff", background="black", fieldbackground="black")
    tree['columns'] = (
        "Book_NO", "Book_Name", "Price", "Category", "Author_Name", "No_of_Pages", "Book_Language", "date_of_purchase",
        "print_date", "Availability")
    tree.column("Book_NO", width=150, minwidth=150, anchor=CENTER)
    tree.column("Book_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("Price", width=120, minwidth=120, anchor=CENTER)
    tree.column("Category", width=120, minwidth=120, anchor=CENTER)
    tree.column("Author_Name", width=120, minwidth=120, anchor=CENTER)
    tree.column("No_of_Pages", width=160, minwidth=150, anchor=CENTER)
    tree.column("Book_Language", width=150, minwidth=150, anchor=CENTER)
    tree.column("date_of_purchase", width=170, minwidth=170, anchor=CENTER)
    tree.column("print_date", width=120, minwidth=120, anchor=CENTER)
    tree.column("Availability", width=150, minwidth=150, anchor=CENTER)
    tree.heading("Book_NO", text="BOOK NUMBER", anchor=CENTER)
    tree.heading("Book_Name", text="BOOK NAME", anchor=CENTER)
    tree.heading("Price", text="PRICE", anchor=CENTER)
    tree.heading("Category", text="CATEGORY", anchor=CENTER)
    tree.heading("Author_Name", text="AUTHOR NAME", anchor=CENTER)
    tree.heading("No_of_Pages", text="NUMBER OF PAGES", anchor=CENTER)
    tree.heading("Book_Language", text="BOOK LANGUAGE", anchor=CENTER)
    tree.heading("date_of_purchase", text="DATE OF PURCHASE", anchor=CENTER)
    tree.heading("print_date", text="PRINT DATE", anchor=CENTER)
    tree.heading("Availability", text="AVAILABILITY", anchor=CENTER)
    hsb = ttk.Scrollbar(iss_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side="bottom")
    tree.pack(side="bottom")
    root.mainloop()


def countdown(t):
    for i in range(t):
        tt["text"] = t - 1
        root.update()
        time.sleep(1)
        t -= 1


def main():
    window = Tk()
    window.title("Library Management")
    h = str(int(window.winfo_screenheight()) - 60)
    w = str(window.winfo_screenwidth())
    window.geometry(w + "x" + h + "+0+0")
    window.minsize(int(w), int(h))
    window.resizable(1, 1)
    window.iconbitmap('C:\library_management_prj\images\ddd.ico')

    def close():
        window.destroy()

    l_im = Image.open("C:\library_management_prj\images\SmartLIB.png")
    new = l_im.resize((int(w), int(h)), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    my_lbl = Label(window, image=r)
    my_lbl.place(x=0, y=0)
    qe = Menubutton(window, text="Enter the program", padx=34, fg="#fff", bg="#e26e34", font=("helvetica", 13, "bold"),
                    relief="raised", borderwidth=4)
    qe.menu = Menu(qe)
    qe["menu"] = qe.menu
    qe.menu.add_command(label="STUDENT                       ")
    qe.menu.add_command(label="      i. ENTERING             ", command=ss)
    qe.menu.add_command(label="     ii. DISPLAYING           ", command=dispstud)
    qe.menu.add_command(label="    iii. UPDATING/DELETING    ", command=updstud)
    qe.menu.add_command(label="BOOK                          ")
    qe.menu.add_command(label="      i. ENTERING             ", command=bb)
    qe.menu.add_command(label="     ii. DISPLAYING           ", command=dispbook)
    qe.menu.add_command(label="    iii. UPDATING/DELETING    ", command=updbook)
    qe.menu.add_command(label="LIBRARIAN                     ")
    qe.menu.add_command(label="      i. ENTERING             ", command=librar)
    qe.menu.add_command(label="     ii. DISPLAYING           ", command=displibr)
    qe.menu.add_command(label="    iii. UPDATING/DELETING    ", command=updlibr)
    qe.menu.add_command(label="DATA                          ")
    qe.menu.add_command(label="       i. ISSUING BOOK        ", command=issbb)
    qe.menu.add_command(label="      ii. RECEIVING BOOK      ", command=rb)
    qe.menu.add_command(label="GRAPH                         ")
    qe.menu.add_command(label="       i. BOOK ISSUED         ", command=graph_iss)
    qe.menu.add_command(label="      ii. FINE                ", command=fine)
    qe.menu.configure(bg="#e26e34", font=("helvetica", 11, "italic", "bold"), fg="black")
    qe.place(x=(int(w)-550),y=(int(h)-380))
    qb = Button(window, text="Exit The Program", command=close, padx=32, fg="#fff", bg="#e26e34",
                font=("helvetica", 13, "bold"), relief="raised", borderwidth=4)
    qb.place(x=(int(w)-550),y=(int(h)-320))
    window.mainloop()


mydb = mycon.connect(host="localhost", user="root", password="root")
mycursor = mydb.cursor()
mycursor.execute("show databases like 'library_management%'")
a = mycursor.fetchall()
if mycursor.rowcount == 0:
    mycursor.execute("create database library_management")
    mycursor.execute("use library_management")
    mycursor.execute("CREATE TABLE `book` (`Book_NO` int(10) NOT NULL,`Book_Name` varchar(50) NOT NULL,"
                     "`Price` int(20) NOT NULL,`Category` varchar(40) NOT NULL,`Author_Name` varchar(40) NOT "
                     "NULL,`No_of_Pages` int(50) DEFAULT NULL,`Book_Language` varchar(50) NOT NULL,"
                     "`date_of_purchase` varchar(50) DEFAULT NULL,`print_date` varchar(50) DEFAULT NULL,"
                     "`Availability` varchar(5) DEFAULT NULL,PRIMARY KEY (`Book_NO`))")
    mycursor.execute("CREATE TABLE `librarian` (`ID` int(5) NOT NULL,`Name` varchar(40) NOT NULL,`Aadhaar_No` "
                     "varchar(20) NOT NULL,`Phone_No` varchar(12) NOT NULL,`Address` varchar(40) DEFAULT NULL,"
                     "`Email` varchar(40) DEFAULT NULL,`password` varchar(30) NOT NULL,`Security` varchar(50) NOT "
                     "NULL,PRIMARY KEY (`ID`),UNIQUE KEY `Aadhaar_No` (`Aadhaar_No`))")
    mycursor.execute("CREATE TABLE `student` (`ADMNO` int(5) NOT NULL,`Name` varchar(50) NOT NULL,`Class_Sec` "
                     "varchar(30) NOT NULL,`Roll_No` int(6) NOT NULL,`Address` varchar(40) NOT NULL,`Book_Issued` "
                     "varchar(10) DEFAULT NULL,`Phone` varchar(30) DEFAULT NULL,`Book_No` int(20) DEFAULT NULL,"
                     "`Book_issued_on` varchar(40) DEFAULT NULL,PRIMARY KEY (`ADMNO`))")
    if not os.path.exists("C:\library_management_prj\_records"):
        os.mkdir("C:\library_management_prj\_records")
        f = open("C:\library_management_prj\_records\issue_books_record.txt", 'w')
        f.close()
        f = open("C:\library_management_prj\_records\_receiving_books_record.txt", 'w')
        f.close()
        f = open("C:\library_management_prj\_records\_fine_record.txt", 'w')
        f.close()
    mydb.commit()
    messagebox.showinfo("WELCOME", "DATABASE HAS BEEN CREATED")
    messagebox.showinfo("----", "PLEASE ENTER A LIBRARIAN INFO")
    librar()
    main()
else:
    mycursor.execute("use library_management")
    ctr = 0
    n = 1
    ctr1 = 0
    n1 = 1


    def login(event=None):
        zz = str(un1.get())
        p = str(password.get())
        mycursor.execute("select password from librarian where id=" + str(zz) + "")
        fet = mycursor.fetchall()
        if mycursor.rowcount != 0:
            if fet[0][0] == p:
                messagebox.showinfo("-----", "WELCOME TO SmartLIB\nEDUCATE-CAPTIVATE-CONNECT")
                root.destroy()
                main()
            else:
                global ctr, n
                ctr += 1
                messagebox.showinfo("!!!!!!", "PLEASE ENTER CORRECT PASSWORD")
                if ctr == 5 * n:
                    messagebox.showinfo("!!!!!!", "YOU HAVE TRIED A WRONG PASSWORD FOR " + str(
                        ctr) + " TIMES...TRY AGAIN AFTER " + str(30 * n) + " SEC")
                    un1.configure(state=DISABLED)
                    password.configure(state=DISABLED)
                    countdown(30 * n)
                    un1.configure(state=NORMAL)
                    password.configure(state=NORMAL)
                    n += 1
        else:
            global ctr1, n1
            ctr1 += 1
            messagebox.showinfo("!!!!!", "WRONG USER ID")
            if ctr1 == 5 * n1:
                messagebox.showinfo("!!!!!!", "YOU HAVE TRIED A WRONG PASSWORD FOR " + str(
                    ctr1) + " TIMES...TRY AGAIN AFTER " + str(30 * n1) + " SEC")
                un1.configure(state=DISABLED)
                password.configure(state=DISABLED)
                countdown(30 * n1)
                un1.configure(state=NORMAL)
                password.configure(state=NORMAL)
                n1 += 1


    ctr2 = 0
    ctr3 = 0


    def forget_password():
        def run():
            mycursor.execute("select security from librarian where ID=" + str(ui1.get()) + "")
            dd = mycursor.fetchall()
            if mycursor.rowcount != 0:
                if dd[0][0] == str(ff1.get()):
                    global pa1
                    pa = Label(forget, text="ENTER YOUR NEW PASSWORD", fg="#fff", font=("Helvetica", 11, "bold"),
                               bg="black")
                    pa.pack(pady=15)
                    pa1 = Entry(forget, textvariable=StringVar(), fg="#fff", font=("Helvetica", 11, "bold"), bg="black",
                                insertbackground="#fff")
                    pa1.pack(pady=2)
                    set_bt = Button(forget, text="SET", command=new, fg="#fff", font=("Helvetica", 13, "bold"),
                                    bg="black")
                    set_bt.pack(pady=15)
                else:
                    global ctr2
                    messagebox.showinfo("!!!!!", "WRONG ANSWER")
                    ctr2 += 1
                    if ctr2 == 5:
                        messagebox.showinfo("!!!!",
                                            "YOU HAVE ALREADY TRIED FOR 5 TIMES\nPLEASE CONTACT YOUR SENIOR MANAGEMENT")
                        forget.destroy()
            else:
                global ctr3
                messagebox.showinfo("!!!!!", "INCORRECT ID")
                ctr3 += 1
                if ctr3 == 5:
                    messagebox.showinfo("!!!!",
                                        "YOU HAVE ALREADY TRIED FOR 5 TIMES\nPLEASE CONTACT YOUR SENIOR MANAGEMENT")
                    forget.destroy()

        def new():
            mycursor.execute("update librarian set password='" + str(pa1.get()) + "' where id=" + str(ui1.get()) + "")
            mydb.commit()
            forget.destroy()

        forget = Toplevel()
        forget.geometry("400x400")
        forget.title("FORGET PASSWORD")
        forget.resizable(0, 0)
        l1 = Image.open("C:\library_management_prj\images\hacker.jpg")
        new1 = l1.resize((400, 400), Image.ANTIALIAS)
        r1 = ImageTk.PhotoImage(new1)
        img1 = Label(forget, image=r1)
        img1.image = r1
        img1.place(relwidth=1, relheight=1)
        ui = Label(forget, text="ENTER YOUR USER ID", fg="#fff", font=("Helvetica", 11, "bold"), bg="black")
        ui.pack(pady=15)
        ui1 = Entry(forget, textvariable=IntVar(), fg="#fff", font=("Helvetica", 11, "bold"), bg="black",
                    insertbackground="#fff")
        ui1.delete(0,END)
        ui1.pack(pady=2)
        ff = Label(forget, text="ENTER YOUR FIRST INSTITUTION", fg="#fff", font=("Helvetica", 11, "bold"), bg="black")
        ff.pack(pady=15)
        ff1 = Entry(forget, textvariable=StringVar, fg="#fff", font=("Helvetica", 11, "bold"), bg="black",
                    insertbackground="#fff")
        ff1.pack(pady=2)
        ff2 = Button(forget, text="OK", command=run, fg="#fff", font=("Helvetica", 13, "bold"), bg="black")
        ff2.pack(pady=15)
        forget.mainloop()


    root = Tk()
    root.geometry("400x400+250+80")
    root.title("LOGIN")
    root.resizable(0, 0)
    l_im = Image.open("C:\library_management_prj\images\lock.jpg")
    new = l_im.resize((400, 400), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(new)
    img = Label(root, image=r)
    img.image = r
    img.place(relwidth=1, relheight=1)
    un = Label(root, text="Enter the user ID", fg="#fff", font=("Helvetica", 11, "bold"), bg="black")
    un.pack(pady=15)
    un1 = Entry(root, textvariable=IntVar(), fg="#fff", font=("Helvetica", 11, "bold"), bg="black",
                insertbackground="#fff")
    un1.delete(0,END)
    un1.pack(pady=5)
    pw = Label(root, text="Enter the password", fg="#fff", font=("Helvetica", 11, "bold"), bg="black")
    pw.pack(pady=10)
    password = Entry(root, textvariable=StringVar(), fg="#fff", font=("Helvetica", 11, "bold"), bg="black",
                     insertbackground="#fff")
    password.pack(pady=5)
    forget = Button(root, text="FORGOT PASSWORD", command=forget_password, fg="red", font=("Helvetica", 6, "bold"),
                    bg="black")
    forget.pack(anchor="e", padx=120)
    login1 = Button(root, text="LOGIN", command=login, fg="#fff", font=("Helvetica", 11, "bold"), bg="black")
    login1.pack(pady=10)
    root.bind('<Return>', login)
    tt = Label(root, text="00", fg="#fff", font=("Helvetica", 14, "bold"), bg="black")
    tt.place(x=300, y=133)
    root.mainloop()
mycursor.close()
mydb.close()
