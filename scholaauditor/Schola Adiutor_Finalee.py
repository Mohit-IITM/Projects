import random
import sqlite3 as sql
import matplotlib.pyplot as plt
import statistics as stat
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image
#from ttkthemes import themed_tk as tk
import urllib.request
import string
#import pygame
import time
import webbrowser
#pygame.mixer.init()
conn = sql.connect('Assistant.db')
c = conn.cursor()
c.execute(
    "CREATE TABLE IF NOT EXISTS teachers (tcode STRING,tname STRING,tsub STRING,password STRING,email_id STRING,phone_number INTEGER)")
c.execute(
    "CREATE TABLE IF NOT EXISTS classes (class STRING,teacher_1 STRING,teacher_2 STRING,teacher_3 STRING,teacher_4 STRING,teacher_5 STRING)")
quotes=[" Start where you are. Use what you have. Do what you can",
        " Don’t wish it were easier; wish you were better",
        " Push yourself, because no one else is going to do it for you",
        "Some people dream of accomplishing great things. Others stay awake and make it happen",
        "You don’t drown by falling in the water; you drown by staying there",
        "Education is not the filling of a pail, but the lighting of a fire",
        "Nothing is 100% parfait",
        "The strength of a chain is its weakest link",
        "An eye for eye only ends up making the whole world blind",
        "Do you even see these lines written here?"]
font1 = {'family':"Consolas", 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink','size':32}
font2 = {'family':'Consolas', 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink' ,'size':32}
font3 = {'family':'Consolas', 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink' ,'size':32}
font4 = {'family':'Consolas', 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink', 'size':32}
font5 = {'family':'Consolas', 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink', 'size':32}
font6 = {'family':'Consolas', 'color':'black', 'weight':'bold','style':'italic','backgroundcolor':'pink', 'size':32}

def home_t():

    root4 = Toplevel()
    root4.geometry("1920x1080")
    root4.title("Teacher Home Page")
    def stop():
        pygame.mixer.music.stop()
    #stop()
    home = ttk.Notebook(root4, width=1920, height=1080)
    home.pack()
    bgimage1= ImageTk.PhotoImage(Image.open("Student,Test Report3.jpg"))
    bgimage2 = ImageTk.PhotoImage(Image.open("Class Create Image.jpg"))
    bgimage3 =ImageTk.PhotoImage(Image.open("Input Marks Image2.jpg"))
    root8 = Canvas(home, width=1920, height=1080)
    root9 = Canvas(home, width=1920, height=1080)
    frame6 = Canvas(home, width=1920, height=1080)
    root7 = Canvas(home, width=1920, height=1080)
    root10 = Canvas(home, width=1920, height=1080)
    lab_1 = Label(root8, image=bgimage3)
    lab_2 = Label(root9, image=bgimage1)
    lab_3 = Label(frame6, image=bgimage2)
    lab_4 = Label(root7, image=bgimage1)
    lab_5 = Label(root10, image=bgimage1)
    lab_1.place(x=0, y=0, relwidth=1, relheight=1)
    lab_2.place(x=0, y=0, relwidth=1, relheight=1)
    lab_3.place(x=0, y=0, relwidth=1, relheight=1)
    lab_4.place(x=0, y=0, relwidth=1, relheight=1)
    lab_5.place(x=0, y=0, relwidth=1, relheight=1)

    def refresh():
        root4.destroy()
        home_t()

    def logout():
        root4.destroy()

    def inputmarks():
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            clock_lab.config(text=hour + ":" + minute + ":" + second)
            clock_lab.after(1000, clock)
        misc = Canvas(root8, width=100, height=50)
        misc.place(x=1280, y=0)
        marks = []
        a = c.execute("SELECT class FROM classes").fetchall()
        #print(a)
        click3 = StringVar()
        click3.set("Choose the class")
        text_font=('Consolas','12','bold')
        class_name_box = OptionMenu(root8, click3, *a)
        class_name_box.config(font=text_font,bg="#9FB6CD")
        class_name_box.grid(row=0, column=10)
        testid_lab = Label(root8, text="Enter the test id ", font="Consolas 12 bold",width=40,justify=LEFT,anchor="w",bg="#9FB6CD")
        testid = Entry(root8, width=30, font="Consolas 12 bold",bg="#C6E2FF")
        test_name_input = Entry(root8, width=30,font="Consolas 12 bold",bg="#C6E2FF")
        test_name_input_lab = Label(root8, text="Enter the name of the test ", font="Consolas 12 bold",width=40,anchor="w",bg="#9FB6CD")
        total_ent = Entry(root8, width=30, font="Consolas 12 bold",bg="#C6E2FF")
        total_ent_lab = Label(root8, text="Enter the total marks  ", font="Consolas 12 bold",width=40,anchor="w",bg="#9FB6CD")
        subject = Entry(root8, width=30, font="Consolas 12 bold",bg="#C6E2FF")
        subject_lab = Label(root8, text="Enter the name of the subject ", font="Consolas 12 bold",width=40,anchor="w",bg="#9FB6CD")
        testid.grid(row=1, column=10)
        test_name_input.grid(row=2, column=10)
        total_ent.grid(row=3, column=10)
        subject.grid(row=4, column=10)
        mark = Entry(root8, width=30, font="Consolas 12 bold",bg="#C6E2FF")
        mark_lab = Label(root8, text="Enter marks of students roll number wise", font="Consolas 12 bold",width=40,anchor="w",bg="#9FB6CD")
        testid_lab.grid(row=1, column=0)
        test_name_input_lab.grid(row=2, column=0)
        total_ent_lab.grid(row=3, column=0)
        subject_lab.grid(row=4, column=0)
        mark.grid(row=5, column=10)
        mark_lab.grid(row=5, column=0)
        ranks = []
        global count_1
        count_1=0

        def submit_4():
            dummy2 = mark.get()
            marks.append(dummy2)
            mark.delete(0, END)
            global count_1
            count_1=count_1+1
            #print(count_1)
            def continue_2():
                str2 = ''
                for i in click3.get():
                    if i.isalnum() == True:
                        str2 = str2 + i

                subname = str2 + "_" + subject.get() + "_marks"
                #print(subname)
                ranks1 = [1]
                subnamer = str2 + "_" + subject.get() + "_rank"
                c.execute("INSERT INTO {}  values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(subname), (
                    testid.get(), test_name_input.get(), total_ent.get(), marks[0], marks[1], marks[2], marks[3], marks[4],
                                    marks[5], marks[6], marks[7], marks[8], marks[9],
                                    marks[10], marks[11], marks[12], marks[13], marks[14],
                                    marks[15], marks[16], marks[17], marks[18], marks[19],
                                    marks[20], marks[21], marks[22], marks[23], marks[24],
                                    marks[25], marks[26], marks[27], marks[28], marks[29],
                                    marks[30], marks[31], marks[32], marks[33], marks[34],
                                    marks[35], marks[36], marks[37], marks[38], marks[39],
                                    marks[40], marks[41], marks[42], marks[43], marks[44],
                                    marks[45], marks[46], marks[47], marks[48], marks[49]))
                marks1 = []
                ranks2 = []
                ranks = []
                for i in marks:
                    marks1.append(i)
                marks1.sort()
                for a, b in zip(marks1, marks1[1:]):
                    ranks1.append(ranks1[-1] if a == b else len(ranks1) + 1)
                for i in marks:
                    for j in range(len(marks1)):
                        if marks1[j] == i:
                            ranks2.append(ranks1[j])
                for i in ranks2:
                    k = 51 - i
                    ranks.append(k)
                c.execute("INSERT INTO {}  values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(subnamer), (
                    testid.get(), test_name_input.get(), total_ent.get(), ranks[0], ranks[1], ranks[2], ranks[3], ranks[4],
                                    ranks[5], ranks[6], ranks[7], ranks[8], ranks[9],
                                    ranks[10], ranks[11], ranks[12], ranks[13], ranks[14],
                                    ranks[15], ranks[16], ranks[17], ranks[18], ranks[19],
                                    ranks[20], ranks[21], ranks[22], ranks[23], ranks[24],
                                    ranks[25], ranks[26], ranks[27], ranks[28], ranks[29],
                                    ranks[30], ranks[31], ranks[32], ranks[33], ranks[34],
                                    ranks[35], ranks[36], ranks[37], ranks[38], ranks[39],
                                    ranks[40], ranks[41], ranks[42], ranks[43], ranks[44],
                                    ranks[45], ranks[46], ranks[47], ranks[48], ranks[49]))
                conn.commit()
                k3 = StringVar()
                k3.set("You have successfully entered marks for test " + test_name_input.get())
                success_lab4 = Label(root8, textvariable=k3, font="Consolas 12 bold", bg="#00FF7F")
                success_lab4.grid(row=8, column=0)
            if count_1==50:
                continue_2_but = Button(root8, text="Continue", command=continue_2, font="Consolas 12 bold",bg="#9FB6CD")
                continue_2_but.grid(row=7, column=10)


        quotes_lab = Label(root8, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white", width=140)
        quotes_lab.place(x=0, y=650)
        refresh_but = Button(misc, text="Refresh", command=refresh, font="Consolas 12 bold", bg="lawngreen")
        refresh_but.pack()
        submit_4_but = Button(root8, text="Submit", command=submit_4, font="Consolas 12 bold",bg="#9FB6CD")
        submit_4_but.grid(row=6, column=10)
        clock_lab = Label(misc, text="", font="Consolas 12 bold")
        clock_lab.pack()
        clock()

        logout_but = Button(misc, text="Log Out", command=logout,font="Consolas 12 bold",bg="red")
        logout_but.pack()
    inputmarks()

    def class_create():
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            clock_lab.config(text=hour + ":" + minute + ":" + second)
            clock_lab.after(1000, clock)
        misc = Canvas(frame6, width=100, height=50)
        misc.place(x=1280, y=0)
        class_name_lab = Label(frame6, text="Enter class name(standard,section)", font="Consolas 12 bold",width=40,bg="#FFC1C1")
        class_name_lab.grid(row=2, column=0)
        class_name = Entry(frame6, font="Consolas 12 bold")
        class_name.grid(row=2, column=1)
        unique_id = []

        def submit_1():
            student_details = str(str(class_name.get())) + "_student_details"
            c.execute(
                '''CREATE TABLE {} (rollno INTEGER,name STRING,uniqueid STRING NOT NULL PRIMARY KEY,passsword)'''.format(
                    student_details))
            conn.commit()
            a = Entry(frame6, font="Consolas 12 bold")
            a_lab = Label(frame6, text="Enter student name :", font="Consolas 12 bold",width=40,bg="#FFC1C1")
            a_lab.grid(row=3, column=0)
            a.grid(row=3, column=1)
            b = Entry(frame6, font="Consolas 12 bold")
            b_lab = Label(frame6, text="Enter student roll number : ", font="Consolas 12 bold",width=40,bg="#FFC1C1")
            b_lab.grid(row=4, column=0)
            b.grid(row=4, column=1)
            warning_lab = Label(frame6,
                                text="Press submit after entering data of each student and continue after entering all students",
                                font="Consolas 12 bold",bg="#FFC1C1")
            warning_lab.grid(row=6, column=0)
            global click
            click=0

            def submit_2():
                student_details = str(str(class_name.get()) + "_student_details")
                unique = str(str(class_name.get()) + "_" + str(b.get()))
                unique_id.append(unique)
                alph_low = string.ascii_lowercase
                alph_up = string.ascii_uppercase
                password = random.choice(alph_up)
                for i in range(5):
                    password = password + random.choice(alph_low)
                password = password + str(random.randint(1000, 9999))
                c.execute("INSERT INTO {}  values(?,?,?,?)".format(student_details), (b.get(), a.get(), unique,password))
                conn.commit()
                a.delete(0, END)
                b.delete(0, END)
                global click
                click = click + 1
                if click == 50:
                    continue_cre_but = Button(frame6, text="Continue", command=continue_create, font="Consolas 12 bold",bg="#FFC1C1")
                    continue_cre_but.grid(row=6, column=1)

            def continue_create():
                def continue_4():
                    def temp(x):
                        for k in x:
                            r = str(class_name.get() + "_" + k)
                            #print(r)
                            rm=r+"_marks"
                            rr = str(r + "_rank")
                            c.execute(
                                "CREATE TABLE {} (test_id STRING NOT NULL,test_name STRING,total_marks INTEGER,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT)".format(
                                    rr, unique_id[0], unique_id[1], unique_id[2], unique_id[3], unique_id[4],
                                    unique_id[5], unique_id[6], unique_id[7], unique_id[8], unique_id[9],
                                    unique_id[10], unique_id[11], unique_id[12], unique_id[13], unique_id[14],
                                    unique_id[15], unique_id[16], unique_id[17], unique_id[18], unique_id[19],
                                    unique_id[20], unique_id[21], unique_id[22], unique_id[23], unique_id[24],
                                    unique_id[25], unique_id[26], unique_id[27], unique_id[28], unique_id[29],
                                    unique_id[30], unique_id[31], unique_id[32], unique_id[33], unique_id[34],
                                    unique_id[35], unique_id[36], unique_id[37], unique_id[38], unique_id[39],
                                    unique_id[40], unique_id[41], unique_id[42], unique_id[43], unique_id[44],
                                    unique_id[45], unique_id[46], unique_id[47], unique_id[48], unique_id[49]))
                            c.execute(
                                "CREATE TABLE {} (test_id STRING NOT NULL,test_name STRING,total_marks INTEGER,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT)".format(
                                    rm
                                    , unique_id[0], unique_id[1], unique_id[2], unique_id[3], unique_id[4],
                                    unique_id[5], unique_id[6], unique_id[7], unique_id[8], unique_id[9],
                                    unique_id[10], unique_id[11], unique_id[12], unique_id[13], unique_id[14],
                                    unique_id[15], unique_id[16], unique_id[17], unique_id[18], unique_id[19],
                                    unique_id[20], unique_id[21], unique_id[22], unique_id[23], unique_id[24],
                                    unique_id[25], unique_id[26], unique_id[27], unique_id[28], unique_id[29],
                                    unique_id[30], unique_id[31], unique_id[32], unique_id[33], unique_id[34],
                                    unique_id[35], unique_id[36], unique_id[37], unique_id[38], unique_id[39],
                                    unique_id[40], unique_id[41], unique_id[42], unique_id[43], unique_id[44],
                                    unique_id[45], unique_id[46], unique_id[47], unique_id[48], unique_id[49]))
                    #Under construction
                    def junk():
                        """def temp5():
                            response = "y"
                            tcode = []
                            i = 0
                            while response == "y":
                                subnamei_lab = Label(frame6, text="Kindly enter the name of the subject without spaces")
                                subnamei = Entry(frame6)
                                subnamei_lab.grid(row=12, column=2)
                                subnamei.grid(row=12, column=3)
                                k = StringVar()

                                def submit_3():
                                    k.set(str("Enter the code of the teacher who handles " + subnamei.get()))
                                    tcodex_lab2 = Label(frame6, textvariable=k)
                                    tcodex_lab2.grid(row=13, column=2)
                                    tcodex.grid(row=13, column=4)
                                    tcodex = Entry(frame6)
                                    tcode.append(tcodex.get())
                                    subnamef = class_name + "_" + subnamei.get()
                                    subnamefr = subname + "_rank"
                                    c.execute('''CREATE TABLE {} (test_id STRING NOT NULL,test_name STRING,total_marks INTEGER,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,
                                                            {} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,
                                                            {} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT)'''.format(subnamef,
                                                                                                           unique_id[0],
                                                                                                           unique_id[1],
                                                                                                           unique_id[2],
                                                                                                           unique_id[3],
                                                                                                           unique_id[4],
                                                                                                           unique_id[5],
                                                                                                           unique_id[6],
                                                                                                           unique_id[7],
                                                                                                           unique_id[8],
                                                                                                           unique_id[9],
                                                                                                           unique_id[10],
                                                                                                           unique_id[11],
                                                                                                           unique_id[12],
                                                                                                           unique_id[13],
                                                                                                           unique_id[14],
                                                                                                           unique_id[15],
                                                                                                           unique_id[16],
                                                                                                           unique_id[17],
                                                                                                           unique_id[18],
                                                                                                           unique_id[19]))
                                    c.execute('''CREATE TABLE {} (test_id STRING NOT NULL,test_name STRING,total_marks INTEGER,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,
                                                                            {} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT,
                                                                            {} FLOAT,{} FLOAT,{} FLOAT,{} FLOAT)'''.format(
                                        subnamefr,
                                        unique_id[0],
                                        unique_id[1],
                                        unique_id[2],
                                        unique_id[3],
                                        unique_id[4],
                                        unique_id[5],
                                        unique_id[6],
                                        unique_id[7],
                                        unique_id[8],
                                        unique_id[9],
                                        unique_id[10],
                                        unique_id[11],
                                        unique_id[12],
                                        unique_id[13],
                                        unique_id[14],
                                        unique_id[15],
                                        unique_id[16],
                                        unique_id[17],
                                        unique_id[18],
                                        unique_id[19]))
                                    conn.commit()
                                    response_lab = Label(frame6, text="Do you want to add more subjects ?")

                                    def yes():
                                        response = y

                                    def no():
                                        response = n

                                    response_yes = Button(frame6, text="YES", command=yes())
                                    response_no = Button(frame6, text="NO", command=no())
                                    response_lab.grid(row=14, column=2)
                                    response_yes.grid(row=14, column=4)
                                    response_no.grid(row=14, column=6)

                            c.execute("INSERT INTO classes values(?,?,?,?,?,?,)",
                                      (class_name.get(), tcode[0], tcode[1], tcode[2], tcode[3], tcode[4]))
                            conn.commit()"""

                    x = click.get()
                    #print(x)
                    x1 = list(x.split())
                    x2 = []
                    for i in x1:
                        str1 = ''
                        for j in i:
                            if j.isalpha() == True:
                                str1 = str1 + j
                        x2.append(str1)
                    print(x2)
                    temp(x2)
                    tcode = []
                    k4 = StringVar()
                    k4.set("Enter the code of teacher in this order" + str(click.get()))
                    tcodex_lab2 = Label(frame6, textvariable=k4, font="Consolas 12 bold",bg="#FF8C69")
                    tcodex_lab2.grid(row=10, column=0)
                    tcodex = Entry(frame6, font="Consolas 12 bold",bg="#FFC1C1")
                    tcodex.grid(row=11, column=0)
                    def submit_4():
                        tcode.append(tcodex.get())
                        tcodex.delete(0, END)


                    def continue_3():
                        c.execute("INSERT INTO classes values(?,?,?,?,?,?)",
                                  (class_name.get(), tcode[0], tcode[1], tcode[2], tcode[3], tcode[4]))
                        sucess_lab = Label(frame6, text="You have sucessfully created class", font="Consolas 12 bold",bg="#00FF7F")
                        sucess_lab.grid(row=14, column=0)
                        conn.commit()

                    submit_but_4 = Button(frame6, text="Submit", command=submit_4, font="Consolas 12 bold",bg="#FF8C69")
                    continue_but_3 = Button(frame6, text="Continue", command=continue_3, font="Consolas 12 bold",bg="#FF8C69")
                    submit_but_4.grid(row=12, column=0)
                    continue_but_3.grid(row=13, column=0)

                select_lab = Label(frame6, text="Select your class structure", font="Consolas 12 bold",bg="#FFC1C1")
                select_lab.grid(row=8, column=0)
                click = StringVar()
                click.set("None")
                L1 = ['Physics', 'Chemistry', 'Maths', 'Computer', 'English']
                L2 = ['Science', 'Social', 'Maths', 'English', 'Language']
                L3 = ['Physics', 'Chemistry', 'Maths', 'Biology', 'English']
                L4 = ['Accountancy', 'BusinessStudies', 'Economics', 'English', 'Maths']
                L5 = ['Custom']
                L = [L1, L2, L3, L4, L5]
                options_box = OptionMenu(frame6, click, *L)
                options_box.configure(font="Consolas 12 bold",bg="yellow")
                options_box.grid(row=8, column=1)
                continue_4_but = Button(frame6, text="Continue", command=continue_4, font="Consolas 12 bold",bg="#FFC1C1")
                continue_4_but.grid(row=8, column=2)

            submit_but2 = Button(frame6, text="Submit", command=submit_2, font="Consolas 12 bold",bg="#FFC1C1")
            submit_but2.grid(row=5, column=1)


        submit_but = Button(frame6, text="Submit", command=submit_1, font="Consolas 12 bold",bg="#FFC1C1")
        submit_but.grid(row=2, column=2)
        quotes_lab = Label(frame6, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white", width=140)
        quotes_lab.place(x=0, y=650)

        def logout():
            root4.destroy()

        clock_lab = Label(misc, text="", font="Consolas 12 bold")
        clock_lab.pack()
        clock()
        logout_but = Button(misc, text="Log Out", command=logout,font="Consolas 12 bold",bg="red")
        logout_but.pack()


    class_create()
    frame6.pack(fill="both", expand=4)

    def onetest():
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            clock_lab.config(text=hour + ":" + minute + ":" + second)
            clock_lab.after(1000, clock)
        misc = Canvas(root7, width=100, height=50)
        misc.place(x=1280, y=0)
        list2 = []
        click1 = StringVar()
        click1.set("Choose the subject")
        Lsubj = c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'").fetchall()
        Lsubj1 = []
        Lsubj2 = []
        for i in Lsubj:
            Lsubj1.append(i[0])
        for i in Lsubj1:
            
            if i.find("marks") != -1:
                Lsubj2.append(i)
        subject_data_box = OptionMenu(root7, click1, *Lsubj2)
        subject_data_box.config(font="Consolas 12 bold",bg="#EEEE00")
        subject_data_box.grid(row=0, column=0)

        def submit_5():
            tabname = click1.get()
            #print(tabname)
            tabname1 = ""
            for i in tabname:
                if i.isalnum() == True:
                    tabname1 = tabname1 + i
                elif i == "_":
                    tabname1 = tabname1 + i
            #print(tabname1)
            tname = c.execute("SELECT test_name FROM {}".format(tabname1)).fetchall()
            testnames = []
            for testname in tname:
                testname1 = testname[0]
                testnames.append(testname1)
            click2 = StringVar()
            click2.set("Choose the test name")
            testname_box = OptionMenu(root7, click2, *testnames)
            testname_box.configure(font="Consolas 12 bold",bg="#EEEE00")

            testname_box.grid(row=1, column=0)

            def submit_6():
                #print(click2.get())
                list5 = c.execute("SELECT * FROM {} WHERE test_name='{}'".format(tabname1, click2.get())).fetchall()
                list1 = list(list5[0])
                class_name = ""
                for i in tabname1:
                    if i == "_":
                        break
                    else:
                        class_name = class_name + i
                #print(class_name)
                details_data = class_name + "_student_details"
                list6 = c.execute("SELECT name FROM {}".format(details_data)).fetchall()
                choice = "A"
                for a in list6:
                    d = str(a[0])
                    list2.append(d)
                marks = list1[3::]
                #print(marks)
                absentees = []
                markspresent = marks
                roll = [x for x in range(1, len(marks) + 1)]
                for i in range(len(marks)):
                    if marks[i] == 'A':
                        marks[i] = 0
                        absentees.append(list2[i])

                totalmark = list1[2]

                # percentage marks
                markpercentage = []

                for i in range(len(marks)):
                    k = (int(marks[i]) / totalmark) * 100
                    markpercentage.append(k)

                # average
                sum = 0

                for i in range(len(marks)):
                    sum += marks[i]
                average = sum / (len(marks) - len(absentees))
                k1 = StringVar()
                k1.set(str(list1[0]))
                k2 = StringVar()
                k2.set(str(list1[1]))
                k3 = StringVar()
                k3.set(str("No. present" + str(len(marks) - len(absentees))))
                k4 = StringVar()
                k4.set(str("No. absent" + str(len(absentees))))
                k5 = StringVar()
                k5.set(str("Average marks" + str(average)))
                k1_lab = Label(root7, textvariable=k1, font="Consolas 12 bold",width=15,bg="#00FFFF")
                k2_lab = Label(root7, textvariable=k2, font="Consolas 12 bold",width=15,bg="#00FFFF")
                k3_lab = Label(root7, textvariable=k3, font="Consolas 12 bold",width=25,bg="#FF8000")
                k4_lab = Label(root7, textvariable=k4, font="Consolas 12 bold",width=25,bg="#FF8000")
                k5_lab = Label(root7, textvariable=k5, font="Consolas 12 bold",width=25,bg="#FF8000")
                k1_lab.grid(row=2, column=0)
                k2_lab.grid(row=3, column=0)
                k3_lab.grid(row=4, column=0)
                k4_lab.grid(row=5, column=0)
                k5_lab.grid(row=6, column=0)

                # students sorting
                above_average = []
                below_average = []
                for i in range(len(marks)):
                    if marks[i] >= average:
                        above_average.append(list2[i])
                    elif 0 <= marks[i] < average:
                        below_average.append(list2[i])
                k6 = StringVar()
                k6.set("ABOVE AVERAGE" + str(above_average))
                k7 = StringVar()
                k7.set("BELOW AVERAGE" + str(below_average))
                averagea_lab = Label(root7, textvariable=k6, font="Consolas 12 bold",bg="black",fg="white")
                averageb_lab = Label(root7, textvariable=k7, font="Consolas 12 bold",bg="black",fg="white")
                averagea_lab.grid(row=7, column=0)
                averageb_lab.grid(row=8, column=0)


                k = list(marks)
                f = list(roll)

                g = list(list2)
                for i in range(1, len(k)):
                    key = k[i]
                    l = f[i]
                    cat = g[i]
                    j = i - 1
                    while j >= 0 and key > k[j]:
                        k[j + 1] = k[j]
                        f[j + 1] = f[j]
                        g[j + 1] = g[j]
                        j -= 1
                    k[j + 1] = key
                    f[j + 1] = l
                    g[j + 1] = cat

                rankwisemarks = k
                rankwisenames = g
                rankwiseroll = f

                p = [('NAME', 'ROLL NO.', 'MARKS', 'RANK')]

                class Table:
                    def __init__(self, root):
                        for i in range(total_rows):
                            for j in range(total_columns):
                                self.e = Entry(root, width=20, fg='blue', font='Consolas 16 bold')

                                self.e.grid(row=i, column=j)
                                self.e.insert(END, p[i][j])

                for i in range(len(f)):
                    p.append((g[i], f[i], k[i], i + 1))

                total_rows = len(p)
                total_columns = len(p[0])

                # create root window
                root = Tk()
                root.title("Table")
                t = Table(root)

                def graph_1():
                    # line graphs
                    plt.style.use('bmh')
                    plt.plot(list2, marks, 'b-',linewidth=5)
                    plt.plot(list2, marks, "r*")
                    plt.xlabel("STUDENTS")
                    plt.ylabel("MARKS")
                    plt.xticks(rotation=90)
                    plt.title(list1[1], fontdict=font1)
                    plt.show()

                def graph_2():
                    plt.style.use('bmh')
                    plt.plot(list2, markpercentage, 'b-',linewidth=5)
                    plt.plot(list2,markpercentage,"y*")
                    plt.xlabel("STUDENTS")
                    plt.ylabel("% MARKS")
                    plt.xticks(rotation=90)
                    plt.title(list1[1], fontdict=font4)
                    plt.show()

                def graph_3():
                    # bar graph
                    plt.style.use('bmh')
                    plt.bar(list2, marks)
                    plt.xlabel("STUDENTS")
                    plt.ylabel("MARKS")
                    plt.xticks(rotation=90)
                    plt.title(list1[1], fontdict=font5)
                    plt.show()

                def graph_4():
                    # pie chart
                    plt.style.use('bmh')
                    plt.pie([len(above_average), len(below_average), len(absentees)],
                            labels=['ABOVE AVERAGE', 'BELOW AVERAGE', 'ABSENTEES'], explode=(0, 0, 0.3),
                            shadow=True,
                            autopct='%1.1f%%')
                    plt.show()

                graph_but_1 = Button(root7, text="Marks-Line", command=graph_1, font="Consolas 12 bold",bg="#00FFFF")
                graph_but_1.grid(row=9, column=0)
                graph_but_2 = Button(root7, text="Marks Percentage", command=graph_2, font="Consolas 12 bold",bg="#00FFFF")
                graph_but_2.grid(row=10, column=0)
                graph_but_3 = Button(root7, text="Marks-Bar", command=graph_3, font="Consolas 12 bold",bg="#00FFFF")
                graph_but_3.grid(row=11, column=0)
                graph_but_4 = Button(root7, text="Average Composition", command=graph_4, font="Consolas 12 bold",bg="#00FFFF")
                graph_but_4.grid(row=12, column=0)
                root.mainloop()

            submit_6_but = Button(root7, text="Continue", command=submit_6, font="Consolas 12 bold",bg="#00FFFF")
            submit_6_but.grid(row=1, column=1)

        def logout():
            root4.destroy()

        clock_lab = Label(misc, text="", font="Consolas 12 bold")
        clock_lab.pack()
        clock()
        logout_but = Button(misc, text="Log Out", command=logout,font="Consolas 12 bold",bg="red")
        logout_but.pack()
        refresh_but = Button(misc, text="Refresh", command=refresh, font="Consolas 12 bold", bg="lawngreen")
        refresh_but.pack()
        quotes_lab = Label(root7, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white", width=140)
        quotes_lab.place(x=0, y=650)
        submit_5_but = Button(root7, text="Continue", command=submit_5, font="Consolas 12 bold",bg="#00FFFF")
        submit_5_but.grid(row=0, column=1)

    onetest()

    def onestudent():
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            clock_lab.config(text=hour + ":" + minute + ":" + second)
            clock_lab.after(1000, clock)
        misc = Canvas(root9, width=100, height=50)
        misc.place(x=1280, y=0)

        click5 = StringVar()
        click6 = StringVar()
        a = c.execute("SELECT class FROM classes").fetchall()
        b = []
        d=[]
        for i in a:
            d.append(i[0])
        for i in range(0, 50):
            b.append(i + 1)
        click5.set("Choose Class")
        click6.set("Choose Roll Number")
        class_name_box = OptionMenu(root9, click5, *d)
        class_name_box.config(font="Consolas 12 bold",bg="#EEEE00")
        roll_no_box = OptionMenu(root9, click6, *b)
        roll_no_box.config(font="Consolas 12 bold ",bg="#EEEE00")
        class_name_box.grid(row=0, column=0)
        roll_no_box.grid(row=1, column=0)

        def submit_7():
            class_name_data = click5.get()
            roll_no_data = click6.get()
            #print(class_name_data)
            #print(roll_no_data)
            unique_data = class_name_data + "_" + roll_no_data
            blah = class_name_data + "_student_details"
            student_name = c.execute("SELECT name FROM {} WHERE rollno={} ".format(blah, click6.get())).fetchall()
            list3 = []
            list5 = []
            list6 = []
            list7 = []
            click7 = StringVar()
            click7.set("Choose Subject")
            Lsubj = c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'").fetchall()
            #print(Lsubj)
            Lsubj1 = []
            Lsubj2 = []
            for i in Lsubj:
                Lsubj1.append(i[0])
            #print(Lsubj1)
            #print(click5.get())
            for i in Lsubj1:
                if i.find(click5.get() + "_") != -1 and i.find("marks") != -1:
                    Lsubj2.append(i)
            #print(Lsubj2)
            subject_data_box = OptionMenu(root9, click7, *Lsubj2)
            subject_data_box.config(font="Consolas 12 bold",bg="#EEEE00")
            subject_data_box.grid(row=2, column=0)

            def submit_8():
                tabname = ''
                for i in range(len(click7.get())):
                    if click7.get()[i].isalnum() == True:
                        tabname += click7.get()[i]
                    elif click7.get()[i] == "_":
                        tabname += click7.get()[i]
                #print(tabname)
                for name in c.execute("SELECT test_name FROM {}".format(tabname)).fetchall():
                    name1 = str(name[0])
                    list3.append(name1)
                    list7.append(name1)
                list4 = (c.execute("SELECT {} FROM {}".format(unique_data, tabname)).fetchall())
                list5=(c.execute("SELECT total_marks FROM {}".format(tabname)).fetchall())
                tabname_1=tabname[:-6]
                tabnamer=tabname_1 +"_rank"
                list6=(c.execute("SELECT {} FROM {}".format(unique_data, tabnamer)).fetchall())
                #print(list6)
                #print(list3)
                k8 = StringVar()
                k8.set(str("Name:" + student_name[0][0]))
                name_lab = Label(root9, textvariable=k8, font="Consolas 12 bold",bg="#DDA0DD")
                name_lab.grid(row=3, column=0)
                tests_attended = []
                tests_absent = []
                k9 = StringVar()
                k9.set(str("Total no. of tests" + str(len(list5))))
                tests_lab = Label(root9, textvariable=k9, font="Consolas 12 bold",bg="#DDA0DD")
                tests_lab.grid(row=3, column=2)
                for i in range(len(list4)):
                    if list4[i] == 'A':
                        list4[i] = 0
                        tests_absent.append(list3[i])
                    else:
                        tests_attended.append(list3[i])
                k10 = StringVar()
                k11 = StringVar()
                k10.set("No. of tests absent" + str(len(tests_absent)))
                k11.set("Tests absent:" + str(tests_absent))
                no_absent_lab = Label(root9, textvariable=k10, font="Consolas 12 bold",bg="#DDA0DD")
                test_absent_lab = Label(root9, textvariable=k11, font="Consolas 12 bold",bg="#DDA0DD")
                no_absent_lab.grid(row=3, column=4)
                test_absent_lab.grid(row=3, column=6)

                # average rank
                sum1 = 0
                for i in range(len(list6)):
                    sum1 += list6[i][0]
                averagerank = sum1 / len(list6)

                # percentage marks
                marks_percentage = []
                #print(list5)
                for i in range(len(list4)):
                    #print(list5[i][0])
                    #print(list4[i][0])
                    k = (list4[i][0] / list5[i][0]) * 100
                    marks_percentage.append(k)

                # variance(%marks)
                variance = stat.variance(marks_percentage)
                k12 = StringVar()
                k12.set("Variance" + "=" + str(variance))
                variance_lab = Label(root9, textvariable=k12,font="Consolas 12 bold",bg="#DDA0DD")
                variance_def_lab = Label(root9, text="This tells about the consistency of a student",font="Consolas 12 bold",bg="#DDA0DD")
                variance_lab.grid(row=5, column=2)
                variance_def_lab.grid(row=5, column=0)

                def graph_5():
                    plt.style.use("dark_background")
                    plt.plot(list3, list6, linestyle='solid', color='cyan')
                    plt.plot(list3, list6, 'ro')
                    plt.xlabel("TESTS")
                    plt.ylabel("RANK")
                    plt.xticks(rotation=45)
                    plt.title("RANK GRAPH", fontdict=font6)
                    plt.show()

                def graph_6():
                    plt.style.use("dark_background")
                    plt.bar(list3, marks_percentage, color='pink')
                    plt.xlabel("TESTS")
                    plt.ylabel("% MARKS")
                    plt.xticks(rotation=45)
                    plt.title("% MARK GRAPH", fontdict=font3)
                    plt.show()

                graph_5_but = Button(root9, text="Graph", command=graph_5, font="Consolas 12 bold",bg="#91FBCD")
                graph_6_but = Button(root9, text="Graph", command=graph_6, font="Consolas 12 bold",bg="#91FBCD")
                graph_5_but.grid(row=6, column=0)
                graph_6_but.grid(row=6, column=2)

            submit_8_but = Button(root9, text="Continue", command=submit_8, font="Consolas 12 bold",bg="#91FBCD")
            submit_8_but.grid(row=2, column=1)

        quotes_lab = Label(root9, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white", width=140)
        quotes_lab.place(x=0, y=650)
        submit_7_but = Button(root9, text="Continue", command=submit_7, font="Consolas 12 bold",bg="#91FBCD")
        submit_7_but.grid(row=1, column=6)
        clock_lab = Label(misc, text="", font="Consolas 12 bold")
        clock_lab.pack()
        clock()
        refresh_but = Button(misc, text="Refresh", command=refresh, font="Consolas 12 bold", bg="lawngreen")
        refresh_but.pack()
        logout_but = Button(misc, text="Log Out", command=logout, font="Consolas 12 bold",bg="red")
        logout_but.pack()


    onestudent()

    def testcomp():
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            clock_lab.config(text=hour + ":" + minute + ":" + second)
            clock_lab.after(1000, clock)
        misc = Canvas(root10, width=100, height=50)
        misc.place(x=1280, y=0)
        click8 = StringVar()
        click8.set("Choose Class")
        a = c.execute("SELECT class FROM classes").fetchall()
        a1 = []
        for i in a:
            a1.append(i[0])
        class_name_box = OptionMenu(root10, click8, *a1)
        class_name_box.config(font="Consolas 12 bold",bg="#FFFF00")
        class_name_box.grid(row=0, column=0)
        def submit_13():
            Lsubj = c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'").fetchall()
            #print(Lsubj)
            Lsubj1 = []
            Lsubj2=[]
            for i in Lsubj:
                Lsubj1.append(i[0])
            for i in Lsubj1:
                if i.find(click8.get()+"_")!=-1 and i.find("marks")!=-1:
                    Lsubj2.append(i)
            click9 = StringVar()
            click9.set("Choose Subject")
            subject_data_box = OptionMenu(root10, click9, *Lsubj2)
            subject_data_box.config(font="Consolas 12 bold", bg="#FFFF00")
            subject_data_box.grid(row=1, column=0)

            def submit_9():
                bleh = click8.get() + "_student_details"
                var = IntVar()
                a = c.execute("SELECT test_name FROM {} ".format(click9.get())).fetchall()
                a2 = []
                click10 = StringVar()
                click10.set("Choose the test names ")
                for i in a:
                    a2.append(i[0])
                test_name_box = OptionMenu(root10, click10, *a2)
                test_name_box.config(font="Consolas 12 bold",bg="yellow")
                test_name_box.grid(row=2, column=0)
                l1 = []
                l2 = []
                l3 = []
                l5 = []
                l25 = c.execute("SELECT name FROM {}".format(bleh)).fetchall()
                for i in l25:
                    l5.append(i[0])

                def submit_10():
                    l1.append(click10.get())

                submit_10_but = Button(root10, text="Submit", command=submit_10, font="Consolas 12 bold", bg="aqua")
                submit_10_but.grid(row=2, column=1)

                def submit_11():
                    abscnt = []
                    for i in l1:
                        # l[i]
                        list1 = c.execute('SELECT * FROM {} WHERE test_name=?'.format(click9.get()), (i,)).fetchall()
                        list2 = list(list1[0])
                        count = 0
                        for j in range(len(list2[3::])):
                            if list2[3::][j] == 'A':
                                list2[3::].pop(j)
                                count += 1
                        abscnt.append(count)
                        l2.append(list2[3::])
                        l3.append(list2[2])
                    #print(l2)
                    l4 = []  # average percentage
                    l6 = []  # average
                    l7 = []  # below average count
                    for i in range(len(l2)):
                        sum = 0
                        for j in l2[i]:
                            sum += j
                        pavg = (sum / (20 * l3[i])) * 100
                        pavg1 = sum / 20

                        l6.append(pavg1)
                        l4.append(pavg)
                    for i in range(len(l2)):
                        count1 = 0
                        for j in l2[i]:
                            if j < l6[i]:
                                count1 += 1
                            l7.append(count1)

                        def average():
                            plt.plot(l1, l4, linestyle='solid', color='lime', marker='o')
                            plt.xlabel('TESTS')
                            plt.xticks(rotation=45)
                            plt.ylabel('AVERAGE')
                            plt.title('AVERAGE COMPARISON', fontdict=font4)
                            plt.show()
                            colors1 = ['cyan', 'coral', 'goldenrod', 'lime', 'plum', 'pink']

                        def student():
                            plt.style.use('dark_background')
                            #print(l2)
                            #print(l5)
                            colors1 = ['cyan', 'coral', 'goldenrod', 'lime', 'plum', 'pink']
                            for i in range(len(l1)):
                                x = l1[i]
                                plt.plot(l5, l2[i], color=colors1[i], label=l1[i], marker='o')
                            plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, title='TESTS')
                            plt.title('STUDENT COMPARISON', fontdict=font1)
                            plt.xlabel('STUDENT')
                            plt.xticks(rotation=90)
                            plt.ylabel('MARKS')
                            plt.show()

                        average_but = Button(root10, text="Graphs", command=average, font="Consolas 12 bold", bg="aqua")
                        average_but.grid(row=3, column=0)
                        student_but = Button(root10, text="Graphs", command=student, font="Consolas 12 bold", bg="aqua")
                        student_but.grid(row=3, column=2)

                        # Table
                        class Table:
                            def __init__(self, root):
                                for i in range(total_rows):
                                    for j in range(total_columns):
                                        self.e = Entry(root, width=20, fg='black', font='Consolas 12 bold')
                                        self.e.grid(row=i, column=j)
                                        self.e.insert(END, p[i][j])

                        p = [('TEST NAME', 'AVERAGE', 'TOTALMARK', 'NO.PRESENT', 'BELOWAVG')]
                        #print(l1, l6, l3, l7)
                        for i in range(len(l1)):
                            p.append((l1[i], l6[i], l3[i], len(l2[i]), l7[i]))

                        total_rows = len(p)
                        total_columns = len(p[0])
                        # Create root window
                        root = Tk()
                        root.title("Table")
                        t = Table(root)
                        root.mainloop()

                submit_11_but = Button(root10, text="Continue", command=submit_11, font="Consolas 12 bold", bg="aqua")
                submit_11_but.grid(row=2, column=2)
            submit_9_but = Button(root10, text="Continue", command=submit_9, font="Consolas 12 bold", bg="aqua")
            submit_9_but.grid(row=1, column=1)

        clock_lab = Label(misc, text="", font="Consolas 12 bold")
        clock_lab.pack()
        clock()
        refresh_but = Button(misc, text="Refresh", command=refresh, font="Consolas 12 bold", bg="lawngreen")
        refresh_but.pack()
        logout_but = Button(misc, text="Log Out", command=logout, font="Consolas 12 bold",bg="red")
        logout_but.pack()
        submit_13_but=Button(root10,text="Proceed",command=submit_13,font="Consolas 12 bold",bg="aqua")
        submit_13_but.grid(row=0,column=1)
        quotes_lab = Label(root10, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white", width=140)
        quotes_lab.place(x=0, y=650)


    testcomp()
    root7.pack(fill="both", expand=1)
    root8.pack(fill="both", expand=1)
    root9.pack(fill="both", expand=1)
    home.add(frame6, text="Create a class")
    home.add(root8, text="Input Marks")
    home.add(root7, text="Test Report")
    home.add(root9, text="Student Report")
    home.add(root10, text="Test Comparison")
    root4.mainloop()

def sign_in_t():
    root2 = Toplevel()
    root2.geometry("1920x1080")
    root2.title("Sign In Page-Teacher")
    bgimage = ImageTk.PhotoImage(Image.open("Sign In Image6.jpg"))
    lab = Label(root2, image=bgimage)
    lab.place(x=0, y=0, relwidth=1, relheight=1)
    canvas1 = Canvas(root2, width=400, height=400,bg="#FFDEAD")
    canvas1.pack(padx=200, pady=200)
    user_id_lab = Label(canvas1, text="User Id ",font="Consolas 12 bold",width=14,bg="#FFB90F")
    user_id_lab.grid(row=1, column=0)
    password_lab = Label(canvas1, text="Password ",font="Consolas 12 bold",width=14,bg="#FFB90F")
    password_lab.grid(row=2, column=0)
    user_id = Entry(canvas1, width=30,font="Consolas 12 bold")
    user_id.grid(row=1, column=1)
    password_check = Entry(canvas1, width=30,font="Consolas 12 bold",show="*")
    password_check.grid(row=2, column=1)
    def hide():
        show_but.config(text="Show",command=show,font="Consolas 12 bold",bg="black",fg="white",width=10)
        password_check.config(show="*")
    def show():
        show_but.config(text="Hide",font="Consolas 12 bold",command=hide,width=10,bg="white",fg="black")
        password_check.config(show="")
    show_but=Button(canvas1,text="Show",font="Consolas 12 bold",bg="black",fg="white",command=show,width=10)
    show_but.grid(row=2,column=2)
    def submit_11():
        k=c.execute("SELECT password FROM teachers WHERE email_id=?",(user_id.get(),)).fetchall()
        #print(k[0][0])
        #print(password_check.get())
        if password_check.get()==k[0][0]:
            password_check.delete(0, END)
            user_id.delete(0, END)
            home_t()
        else:
            password_check.delete(0,END)
            warning_label=Label(canvas1,text="Wrong Password,Try Again",font="Consolas 12 bold")
            warning_label.grid(row=3,column=1)
            password_check.delete(0,END)

    get_started_but = Button(canvas1, text="Lets get started",command=submit_11,font="Consolas 12 bold",bg="#FFB90F")
    get_started_but.grid(row=4, column=1)
    root2.mainloop()

def sign_in_s():
    root3 = Toplevel()
    root3.geometry("1920x1080")
    root3.title("Sign In Page-Student")
    bgimage = ImageTk.PhotoImage(Image.open("Sign In Image6.jpg"))
    lab = Label(root3, image=bgimage)
    lab.place(x=0, y=0, relwidth=1, relheight=1)
    canvas = Canvas(root3, width=1000, height=1000,bg="#FFDEAD")
    canvas.pack(padx=200,pady=200)
    user_id_lab = Label(canvas, text="User Id ",font="Consolas 12 bold",width=15,bg="#FFB90F")
    user_id_lab.grid(row=1, column=0)
    password_lab = Label(canvas, text="Password ",font="Consolas 12 bold",width=15,bg="#FFB90F")
    password_lab.grid(row=2, column=0)
    user_id = Entry(canvas,font="Consolas 12 bold",bg="#FFDEAD",width=80)
    user_id.grid(row=1, column=1)
    password_check = Entry(canvas,font="Consolas 12 bold",bg="#FFDEAD",width=80,show="*")
    password_check.grid(row=2, column=1)
    def hide():
        show_but.config(text="Show",command=show,font="Consolas 12 bold",bg="black",fg="white",width=10)
        password_check.config(show="*")
    def show():
        show_but.config(text="Hide",font="Consolas 12 bold",command=hide,width=10,bg="white",fg="black")
        password_check.config(show="")
    show_but=Button(canvas,text="Show",font="Consolas 12 bold",bg="black",fg="white",command=show,width=10)
    show_but.grid(row=2,column=3)
    def check_step():
        global class_name
        class_name=""
        global unique_id
        unique_id=user_id.get()
        for i in user_id.get():
            if i=="_":
                break
            else:
                class_name=class_name+i
        global stud_det
        stud_det=class_name+"_student_details"
        check=c.execute("SELECT password FROM {} WHERE uniqueid = ?".format(stud_det),(unique_id,)).fetchall()
        if password_check.get()==check[0][0]:
            user_id.delete(0,END)
            password_check.delete(0,END)
            home_s()
        #elif int(password_check.get())==314159:
        #bazinga()
        else:
            #print(check[0][0])
            #print(password_check.get())
            retry_lab=Label(canvas,text="Please enter the correct password",font="Consolas 12 bold",bg="#FFB90F",width=80)
            retry_lab.grid(row=4,column=1)
            password_check.delete(0,END)
    get_started_but = Button(canvas, text="Lets get started", command=check_step,font="Consolas 12 bold",bg="#FFB90F",width=80)
    get_started_but.grid(row=3, column=1)
    clock_lab=Label(root3,text="",font="Consolas 12 bold")
    clock_lab.pack()

    def home_s():
        def redlist(stdid):
            l1 = []  # testids
            l2 = []  # ranks
            classname = ""
            for i in range(len(stdid)):
                if stdid[i] == "_":
                    break
                else:
                    classname += stdid[i]

            Lsubj = c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'").fetchall()
            Lsubj1 = []
            Lsubj2 = []
            Lsubj3 = []
            l4 = []
            l3 = []
            for i in Lsubj:
                Lsubj1.append(i[0])
            for i in Lsubj1:
                if i.find(classname + "_") != -1 and i.find("marks") != -1:
                    Lsubj2.append(i)
                if i.find(classname + "_") != -1 and i.find("rank") != -1:
                    Lsubj3.append(i)
            for i in Lsubj2:
                l3.append(c.execute("SELECT test_id FROM {}".format(i)).fetchall())
            for i in Lsubj3:
                l4.append(c.execute("SELECT {} FROM {}".format(stdid, i)).fetchall())
            for i in l3:
                for j in i:
                    l1.append(j[0])
            for i in l4:
                for j in i:
                    l2.append(j[0])
            points = 0
            for i in l2:
                points += 21 - i
            if points <= (3 * len(l1)):
                achcha = 'IN RED LIST!!!!!!!!'
                color = StringVar()
                color.set('#B22222')
            elif (3 * len(l1)) < points <= (5 * len(l1)):
                achcha = "RED LIST WARNING!!!"
                color = StringVar()
                color.set('#FF3030')
            elif (5 * len(l1)) < points <= (8 * len(l1)):
                achcha = "NOT GOOD ENOUGH,WORK HARD"
                color = StringVar()
                color.set('orange')
            elif (8 * len(l1)) < points <= (12 * len(l1)):
                achcha = "CAN DO BETTER"
                color = StringVar()
                color.set('yellow')
            elif (12 * len(l1)) < points <= (15 * len(l1)):
                achcha = 'GOING GOOD STILL AIM HIGHER!'
                color = StringVar()
                color.set('green')
            elif (15 * len(l1)) < points <= (18 * len(l1)):
                achcha = 'GREAT WORK,AIM FOR THE HIGHEST!!'
                color = StringVar()
                color.set('#00C957')
            elif points > 18 * (len(l1)):
                achcha = "ARE YOU EVEN HUMAN?"
                color = StringVar()
                color.set('gold')
            return (achcha, color,points/len(l1))
        a,l,pts=redlist(unique_id)
        root5 = Toplevel()
        root5.geometry("1920x1080")
        root5.title("Student Home Page")
        bgimage = ImageTk.PhotoImage(Image.open("Sign In Image8.jpg"))
        lab = Label(root5, image=bgimage)
        lab.place(x=0, y=0, relwidth=1, relheight=1)
        rooti = Canvas(root5, width=400, height=400,bg=l.get())
        rooti.pack(padx=200, pady=200)

        def onestudent():
            root11 = Toplevel()
            root11.geometry("1920x1080")
            root11.title("Student Home Page")
            bgimage = ImageTk.PhotoImage(Image.open("Student Home Page.jpg"))
            lab = Label(root11, image=bgimage)
            lab.place(x=0, y=0, relwidth=1, relheight=1)
            root9 = Canvas(root11, width=1920, height=1080)
            root9.pack(padx=200, pady=200)
            #print(class_name)
            k9=len(class_name)
            #print(unique_id)
            student_name = c.execute("SELECT name FROM {} WHERE uniqueid=? ".format(stud_det),(unique_id,)).fetchall()
            list3 = []
            list5 = []
            list6 = []
            list7 = []
            click7 = StringVar()
            click7.set("Choose Subject")
            Lsubj = c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'").fetchall()
            #print(Lsubj)
            Lsubj1 = []
            Lsubj2 = []
            for i in Lsubj:
                Lsubj1.append(i[0])
            for i in Lsubj1:
                if i.find(class_name + "_") != -1 and i.find("marks") != -1:
                    Lsubj2.append(i)
            subject_data_box = OptionMenu(root9, click7, *Lsubj2)
            subject_data_box.config(font="Consolas 12 bold", bg="#EEEE00")
            subject_data_box.grid(row=2, column=0)

            def submit_8():
                tabname = ''
                for i in range(len(click7.get())):
                    if click7.get()[i].isalnum() == True:
                        tabname += click7.get()[i]
                    elif click7.get()[i] == "_":
                        tabname += click7.get()[i]
                #print(tabname)
                for name in c.execute("SELECT test_name FROM {}".format(tabname)).fetchall():
                    name1 = str(name[0])
                    list3.append(name1)
                    list7.append(name1)
                list4 = (c.execute("SELECT {} FROM {}".format(unique_id, tabname)).fetchall())
                list5 = (c.execute("SELECT total_marks FROM {}".format(tabname)).fetchall())
                tabname_1 = tabname[:-6]
                tabnamer = tabname_1 + "_rank"
                list6 = (c.execute("SELECT {} FROM {}".format(unique_id, tabnamer)).fetchall())
                #print(list6)
                #print(list3)
                k8 = StringVar()
                k8.set(str("Name:" + student_name[0][0]))
                name_lab = Label(root9, textvariable=k8, font="Consolas 12 bold", bg="#DDA0DD")
                name_lab.grid(row=3, column=0)
                tests_attended = []
                tests_absent = []
                k9 = StringVar()
                k9.set(str("Total no. of tests" + str(len(list5))))
                tests_lab = Label(root9, textvariable=k9, font="Consolas 12 bold", bg="#DDA0DD")
                tests_lab.grid(row=3, column=2)
                for i in range(len(list4)):
                    if list4[i] == 'A':
                        list4[i] = 0
                        tests_absent.append(list3[i])
                    else:
                        tests_attended.append(list3[i])
                k10 = StringVar()
                k11 = StringVar()
                k10.set("No. of tests absent" + str(len(tests_absent)))
                k11.set("Tests absent:" + str(tests_absent))
                no_absent_lab = Label(root9, textvariable=k10, font="Consolas 12 bold", bg="#DDA0DD")
                test_absent_lab = Label(root9, textvariable=k11, font="Consolas 12 bold", bg="#DDA0DD")
                no_absent_lab.grid(row=3, column=4)
                test_absent_lab.grid(row=3, column=6)

                # average rank
                sum1 = 0
                for i in range(len(list6)):
                    sum1 += list6[i][0]
                averagerank = sum1 / len(list6)

                # percentage marks
                marks_percentage = []
                #print(list5)
                for i in range(len(list4)):
                    #print(list5[i][0])
                    #print(list4[i][0])
                    k = (list4[i][0] / list5[i][0]) * 100
                    marks_percentage.append(k)

                # variance(%marks)
                variance = stat.variance(marks_percentage)
                k12 = StringVar()
                k12.set("Variance" + "=" + str(variance))
                variance_lab = Label(root9, textvariable=k12, font="Consolas 12 bold", bg="#DDA0DD")
                variance_def_lab = Label(root9, text="This tells about the consistency of a student",
                                         font="Consolas 12 bold", bg="#DDA0DD")
                variance_lab.grid(row=5, column=2)
                variance_def_lab.grid(row=5, column=0)

                def graph_5():
                    plt.style.use("dark_background")
                    plt.plot(list3, list6, linestyle='solid', color='cyan')
                    plt.plot(list3, list6, 'ro')
                    plt.xlabel("TESTS")
                    plt.ylabel("RANK")
                    plt.xticks(rotation=45)
                    plt.title("RANK GRAPH", fontdict=font6)
                    plt.show()

                def graph_6():
                    plt.style.use("dark_background")
                    plt.bar(list3, marks_percentage, color='pink')
                    plt.xlabel("TESTS")
                    plt.ylabel("% MARKS")
                    plt.xticks(rotation=45)
                    plt.title("% MARK GRAPH", fontdict=font3)
                    plt.show()

                quotes_lab = Label(root9, textvariable=k16, font="Consolas 14 bold italic", bg="black", fg="white",
                                   width=140)
                quotes_lab.place(x=0, y=650)
                #refresh_but = Button(root9, text="Refresh", command=refresh, font="Consolas 12 bold", bg="lawngreen")
                #refresh_but.grid(row=8, column=11)
                #logout_but = Button(root9, text="Log Out", command=logout, font="Consolas 12 bold", bg="red")
                #logout_but.grid(row=8, column=10)

                graph_5_but = Button(root9, text="Graph", command=graph_5, font="Consolas 12 bold", bg="#91FBCD")
                graph_6_but = Button(root9, text="Graph", command=graph_6, font="Consolas 12 bold", bg="#91FBCD")
                graph_5_but.grid(row=6, column=0)
                graph_6_but.grid(row=6, column=2)

            submit_8_but = Button(root9, text="Continue", command=submit_8, font="Consolas 12 bold", bg="#91FBCD")
            submit_8_but.grid(row=2, column=1)
            root11.mainloop()



        k25=StringVar()
        k25.set(a)
        k26=StringVar()
        pts1="You have secured "+str(pts)+" points out of 20"
        k26.set(pts1)
        one_student_lab = Label(rooti, text="Test reports", font="Consolas 12 bold",bg="#96CDCD")
        one_student_lab.grid(row=0, column=0)
        one_student_but = Button(rooti, text="Click to generate your test report", font="Consolas 12 bold", command=onestudent,bg="#96CDCD")
        one_student_but.grid(row=0, column=1)
        redlist_lab0=Label(rooti,text="Remark",font="Consolas 12 bold",bg="#96CDCD")
        redlist_lab0.grid(row=1,column=0)
        redlist_lab=Label(rooti,textvariable=k25,font="Consolas 12 bold",bg=l.get(),width=35)
        redlist_lab.grid(row=1,column=1)
        redlist_lab2=Label(rooti,textvariable=k26,font="Consolas 12 bold",bg="#96CDCD")
        redlist_lab2.grid(row=3,column=0)
        def ncert_open():
            new=1
            webbrowser.open("http://epathshala.nic.in/process.php?id=students&type=eTextbooks&ln=en",new=new)
        url_lab=Label(rooti,text="For NCERT text books",font="Consolas 12 bold",bg="#96CDCD")
        url_but=Button(rooti,text="Click Here",font="Consolas 12 bold",command=ncert_open,bg="#96CDCD")
        url_lab.grid(row=2,column=0)
        url_but.grid(row=2,column=1)

        root5.mainloop()
    root3.mainloop()

def sign_up():
    root1 = Toplevel()
    root1.geometry("1920x1080")
    root1.title("Sign Up Page")
    bgimage = ImageTk.PhotoImage(Image.open("Sign Up Image2.jpg"))
    lab = Label(root1, image=bgimage)
    lab.place(x=0, y=0, relwidth=1, relheight=1)
    frame3 = Canvas(root1, width=400, height=400,bg="#FFDEAD")
    frame3.pack(padx=200, pady=200)
    name_t = Entry(frame3, width=30,font="Consolas 12 bold",bg="#FFDEAD")
    name_t.grid(row=1, column=1)
    subject_t = Entry(frame3, width=30,font="Consolas 12 bold",bg="#FFDEAD")
    subject_t.grid(row=2, column=1)
    phone_t = Entry(frame3, width=30,font="Consolas 12 bold",bg="#FFDEAD")
    phone_t.grid(row=3, column=1)
    email_t = Entry(frame3, width=30,font="Consolas 12 bold",bg="#FFDEAD")
    email_t.grid(row=4, column=1)
    password_t = Entry(frame3, width=30,font="Consolas 12 bold",bg="#FFDEAD")
    password_t.grid(row=5, column=1)
    code_t=Entry(frame3,width=30,font="Consolas 12 bold",bg="#FFDEAD")
    code_t.grid(row=6,column=1)
    def continue_():
        success_t_lab = Label(frame3, text="You have successfully signed up!!!!:)",font="Consolas 12 bold")
        success_t_lab.grid(row=8, column=1)
        continue_t_but = Button(frame3, text="Continue ", command=sign_in_t,font="Consolas 12 bold")
        continue_t_but.grid(row=8, column=2)
        c.execute("INSERT INTO teachers values(?,?,?,?,?,?)",
                  (code_t.get(), name_t.get(), subject_t.get(), password_t.get(), email_t.get(), phone_t.get()))
        conn.commit()
        name_t.delete(0,END)
        subject_t.delete(0, END)
        phone_t.delete(0, END)
        email_t.delete(0, END)
        password_t.delete(0, END)
        code_t.delete(0,END)
    name_t_lab = Label(frame3, text="Name ", width=15,font="Consolas 12 bold",bg="#FFB90F")
    name_t_lab.grid(row=1, column=0)
    subject_t_lab = Label(frame3, text="Subject ", width=15,font="Consolas 12 bold",bg="#FFB90F")
    subject_t_lab.grid(row=2, column=0)
    phone_t_lab = Label(frame3, text="Phone Number ", width=15,font="Consolas 12 bold",bg="#FFB90F")
    phone_t_lab.grid(row=3, column=0)
    email_t_lab = Label(frame3, text="Email-Id ", width=15,font="Consolas 12 bold",bg="#FFB90F")
    email_t_lab.grid(row=4, column=0)
    password_t_lab = Label(frame3, text="Password ", width=15,font="Consolas 12 bold",bg="#FFB90F")
    password_t_lab.grid(row=5, column=0)
    code_t_lab=Label(frame3,text="Teacher Code ",width=15,font="Consolas 12 bold",bg="#FFB90F")
    code_t_lab.grid(row=6,column=0)
    sign_up_but = Button(frame3, text="Sign-Up ", command=continue_ ,font="Consolas 12 bold",bg="#FFB90F")
    sign_up_but.grid(row=7, column=1)
    root1.mainloop()

def start():
    root0 =Tk()
    root0.geometry("1920x1080")
    root0.title("Start")
    bgimage = ImageTk.PhotoImage(Image.open("Start Image 3.jpg"))
    lab = Label(root0, image=bgimage)
    lab.place(x=0, y=0, relwidth=1, relheight=1)
    global k16
    global k15
    k16 = StringVar()
    k15 = random.randint(0, (len(quotes) - 1))
    k16.set(str(quotes[k15]))
    def choose():
        sign_in_but = Button(frame1, text="Sign In", command=sign_in_t,font="Consolas 16 bold",width=15,bg="#4169E1")
        sign_in_but.pack()
        sign_up_but2 = Button(frame1, text="Sign Up", command=sign_up,font="Consolas 16 bold",width=15,bg="#4169E1")
        sign_up_but2.pack()
    frame1 = Canvas(root0,width=200,height=200)
    frame1.place(x=360, y=115)
    frame2 = Canvas(root0,width=200,height=200)
    frame2.place(x=960, y=115)
    start_lab=Label(root0,text="SCHOLA ADIUTOR",bg="#4169E1",fg="#00EE76",font=('Segoe UI Black', '36', 'bold italic'),width=46)
    start_lab.place(x=0,y=0)
    bgimage3 = ImageTk.PhotoImage(Image.open("Teacher Icon 2.png"))
    teacher_but = Button(frame1,text="Teacher", command=choose,bg="#7D26CD",font="Consolas 16 bold",width=15)
    teacher_but.pack()
    bgimage2=ImageTk.PhotoImage(Image.open("Student Icon 1.jpg"))
    student_but =Button(frame2, text="Student", command=sign_in_s,bg="#7D26CD",font="Consolas 16 bold",width=15)
    student_but.pack()
    quotes_lab=Label(root0,textvariable=k16,font="Consolas 14 bold italic",bg="black",fg="white",width=140)
    quotes_lab.place(x=0,y=650)
    def play():
        pygame.mixer.music.load("D:\The Assistant\Shire Theme.mp3")
        pygame.mixer.music.play(loops=5)
    #play()
    root0.mainloop()

start()





