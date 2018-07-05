"""Imports"""
#++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime
from tkinter import *

import tkinter.ttk,tkinter.messagebox,tkinter.font,os
from prettytable import PrettyTable
import sqlite3
import os.path

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

        self.customFont = tkinter.font.Font(family="Helvetica", size=12)       

        #initializing functions
        self.root.resizable(0,0)
        self.createMenu()
        self.MainTabs()
        self.TabContent()
        self.retrieveTab()
        # self.deleteEvent()
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
        self.AddingEventTab.add(self.tab2, text="GENERATE TABLE")
        self.AddingEventTab.add(self.tab3, text="DELETE TABLE")
        self.AddingEventTab.pack(expand=10,pady=7, fill="both")

#**********************************************************************************************************
    """Adding content to the 'Add table tab'"""
    def TabContent(self):

        def desElement():
            root1.destroy()
            self.addElement()

        root1= tkinter.ttk.LabelFrame(self.tab1, text="Add TABLE")
        root1.grid(column=0, row=0,padx=8,pady=4,sticky="W")
        lab=tkinter.ttk.Label(root1, text="Please Choose the number of labs:").grid(column=0,row=1,sticky='W')
        self.lab=IntVar()
        self.Agenda=tkinter.ttk.Entry(root1,width=10,textvariable=self.lab)
        self.Agenda.grid(column=1,row=1,sticky='W')
        create=Button(root1,text="CREATE  ",bg='#4d79ff',fg='white',font=("Helvetica",14),command=desElement).grid(column=0,ipadx=62,pady=5,row=3,sticky="W")

        

    def addElement(self):

        numLabs = self.lab.get()

        def dbQuery():
            iterVal = self.iv
            sysNum = self.sysNum.get()
            windows = self.windows.get()
            ubuntu = self.ubuntu.get()
            codeBlocks = self.codeBlocks.get()
            python = self.Python.get()
            andStudio = self.andStudio.get()
            visStudio = self.visStudio.get()
            
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            dbPath = os.path.join(BASE_DIR, "lab.db")

            conn = sqlite3.connect(dbPath)
            c = conn.cursor()
            values = (sysNum,windows, ubuntu, andStudio, codeBlocks, python, visStudio)
            c.execute("INSERT INTO lab(systemNum,windows,ubuntu,androidStudio,codeBlocks,python,visualStudio) VALUES (?,?,?,?,?,?,?) ", values)
            conn.commit()
            conn.close()
            if iterVal == numLabs:
                return
            labEntry(iterVal+1,numLabs)

        def labEntry(iterVal, numLabs):
            self.iv         = iterVal
            self.sysNum     = IntVar()
            self.windows    = IntVar()
            self.ubuntu     = IntVar()
            self.codeBlocks = IntVar()
            self.Python     = IntVar()
            self.andStudio  = IntVar()
            self.visStudio  = IntVar()

            lab=tkinter.ttk.Label(root2, text="Please enter the details of lab "+str(iterVal)+":").grid(column=0,row=1,sticky='W')
            
            systemNum =tkinter.ttk.Label(root2, text="Enter the number of Systems: ").grid(column=0,row=2,sticky='W',padx=10, pady=10)

            
            Agenda=tkinter.ttk.Entry(root2,width=10,textvariable=self.sysNum)
            Agenda.grid(column=1,row=2,sticky='W')

            os=tkinter.ttk.Label(root2, text="Enter the OS used: ").grid(column=0,row=3,sticky='W')
            
            Checkbutton(root2, text="Windows", variable=self.windows).grid(column=0,row=4, sticky=W)
            Checkbutton(root2, text="Ubuntu", variable=self.ubuntu).grid(column=0,row=5, sticky=W)
            
            software = tkinter.ttk.Label(root2, text="Enter the Softwares used: ").grid(column=0,row=6,sticky='W')

            Checkbutton(root2, text="Codeblocks", variable=self.codeBlocks).grid(column=0,row=7, sticky=W)
            Checkbutton(root2, text="Python", variable=self.Python).grid(column=1,row=7, sticky=W)
            Checkbutton(root2, text="Android Studio", variable=self.andStudio).grid(column=0,row=8, sticky=W)
            Checkbutton(root2, text="Visual Studio", variable=self.visStudio).grid(column=1,row=8, sticky=W)

            if iterVal != numLabs:
                self.continueButton=Button(root2,text="Continue  ",bg='#4d79ff',fg='white',font=("Helvetica",14),command=dbQuery).grid(column=0,ipadx=62,pady=5,row=16,sticky="W")
            else:
                finish=Button(root2,text="Finish  ",bg='#4d79ff',fg='white',font=("Helvetica",14),command=dbQuery).grid(column=0,ipadx=62,pady=5,row=16,sticky="W")

        root2= tkinter.ttk.LabelFrame(self.tab1, text="ADD Details")
        root2.grid(column=0, row=0,padx=8,pady=4,sticky="W")
        labEntry(1,numLabs)


    def retrieveTab(self):
        root1= tkinter.ttk.LabelFrame(self.tab2, text="Assign Subjects")
        root1.grid(column=0, row=0,padx=8,pady=4,sticky="W")
        prof            =tkinter.ttk.Label(root1, text="Enter the Professor's name:").grid(column=0,row=1,sticky='W')
        
        self.prof       = StringVar()
        self.systemNum  = IntVar()
        self.windows    = IntVar()
        self.ubuntu     = IntVar()
        self.codeBlocks = IntVar()
        self.Python     = IntVar()
        self.andStudio  = IntVar()
        self.visStudio  = IntVar()

        self.profentry  =tkinter.ttk.Entry(root1,width=10,textvariable=self.prof)
        self.profentry.grid(column=1,row=1,sticky='W')
        systemNum       =tkinter.ttk.Label(root1, text="Enter the number of systems needed:").grid(column=0,row=2,sticky='W')
        self.systemNum =tkinter.ttk.Entry(root1,width=10,textvariable=self.systemNum)
        self.systemNum.grid(column=1,row=2,sticky='W')

        os=tkinter.ttk.Label(root1, text="Enter the OS needed: ").grid(column=0,row=3,sticky='W')
            
        Checkbutton(root1, text="Windows", variable=self.windows).grid(column=0,row=4, sticky=W)
        Checkbutton(root1, text="Ubuntu", variable=self.ubuntu).grid(column=0,row=5, sticky=W)
            
        software = tkinter.ttk.Label(root1, text="Enter the Softwares needed: ").grid(column=0,row=6,sticky='W')

        Checkbutton(root1, text="Codeblocks", variable=self.codeBlocks).grid(column=0,row=7, sticky=W)
        Checkbutton(root1, text="Python", variable=self.Python).grid(column=1,row=7, sticky=W)
        Checkbutton(root1, text="Android Studio", variable=self.andStudio).grid(column=0,row=8, sticky=W)
        Checkbutton(root1, text="Visual Studio", variable=self.visStudio).grid(column=1,row=8, sticky=W)

app= EventApp()
app.root.mainloop()