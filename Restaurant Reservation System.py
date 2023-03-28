from cgitb import text
from os import system
from tkinter import *
from tkinter import ttk
from time import strftime
from tkinter import messagebox as ms
import tkinter as tk
from tkcalendar import DateEntry
import random
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome " + self.username.get()
            self.head.configure(fg="black",bg="DodgerBlue2")
            self.head.pack(fill=X)
            application = reserve(root)
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'Login Panel',font = ('Britannic Bold',30), bg="SkyBlue2",pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10, bg="SkyBlue2",pady = 10)
        Label(self.logf,text = 'Username: ',font = ('Arial Rounded MT Bold',20), bg="SkyBlue2",pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('Arial Rounded MT Bold',20), bg="SkyBlue2",pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('Bahnschrift',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('Bahnschrift',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10, bg="SkyBlue2",pady = 10)
        Label(self.crf,text = 'Username: ',font = ('Arial Rounded MT Bold',20), bg="SkyBlue2",pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('Arial Rounded MT Bold',20), bg="SkyBlue2",pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('Bahnschrift',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('Bahnschrift',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

class reserve:

    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Restaurant Reservation System")
        self.root.configure(background='black')

    #definefunction

        def iexit():
            i= ms.askyesno("Prompt!","Do you want to exit?")
            if i > 0:
                root.destroy()
            return
        
        def icancel():
            i= ms.askyesno("Prompt!","Do you want to discard your Reservation?")
            if i > 0:
                make()
            return

        def clock():
            string = strftime('%A \n %x \n %H:%M:%S %p')
            time.config(text=string)
            time.after(1000, clock)

    
        def make():
            ReceiptRef = StringVar()
            name1 = StringVar()
            age1 = IntVar()
            ReserveDate1 = StringVar()
            ReserveTime1 = StringVar()
            Numberperson1 = IntVar()
            contact1 = IntVar()
            DateofReserve=StringVar()
            #Frame
            ButtonFrame4=LabelFrame(ButtonFrame2, text="Customer Details", font=("Britannic Bold",21), bg="SkyBlue2", bd=10, relief=RIDGE)
            ButtonFrame4.place(x=0, y=156, width=410, height=335)
            #Entry
            name1 = Label(ButtonFrame4,text="Name ", font=("Arial",14,"bold"), bg="SkyBlue2")
            name1.grid(row=0,column=0,padx=2,pady=2)
            age1 = Label(ButtonFrame4,text="Age ", font=("Arial",14,"bold"), bg="SkyBlue2")
            age1.grid(row=1,column=0,padx=2,pady=2)
            ReserveDate1 = Label(ButtonFrame4,text="Reserve Date", font=("Arial",14,"bold"), bg="SkyBlue2")
            ReserveDate1.grid(row=2,column=0,padx=2,pady=2)
            ReserveTime1 = Label(ButtonFrame4,text="Reserve Time", font=("Arial",14,"bold"), bg="SkyBlue2")
            ReserveTime1.grid(row=3,column=0,padx=2,pady=2)
            Numberperson1 = Label(ButtonFrame4,text="No. of Persons", font=("Arial",14,"bold"), bg="SkyBlue2")
            Numberperson1.grid(row=4,column=0,padx=2,pady=2)
            contact1 = Label(ButtonFrame4,text="Contact No.", font=("Arial",14,"bold"), bg="SkyBlue2")
            contact1.grid(row=5,column=0,padx=2,pady=2)

            name1 = Entry(ButtonFrame4, font=("Arial",14))
            name1.grid(row=0,column=1,padx=2,pady=2)
            age1 = Entry(ButtonFrame4, font=("Arial",14))
            age1.grid(row=1,column=1,padx=2,pady=2)
            ReserveDate1 = DateEntry(ButtonFrame4, selectmode='day', font=("Arial",14), width=18)
            ReserveDate1.grid(row=2,column=1,padx=2,pady=2)
            ReserveTime1 = ttk.Combobox(ButtonFrame4, font=("Arial",14), width=18)
            ReserveTime1['value']=('12:00 am','01:00 am','02:00 am','03:00 am',
            '04:00 am','05:00 am','06:00 am','07:00 am','08:00 am',
            '09:00 am','10:00 am','11:00 am','12:00 pm','01:00 pm',
            '02:00 pm','03:00 pm','04:00 pm','05:00 pm','06:00 pm',
            '07:00 pm','08:00 pm','09:00 pm','10:00 pm','11:00 pm')
            ReserveTime1.grid(row=3,column=1,padx=2,pady=2)
            Numberperson1 = ttk.Combobox(ButtonFrame4, font=("Arial",14), width=18)
            Numberperson1['value']=('2','3','4')
            Numberperson1.current(0)
            Numberperson1.grid(row=4,column=1,padx=2,pady=2)
            contact1 = Entry(ButtonFrame4, font=("Arial",14))
            contact1.grid(row=5,column=1,padx=2,pady=2)

            def makersrv():
                x=random.randint(10853,500831)
                randomRef = str(x)
                ReceiptRef.set(randomRef)
                DateofReserve.set(strftime("%d/%m/%Y"))

                ReserveNumber = Label(ReceiptFrame1,text="Reservation No. : ", font=("Arial",13,"bold"), bg="LightBlue1")
                ReserveNumber.grid(row=0,column=0,padx=2,pady=2)
                Date = Label(ReceiptFrame1,text="Date                   : ", font=("Arial",13,"bold"), bg="LightBlue1")
                Date.grid(row=1,column=0,padx=2,pady=2)
                name = Label(ReceiptFrame1,text="Name                 : ", font=("Arial",13,"bold"), bg="LightBlue1")
                name.grid(row=2,column=0,padx=2,pady=2)
                age = Label(ReceiptFrame1,text="Age                   : ", font=("Arial",13,"bold"), bg="LightBlue1")
                age.grid(row=3,column=0,padx=2,pady=2)
                ReserveDate = Label(ReceiptFrame1,text="Reserve Date    : ", font=("Arial",13,"bold"), bg="LightBlue1")
                ReserveDate.grid(row=4,column=0,padx=2,pady=2)
                ReserveTime = Label(ReceiptFrame1,text="Reserve Time    : ", font=("Arial",13,"bold"), bg="LightBlue1")
                ReserveTime.grid(row=5,column=0,padx=2,pady=2)
                Numberperson = Label(ReceiptFrame1,text="No. of Persons  : ", font=("Arial",13,"bold"), bg="LightBlue1")
                Numberperson.grid(row=6,column=0,padx=2,pady=2)
                contact = Label(ReceiptFrame1,text="Contact No.       : ", font=("Arial",13,"bold"), bg="LightBlue1")
                contact.grid(row=7,column=0,padx=2,pady=2)
                
                makersrv=Label(ReceiptFrame1, text=ReceiptRef.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv.grid(row=0,column=1,padx=2,pady=2)
                makersrv0=Label(ReceiptFrame1, text=DateofReserve.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv0.grid(row=1,column=1,padx=2,pady=2)        
                makersrv1=Label(ReceiptFrame1, text=name1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv1.grid(row=2,column=1,padx=2,pady=2)
                makersrv2=Label(ReceiptFrame1, text=age1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv2.grid(row=3,column=1,padx=2,pady=2)
                makersrv3=Label(ReceiptFrame1, text=ReserveDate1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv3.grid(row=4,column=1,padx=2,pady=2)
                makersrv4=Label(ReceiptFrame1, text=ReserveTime1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv4.grid(row=5,column=1,padx=2,pady=2)   
                makersrv5=Label(ReceiptFrame1, text=Numberperson1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv5.grid(row=6,column=1,padx=2,pady=2)
                makersrv6=Label(ReceiptFrame1, text=contact1.get(), font=("Arial",13,"bold"), bg="LightBlue1")
                makersrv6.grid(row=7,column=1,padx=2,pady=2)

                with open("user.txt","a+") as file:
                    file.seek(0)
                    data = file.read(100)
                    if len(data) > 0 :
                        file.write("\n")
                    file.write(f"Reservation No.   : {ReceiptRef.get()}\nDate                     : {DateofReserve.get()}\nName                   : {name1.get()}\nAge                      : {age1.get()}\nReservation Date : {ReserveDate1.get()}\nReservation Time : {ReserveTime1.get()}\nNo. of Persons     : {Numberperson1.get()}\nContact No.          : {contact1.get()}")
                    file.close()
                    print()
                view()

            ButtonFrame6=LabelFrame(ButtonFrame4, bg="SkyBlue2", bd=10, relief=RIDGE)
            ButtonFrame6.place(x=23, y=206, width=345, height=66)

            btnmakersrv = Button(ButtonFrame6,bd=7,font=("Arial",11,"bold"),text="Make a Reservation", width=15, command=makersrv)
            btnmakersrv.grid(row=15,column=0,padx=2,pady=2)

            btnicancel = Button(ButtonFrame6,padx=18,bd=7,font=("Arial",11,"bold"),text="Cancel", width=12, command=icancel)
            btnicancel.grid(row=15,column=1,padx=2,pady=2)

            ReceiptFrame1=LabelFrame(ReceiptFrame, width=250, height=250, font=("Arial",12,"bold"), bg="LightBlue1", relief=RIDGE)
            ReceiptFrame1.place(x=7, y=0, width=448, height=247)

            btnreset = Button(ReceiptFrame1,bd=7,font=("Arial",11,"bold"),text="Reset", width=15, command=make)
            btnreset.place(x=280,y=180,width=150,height=50)

        def view():
            ButtonFrame5=LabelFrame(ButtonFrame2, text="View Reservations", font=("Britannic Bold",20), bg="SkyBlue2", bd=10, relief=RIDGE)
            ButtonFrame5.place(x=410, y=0, width=410, height=245)

            scroll_y =  Scrollbar(ButtonFrame5)
            scroll_y.pack(side=RIGHT, fill=Y)
            rsrv_text=Text(ButtonFrame5, font=("Arial",15,"bold"), bg="LightBlue1", relief='groove', wrap= 'word', yscrollcommand=scroll_y.set)
            rsrv_text.place(x=5, y=0, width=363, height=195)

            count = 0
            file = open("user.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1
            if count == 0:
                v = ms.showwarning("Error !","There are no Reservation!\nPlease make a Reservation !!!")
            else:
                file = open ("user.txt","r")
                rsrvtext = file.read()
                rsrv_text.insert(END, rsrvtext)
                file.close()

        def delete():
            ButtonFrame7=LabelFrame(ButtonFrame2, text="Delete Reservation", font=("Britannic Bold",21), bg="SkyBlue2", bd=10, relief=RIDGE)
            ButtonFrame7.place(x=410, y=245, width=410, height=245)

            cnclfrsrv = Label(ButtonFrame7,text="First Reservation     ", font=("Bahnschrift",18), bg="SkyBlue2")
            cnclfrsrv.grid(row=0,column=0,padx=2,pady=2)
            cnclfrsrv = Label(ButtonFrame7,text="Second Reservation", font=("Bahnschrift",18), bg="SkyBlue2")
            cnclfrsrv.grid(row=1,column=0,padx=2,pady=2)
            cnclfrsrv = Label(ButtonFrame7,text="Third Reservation    ", font=("Bahnschrift",18), bg="SkyBlue2")
            cnclfrsrv.grid(row=2,column=0,padx=2,pady=2)
            cnclfrsrv = Label(ButtonFrame7,text="Fourth Reservation ", font=("Bahnschrift",18), bg="SkyBlue2")
            cnclfrsrv.grid(row=3,column=0,padx=2,pady=2)

            def cnclrsrv1():
                file1 = open("user.txt", "r")
                lines = file1.readlines()
                file1.close()
                file2 = open("user.txt", "w")

                for number, line in enumerate (lines):
                    if number not in [0,1,2,3,4,5,6,7]:
                        file2.write(line)
                file2.close()
                view()
            def cnclrsrv2():
                file1 = open("user.txt", "r")
                lines = file1.readlines()
                file1.close()
                file2 = open("user.txt", "w")

                for number, line in enumerate (lines):
                    if number not in [8,9,10,11,12,13,14,15]:
                        file2.write(line)
                file2.close()
                view()
            def cnclrsrv3():
                file1 = open("user.txt", "r")
                lines = file1.readlines()
                file1.close()
                file2 = open("user.txt", "w")

                for number, line in enumerate (lines):
                    if number not in [16,17,18,19,20,21,22,23]:
                        file2.write(line)
                file2.close()
                view()
            def cnclrsrv4():
                file1 = open("user.txt", "r")
                lines = file1.readlines()
                file1.close()
                file2 = open("user.txt", "w")

                for number, line in enumerate (lines):
                    if number not in [24,25,26,27,28,29,30,31]:
                        file2.write(line)
                file2.close()
                view()

            btndelete1 = Button(ButtonFrame7,bd=7,font=("Arial",11,"bold"),text="Delete", width=10, command=cnclrsrv1)
            btndelete1.grid(row=0,column=1,padx=1,pady=1)
            btndelete2 = Button(ButtonFrame7,bd=7,font=("Arial",11,"bold"),text="Delete", width=10, command=cnclrsrv2)
            btndelete2.grid(row=1,column=1,padx=1,pady=1)
            btndelete3 = Button(ButtonFrame7,bd=7,font=("Arial",11,"bold"),text="Delete", width=10, command=cnclrsrv3)
            btndelete3.grid(row=2,column=1,padx=1,pady=1)
            btndelete4 = Button(ButtonFrame7,bd=7,font=("Arial",11,"bold"),text="Delete", width=10, command=cnclrsrv4)
            btndelete4.grid(row=3,column=1,padx=1,pady=1)

            count = 0
            file = open("user.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1
            if count == 0:
                c = ms.showwarning("Error !","There are no Reservation!\nPlease make a Reservation !!!")

    #Mainframe
        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, bd=10, bg="SkyBlue2", width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('Forte',35,'bold'), bg="SkyBlue2",text="\t RESTAURANT RESERVATION SYSTEM ")
        self.lblTitle.grid()

    #Frames
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=500,bd=20, bg="DodgerBlue2", pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        ButtonFrame1=LabelFrame(CustomerDetailsFrame, text="Menu", font=("Britannic Bold",30), bg="DodgerBlue2", width=100,height=50,bd=10, relief=RIDGE)
        ButtonFrame1.pack(side=LEFT,fill=BOTH,expand=True)

        ButtonFrame2=LabelFrame(CustomerDetailsFrame, bd=10, width=450, bg="DodgerBlue2",height=400, relief=RIDGE)
        ButtonFrame2.pack(side=RIGHT,fill=BOTH,expand=True)

        ButtonFrame3=LabelFrame(ButtonFrame1, bg="SkyBlue2", bd=10, relief=RIDGE)
        ButtonFrame3.place(x=30, y=20, width=410, height=112)

        ReceiptFrame=LabelFrame(ButtonFrame1, width=350, bg="SkyBlue2",height=300, font=("Britannic Bold",13),text="Receipt", relief=RIDGE)
        ReceiptFrame.place(x=0, y=175, width=467, height=278)

        DTFrame=LabelFrame(ButtonFrame2, width=350,height=300, bg="SkyBlue2", font=("Britannic Bold",13),text="Date/Time", relief=RIDGE)
        DTFrame.place(x=0, y=0, width=410, height=155)

    #Buttons
        self.btnmake = Button(ButtonFrame3,bd=7,font=("Arial",11,"bold"),text="Make Reservation", width=19, command=make)
        self.btnmake.grid(row=0,column=0,padx=2,pady=2)

        self.btnview = Button(ButtonFrame3,padx=18,bd=7,font=("Arial",11,"bold"),text="View all Reservation", width=15, command=view)
        self.btnview.grid(row=0,column=1,padx=3,pady=2)

        self.btndelete = Button(ButtonFrame3,padx=18,bd=7,font=("Arial",11,"bold"),text="Delete Reservation", width=15, command=delete)
        self.btndelete.grid(row=1,column=0,padx=2,pady=2)

        self.btnExit = Button(ButtonFrame3,padx=18,bd=7,font=("Arial",11,"bold"),text="Exit", width=15, command=iexit)
        self.btnExit.grid(row=1,column=1,padx=3,pady=2)

        time = Button(DTFrame, font=("Bahnschrift",20), bg="LightBlue1", text="Date/Time", width=25, command=clock, relief=RIDGE)
        time.pack(anchor='center')

if __name__=='__main__':
    root = tk.Tk()
    
    root.geometry("500x300+420+200")
    root.title('Login Form')
    root.configure(bg="SkyBlue2")
    application = user(root,)
    root.mainloop()

