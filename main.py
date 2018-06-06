"""Imports"""
#++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime
from tkinter import *

import tkinter.ttk,tkinter.messagebox,tkinter.font,os
from prettytable import PrettyTable
#++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++
"""Creating the window, menubar and title"""
class EventApp():
    def __init__(self):

        #Creating instance
        self.root=Tk()
        self.root.title("Time Schedule")
        self.messagebox=tkinter.messagebox
        self.ttk=tkinter.ttk

        #Using prettytable to create the tables for timetable
        headerFormat = ["Period","1","2","3","4","5","6","7"]
        self.mains=PrettyTable(headerFormat)
        self.main1=PrettyTable(headerFormat)
        self.main2=PrettyTable(headerFormat)
        self.main3=PrettyTable(headerFormat)
        self.main4=PrettyTable(headerFormat)
        self.main5=PrettyTable(headerFormat)

        self.customFont = tkinter.font.Font(family="Helvetica", size=12)       

        #initializing functions
        self.root.resizable(0,0)
        self.createMenu()
        self.MainTabs()
        self.TabContent()
        self.retrieveTab()
        self.deleteEvent()
#++++++++++++++++++++++++++++++++++++++++++

#==================================================================        
   #creating the menu bar
    def createMenu(self):
        self.menuBar=Menu(self.root)
        self.root.configure(menu= self.menuBar)
            ##
        self.FileMenu = Menu(self.menuBar,tearoff=0)
        self.FileMenu.add_command(label="New")
        self.FileMenu.add_command(label="Exit", command=self.root.destroy)
        self.HelpMenu= Menu(self.menuBar,tearoff=0)
        self.HelpMenu.add_command(label="About", command=self._msgBox)
        self.menuBar.add_cascade(label="File", menu=self.FileMenu)
        self.menuBar.add_cascade(label="Help", menu=self.HelpMenu)
        
    def _msgBox(self):
        self.messagebox.showinfo('About the App','This App is designed to create a schedule for the days of the week and the time with an hour between between the times.The schedule can be accessed by the days of the week')
#=====================================================================

    #creating the tabs
    def MainTabs(self):
        """Adding tabs to make navigation easy"""
        self.AddingEventTab=tkinter.ttk.Notebook(self.root)
        self.tab1= tkinter.ttk.Frame(self.AddingEventTab)
        self.tab2= tkinter.ttk.Frame(self.AddingEventTab)
        self.tab3= tkinter.ttk.Frame(self.AddingEventTab)
        self.AddingEventTab.add(self.tab1, text="ADD TABLE")
        self.AddingEventTab.add(self.tab2, text="VIEW TABLE")
        self.AddingEventTab.add(self.tab3, text="DELETE TABLE")
        self.AddingEventTab.pack(expand=5,pady=7, fill="both")

#**********************************************************************************************************
    """Adding content to the 'Add event tab'"""
    def TabContent(self):
        #first choosing day
        root1= tkinter.ttk.LabelFrame(self.tab1, text="Add TABLE")
        root1.grid(column=0, row=0,padx=8,pady=4,sticky="W")
        Day=tkinter.ttk.Label(root1, text="Please Choose the Department:").grid(column=0,row=0,sticky='W')
        self.dept=StringVar()
        self.year=StringVar()

        #Monday values
        self.ttval11=StringVar()
        self.ttval12=StringVar()
        self.ttval13=StringVar()
        self.ttval14=StringVar()
        self.ttval15=StringVar()
        self.ttval16=StringVar()
        self.ttval17=StringVar()

        #Tuesday values
        self.ttval21=StringVar()
        self.ttval22=StringVar()
        self.ttval23=StringVar()
        self.ttval24=StringVar()
        self.ttval25=StringVar()
        self.ttval26=StringVar()
        self.ttval27=StringVar()

        #Wednesday values
        self.ttval31=StringVar()
        self.ttval32=StringVar()
        self.ttval33=StringVar()
        self.ttval34=StringVar()
        self.ttval35=StringVar()
        self.ttval36=StringVar()
        self.ttval37=StringVar()

        #Thursday values
        self.ttval41=StringVar()
        self.ttval42=StringVar()
        self.ttval43=StringVar()
        self.ttval44=StringVar()
        self.ttval45=StringVar()
        self.ttval46=StringVar()
        self.ttval47=StringVar()

        #Friday values
        self.ttval51=StringVar()
        self.ttval52=StringVar()
        self.ttval53=StringVar()
        self.ttval54=StringVar()
        self.ttval55=StringVar()
        self.ttval56=StringVar()
        self.ttval57=StringVar()

        option1=self.ttk.Combobox(root1, width=20, textvariable=self.dept,state="readonly")
        option1['values']=("CSE","EEE","MECH","CIVIL","ECE")
        option1.grid(column=0,row=1,sticky='W')
        option1.current(0)
#**************************************************************************************************************

        ###choosing start time
        Time=tkinter.ttk.Label(root1, text="Please Choose the Year").grid(column=0,row=2,sticky='W')
        startTime=tkinter.ttk.Label(root1, text="Year").grid(column=0,row=3,sticky='W')

        ###Drop down days of the week
        Timedrop=tkinter.ttk.Combobox(root1, width=20, textvariable=self.year,state="readonly")
        Timedrop['values']=("I","II","III","IV")
        Timedrop.grid(column=0,row=4,sticky='W')
        Timedrop.current(0)
        
        tkinter.ttk.Label(root1,text="Please enter the table").grid(column=0,row=6,pady=10,sticky='W')
        tkinter.ttk.Label(root1,text="Period").grid(column=0,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="1").grid(column=1,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="2").grid(column=2,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="3").grid(column=3,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="4").grid(column=4,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="5").grid(column=5,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="6").grid(column=6,row=7,sticky='W')
        tkinter.ttk.Label(root1,text="7").grid(column=7,row=7,sticky='W')

        #------------------------ Monday Entry -------------------------
        tkinter.ttk.Label(root1,text="Monday").grid(column=0,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval11)
        self.Agenda.grid(column=1,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval12)
        self.Agenda.grid(column=2,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval13)
        self.Agenda.grid(column=3,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval14)
        self.Agenda.grid(column=4,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval15)
        self.Agenda.grid(column=5,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval16)
        self.Agenda.grid(column=6,row=8,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval17)
        self.Agenda.grid(column=7,row=8,sticky='W')

        #------------------------ Tuesday Entry -------------------------
        tkinter.ttk.Label(root1,text="Tuesday").grid(column=0,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval21)
        self.Agenda.grid(column=1,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval22)
        self.Agenda.grid(column=2,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval23)
        self.Agenda.grid(column=3,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval24)
        self.Agenda.grid(column=4,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval25)
        self.Agenda.grid(column=5,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval26)
        self.Agenda.grid(column=6,row=9,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval27)
        self.Agenda.grid(column=7,row=9,sticky='W')

        #------------------------ Wednesday Entry -------------------------
        tkinter.ttk.Label(root1,text="Wednesday").grid(column=0,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval31)
        self.Agenda.grid(column=1,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval32)
        self.Agenda.grid(column=2,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval33)
        self.Agenda.grid(column=3,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval34)
        self.Agenda.grid(column=4,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval35)
        self.Agenda.grid(column=5,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval36)
        self.Agenda.grid(column=6,row=10,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval37)
        self.Agenda.grid(column=7,row=10,sticky='W')

        #------------------------ Thursday Entry -------------------------
        tkinter.ttk.Label(root1,text="Thursday").grid(column=0,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval41)
        self.Agenda.grid(column=1,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval42)
        self.Agenda.grid(column=2,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval43)
        self.Agenda.grid(column=3,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval44)
        self.Agenda.grid(column=4,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval45)
        self.Agenda.grid(column=5,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval46)
        self.Agenda.grid(column=6,row=11,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval47)
        self.Agenda.grid(column=7,row=11,sticky='W')

        #------------------------ Friday Entry -------------------------
        tkinter.ttk.Label(root1,text="Friday").grid(column=0,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval51)
        self.Agenda.grid(column=1,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval52)
        self.Agenda.grid(column=2,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval53)
        self.Agenda.grid(column=3,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval54)
        self.Agenda.grid(column=4,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval55)
        self.Agenda.grid(column=5,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval56)
        self.Agenda.grid(column=6,row=12,sticky='W')
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.ttval57)
        self.Agenda.grid(column=7,row=12,sticky='W')

        def viewPrint():
            showbiz2.delete(1.0,END)
            self.messagebox.showinfo("View","The View button shows all the Events")
            if os.stat("text.txt").st_size==0:
                showbiz2.insert(INSERT,"No Event Found")
            else:
                with open ("text.txt","r")as file_new:
                    contents=file_new.read()
                    showbiz2.insert(INSERT,contents)
                    showbiz2.see(INSERT)
        def clean():
            showbiz2.delete(1.0,END)
            self.messagebox.showinfo("Clear","Please note that the clear button only cleans the display field but not the schedule. Please use 'DELETE EVENT' to delete any event")
            
                
        creat=Button(self.tab1,text="CREATE  ",bg='#4d79ff',fg='white',font=("Helvetica",14),command=self.addElement).grid(column=0,ipadx=62,pady=5,row=10,sticky="W")
        view=Button(self.tab1, text="All Event",bg='#ff5050',fg='white',font=("Helvetica",14),command=viewPrint).grid(column=0,ipadx=70,row=11,pady=5,sticky="W")
        clear=Button(self.tab1,text="CLEAR   ",bg='#ffc34d',fg='white',font=("Helvetica",14),command=clean).grid(column=0,ipadx=66,row=12,pady=5,sticky="W")

    def addElement(self):
        def allEvent():
            self.messagebox.showinfo("Created","Event Created")
            self.Agenda.delete(0,'end')
            self.main1.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main1.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main1.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main1.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main1.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("text.txt","a")
            file_new.write(str("Department: " + self.dept.get()+'\t'+"Year: " + self.year.get()+'\n'))
            if self.dept.get()=="CSE":
                file_new.write(str(self.main1)+'\n')
            elif self.dept.get()=="EEE":
                file_new.write(str(self.main2)+'\n')
            elif self.dept.get()=="MECH":
                file_new.write(str(self.main3)+'\n')
            elif self.dept.get()=="CIVIL":
                file_new.write(str(self.main4)+'\n')
            elif self.dept.get()=="ECE":
                file_new.write(str(self.main5)+'\n')

            file_new.close()
        def cse():
            self.main1.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main1.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main1.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main1.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main1.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("cse.txt","a")
            file_new.write(str('\n'+self.year.get()+'\n'))
            file_new.write(str(self.main1))
            file_new.close()
            allEvent()
        def eee():
            self.main2.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main2.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main2.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main2.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main2.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("eee.txt","w")
            file_new.write(str('\n'+self.year.get()+'\n'))
            file_new.write(str(self.main2))
            file_new.close()
            allEvent()

        def mech():
            self.main3.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main3.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main3.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main3.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main3.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("mech.txt","w")
            file_new.write(str('\n'+self.year.get()+'\n'))
            file_new.write(str(self.main3))
            file_new.close()
            allEvent()

        def civil():
            self.main4.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main4.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main4.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main4.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main4.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("civil.txt","w")
            file_new.write(str('\n'+self.year.get()+'\n'))
            file_new.write(str(self.main4))
            file_new.close()
            allEvent()

        def ece():
            self.main5.add_row(["Monday",self.ttval11.get(),self.ttval12.get(),self.ttval13.get(),self.ttval14.get(),self.ttval15.get(),self.ttval16.get(),self.ttval17.get()])
            self.main5.add_row(["Tuesday",self.ttval21.get(),self.ttval22.get(),self.ttval23.get(),self.ttval24.get(),self.ttval25.get(),self.ttval26.get(),self.ttval27.get()])
            self.main5.add_row(["Wednesday",self.ttval31.get(),self.ttval32.get(),self.ttval33.get(),self.ttval34.get(),self.ttval35.get(),self.ttval36.get(),self.ttval37.get()])
            self.main5.add_row(["Thursday",self.ttval41.get(),self.ttval42.get(),self.ttval43.get(),self.ttval44.get(),self.ttval45.get(),self.ttval46.get(),self.ttval47.get()])
            self.main5.add_row(["Friday",self.ttval51.get(),self.ttval52.get(),self.ttval53.get(),self.ttval54.get(),self.ttval55.get(),self.ttval56.get(),self.ttval57.get()])
            file_new=open("ece.txt","w")
            file_new.write(str('\n'+self.year.get()+'\n'))
            file_new.write(str(self.main5))
            file_new.close()
            allEvent()

        if self.dept.get()=="CSE":
            cse()
        elif self.dept.get()=="EEE":
            eee()
        elif self.dept.get()=="MECH":
            mech()
        elif self.dept.get()=="CIVIL":
            civil()
        elif self.dept.get()=="ECE":
            ece()
            

#************************************************************************************************************************
        """Retrieving the Table"""
    def retrieveTab(self):
        root2=tkinter.ttk.LabelFrame(self.tab2, text="Retrieve")
        greetings=tkinter.ttk.Label(self.tab2,text="Please click on the department and year you want to retrieve",font=self.customFont)
        greetings.grid(column=0,row=0,pady=5)
        
        self.yearet=StringVar()

        def printAllEvent():
            showbiz.delete(1.0,END)
            file_new=open("text.txt",'a')
            if os.stat("text.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, No Event Found")
            else:
                with open ("text.txt","a")as file_new:
                    file_new=open("text.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printCse():
            showbiz.delete(1.0,END)
            file_new=open("cse.txt","a")
            if os.stat("cse.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, CSE is Empty")
            else:
                with open ("cse.txt","a")as file_new:
                    file_new=open("cse.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printEee():
            showbiz.delete(1.0,END)
            file_new=open("eee.txt","a")
            if os.stat("eee.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, EEE is Empty")
            else:
                with open ("eee.txt","a")as file_new:
                    file_new=open("eee.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printMech():
            showbiz.delete(1.0,END)
            file_new=open("mech.txt",'a')
            if os.stat("mech.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, MECH is Empty")
            else:
                with open ("mech.txt","a")as file_new:
                    file_new=open("mech.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printCivil():
            showbiz.delete(1.0,END)
            file_new=open("civil.txt",'a')
            if os.stat("civil.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, CIVIL is Empty")
            else:
                with open ("civil.txt","a")as file_new:
                    file_new=open("civil.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printEce():
            showbiz.delete(1.0,END)
            file_new=open("ece.txt",'a')
            if os.stat("ece.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, ECE is Empty")
            else:
                with open ("ece.txt","a")as file_new:
                    file_new=open("ece.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
       
        cse=Button(self.tab2, text="CSE",bg="blue2",fg="white",font=("Helvetica",14),command=printCse).grid(column=0,row=2,ipadx=10,pady=5)
        cseyear=tkinter.ttk.Combobox(self.tab2, width=20, textvariable=self.yearet,state="readonly")
        cseyear['values']=("I","II","III","IV")
        cseyear.grid(column=1,row=2)
        cseyear.current(0)
        eee=Button(self.tab2, text="EEE",bg="#ff5050",fg="white",font=("Helvetica",14),command=printEee).grid(column=0,row=3,ipadx=10,pady=5)
        eeeyear=tkinter.ttk.Combobox(self.tab2, width=20, textvariable=self.yearet,state="readonly")
        eeeyear['values']=("I","II","III","IV")
        eeeyear.grid(column=1,row=3)
        eeeyear.current(0)
        mech=Button(self.tab2, text="MECH",bg="#ffc34d",fg="white",font=("Helvetica",14),command=printMech).grid(column=0,row=4,pady=5)
        mechyear=tkinter.ttk.Combobox(self.tab2, width=20, textvariable=self.yearet,state="readonly")
        mechyear['values']=("I","II","III","IV")
        mechyear.grid(column=1,row=4,sticky='W')
        mechyear.current(0)
        civil=Button(self.tab2, text="CIVIL",bg="#4d79ff",fg="white",font=("Helvetica",14),command=printCivil).grid(column=0,row=5,ipadx=10,pady=5)
        civilyear=tkinter.ttk.Combobox(self.tab2, width=20, textvariable=self.yearet,state="readonly")
        civilyear['values']=("I","II","III","IV")
        civilyear.grid(column=1,row=5,sticky='W')
        civilyear.current(0)
        ece=Button(self.tab2, text="ECE",bg="#009900",fg="white",font=("Helvetica",14),command=printEce).grid(column=0,row=6,pady=5,ipadx=24)
        eceyear=tkinter.ttk.Combobox(self.tab2, width=20, textvariable=self.yearet,state="readonly")
        eceyear['values']=("I","II","III","IV")
        eceyear.grid(column=1,row=6,sticky='W')
        eceyear.current(0)
        showbiz=Text(self.tab2,width=97,height=22)
        showbiz.grid(columnspan=3)
        allEvent=Button(self.tab2, text="All Events",bg="orange",fg="white",font=("Helvetica",14),command=printAllEvent).grid(column=1,row=7,ipadx=8,pady=5)    
#***********************************************************************************************************************
    def deleteEvent(self):
        def deleteCse():
            result=self.messagebox.askyesno("delete","Are you sure you want to delete CSE timetable ?")
            if result is True:
                file_new=open("cse.txt","w").close()
                self.messagebox.showinfo("Deleted","CSE timetable Deleted")
        def deleteEee():
            result=self.messagebox.askyesno("delete","Are you sure you want to delete CSE timetable ?")
            if result is True:
                file_new=open("eee.txt","w").close()
                self.messagebox.showinfo("Deleted","EEE timetable Deleted")
            
        def deleteMech():
            result=self.messagebox.askyesno("delete","Are you sure you want to delete CSE timetable ?")
            if result is True:
                file_new=open("mech.txt","w").close()
                tkMessageBox.showinfo("Deleted","MECH timetable Deleted")
        def deleteCivil():
            result=tkMessageBox.askyesno("delete","Are you sure you want to delete CSE timetable ?")
            if result is True:
                file_new=open("civil.txt","w").close()
                tkMessageBox.showinfo("Deleted","CIVIL timetable Deleted")
        def deleteEce():
            result=tkMessageBox.askyesno("delete","Are you sure you want to delete CSE timetable ?")
            if result is True:
                file_new=open("ece.txt","w").close()
                tkMessageBox.showinfo("Deleted","ECE timetable Deleted")
        def deleteAllEvent():
            result=tkMessageBox.askyesno("delete","Are you sure you want to delete All Time table?")
            files = ["text.txt", "cse.txt", "eee.txt", "ece.txt","mech.txt","civil.txt" ]
            if result is True:
                for file_name in files:
                    file_new=open(file_name,"w").close()
                tkMessageBox.showinfo("Deleted","All timetable Deleted")

        monday=Button(self.tab3, text="Delete CSE",bg='#4d79ff',fg='white',font=("Helvetica",14),command=deleteCse).pack(fill=X,padx=100,ipady=10,pady=10)
        tuesday=Button(self.tab3, text="Delete EEE",bg='#ff5050',fg='white',font=("Helvetica",14),command=deleteEee).pack(fill=X,padx=100,ipady=10,pady=10)
        wednesday=Button(self.tab3, text="Delete MECH",bg='#ffc34d',fg='white',font=("Helvetica",14),command=deleteMech).pack(fill=X,padx=100,ipady=10,pady=10)
        thursday=Button(self.tab3, text="Delete CIVIL",bg='#4d79ff',fg='white',font=("Helvetica",14),command=deleteCivil).pack(fill=X,padx=100,ipady=10,pady=10)
        friday=Button(self.tab3, text="Delete ECE",bg='#009900',fg='white',font=("Helvetica",14),command=deleteEce).pack(fill=X,padx=100,ipady=10,pady=10)
        allEvent=Button(self.tab3, text="Delete all Time table",bg='orange',fg='white',font=("Helvetica",14),command=deleteAllEvent).pack(fill=X,padx=100,ipady=10,pady=10)

app= EventApp()
app.root.mainloop()
