#Imaadh Uzair
#School Inventory Management System
#------------
import tkinter as tk
import sqlite3 as sqlite
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from pathlib import Path

database_pathfile = ''
database_pathfile = str(os.path.abspath("User_Details.db"))
#global variable used to store the pathfile of the database


folder_pathfile = ''
folder_pathfile = database_pathfile.replace(r"\User_Details.db" , "")
#global variable used to store the pathfile of the application folder

userLoggedIn = ''
#global variable to store the username of the user that is currently logged in


def exit_btn(window_input):
        top = window_input
        top.destroy()
#defining a function which takes in a  window and destroys it

def setUserLoggedIn():
        global userLoggedIn
        userLoggedIn = ''
        print(userLoggedIn)

#short functions for verifying if input contains digits, lowercase and uppercase letters:
def hasNumber(inputString):
        return any(char.isdigit() for char in inputString)
        #check if inputString has any numbers
            
def hasUpper(inputString):
        return any(char.isupper() for char in inputString)
        #check if inputString has any uppercase letters
            
def hasLower(inputString):
        return any(char.islower() for char in inputString)
        #check if inputString has any lowercase letters
        

###################Initiation - Opening the program for the first time###################



#add the creation of user_details into first_ open so that init cannot be skipped. also make creation of user_details after the user has inputted a valid username and passwords
#under addDetails funct
def first_open():
    
    toplevel_font = ("Bedini", 8)
    
    window = tk.Tk()
    window.config(bg='#ffffff')
    window.geometry('1280x720')
    window.title('Register')
    

    def addDetails(username, password):
        #function for adding details to the database
        
        #if the entered username and password meet the requirements, then create the source database
        
        user_details = sqlite.connect("User_Details.db")
        c = user_details.cursor()
        c.execute('''CREATE TABLE Admin
                (adminID integer,
                user_name text,
                password text
                )
                ''')
        #Admin table to store admin details
        c.execute('''CREATE TABLE User
                (userID integer,
                user_name text,
                password text,
                first_name text,
                last_name text,
                departmentID integer
                )
                ''')
        #User table to store normal user details
        c.execute('''CREATE TABLE Item
                (itemID integer,
                item_name text,
                item_desc text
                )
                ''')
        #Item table to uniquely store details of existing items  
        c.execute('''CREATE TABLE Department
                (departmentID integer,
                department_name text,
                department_desc text
                )
                ''')
        #Department table to store department ID, name and details
        c.execute('''CREATE TABLE Room
                (roomID integer,
                room_name text,
                room_desc text
                )
                ''')
        #Room table to store room ID, name and details
        c.execute('''CREATE TABLE ItemRoom
                (itemID integer,
                roomID integer,
                item_Quantity integer
                )
                ''')
        #'ItemRoom' link table to link 'item' and 'room' table 
        c.execute('''CREATE TABLE RoomDept
                (roomID integer,
                departmentID integer
                )
                ''')
        #UserDept table to link 'Room' and 'Department' tables

        c.execute('''CREATE TABLE ItemDept
                (itemID integer,
                departmentID integer
                )
                ''')
        #'ItemDept' link table to link 'item' and 'department' table 

        c.execute('''INSERT INTO Department(departmentID, department_name)
                VALUES(0,"Select a Department")''')
        #adding placeholder text into department table

        

        
        
        global database_pathfile
        database_pathfile = str(os.path.abspath("User_Details.db"))
        #storing the pathfile of 'User_Details.db' in the 'database_pathfile' global variable
        
        #adding the details to the fields in the database
        detailsAdd = '''INSERT INTO Admin
                (adminID,user_name,password)
                VALUES(?,?,?);'''
        
        #adminID is '1' becase it is the first user to be initiated onto the program.
        adminDetails = (1,username,password)
        
        c.execute(detailsAdd,adminDetails)

        user_details.commit()
        user_details.close()

        global userLoggedIn
        userLoggedIn = username
        #username of the user stored in userLoggedIn variable


        
    #defining event handler for the 'submit' button:
    def submit_click(event):        
        username_get = username_ent.get()
        password_get = password_ent.get()
        re_enter_get = re_enter_ent.get()
        #getting the inputs from each of the entry widgets respectively

        usernameCheck = False
        passwordCheck = False
        #two boolean variables for the two loops



        #not str.islower() and not str.isupper()
        
        
        #while loop for verifying usernames
        
        while (usernameCheck == False):
            if (len(username_get) > 2) and (' ' not in username_get):
                usernameCheck = True
                break
                #setting the loop condition to 'True' and breaking the loop if the username meets the conditions
            elif (' ' in username_get):
                usernameFail_tp = tk.Toplevel()
                usernameFail_tp.geometry('250x250')
                usernameFail_tp.title('Error')
                usernameFailText = tk.Label(master= usernameFail_tp, text = 'Username cannot contain spaces',font = ("Bedini", 10))
                usernameFailText.pack(side=TOP, padx = 5, pady = 10)
                usernameFailClose = tk.Button(master = usernameFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(usernameFail_tp)])
                usernameFailClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #a toplevel window if the username contains spaces, and not breaking the loop
            elif (len(username_get) < 3):
                usernameFail_tp = tk.Toplevel()
                usernameFail_tp.geometry('250x250')
                usernameFail_tp.title('Error')
                usernameFailText = tk.Label(master= usernameFail_tp, text = 'Username has to be 3 or more characters',font = ("Bedini", 10))
                usernameFailText.pack(side=TOP, padx = 5, pady = 10)
                usernameFailClose = tk.Button(master = usernameFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(usernameFail_tp)])
                usernameFailClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #a toplevel window if the username length is less than 3 characters.
            
            
                
        

        #while loop for checking passwords, will only run if usernameCheck is True. and passwordCheck is False.
            
        while (passwordCheck == False) and (usernameCheck == True):
            
            
            
            if hasNumber(password_get) and hasUpper(password_get) and hasLower(password_get) and (len(password_get) > 5) and (' ' not in password_get) and (password_get == re_enter_get):
                #set passwordCheck to True so that the loop will not run again and break the loop if all the login information meet the requirements
                passwordCheck = True
                addDetails(username_get, password_get)
                #running the addDetails function to create the database and add the details to the database
                global userLoggedIn
                userLoggedIn = username_get
                veriSuc_tp = tk.Toplevel()
                veriSuc_tp.geometry('250x250')
                veriSuc_tp.title('')
                veriSuc_tpText1 = tk.Label(master = veriSuc_tp, text = 'Success',font = ("Bedini", 8))
                veriSuc_tpText2 = tk.Label(master = veriSuc_tp, text = f'Your username is: {username_get}.\n Your password is: {password_get}')
                veriSuc_tpText1.pack(side=TOP, padx = 5, pady = 10)
                veriSuc_tpText2.pack(side=TOP, padx = 5, pady = 10)
                veriSuc_tpClose = tk.Button(master = veriSuc_tp, text = 'Continue to admin interface', width = 20, height = 1,font = toplevel_font,
                                            command=lambda:[exit_btn(veriSuc_tp), exit_btn(window), adminMain()])
                #using exit_btn() function to close the 'veriSuc_tp' window as well as the 'window' main window when the verification is sucessful
                veriSuc_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                
                break            
                #a toplevel window if the all the entries meet the requirements (password has a lowercase, uppercase letter, has a number and is longer than 6 characters and has no spaces.

            elif password_get != re_enter_get:
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Passwords do not match',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window if paswords do not match
            
            elif (' ' in password_get):
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Password cannot contain spaces',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window if the password has spaces
            
            elif len(password_get) < 6:
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Password must be 6 or more characters',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window is the password is too short

            elif (hasLower(password_get) == False):
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Password must contain at least one lowercase letter',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window if password does not have a lowercase letter
            
            elif (hasUpper(password_get) == False):
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Password must contain at least one uppercase letter',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window if  pasword does not have an uppercase letter
            
            
            
            elif (hasNumber(password_get) == False):
                veriFail_tp = tk.Toplevel()
                veriFail_tp.geometry('250x250')
                veriFail_tp.title('Error')
                veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Password must contain at least one number',font = ("Bedini", 8))
                veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
                veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
                veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
                break
                #error window if pasword does not have a digit
            
    def first_open_db():
        open_popup = tk.Toplevel()
        open_popup.geometry('250x250')
        open_popup.title('')
        #creating a function called first_open_db which creates a Toplevel() window and giving it size and title
        open_popup_txt = tk.Label(master= open_popup, text = 'Choose a source Database(.db) file.\nContact your admin for more information.\nSource file is User_Details.db',
                                  font = ("Bedini", 10))
        open_popup_txt.pack(side=TOP, padx = 5, pady = 10)
        open_popup_close = tk.Button(master = open_popup, text = 'Close', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(open_popup)])
        open_popup_close.pack(side=LEFT, padx = 20, pady = 5)
        #open_popup_close allows user to close the Toplevel window by running the exit_btn() function and passing its' own Toplevel into the function.
        open_popup_db_choose = tk.Button(master = open_popup, text = 'Choose a File', width = 10, height = 1,font = toplevel_font, command=lambda:[exit_btn(open_popup), second_open_db()])
        open_popup_db_choose.pack(side=RIGHT, padx = 20, pady = 5)
        #open_popup_db_choose allows user to choose a file, which will run the command exit_btn()and second_open_db(), closing the window and running the code to select a file.
        open_popup.mainloop()

    def second_open_db():
        #creating a function called second_open_db which uses askopenfilename() and Windows explorer to select a file, and storing the filename in variable 'filepath'
        filepath = askopenfilename(
            filetypes=[("Database Files", "*.db"), ("All Files", "*.*")])
        if filepath.endswith('User_Details.db'):
            global database_pathfile
            database_pathfile = str(filepath)
            #if the file selected is a .db file, then save the filepath to the global variable 'database_pathfile' 
            success_db = tk.Toplevel()
            success_db.title('')
            success_db.geometry('250x250')
            #configuring the Toplevel window
            success_txt = tk.Label(master = success_db, text = 'Success\nSource file found', width = 15, font = toplevel_font)
            success_txt.pack(side=TOP, padx = 10, pady = 10)
            success_btn = tk.Button(master = success_db, text = 'Go to login', command=lambda:[exit_btn(success_db), exit_btn(window), normal_open()], font = toplevel_font)
            #closing the initiation page and opening the login UI when the file is successfully selected
            success_btn.pack(side=BOTTOM, padx = 20, pady = 20)
            success_btn.pack()
            success_txt.pack()
            #similar buttons as before except there is no other function for the button, only closes the windowsuccess_db.mainloop()
        else:
            error_db = tk.Toplevel()
            error_db.title('')
            error_db.geometry('250x250')
            #if the file selected is not a .db file, then show an error window
            error_txt = tk.Label(master = error_db, text = 'File chosen is not the source database file', font = toplevel_font)
            error_txt.pack(side=TOP, padx = 10, pady = 10)
            error_btn = tk.Button(master = error_db, text = 'Close', command=lambda:[exit_btn(error_db)], font = toplevel_font)
            error_btn.pack(side=BOTTOM, padx = 20, pady = 20)
            #same buttons as before, text states that the file is not a database file.
            error_db.mainloop()
                        
    #creating the frame for initialisation interface
    init_frm = tk.Frame(master = window) 
    init_frm.pack(fill = BOTH, expand = True)
    init_frm.config(bg='#42f5da')
    #configuring the rows and columns for the widgets:
    init_frm.rowconfigure([0,1,2,3,4,5], weight=1, minsize=100)
    #rows are for the 'welcome' label, 'username' entry and label, 'password' entry and label, 'submit' button and 'error' button
    init_frm.columnconfigure([1,2], weight=3)
    #giving the middle columns weight of 3 so it is 3x bigger than the outer two columns
    init_frm.columnconfigure([0,3],weight=1)
    #two columns on edge to ensure that the main widgets stay in the middle
    #welcome label widget
    welcome_lbl = tk.Label(master=init_frm,text='Welcome. Create your account:',font=("Bedini", 20),fg='black',bg='#42f5da')
    
    #username label and entry widget
    username_lbl = tk.Label(master=init_frm,text='Username:',font=("Bedini", 15),fg='black',bg='#42f5da')
    username_ent = tk.Entry(master=init_frm,fg='black',bg='white',width=45)
    
    #password label and entry widget
    password_lbl = tk.Label(master=init_frm,text='Password:',font=("Bedini", 15),fg='black',bg='#42f5da')
    password_ent = tk.Entry(master=init_frm,fg='black',bg='white',width=45)
    password_ent.config(show='*')
    
    #re-enter password label and entry widget
    re_enter_lbl = tk.Label(master=init_frm,text='Re-enter Password:',font=("Bedini", 15),fg='black',bg='#42f5da')
    re_enter_ent = tk.Entry(master=init_frm,fg='black',bg='white',width=45)
    re_enter_ent.config(show='*')
    #'submit' button widget
    submit_btn = tk.Button(master=init_frm,text='Submit',font=("Bedini", 12),fg='white',bg='black',width=10,height=2,borderwidth = 5)
    submit_btn.bind('<Button-1>', submit_click)
    error_btn = tk.Button(master=init_frm,text='Not first time launching this program?',font=('Courier',8),fg='black',bg='white',width=37,command = first_open_db, borderwidth = 3)

    #assigning the different widgets to their places in the grid
    welcome_lbl.grid(row=0,column=1,pady=5,padx=5,columnspan=2)
    username_lbl.grid(row=1,column=1,pady=5, padx=5)
    username_ent.grid(row=1,column=2,pady=5,padx=5)
    password_lbl.grid(row=2,column=1,pady=5,padx=5)
    password_ent.grid(row=2,column=2,pady=5,padx=5)
    re_enter_lbl.grid(row=3,column=1, pady=5,padx=5)
    re_enter_ent.grid(row=3,column=2,pady=5,padx=5)
    submit_btn.grid(row=4,column=1,pady=5,padx=5,columnspan=2)
    error_btn.grid(row=5,column=0,padx=5,pady=5,columnspan=2,sticky = 'sw')
    #a button for if an error occours and the user has already initiated an account
    window.mainloop()


    
    

def normal_open():
    global database_pathfile
    database_pathfile = str(os.path.abspath("User_Details.db"))
    
    #verification after entering login details
    def login_verification(event):
        username_get = username_ent.get()
        password_get = password_ent.get()
        detailsEntered = [str(username_get), str(password_get)]
        #loop variables
        user_details = sqlite.connect(database_pathfile)
        c = user_details.cursor()
        #connecting to database stores in variable 'database_pathfile' 
        
        #fetching from database

        c.execute('''SELECT user_name, password, adminID
                FROM Admin
                ''')
        a_u_p_fetch = c.fetchall()
        #fetching all the usernames and passwords from 'admin' table

        c.execute('''SELECT user_name, password, userID
                FROM User
                ''')
        u_u_p_fetch = c.fetchall()
        #fetching all the usernames and passwords from 'user' table
        
        loopLength = len(a_u_p_fetch) + len(u_u_p_fetch)
        #setting the loop length as the length of the username combos in the 'admin' and 'user' table added together
        
        #for loop to check if the details entered match any combinations in the database
        try:
            for x in range (loopLength + 1):
                #loopLength+1 as the iterative range because easier to break the loop with try, except
                
                if (detailsEntered[0] == a_u_p_fetch[x][0] and detailsEntered[1] == a_u_p_fetch[x][1]) or (detailsEntered[0] == u_u_p_fetch[x][0] and detailsEntered[1] == u_u_p_fetch[x][1]):
                    #if details entered match any combination of username and password, show a success popup and redirect the user to the homepage.
                    veriSuc_tp = tk.Toplevel()
                    veriSuc_tp.geometry('250x250')
                    veriSuc_tp.title('')
                    veriSuc_tpText1 = tk.Label(master = veriSuc_tp, text = 'Success',font = ("Bedini", 8))
                    veriSuc_tpText2 = tk.Label(master = veriSuc_tp, text = f'Successful login')
                    veriSuc_tpText1.pack(side=TOP, padx = 5, pady = 10)
                    veriSuc_tpText2.pack(side=TOP, padx = 5, pady = 10)
                    veriSuc_tpClose = tk.Button(master = veriSuc_tp, text = 'Click to go to homepage', width = 20, height = 1,font = toplevel_font,
                                                command=lambda:[exit_btn(veriSuc_tp), exit_btn(window), userDetermine(username_get, password_get)])
                    #using exit_btn() function to close the 'veriSuc_tp' window and main window
                    veriSuc_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)

                    
                    #storing the user/adminID into the global variable userLoggedIn so that the program knows which user is logged in via the ID.
                        
                    break
                else:
                    continue

        except IndexError:
            veriFail_tp = tk.Toplevel()
            veriFail_tp.geometry('250x250')
            veriFail_tp.title('Error')
            veriFail_tpText = tk.Label(master = veriFail_tp, text = 'Username and password combination is incorrect',font = ("Bedini", 8))
            veriFail_tpText.pack(side=TOP, padx = 5, pady = 10)
            veriFail_tpClose = tk.Button(master = veriFail_tp, text = 'Try Again', width = 7, height = 1,font = toplevel_font, command=lambda:[exit_btn(veriFail_tp)])
            veriFail_tpClose.pack(side=BOTTOM, padx = 20, pady = 5)
            
        
        
                
                    
                
    toplevel_font = ("Bedini", 8)
    
    window = tk.Tk()
    window.config(bg='#ffffff')
    window.geometry('1280x720')
    window.title('Log In')
    
    
    
    login_frm  = tk.Frame(master = window)
    login_frm.pack(fill = BOTH, expand = True)
    login_frm.config(bg='#42f5da')

    #configuring the rows and columns for the widgets:
    login_frm.rowconfigure([0,1,2,3], weight=1)
    #row configuration
    login_frm.columnconfigure([1,2], weight=3)
    #giving the middle columns weight of 3 so it is 3x bigger than the outer two columns
    login_frm.columnconfigure([0,3],weight=1)
    #two columns on edge to ensure that the main widgets stay in the middle

    welcome_lbl = tk.Label(master=login_frm,text='Welcome. Log in to your account:',font=("Bedini", 20),fg='black',bg='#42f5da')
    #welcome label
    username_lbl = tk.Label(master=login_frm,text='Username:',font=("Bedini", 15),fg='black',bg='#42f5da')
    username_ent = tk.Entry(master=login_frm,fg='black',bg='white',width=45)
    #username label and entry and storing the input in username_get
    password_lbl = tk.Label(master=login_frm,text='Password:',font=("Bedini", 15),fg='black',bg='#42f5da')
    password_ent = tk.Entry(master=login_frm,fg='black',bg='white',width=45)
    password_ent.config(show='*')
    #password label and entry and storing the input in password_get
    #'submit' button widget
    submit_btn = tk.Button(master=login_frm,text='Submit',font=("Bedini", 12),fg='white',bg='black',width=10,height=2, borderwidth = 5)
    submit_btn.bind('<ButtonRelease-1>', login_verification)
    

    #configuring the locations of the widgets
    welcome_lbl.grid(row=0,column=1,pady=5,padx=5,columnspan=2)
    username_lbl.grid(row=1,column=1,pady=5, padx=5)
    username_ent.grid(row=1,column=2,pady=5,padx=5)
    password_lbl.grid(row=2,column=1,pady=5,padx=5,)
    password_ent.grid(row=2,column=2,pady=5,padx=5,)
    submit_btn.grid(row=3,column=1,pady=5,padx=5,columnspan = 2)
    
    window.mainloop()


def userDetermine(username, password):
        userDetails = sqlite.connect(database_pathfile)
        c = userDetails.cursor()
        c.execute('''SELECT user_name, password FROM Admin WHERE user_name = ? AND password = ?''', (username,password,))
        adminFetch = c.fetchall()
        c.execute('''SELECT user_name, password FROM User WHERE user_name = ? AND password = ?''', (username,password,))
        userFetch = c.fetchall()
        adminUser = False
        userUser = False
        
        try:
                adminFetch[0][0]
                
                adminUser = True
        except IndexError:
                pass
        
        try:
                userFetch[0][0]
                userUser = True
        except IndexError:
                pass
                

        
        global userLoggedIn
        
        if adminUser == True:
                userLoggedIn = username
                adminMain()
        elif userUser == True:
                userLoggedIn = username
                userMain()
                


#########MAIN PROGRAM#####################
def adminMain():
        mainwindow = Tk()
        mainwindow.title('Admin')
        mainwindow.geometry('1280x720')
        m = Admin(mainwindow)
        mainwindow.mainloop()
#function to call the admin UI

def userMain():
        mainwindow = Tk()
        mainwindow.title('User')
        mainwindow.geometry('1280x720')
        m = User(mainwindow)
        mainwindow.mainloop()
#function to call the user UI



class Admin:
        #class for the admin UI
        def __init__(self, master):
                self.master = master
                #assigning the 'master' attribute to the window/root that is passed into the init function

                
                
                self.adminFont = ('Arial', 10)
                self.adminLargeFont = ('Arial', 20)
                #global fonts for the admin UI
                
                #########homepage frame#######
                self.homepageFrm = Frame(master = self.master)
                self.homepageFrm.config(bg = 'white')
                self.homepageFrm.rowconfigure([0,1,2,3,4,5], weight = 1)
                self.homepageFrm.columnconfigure([0,2], weight = 1)
                self.homepageFrm.columnconfigure(1, weight = 3)
                self.homepageFrm.pack(fill = BOTH, expand = True)
                #packing the homepageFrm as it is the first screen displayed when the program is opened
                #configuring dimensions for the homepage

                self.settingsBtn = Button(master = self.homepageFrm, width = 9, height = 4, text = 'Settings', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.settingsFrm, self.homepageFrm)])
                self.settingsBtn.grid(row = 0, column = 2, padx = 10, sticky = 'e')
                #settings button to go to the settings page

                self.newDeptBtn = Button(master = self.homepageFrm, text = 'Create a new Department', width = 70, height = 3, font = self.adminFont,
                                             bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.newDeptFrm, self.homepageFrm)])
                self.newDeptBtn.grid(row = 0, column = 1 , columnspan = 1)
                #a button to create a new department - takes to new department page

                self.newItemBtn = Button(master = self.homepageFrm, text = 'Create a new Item instance', width = 70, height = 3, font = self.adminFont,
                                             bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.newItemFrm, self.homepageFrm)])
                self.newItemBtn.grid(row = 1, column = 1 , columnspan = 1)
                #a button to create a new department - takes to new item page

                self.newUsersBtn = Button(master = self.homepageFrm, text = 'Create a new User', width = 70, height = 3, font = self.adminFont,
                                             bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.newUsersFrm, self.homepageFrm)])
                self.newUsersBtn.grid(row = 2, column = 1 , columnspan = 1)
                #button to create a new user - takes to new user page

                self.newRoomBtn = Button(master = self.homepageFrm, text = 'Create a new Room', width = 70, height = 3, font = self.adminFont,
                                             bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.newRoomFrm, self.homepageFrm)])
                self.newRoomBtn.grid(row = 3, column = 1 , columnspan = 1)
                #button to create a new room - takes to new rooms page
                

                self.manageUsersBtn = Button(master = self.homepageFrm, text = 'Manage Users', width = 70, height = 3, font = self.adminFont,
                                                bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.manageUsersFrm, self.homepageFrm)])
                self.manageUsersBtn.grid(row = 4, column = 1 , columnspan = 1)
                #button to take user to 'manage users' page
                
                self.manageRoomsBtn = Button(master = self.homepageFrm, text = 'Manage Rooms', width = 70, height = 3, font = self.adminFont,
                                                bg = 'black', fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.manageRoomsFrm, self.homepageFrm)])
                self.manageRoomsBtn.grid(row = 5, column = 1 , columnspan = 1)
                #button to take user to 'manage rooms' page

                self.refreshBtn = Button(master = self.homepageFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 3, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 0, column = 0, padx = 10,sticky = 'w')




                ############new users page############
                self.newUsersFrm = Frame(master = self.master)
                self.newUsersFrm.config(bg = 'black')
                self.newUsersFrm.rowconfigure([0,1,2,3,4,5], weight = 1)
                self.newUsersFrm.columnconfigure([0,1,2], weight = 1)
                self.newUsersFrm.columnconfigure(3, weight = 3)
                #dimensions for the new users page 
                self.newUserReturnBtn = Button(master = self.newUsersFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.newUsersFrm)])
                self.newUserReturnBtn.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 5)
                #button to return to the homepage, uses self.showFrame function
                self.newUserTopLbl = Label(master = self.newUsersFrm, width = 50, height = 3, text = 'Create a new user:', fg = 'white' , bg = 'black', font = self.adminLargeFont)
                self.newUserTopLbl.grid(row = 0, column = 1, columnspan = 2,sticky = 'nsew')
                #heading at the top of the page
                self.newUserFirstEnt = Entry(master = self.newUsersFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newUserFirstEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.newUserFirstLbl = Label(master = self.newUsersFrm,text = 'Firstname:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newUserFirstLbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #firstname entry and label saying 'firstname'
                self.newUserLastEnt = Entry(master = self.newUsersFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newUserLastEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.newUserLastLbl = Label(master = self.newUsersFrm,text = 'Lastname', width = 50, font = self.adminFont, fg = 'white', bg = 'black')
                self.newUserLastLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #lastname entry and label saying 'lastname'
                self.newUserUserEnt = Entry(master = self.newUsersFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newUserUserEnt.grid(row = 3, column = 2, padx = 10, pady = 10)
                self.newUserUserLbl = Label(master = self.newUsersFrm,text = 'Username(optional):', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newUserUserLbl.grid(row = 3, column = 1, padx = 10, pady = 10,sticky = 'e')
                #username entry and label saying 'username'
                self.departmentList = self.getDepartmentList()
                #using the function getDepartmentList to get a list of the departments stored in the database.
                self.variable = tk.StringVar(master)
                self.variable.set(self.departmentList[0])
                self.newUserDeptMenu = OptionMenu(self.newUsersFrm, self.variable ,*self.departmentList)
                                                  #command=self.optionMenuGet)
                #using self.variable so that the drop-down menu will show what is selected on the menu bar
                self.newUserDeptMenu.grid(row = 4, column = 2, padx = 10, pady = 10,sticky = 'ew')
                self.newUserMenuLbl = Label(master = self.newUsersFrm, text = 'Department:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newUserMenuLbl.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = 'e')
                #packing the drop-down menu and its' label
                self.newUserSubmitBtn = Button(master = self.newUsersFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                               command=lambda:[self.newUser(self.newUserFirstEnt.get(),self.newUserLastEnt.get(), self.newUserUserEnt.get(),
                                                                            self.variable.get())]) 
                self.newUserSubmitBtn.grid(row = 5, column = 1, padx = 10, pady = 10, columnspan = 2)
                #submit button

                self.refreshBtn = Button(master = self.newUsersFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')

                

                ############new department page###########

                self.newDeptFrm = Frame(master = self.master)
                self.newDeptFrm.config(bg = 'black')
                self.newDeptFrm.rowconfigure([0,1,2,3], weight = 1)
                self.newDeptFrm.columnconfigure([1,2], weight = 2)
                self.newDeptFrm.columnconfigure([0,3], weight = 1)
                #dimensions for the new department frame

                self.newDeptReturnBtn = Button(master = self.newDeptFrm, text='Return',width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.newDeptFrm)])
                self.newDeptReturnBtn.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 5)
                #button to return to the homepage, uses self.showFrame function

                self.newDeptTopLbl = Label(master = self.newDeptFrm, width = 50, height = 3, text = 'Create a new Department:', fg = 'white' , bg = 'black', font = self.adminLargeFont)
                self.newDeptTopLbl.grid(row = 0, column = 1, columnspan = 2,sticky = 'nsew')
                #label at the top of the department page

                self.newDeptDeptEnt = Entry(master = self.newDeptFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newDeptDeptEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.newDeptDeptLbl = Label(master = self.newDeptFrm,text = 'Department Name:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newDeptDeptLbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #deparment text and entry

                self.newDeptDescEnt = Entry(master = self.newDeptFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newDeptDescEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.newDeptDescLbl = Label(master = self.newDeptFrm,text = 'Description(optional):', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newDeptDescLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #dept desciption and entry

                self.newDeptSubmitBtn = Button(master = self.newDeptFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                               command=lambda:[self.newDepartment(self.newDeptDeptEnt.get(), self.newDeptDescEnt.get())]) 
                self.newDeptSubmitBtn.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)



                #################new item page#################

                self.newItemFrm = Frame(master = self.master)
                self.newItemFrm.config(bg = 'black')
                self.newItemFrm.rowconfigure([0,1,2,3,4], weight = 1)
                self.newItemFrm.columnconfigure([1,2], weight = 2)
                self.newItemFrm.columnconfigure([0,3], weight = 1)
                #dimensions for the new item frame

                self.newItemReturnBtn = Button(master = self.newItemFrm, text='Return',width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.newItemFrm)])
                self.newItemReturnBtn.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 5)
                #button to return to the homepage, uses self.showFrame function

                self.newItemTopLbl = Label(master = self.newItemFrm, width = 50, height = 3, text = 'Create a new Item:', fg = 'white' , bg = 'black', font = self.adminLargeFont)
                self.newItemTopLbl.grid(row = 0, column = 1, columnspan = 2,sticky = 'nsew')
                #label at the top of the item page

                self.newItemItemEnt = Entry(master = self.newItemFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newItemItemEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.newItemItemLbl = Label(master = self.newItemFrm,text = 'Item Name:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newItemItemLbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #item text and entry

                self.newItemDescEnt = Entry(master = self.newItemFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newItemDescEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.newItemDescLbl = Label(master = self.newItemFrm,text = 'Description(optional):', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newItemDescLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #item desciption and entry


                self.itemVariable = tk.StringVar(master)
                self.itemVariable.set(self.departmentList)
                
                self.newItemDeptLst = Listbox(master = self.newItemFrm, listvariable = self.itemVariable, selectmode=MULTIPLE, fg = 'white', bg = 'black', font = self.adminFont)
                self.newItemDeptLst.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)
                
                #item desciption and entry

                self.newItemSubmitBtn = Button(master = self.newItemFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                               command=lambda:[self.newItem(self.newItemItemEnt.get(), self.newItemDescEnt.get(),self.newItemDeptLst)]) 
                self.newItemSubmitBtn.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2)
                #submit button for new item page
                
                self.refreshBtn = Button(master = self.newItemFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')



                ################new rooms page##############
                self.newRoomFrm = Frame(master = self.master)
                self.newRoomFrm.config(bg = 'black')
                self.newRoomFrm.rowconfigure([0,1,2,3,4], weight = 1)
                self.newRoomFrm.columnconfigure([1,2], weight = 2)
                self.newRoomFrm.columnconfigure([0,3], weight = 1)
                #dimensions for the new rooms frame
                
                self.newRoomReturnBtn = Button(master = self.newRoomFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.newRoomFrm)])
                self.newRoomReturnBtn.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 5)
                #button to return to the homepage, uses self.showFrame function

                self.newRoomTopLbl = Label(master = self.newRoomFrm, width = 50, height = 3, text = 'Create a new Room:', fg = 'white' , bg = 'black', font = self.adminLargeFont)
                self.newRoomTopLbl.grid(row = 0, column = 1, columnspan = 2,sticky = 'nsew')
                #label at the top of the page

                self.newRoomRoomEnt = Entry(master = self.newRoomFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newRoomRoomEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.newRoomRoomLbl = Label(master = self.newRoomFrm,text = 'Room name/Code:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newRoomRoomLbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #room name entry and text

                self.newRoomDescEnt = Entry(master = self.newRoomFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.newRoomDescEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.newRoomDescLbl = Label(master = self.newRoomFrm,text = 'Description(optional):', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newRoomDescLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #room desc and text
                
                #self.variable and self.departmentList has already been created in new department page so dont need to create again
                self.newRoomDeptMenu = OptionMenu(self.newRoomFrm, self.variable ,*self.departmentList) 
                self.newRoomDeptMenu.grid(row = 3, column = 2, padx = 10, pady = 10,sticky = 'ew')
                self.newRoomDeptLbl = Label(master = self.newRoomFrm,text = 'Department:', font = self.adminFont, width = 50, fg = 'white', bg = 'black')
                self.newRoomDeptLbl.grid(row = 3, column = 1, padx = 10, pady = 10,sticky = 'e')
                #room department label and entry
                
                self.newRoomSubmitBtn = Button(master = self.newRoomFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                               command=lambda:[self.newRoom(self.newRoomRoomEnt.get(), self.newRoomDescEnt.get(), self.variable.get())]) 
                self.newRoomSubmitBtn.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2)
                #submit button

                self.refreshBtn = Button(master = self.newRoomFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')


                

                #############settings page########
                self.settingsFrm = Frame(master = self.master)
                self.settingsFrm.config(bg = 'white')
                self.settingsFrm.rowconfigure([0], weight = 2)
                self.settingsFrm.rowconfigure([1,2], weight = 1)
                self.settingsFrm.columnconfigure([1], weight = 2)
                self.settingsFrm.columnconfigure([0,2], weight = 1)
                #dimensions for the new department frame
                
                self.settingsReturnBtn = Button(master = self.settingsFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.settingsFrm)])
                self.settingsReturnBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to the homepage, uses self.showFrame function

                self.settingsLogoutBtn = Button(master = self.settingsFrm, text='Logout', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.logoutConfirm(self.master)])
                self.settingsLogoutBtn.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'ne')
                #button to logout, uses self.logoutConfirm function

                self.settingsTopLbl = Label(master = self.settingsFrm, width = 50, height = 3, text = 'Settings:', fg = 'black' , bg = 'white', font = self.adminLargeFont)
                self.settingsTopLbl.grid(row = 0, column = 1)
                #label at the top of the page
                
                self.settingsDetailsBtn = Button(master = self.settingsFrm,text = 'Edit your Details', font = self.adminFont, width = 50, height = 5, fg = 'white', bg = 'black',
                                                 command=lambda:[self.showFrame(self.changeDetFrm, self.settingsFrm)])
                self.settingsDetailsBtn.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'n')
                #button to edit details, takes user to changeDetFrm frame
                

                self.settingsSourceBtn = Button(master = self.settingsFrm,text = 'Change Source(.db) file', width = 50, height = 5, font = self.adminFont, fg = 'white',
                                               bg = 'black', command=lambda:[self.changeSource()])
                self.settingsSourceBtn.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'n')
                #button to change the source file, uses self.changeSource function

                self.refreshBtn = Button(master = self.settingsFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')

                
                

                ####################change details frame##################
                self.changeDetFrm = Frame(master = self.master)
                self.changeDetFrm.config(bg = 'white')
                self.changeDetFrm.rowconfigure([0], weight = 2)
                self.changeDetFrm.rowconfigure([1,2,3,4], weight = 1)
                self.changeDetFrm.columnconfigure([1,2], weight = 2)
                self.changeDetFrm.columnconfigure([0,3], weight = 1)
                #dimensions for change details page

                self.changeDetRetBtn = Button(master = self.changeDetFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.settingsFrm, self.changeDetFrm)])
                self.changeDetRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to settings page


                self.changeDetTopLbl = Label(master = self.changeDetFrm, width = 50, height = 3, text = 'Edit Details:', fg = 'black' , bg = 'white', font = self.adminLargeFont)
                self.changeDetTopLbl.grid(row = 0, column = 1, columnspan = 2)
                #top text

                self.changeDetUEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetUEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.changeDetULbl = Label(master = self.changeDetFrm,text = 'Username:', font = self.adminFont, width = 50, fg = 'black', bg = 'white')
                self.changeDetULbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #username entry and text

                self.changeDetPEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetPEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.changeDetPLbl = Label(master = self.changeDetFrm,text = 'Password:', font = self.adminFont, width = 50, fg = 'black', bg = 'white')
                self.changeDetPLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #password entry and label

                
                self.changeDetNPEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetNPEnt.grid(row = 3, column = 2, padx = 10, pady = 10)
                self.changeDetNPLbl = Label(master = self.changeDetFrm,text = 'New Password:', font = self.adminFont, width = 50, fg = 'black', bg = 'white')
                self.changeDetNPLbl.grid(row = 3, column = 1, padx = 10, pady = 10,sticky = 'e')
                #new password entry and label

                self.changeDetSubmitBtn = Button(master = self.changeDetFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                                 command=lambda:[self.updateDetails(self.changeDetUEnt.get(), self.changeDetPEnt.get(), self.changeDetNPEnt.get())])
                self.changeDetSubmitBtn.grid(row = 4, column = 1, columnspan = 2)
                #submit buton,passes the 3 fields the user has types into the function self.updateDetails


                #############manage Users frame###############
                self.manageUsersFrm = Frame(master = self.master)
                self.manageUsersFrm.config(bg = 'black')
                self.manageUsersFrm.rowconfigure([0], weight = 1)
                self.manageUsersFrm.rowconfigure([1], weight = 1, minsize = 400)
                self.manageUsersFrm.columnconfigure([0,3], weight = 1)
                self.manageUsersFrm.columnconfigure([1,2], weight = 1, minsize = 200)
                #dimensions for change details page

                self.manageUsersRetBtn = Button(master = self.manageUsersFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.manageUsersFrm)])
                self.manageUsersRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page
                
                self.manageUsersSearchLbl = Label(master = self.manageUsersFrm,text = 'User firstname:',  fg = 'white', bg = 'black', font = self.adminFont)
                self.manageUsersSearchLbl.grid(row = 0, column = 0,padx = 15, pady = 15, columnspan = 2)

                self.manageUsersSearch = Entry(master = self.manageUsersFrm, width = 35, borderwidth = 2)
                self.manageUsersSearch.grid(row = 0, column = 1,padx = 15, pady = 15,sticky = 'e')


                self.manageUsersSelectDept = OptionMenu(self.manageUsersFrm, self.variable ,*self.departmentList) 
                self.manageUsersSelectDept.grid(row = 0, column = 2, padx = 10, pady = 10,sticky = 'e')
                self.manageUsersDeptLbl = Label(master = self.manageUsersFrm,text = 'Department(optional):', font = self.adminFont, width = 15, fg = 'white', bg = 'black')
                self.manageUsersDeptLbl.grid(row = 0, column = 2, padx = 10, pady = 10,sticky = 'w')
                #manage users department label and entry

                self.manageUsersSearchBtn = Button(master = self.manageUsersFrm, width = 10, height = 2, text = 'Search Users', fg = 'white', bg = 'black', borderwidth = 5,
                                                 command=lambda:[self.userSearch(self.manageUsersSearch.get(),self.variable.get())])
                self.manageUsersSearchBtn.grid(row = 0, column = 4,padx = 20, pady = 10, sticky = 'e')

                self.manageUsersDisplayFrm = Frame(master = self.manageUsersFrm,bg = 'white', borderwidth = 3)
                self.manageUsersDisplayFrm.grid(row = 1, column = 1, sticky = 'nesw', pady = 20, columnspan = 2)

                self.refreshBtn = Button(master = self.manageUsersFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')






                ##########manage Rooms frame##################
                self.manageRoomsFrm = Frame(master = self.master)
                self.manageRoomsFrm.config(bg = 'black')
                self.manageRoomsFrm.rowconfigure([0], weight = 1)
                self.manageRoomsFrm.rowconfigure([1], weight = 1, minsize = 400)
                self.manageRoomsFrm.columnconfigure([0,3], weight = 1)
                self.manageRoomsFrm.columnconfigure([1,2], weight = 1, minsize = 200)
                #dimensions for change details page

                self.manageRoomsRetBtn = Button(master = self.manageRoomsFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.manageRoomsFrm)])
                self.manageRoomsRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page
                
                self.manageRoomsSearchLbl = Label(master = self.manageRoomsFrm,text = 'Room name/code:',  fg = 'white', bg = 'black', font = self.adminFont)
                self.manageRoomsSearchLbl.grid(row = 0, column = 0,padx = 15, pady = 15, columnspan = 2)

                self.manageRoomsSearch = Entry(master = self.manageRoomsFrm, width = 35, borderwidth = 2)
                self.manageRoomsSearch.grid(row = 0, column = 1,padx = 15, pady = 15,sticky = 'e')


                self.manageRoomsSelectDept = OptionMenu(self.manageRoomsFrm, self.variable ,*self.departmentList) 
                self.manageRoomsSelectDept.grid(row = 0, column = 2, padx = 10, pady = 10,sticky = 'e')
                self.manageRoomsDeptLbl = Label(master = self.manageRoomsFrm,text = 'Department(optional):', font = self.adminFont, width = 15, fg = 'white', bg = 'black')
                self.manageRoomsDeptLbl.grid(row = 0, column = 2, padx = 10, pady = 10,sticky = 'w')
                #manage users department label and entry

                self.manageRoomsSearchBtn = Button(master = self.manageRoomsFrm, width = 13, height = 2, text = 'Search Rooms', fg = 'white', bg = 'black', borderwidth = 5,
                                                 command=lambda:[self.roomSearch(self.manageRoomsSearch.get(),self.variable.get())])
                self.manageRoomsSearchBtn.grid(row = 0, column = 4,padx = 20, pady = 10, columnspan = 2, sticky = 'e')

                self.manageRoomsDisplayFrm = Frame(master = self.manageRoomsFrm,bg = 'white', borderwidth = 3)
                self.manageRoomsDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 2)

                self.refreshBtn = Button(master = self.manageRoomsFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.adminFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 1, column = 0,padx = 5,pady=5,sticky = 'nw')                






        def refresh(self):
                self.master.destroy()
                adminMain()
                #function to refresh the page(by destroying it and re-opening it)

        def newItem(self, itemName, itemDesc, selectionList):
                self.itemDepts = [selectionList.get(i) for i in selectionList.curselection()]                
                self.itemName1 = str(itemName)
                self.itemDesc = str(itemDesc)
                self.itemName = self.itemName1.replace(" ", "")
                self.itemExists = False
                self.deptSelected = True
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.c.execute('''SELECT item_name
                                FROM Item
                                '''
                                )
                self.ItemNames = []
                self.ItemNamesFetch = self.c.fetchall()
                for x in range (len(self.ItemNamesFetch)):
                        self.ItemNames.append(self.ItemNamesFetch[x][0])  
                if self.itemName in self.ItemNames:
                        self.itemExists = True
                try:
                        self.itemDepts[0][0] 
                except IndexError:
                        self.deptSelected = False
                if len(self.itemName) > 0 and self.itemExists == False and self.deptSelected == True:
                        
                        self.itemID = self.getUniqueID('Item','itemID')
                        for x in range (len(self.itemDepts)):
                                self.c.execute('''SELECT departmentID FROM Department WHERE department_name = ?''',(self.itemDepts[x][0],))
                                self.getDeptID = self.c.fetchall()
                                self.c.execute('''INSERT INTO ItemDept(itemID, departmentID) VALUES(?,?)''',(self.itemID, self.getDeptID[0][0],))
                        
                        self.c.execute('''INSERT INTO Item(itemID, item_name, item_desc)
                                VALUES(?,?,?)
                                ''',(self.itemID,self.itemName, self.itemDesc)
                                )
                        self.userDetails.commit()
                        self.c.close()
                        
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp, text = f'Success\nItem ID:{self.itemID}\nItem Name: {self.itemName}',
                                                         font = self.adminFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.adminFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                elif self.itemExists == True:
                        self.errorItem = Toplevel()
                        self.errorItem.title('')
                        self.errorItem.geometry('300x300')
                        self.errorItemLbl = tk.Label(master = self.errorItem, text = 'Item instance already exists.\nEnter a different item name.', font = self.adminFont)
                        self.errorItemLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorItemBtn = tk.Button(master = self.errorItem, text = 'Try again', command=lambda:[exit_btn(self.errorItem)], font = self.adminFont)
                        self.errorItemBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.userDetails.commit()
                        self.c.close()
                elif len(self.itemName) < 1:
                        self.errorUpdatetp = Toplevel()
                        self.errorUpdatetp.title('')
                        self.errorUpdatetp.geometry('300x300')
                        self.errorUpdateLbl = tk.Label(master = self.errorUpdatetp, text = 'Please enter an item name', font = self.adminFont)
                        self.errorUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUpdateBtn = tk.Button(master = self.errorUpdatetp, text = 'Try again', command=lambda:[exit_btn(self.errorUpdatetp)], font = self.adminFont)
                        self.errorUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.userDetails.commit()
                        self.c.close()
                        
                        
        
        def newUser(self, userFirst, userLast, userName, department):
                self.userFirst = str(userFirst.replace(" ", ""))
                self.userLast = str(userLast.replace(" ", ""))
                self.userName = str(userName.replace(" ", ""))
                self.department = department
                self.department = self.department.replace("(","")
                self.department = self.department.replace("'","")
                self.department = self.department.replace(")","")
                self.department = self.department.replace(",","")
                self.generateUser = False
                self.usernameExists = False
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                if self.userName == "":
                        self.generateUser = True
                if self.generateUser == True:
                        try:
                                self.userName = self.userFirst[0] + self.userLast[0:2]
                                self.generateUser = False
                        except IndexError:
                                pass
                self.c.execute('''SELECT user_name
                                FROM User
                                '''
                                )
                self.userNames = []
                self.userNamesFetch = self.c.fetchall()
                for x in range (len(self.userNamesFetch)):
                        self.userNames.append(self.userNamesFetch[x][0])   
                if self.userName in self.userNames:
                        self.usernameExists = True                                                      
                if len(self.userFirst) > 0 and len(self.userLast) > 0 and self.usernameExists == False and self.department != "Select a Department":
                        self.userID = self.getUniqueID('User', 'userID')
                        self.c.execute('''SELECT departmentID
                                FROM Department
                                WHERE department_name = ?
                                ''',(self.department,)
                                )
                        self.departmentID = self.c.fetchall()
                        self.departmentID  = self.departmentID[0][0]
                        self.c.execute('''INSERT INTO User(userID,first_name, last_name, user_name, password, departmentID)
                                        VALUES(?,?,?,?,?,?)
                                        ''',(self.userID, self.userFirst, self.userLast, self.userName,'password',self.departmentID)
                                       )
                        self.userDetails.commit()
                        self.c.close()
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp,
                                                         text = f"Success\nUsername:{self.userName}\nPassword: password\nFirstname: {self.userFirst}\n Lastname: {self.userLast}\nUser ID: {self.userID}\nDepartment ID:{self.departmentID}",
                                                         font = self.adminFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.adminFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                elif self.usernameExists == True:
                        self.errorUsername = Toplevel()
                        self.errorUsername.title('')
                        self.errorUsername.geometry('300x300')
                        self.errorUsernameLbl = tk.Label(master = self.errorUsername, text = 'Username already exists.\nEnter a different username.', font = self.adminFont)
                        self.errorUsernameLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUsernameBtn = tk.Button(master = self.errorUsername, text = 'Try again', command=lambda:[exit_btn(self.errorUsername)], font = self.adminFont)
                        self.errorUsernameBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                else:
                        self.errorUserDetails = Toplevel()
                        self.errorUserDetails.title('')
                        self.errorUserDetails.geometry('300x300')
                        self.errorUserDetailsLbl = tk.Label(master = self.errorUserDetails, text = 'One or more invalid fields.\nPlease try again.', font = self.adminFont)
                        self.errorUserDetailsLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUserDetailsBtn = tk.Button(master = self.errorUserDetails, text = 'Try again', command=lambda:[exit_btn(self.errorUserDetails)], font = self.adminFont)
                        self.errorUserDetailsBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        #error window to enter all the fields properly
                        
                
        
        def newRoom(self, roomName1, roomDesc, department):
                #change to room variables.
                self.roomName1 = str(roomName1)
                self.roomDesc = str(roomDesc)
                self.roomName = self.roomName1.replace(" ", "")
                self.roomExists = False
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.department = department
                self.department = self.department.replace("(","")
                self.department = self.department.replace("'","")
                self.department = self.department.replace(")","")
                self.department = self.department.replace(",","")
                
                self.c.execute('''SELECT room_name
                                FROM Room
                                '''
                                )
                
                self.RoomNames = []
                self.RoomNamesFetch = self.c.fetchall()
                for x in range (len(self.RoomNamesFetch)):
                        self.RoomNames.append(self.RoomNamesFetch[x][0])
                        
                if self.roomName in self.RoomNames:
                        self.roomExists = True
                        

                
                if len(self.roomName) > 0 and self.roomExists == False and self.department != "Select a Department":
                        
                        #connecting to database stored in variable 'database_pathfile' 
                        #fetching from database
                        self.roomID = self.getUniqueID('Room','RoomID')
                        self.c.execute('''INSERT INTO Room(roomID, room_name, room_desc) VALUES(?,?,?)''',(self.roomID,self.roomName, self.roomDesc))
                        self.c.execute('''SELECT departmentID FROM Department WHERE department_name = ?''',(self.department,))
                        self.departmentIDs = self.c.fetchone()
                        self.departmentID = self.departmentIDs[0]
                             
                        self.c.execute('''INSERT INTO RoomDept(roomID, departmentID)
                                VALUES(?,?)
                                ''',(self.roomID,self.departmentID)
                                )
                        self.userDetails.commit()
                        self.c.close()
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp, text = f'Success\nRoom ID:{self.roomID}\nRoom Name: {self.roomName}\nDepartment: {self.department}',
                                                         font = self.adminFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.adminFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                elif self.roomExists == True:
                        self.errorRoom = Toplevel()
                        self.errorRoom.title('')
                        self.errorRoom.geometry('300x300')
                        self.errorRoomLbl = tk.Label(master = self.errorRoom, text = 'Room name/code already exists.\nEnter a different room name.', font = self.adminFont)
                        self.errorRoomLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorRoomBtn = tk.Button(master = self.errorRoom, text = 'Try again', command=lambda:[exit_btn(self.errorRoom)], font = self.adminFont)
                        self.errorRoomBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.userDetails.commit()
                        self.c.close()
                elif len(self.roomName) < 1:
                        self.errorUpdatetp = Toplevel()
                        self.errorUpdatetp.title('')
                        self.errorUpdatetp.geometry('300x300')
                        self.errorUpdateLbl = tk.Label(master = self.errorUpdatetp, text = 'Please enter a room name', font = self.adminFont)
                        self.errorUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUpdateBtn = tk.Button(master = self.errorUpdatetp, text = 'Try again', command=lambda:[exit_btn(self.errorUpdatetp)], font = self.adminFont)
                        self.errorUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.userDetails.commit()
                        self.c.close()

                        
                
        
        def userSearch(self, userFirst, department):
                self.userFirst = userFirst
                self.department = department
                self.department = self.department.replace("(","")
                self.department = self.department.replace("'","")
                self.department = self.department.replace(")","")
                self.department = self.department.replace(",","")
                self.manageUsersDisplayFrm.destroy()
                self.manageUsersDisplayFrm = Frame(master = self.manageUsersFrm,bg = 'white', borderwidth = 3)
                self.manageUsersDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 2)
                self.userCriteria = True
                if self.userFirst == '':
                        self.userCriteria = False
                self.departmentCriteria = True
                if self.department == 'Select a Department':
                        self.departmentCriteria = False
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.c.execute('''SELECT departmentID FROM Department WHERE department_name = ?''',(self.department,))
                self.departmentResults = self.c.fetchall()
                self.departmentID = self.departmentResults[0][0]
                if self.departmentCriteria == True and self.userCriteria == True:
                        self.c.execute('''SELECT * FROM User WHERE first_name = ? AND departmentID = ?''',(self.userFirst,self.departmentID,))
                        self.userResults = self.c.fetchall()
                        self.searchResultNumber = len(self.userResults)    
                elif self.departmentCriteria == False and self.userCriteria == True:
                        self.c.execute('''SELECT * FROM User WHERE first_name = ?''',(self.userFirst,))
                        self.userResults = self.c.fetchall()
                        self.searchResultNumber = len(self.userResults)  
                elif self.departmentCriteria == True and self.userCriteria == False:
                        self.c.execute('''SELECT * FROM User WHERE departmentID = ?''',(self.departmentID,))
                        self.userResults = self.c.fetchall()
                        self.searchResultNumber = len(self.userResults)
                elif self.departmentCriteria == False and self.userCriteria == False:
                        self.searchResultNumber = 0

                
                        
                self.usersStore = []
                self.userFrames = []
                for i in range (self.searchResultNumber):
                        self.usersStore.append(self.userResults[i][0])
                        self.userFrames.append(self.createSearchUserFrame(self.userResults[i][0],self.userResults[i][1],self.userResults[i][2],
                                                                          self.userResults[i][3],self.userResults[i][4],
                                                                          self.userResults[i][5]))
                        #self.commandStore.append(self.showFrame(self., self.manageUsersFrm))
                        
                #print(self.commandStore)
                
                                        
                                
                if self.searchResultNumber < 8:
                        self.button = []
                        for i in range(self.searchResultNumber):
                                self.button.append(Button(master = self.manageUsersDisplayFrm, width = 50, height = 1, borderwidth = 5,fg = 'white', bg = 'black',
                                                          text = f'Username: {self.userResults[i][1]}  |    Password:{self.userResults[i][2]}  |    Department:{self.department}',
                                                          command=self.callbackUser(i+1)))  
                                self.button[i].pack(side = TOP, fill = BOTH)
                                
                elif self.searchResultNumber > 8:
                        for i in range(7):
                                self.button.append(Button(master = self.manageUsersDisplayFrm, width = 50, height = 1, borderwidth = 5,fg = 'white', bg = 'black',
                                                          text = f'Username: {self.userResults[i][1]}  |    Password:{self.userResults[i][2]}  |    Department:{self.department}',
                                                          command=self.callbackUser(i+1)))       
                                self.button[i].pack(side = TOP, fill = BOTH)

                elif self.searchResultNumber == 0:
                        pass
                        
                



        def callbackUser(self,i): #function to bring up the frame of the button.
                def _callback():
                        self.userFrames[i-1] = self.createSearchUserFrame(self.userResults[i-1][0],self.userResults[i-1][1],self.userResults[i-1][2],self.userResults[i-1][3],
                                                self.userResults[i-1][4],
                                                self.userResults[i-1][5])
                        self.showFrame(self.userFrames[i-1], self.manageUsersFrm)
                return _callback
                


        def createSearchUserFrame(self, userID, userName, userPassword, userFirst, userLast, userDept):
                self.userID = userID
                self.userName = userName
                self.userPassword = userPassword
                self.userFirst = userFirst
                self.userLast = userLast
                self.userDept = userDept
                self.userSearchFrm = Frame(master = self.master)
                self.userSearchFrm.config(bg = 'black')
                self.userSearchFrm.rowconfigure([0], weight = 1)
                self.userSearchFrm.rowconfigure([1], weight = 1, minsize = 300)
                self.userSearchFrm.columnconfigure([0,2], weight = 1)
                self.userSearchFrm.columnconfigure([1], weight = 1, minsize = 200)
                self.userSearchTop = Label(master = self.userSearchFrm, text = f'Name of user: {self.userName}', font = self.adminLargeFont, fg = 'white', bg = 'black')
                self.userSearchTop.grid(row = 0, column = 1)
                self.userSearchDisplayFrm = Frame(master = self.userSearchFrm,bg = 'white', borderwidth = 3)
                self.userSearchDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 1)
                self.userSearchRetBtn = Button(master = self.userSearchFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.manageUsersFrm, self.userSearchFrm)])
                self.userSearchRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page
                self.userSearchUserDetails = Label(master = self.userSearchDisplayFrm,
                                                   text = f'UserID:{self.userID}\nPassword:{self.userPassword}\nLastname: {self.userLast}\nDepartment: {self.userDept}',
                                                   fg = 'black', bg = 'white', font = self.adminLargeFont)
                self.userSearchUserDetails.pack(fill = BOTH, expand = True)

                self.userSearchUserDelete = Button(master = self.userSearchFrm, width = 15, height = 4, text = 'Delete this User', borderwidth = 5,
                                                   command=lambda:[self.deleteUserWarning(self.userID, self.userFirst)])
                self.userSearchUserDelete.grid(row = 1, column = 2,sticky = 'se', padx = 20, pady = 20)

                

                                                                   
                return self.userSearchFrm


        def deleteUserWarning(self, userID, userFirst):
                self.userID = userID
                self.userFirst = userFirst
                
                self.userDel = Toplevel()
                self.userDel.title('')
                self.userDel.geometry('300x300')
                self.userDelLbl = tk.Label(master = self.userDel, text = f'Are you sure you want to delete user {self.userFirst}?', font = self.adminFont)
                self.userDelLbl.pack(side=TOP, padx = 10, pady = 10)
                self.userDelBtn1 = tk.Button(master = self.userDel, text = 'Delete', command=lambda:[exit_btn(self.userDel), self.deleteUser(self.userID)],
                                             font = self.adminFont)
                self.userDelBtn1.pack(side=LEFT, padx = 55, pady = 40)
                self.userDelBtn2 = tk.Button(master = self.userDel, text = 'Close', command=lambda:[exit_btn(self.userDel)], font = self.adminFont)
                self.userDelBtn2.pack(side=RIGHT, padx = 55, pady = 40)

        def deleteUser(self, userID):
                self.userID = userID
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.c.execute('''DELETE FROM User
                                WHERE userID = ?
                                ''',(self.userID,))
                
                self.userDetails.commit()
                self.c.close()
                
                self.userDeleted = Toplevel()
                self.userDeleted.title('')
                self.userDeleted.geometry('300x300')
                self.userDeletedLbl = tk.Label(master = self.userDeleted, text = f'User has been deleted', font = self.adminFont)
                self.userDeletedLbl.pack(side=TOP, padx = 10, pady = 10)
                self.userDeletedBtn = tk.Button(master = self.userDeleted, text = 'Close', command=lambda:[exit_btn(self.userDeleted)], font = self.adminFont)
                self.userDeletedBtn.pack( padx = 40, pady = 20)
                
                self.showFrame(self.manageUsersFrm, self.userSearchFrm)
                self.manageUsersDisplayFrm.destroy()
                self.manageUsersDisplayFrm = Frame(master = self.manageUsersFrm,bg = 'white', borderwidth = 3)
                self.manageUsersDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 2) 



                
        
        def roomSearch(self, roomName, department):
                self.roomName = roomName
                self.department = department
                self.department = self.department.replace("(","")
                self.department = self.department.replace("'","")
                self.department = self.department.replace(")","")
                self.department = self.department.replace(",","")
                self.manageRoomsDisplayFrm.destroy()
                self.manageRoomsDisplayFrm = Frame(master = self.manageRoomsFrm,bg = 'white', borderwidth = 3)
                self.manageRoomsDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 2)
                self.roomCriteria = True
                if self.roomName == '':
                        self.roomCriteria = False    
                self.departmentCriteria = True
                if self.department == 'Select a Department':
                        self.departmentCriteria = False    
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()

                if self.departmentCriteria == True and self.roomCriteria == True:
                        self.c.execute('''SELECT departmentID FROM Department WHERE department_name = ?''',(self.department,))
                        self.departmentResults = self.c.fetchall()
                        self.departmentID = self.departmentResults[0][0]
                        self.c.execute('''SELECT roomID FROM Room WHERE room_name = ?''',(self.roomName,))
                        self.roomIDResults = self.c.fetchall()
                        self.roomID = self.roomIDResults[0][0]
                        self.c.execute('''SELECT * FROM RoomDept WHERE roomID = ? AND departmentID = ?''',(self.roomID,self.departmentID,))
                        self.roomDeptResults = self.c.fetchall()
                        self.searchResultNumber = len(self.roomDeptResults)                        
                elif self.departmentCriteria == False and self.roomCriteria == True:
                        self.c.execute('''SELECT roomDept.departmentID FROM roomDept INNER JOIN Room ON (Room.roomID = roomDept.roomID) WHERE Room.room_name = ?''',(self.roomNames,))
                        self.departmentResults = self.c.fetchall()
                        self.departmentID = self.departmentResults[0][0]
                        self.c.execute('''SELECT roomID FROM Room WHERE room_name = ?''',(self.roomName,))
                        self.roomIDResults = self.c.fetchall()
                        self.roomID = self.roomIDResults[0][0]
                        self.c.execute('''SELECT * FROM RoomDept WHERE roomID = ?''',(self.roomID,))
                        self.roomDeptResults = self.c.fetchall()
                        self.searchResultNumber = len(self.roomDeptResults)

                elif self.departmentCriteria == True and self.roomCriteria == False:
                        self.searchResultNumber = 0
                        
                elif self.departmentCriteria == False and self.roomCriteria == False:
                        self.searchResultNumber = 0
                        
                self.roomFrames = []
                for i in range (self.searchResultNumber):
                        self.roomFrames.append(self.createSearchRoomFrame(self.roomID, self.departmentID))                             
                if self.searchResultNumber < 8:
                        self.button = []
                        for i in range(self.searchResultNumber):
                                self.button.append(Button(master = self.manageRoomsDisplayFrm, width = 50, height = 1, borderwidth = 5,fg = 'white', bg = 'black',
                                                          text = f'Room ID: {self.roomID} |    DepartmentID:{self.departmentID}',
                                                          command=self.callbackRoom(i+1)))  
                                self.button[i].pack(side = TOP, fill = BOTH)
                                
                elif self.searchResultNumber > 8:
                        for i in range(7):
                                self.button.append(Button(master = self.manageRoomsDisplayFrm, width = 50, height = 1, borderwidth = 5,fg = 'white', bg = 'black',
                                                          text = f'Room ID: {self.roomID} |    DepartmentID:{self.departmentID}',
                                                          command=self.callbackRoom(i+1)))  
                                self.button[i].pack(side = TOP, fill = BOTH)

                elif self.searchResultNumber == 0:
                        pass



        def callbackRoom(self,i): #function to bring up the frame of the button.
                def _callback():
                        self.roomFrames[i-1] = self.createSearchRoomFrame(self.roomDeptResults[i-1][0],self.roomDeptResults[i-1][1])
                        self.showFrame(self.roomFrames[i-1], self.manageRoomsFrm)
                return _callback
        def createSearchRoomFrame(self, roomID, deptID):
                self.roomID = roomID
                self.deptID = deptID

                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()

                self.c.execute('''SELECT * FROM Room WHERE roomID = ?''',(self.roomID,))

                self.roomDetailsFetch = self.c.fetchall()
                self.roomName = self.roomDetailsFetch[0][1]
                self.roomDesc = self.roomDetailsFetch[0][2]

                self.c.execute('''SELECT department_name FROM Department WHERE departmentID = ?''',(self.deptID,))
                

                self.deptDetailsFetch = self.c.fetchall()
                self.deptName = self.deptDetailsFetch[0][0]

                self.c.execute('''SELECT Item.item_name, ItemRoom.item_Quantity FROM Item INNER JOIN ItemRoom ON Item.itemID = ItemRoom.itemID WHERE ItemRoom.roomID = ?''',(self.roomID,))
                self.itemDetailsFetch = self.c.fetchall()
                
                
                self.roomSearchFrm = Frame(master = self.master)
                self.roomSearchFrm.config(bg = 'black')
                self.roomSearchFrm.rowconfigure([0], weight = 1)
                self.roomSearchFrm.rowconfigure([1], weight = 1, minsize = 300)
                self.roomSearchFrm.columnconfigure([0,2], weight = 1)
                self.roomSearchFrm.columnconfigure([1], weight = 1, minsize = 200)
                self.roomSearchTop = Label(master = self.roomSearchFrm, text = f'Name of room: {self.roomName}', font = self.adminLargeFont, fg = 'white', bg = 'black')
                self.roomSearchTop.grid(row = 0, column = 1)
                self.roomSearchDisplayFrm = Frame(master = self.roomSearchFrm,bg = 'white', borderwidth = 3)
                self.roomSearchDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 1)
                self.roomSearchRetBtn = Button(master = self.roomSearchFrm, text='Return', width = 9, height = 4,font = self.adminFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.manageRoomsFrm, self.roomSearchFrm)])
                self.roomSearchRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page
                self.roomSearchRoomDetails = Label(master = self.roomSearchDisplayFrm,
                                                   text = f'RoomID:{self.roomID}\nRoom Description:{self.roomDesc}\nDepartment: {self.deptName}\nDepartment ID: {self.deptID}\n\n',
                                                   fg = 'black', bg = 'white', font = self.adminLargeFont)
                self.roomSearchRoomDetails.pack(side = TOP, expand = True)
                
                for i in range (len(self.itemDetailsFetch)):
                        self.roomSearchRoomItem = Label(master = self.roomSearchDisplayFrm,
                                                   text = f'Item: {self.itemDetailsFetch[i][0]} | Quantity: {self.itemDetailsFetch[i][1]}',
                                                   fg = 'black', bg = 'white', font = self.adminFont)
                        self.roomSearchRoomItem.pack(expand = True)

                
                self.roomSearchRoomDelete = Button(master = self.roomSearchFrm, width = 15, height = 4, text = 'Delete this Room', borderwidth = 5,
                                                   command=lambda:[self.deleteRoomWarning(self.roomID, self.roomName)])
                self.roomSearchRoomDelete.grid(row = 1, column = 2,sticky = 'se', padx = 20, pady = 20)         
                return self.roomSearchFrm







        def deleteRoomWarning(self, roomID, roomName):
                self.roomID = roomID
                self.roomName = roomName
                
                self.roomDel = Toplevel()
                self.roomDel.title('')
                self.roomDel.geometry('300x300')
                self.roomDelLbl = tk.Label(master = self.roomDel, text = f'Are you sure you want to delete {self.roomName}?', font = self.adminFont)
                self.roomDelLbl.pack(side=TOP, padx = 10, pady = 10)
                self.roomDelBtn1 = tk.Button(master = self.roomDel, text = 'Delete', command=lambda:[exit_btn(self.roomDel), self.deleteRoom(self.roomID)],
                                             font = self.adminFont)
                self.roomDelBtn1.pack(side=LEFT, padx = 55, pady = 40)
                self.roomDelBtn2 = tk.Button(master = self.roomDel, text = 'Close', command=lambda:[exit_btn(self.roomDel)], font = self.adminFont)
                self.roomDelBtn2.pack(side=RIGHT, padx = 55, pady = 40)

        def deleteRoom(self, roomID):
                self.roomID = roomID
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.c.execute('''DELETE FROM Room
                                WHERE roomID = ?
                                ''',(self.roomID,))
                self.c.execute('''DELETE FROM RoomDept
                        WHERE roomID = ?
                        ''',(self.roomID,))
                self.c.execute('''DELETE FROM ItemRoom
                        WHERE roomID = ?
                        ''',(self.roomID,))
                
                self.userDetails.commit()
                self.c.close()
                
                self.roomDeleted = Toplevel()
                self.roomDeleted.title('')
                self.roomDeleted.geometry('300x300')
                self.roomDeletedLbl = tk.Label(master = self.roomDeleted, text = f'Room has been deleted', font = self.adminFont)
                self.roomDeletedLbl.pack(side=TOP, padx = 10, pady = 10)
                self.roomDeletedBtn = tk.Button(master = self.roomDeleted, text = 'Close', command=lambda:[exit_btn(self.roomDeleted)], font = self.adminFont)
                self.roomDeletedBtn.pack( padx = 40, pady = 20)
                
                self.showFrame(self.manageRoomsFrm, self.roomSearchFrm)
                self.manageRoomsDisplayFrm.destroy()
                self.manageRoomsDisplayFrm = Frame(master = self.manageRoomsFrm,bg = 'white', borderwidth = 3)
                self.manageRoomsDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 2)
                





        

        def newDepartment(self, deptName, deptDesc):
                self.deptName1 = str(deptName)
                self.deptDesc = str(deptDesc)
                self.deptName = self.deptName1.replace(" ", "")
                self.deptExists = False
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()

                        
                self.c.execute('''SELECT department_name
                                FROM Department
                                '''
                                )
                self.departmentNames = []
                #sqlite3.OperationalError:
                self.departmentNamesFetch = self.c.fetchall()
                for x in range (len(self.departmentNamesFetch)):
                        self.departmentNames.append(self.departmentNamesFetch[x][0])
                        
                if self.deptName in self.departmentNames:
                        self.errorDepartment = Toplevel()
                        self.errorDepartment.title('')
                        self.errorDepartment.geometry('300x300')
                        self.errorDepartmentLbl = tk.Label(master = self.errorDepartment, text = 'Department already exists.\nEnter a different department name.', font = self.adminFont)
                        self.errorDepartmentLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorDepartmentBtn = tk.Button(master = self.errorDepartment, text = 'Try again', command=lambda:[exit_btn(self.errorDepartment)], font = self.adminFont)
                        self.errorDepartmentBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.deptExists = True
                        self.userDetails.commit()
                        self.c.close()
                if len(self.deptName) > 0 and self.deptExists == False:
                        self.deptID = self.getUniqueID('Department','departmentID')
                        self.c.execute('''INSERT INTO Department(departmentID, department_name, department_desc)
                                VALUES(?,?,?)
                                ''',(self.deptID,self.deptName, self.deptDesc,)
                                )
                        self.userDetails.commit()
                        self.userDetails.close()
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp, text = f'Success\nDepartment ID:{self.deptID}\nDepartment Name: {self.deptName}',
                                                         font = self.adminFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.adminFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                else:
                        self.errorDept = Toplevel()
                        self.errorDept.title('')
                        self.errorDept.geometry('300x300')
                        self.errorDeptmentLbl = tk.Label(master = self.errorDept, text = 'Please enter a department name', font = self.adminFont)
                        self.errorDeptmentLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorDeptmentBtn = tk.Button(master = self.errorDept, text = 'Try again', command=lambda:[exit_btn(self.errorDept)], font = self.adminFont)
                        self.errorDeptmentBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        self.userDetails.commit()
                        self.c.close()

        def getUniqueID(self, tableName, tableID):
                self.tableName = tableName
                self.tableID = tableID
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.IDList = []
                self.c.execute('''SELECT {}
                        FROM {}
                        '''.format(self.tableID,self.tableName)
                        )
                
                self.IDFetch = self.c.fetchall()
                for x in range (len(self.IDFetch)):
                        self.IDList.append(self.IDFetch[x][0])
                self.IDList.sort()
                try:
                        self.largestID = self.IDList[-1]
                        self.uniqueID = self.largestID + 1
                except ValueError:
                        self.uniqueID = 1
                except IndexError:
                        self.uniqueID = 1
                return self.uniqueID
                                
                

        def updateDetails(self, username, password, newPassword):
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.username = username
                self.password = password
                self.newPassword = newPassword
                #connecting to database stored in variable 'database_pathfile' 
                #fetching from database
                self.c.execute('''SELECT user_name, password
                        FROM Admin
                        WHERE user_name = ? AND password = ?
                        ''',(self.username,self.password)
                        )
                self.fetch = self.c.fetchall()
                #selecting usernames and passwords where it matches the username and password entered by the user
                try:
                        self.throwaway = self.fetch[0][0]
                        #tests if the list self.fetch has any indexes, if it doesn't, then run the code in the Except IndexError block.
                        self.c.execute('''UPDATE Admin
                                SET password = ?
                                WHERE user_name = ? 
                                ''',(self.newPassword, self.username)
                                )
                        self.userDetails.commit()
                        self.c.close()
                        #update the database with the new password
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp, text = f'Success\nYour new password is\n {self.newPassword}', font = self.adminFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.adminFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        #success window if the username and password match and the details were successfully updated      
                except IndexError:
                        #error window if the self.fetch[0][0] list has no entries(username and password do not match)
                        self.errorUpdatetp = Toplevel()
                        self.errorUpdatetp.title('')
                        self.errorUpdatetp.geometry('300x300')
                        self.errorUpdateLbl = tk.Label(master = self.errorUpdatetp, text = 'Your password does not match your username', font = self.adminFont)
                        self.errorUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUpdateBtn = tk.Button(master = self.errorUpdatetp, text = 'Try again', command=lambda:[exit_btn(self.errorUpdatetp)], font = self.adminFont)
                        self.errorUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)

                        
        def databaseLocate(self, oldSource):
                #function to change the source file database
                self.oldSource = oldSource
                self.filepath = askopenfilename(
                filetypes=[("Database Files", "*.db"), ("All Files", "*.*")])
                self.filepath = str(self.filepath)
                #asks for the filepath and stores it in self.filepath
                if self.filepath.endswith('User_Details.db'):
                        self.successLocate = Toplevel()
                        self.successLocate.title('')
                        self.successLocate.geometry('300x300')
                        self.successLocateLbl = tk.Label(master = self.successLocate, text = f'Success\nSource file found:\n{self.filepath}', width = 40,
                                                         height =10, font = self.adminFont)
                        self.successLocateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successLocateBtn = tk.Button(master = self.successLocate, text = 'Go to login',
                                                      command=lambda:[exit_btn(self.successLocate),exit_btn(self.master), self.changePathfile(self.filepath), normal_open()],
                                                                      font = self.adminFont)
                        self.successLocateBtn.pack(side=BOTTOM, padx = 10, pady = 10)
                        #success window if source file is valid. on pressing the button, saves the filepath to variable database_pathfile, closes the window, and opens login

                else:
                        self.errorLocate = Toplevel()
                        self.errorLocate.title('')
                        self.errorLocate.geometry('300x300')
                        self.errorLocateLbl = tk.Label(master = self.errorLocate, text = 'File chosen is not a source database file', font = self.adminFont)
                        self.errorLocateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorLocateBtn = tk.Button(master = self.errorLocate, text = 'Close', command=lambda:[exit_btn(self.errorLocate)], font = self.adminFont)
                        self.errorLocateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        #error window if file chosen is not valid.
                
                
        def changePathfile(self, filepath):
                database_pathfile = str(filepath)
                #function to save the database pathfile to the variable after the user clicks on the button

        def changeSource(self):
                #function to change the source database
                self.updateSelect = Toplevel()
                self.updateSelect.geometry('300x300')
                self.updateSelect.title('')
                #creating a function called first_open_db which creates a Toplevel() window and giving it size and title
                self.updateSelectLbl = tk.Label(master= self.updateSelect, text = 'Choose a source Database(.db) file.\nName of file is "User_Details.db"',
                                          font = self.adminFont)
                self.updateSelectLbl.pack(side=TOP, padx = 5, pady = 10)
                self.updateSelectClose = tk.Button(master = self.updateSelect, text = 'Close', width = 7, height = 1, font = self.adminFont, command=lambda:[exit_btn(self.updateSelect)])
                self.updateSelectClose.pack(side=LEFT, padx = 20, pady = 5)
                #open_popup_close allows user to close the Toplevel window by running the exit_btn() function and passing its' own Toplevel into the function.
                self.updateSelectOpen = tk.Button(master = self.updateSelect, text = 'Choose a File', width = 10, height = 1,font = self.adminFont,
                                                  command=lambda:[exit_btn(self.updateSelect), self.databaseLocate(database_pathfile)])
                self.updateSelectOpen.pack(side=RIGHT, padx = 20, pady = 5)
                #open_popup_db_choose allows user to choose a file, which will run the command exit_btn()and second_open_db(), closing the window and running the code to select a file.
                  
        
        def logoutConfirm(self, windowInput):
                self.windowInput = windowInput
                self.logConfirm = Toplevel()
                self.logConfirm.geometry('250x250')
                self.logConfirm.title('Confirm')
                self.logConfirmLbl = tk.Label(master = self.logConfirm, text = 'Are you sure you want to log out?')
                self.logConfirmLbl.pack(side=TOP, padx = 5, pady = 10)
                self.logConfirmBtn = tk.Button(master = self.logConfirm, text = 'Logout', width = 20, height = 1,font = self.adminFont, fg = 'black', bg = 'white',
                                            command=lambda:[exit_btn(self.windowInput), normal_open(), setUserLoggedIn()])
                self.logConfirmBtn.pack(side=BOTTOM, padx = 5, pady = 30)
                #pop-up window asking to confirm before logging the user out, takes user back to login - normal_open()



        def showFrame(self, frameRaise, frameForget):
                self.frameForget = frameForget
                self.frameForget.forget()
                self.frameRaise = frameRaise
                self.frameRaise.pack(fill = BOTH, expand = True)
                self.frameRaise.tkraise()
                #a function used to raise a frame to the top of the stack(i.e. when the user wants to change screens
                #takes in two parameters, the frame to raise and the frame to drop, forgets one frame and fills the frame to the window


        def getDepartmentList(self):
                #get the names of all departments and store them in a list for an optionMenu widget 
                self.user_details = sqlite.connect(database_pathfile)
                self.c = self.user_details.cursor()
                
                self.c.execute('''SELECT department_name
                        FROM Department 
                        ''')
                
                self.departmentList = self.c.fetchall()
                
                return self.departmentList
                




class User():
        def __init__(self, master):
                self.master = master
                #assigning the 'master' attribute to the window/root that is passed into the init function
                global userLoggedIn
                
                
                self.userFont = ('Arial', 10)
                self.userLargeFont = ('Arial', 20)
                #global fonts for the admin UI
                
                #########homepage frame#######
                self.homepageFrm = Frame(master = self.master)
                self.homepageFrm.config(bg = '#42f5da')
                self.homepageFrm.rowconfigure([0,1], weight = 1)
                self.homepageFrm.rowconfigure([2], weight = 3,minsize = 500)
                self.homepageFrm.columnconfigure([0,2], weight = 1)
                self.homepageFrm.columnconfigure(1, weight = 3,minsize = 400)
                self.homepageFrm.pack(fill = BOTH, expand = True)
                #packing the homepageFrm as it is the first screen displayed when the program is opened
                #configuring dimensions for the homepage

                self.settingsBtn = Button(master = self.homepageFrm, width = 9, height = 4, text = 'Settings', bg = 'black', font = self.userFont,
                                          fg = 'white', borderwidth = 3, command=lambda:[self.showFrame(self.settingsFrm, self.homepageFrm)])
                self.settingsBtn.grid(row = 0, column = 2, padx = 10, sticky = 'e')
                #settings button to go to the settings page

                self.homepageTopLbl = Label(master = self.homepageFrm, width = 30, height = 5, bg = '#42f5da', font = self.userLargeFont,
                                            fg = 'black', text = f'Welcome, user {userLoggedIn}')
                self.homepageTopLbl.grid(row = 0, column = 1, pady = 15, sticky = 'nsew')

                self.homepageMidLbl = Label(master = self.homepageFrm, width = 30, height = 5, bg = '#42f5da', font = self.userFont,
                                            fg = 'black', text = f'Rooms in your department:')
                self.homepageMidLbl.grid(row = 1, column = 1, pady = 15,sticky = 's')

                self.homepageDisplayFrm = Frame(master = self.homepageFrm, bg = 'white')
                self.homepageDisplayFrm.grid(row = 2, column = 1, sticky = 'nsew', pady = 15)
                
                self.roomDisplay()

                self.refreshBtn = Button(master = self.homepageFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.userFont,
                                          fg = 'white', borderwidth = 3, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row = 0, column = 0, padx = 10, sticky = 'w', pady = 10)




                #########settings frame##########
                self.settingsFrm = Frame(master = self.master)
                self.settingsFrm.config(bg = '#42f5da')
                self.settingsFrm.rowconfigure([0], weight = 2)
                self.settingsFrm.rowconfigure([1,2], weight = 1)
                self.settingsFrm.columnconfigure([1], weight = 2)
                self.settingsFrm.columnconfigure([0,2], weight = 1)
                
                self.settingsReturnBtn = Button(master = self.settingsFrm, text='Return', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.settingsFrm)])
                self.settingsReturnBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to the homepage, uses self.showFrame function

                self.settingsLogoutBtn = Button(master = self.settingsFrm, text='Logout', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.logoutConfirm(self.master)])
                self.settingsLogoutBtn.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'ne')
                #button to logout, uses self.logoutConfirm function

                self.settingsTopLbl = Label(master = self.settingsFrm, width = 50, height = 3, text = 'Settings:', fg = 'black' , bg = '#42f5da', font = self.userLargeFont)
                self.settingsTopLbl.grid(row = 0, column = 1)
                #label at the top of the page
                
                self.settingsDetailsBtn = Button(master = self.settingsFrm,text = 'Change your password', font = self.userFont, width = 50, height = 5, fg = 'white', bg = 'black',
                                                 command=lambda:[self.showFrame(self.changeDetFrm, self.settingsFrm)])
                self.settingsDetailsBtn.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'n')
                #button to edit details, takes user to changeDetFrm frame
                

                self.settingsSourceBtn = Button(master = self.settingsFrm,text = 'Show user details', width = 50, height = 5, font = self.userFont, fg = 'white',
                                               bg = 'black', command=lambda:[self.showFrame(self.userDetailsFrm, self.settingsFrm)])
                self.settingsSourceBtn.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'n')
                #button to change the source file, uses self.changeSource function

                self.refreshBtn = Button(master = self.settingsFrm, width = 9, height = 4, text = 'Refresh', bg = 'black', font = self.userFont,
                                          fg = 'white', borderwidth = 5, command=lambda:[self.refresh()])
                self.refreshBtn.grid(row=0,column = 1, padx = 5, pady = 5, sticky = 'nw')



                ##################show User details frame###################
                self.userDetailsFrm = Frame(master = self.master)
                self.userDetailsFrm.config(bg = '#42f5da')
                self.userDetailsFrm.rowconfigure([0], weight = 1)
                self.userDetailsFrm.rowconfigure([1], weight = 2, minsize = 400)
                self.userDetailsFrm.columnconfigure([0,2], weight = 1)
                self.userDetailsFrm.columnconfigure([1], weight = 2, minsize = 400)

                self.user_details = sqlite.connect(database_pathfile)
                self.c = self.user_details.cursor()
                
                self.c.execute('''SELECT *
                        FROM User
                        WHERE user_name = ?
                        ''', (userLoggedIn,))
                
                self.userDetailsList = self.c.fetchall()

                
                self.c.execute('''SELECT department_name FROM department WHERE departmentID = ?''', (self.userDetailsList[0][5],))

                self.userDept = self.c.fetchall()
                
                
                self.userDetailsTop = Label(master = self.userDetailsFrm, text = f'Name of user: {self.userDetailsList[0][3]}', font = self.userLargeFont, fg = 'black', bg = '#42f5da')
                self.userDetailsTop.grid(row = 0, column = 1)
                
                self.userDetailsDisplayFrm = Frame(master = self.userDetailsFrm,bg = 'white', borderwidth = 3)
                self.userDetailsDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 1)
               

                self.userDetailsRetBtn = Button(master = self.userDetailsFrm, text='Return', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.settingsFrm, self.userDetailsFrm)])
                self.userDetailsRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page
                
                

                self.userDetails = Label(master = self.userDetailsDisplayFrm,
                                                   text = f'UserID:{self.userDetailsList[0][0]}\nUsername: {userLoggedIn}\nPassword:{self.userDetailsList[0][2]}\nLastname: {self.userDetailsList[0][4]}\nDepartment: {self.userDept[0][0]}',
                                                   fg = 'black', bg = 'white', font = self.userLargeFont)
                self.userDetails.pack(side = TOP)
                



                ####################change details frame##################
                self.changeDetFrm = Frame(master = self.master)
                self.changeDetFrm.config(bg = '#42f5da')
                self.changeDetFrm.rowconfigure([0], weight = 2)
                self.changeDetFrm.rowconfigure([1,2,3,4], weight = 1)
                self.changeDetFrm.columnconfigure([1,2], weight = 2)
                self.changeDetFrm.columnconfigure([0,3], weight = 1)
                #dimensions for change details page

                self.changeDetRetBtn = Button(master = self.changeDetFrm, text='Return', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.settingsFrm, self.changeDetFrm)])
                self.changeDetRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to settings page


                self.changeDetTopLbl = Label(master = self.changeDetFrm, width = 50, height = 3, text = 'Edit Details:', fg = 'black' , bg = '#42f5da', font = self.userLargeFont)
                self.changeDetTopLbl.grid(row = 0, column = 1, columnspan = 2)
                #top text

                self.changeDetUEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetUEnt.grid(row = 1, column = 2, padx = 10, pady = 10)
                self.changeDetULbl = Label(master = self.changeDetFrm,text = 'Username:', font = self.userFont, width = 50, fg = 'black', bg = '#42f5da')
                self.changeDetULbl.grid(row = 1, column = 1, padx = 10, pady = 10,sticky = 'e')
                #username entry and text

                self.changeDetPEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetPEnt.grid(row = 2, column = 2, padx = 10, pady = 10)
                self.changeDetPLbl = Label(master = self.changeDetFrm,text = 'Password:', font = self.userFont, width = 50, fg = 'black', bg = '#42f5da')
                self.changeDetPLbl.grid(row = 2, column = 1, padx = 10, pady = 10,sticky = 'e')
                #password entry and label

                
                self.changeDetNPEnt = Entry(master = self.changeDetFrm, width = 50, fg = 'black', bg = 'white', borderwidth = 2)
                self.changeDetNPEnt.grid(row = 3, column = 2, padx = 10, pady = 10)
                self.changeDetNPLbl = Label(master = self.changeDetFrm,text = 'New Password:', font = self.userFont, width = 50, fg = 'black', bg = '#42f5da')
                self.changeDetNPLbl.grid(row = 3, column = 1, padx = 10, pady = 10,sticky = 'e')
                #new password entry and label

                self.changeDetSubmitBtn = Button(master = self.changeDetFrm, width = 30, height = 5, text = 'Submit', fg = 'white', bg = 'black', borderwidth = 5,
                                                 command=lambda:[self.updateDetails(self.changeDetUEnt.get(), self.changeDetPEnt.get(), self.changeDetNPEnt.get())])
                self.changeDetSubmitBtn.grid(row = 4, column = 1, columnspan = 2)
                #submit buton,passes the 3 fields the user has types into the function self.updateDetails


                
        def roomDisplay(self):
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()

                self.c.execute('''SELECT departmentID FROM User WHERE user_name = ?''',(userLoggedIn,))
                self.deptID = self.c.fetchall()

                self.c.execute('''SELECT roomID FROM RoomDept WHERE departmentID = ?''', (self.deptID[0][0],))
                self.roomID = self.c.fetchall()

                self.searchResultNumber = len(self.roomID)
                self.roomList = []
                for x in range(self.searchResultNumber):
                        self.c.execute('''SELECT room_name FROM Room WHERE roomID = ?''', (self.roomID[x][0],))
                        self.throwaway = self.c.fetchall()
                        self.roomList.append(self.throwaway[0][0])
                self.c.execute('''SELECT * FROM RoomDept WHERE departmentID = ?''', (self.deptID[0][0],))
                self.roomDeptResults = self.c.fetchall()
                ##
                self.homepageDisplayFrm.destroy()
                self.homepageDisplayFrm = Frame(master = self.homepageFrm, bg = 'white')
                self.homepageDisplayFrm.grid(row = 2, column = 1, sticky = 'nsew', pady = 15)

                self.roomIDs = []
                self.deptIDs = []
                for i in range (self.searchResultNumber):
                        self.roomIDs.append(self.roomDeptResults[i][0])
                        self.deptIDs.append(self.roomDeptResults[i][1])

                
                self.roomFrames = []
                for i in range (self.searchResultNumber):
                        self.roomFrames.append(self.createRoomFrame(self.roomDeptResults[i][0], self.roomDeptResults[i][1]))
                
                
                if self.searchResultNumber > 0:
                        self.button = []
                        for i in range(self.searchResultNumber):
                                self.button.append(Button(master = self.homepageDisplayFrm, width = 50, height = 1, borderwidth = 5,fg = 'white', bg = 'black',
                                                text = f'Room: {self.roomList[i]}',
                                                command=self.callbackRoom(i+1)))  
                                self.button[i].pack(side = TOP, fill = BOTH)
                

                elif self.searchResultNumber == 0:
                        pass



        def callbackRoom(self,i):#function to bring up the frame of the button.
                def _callback():
                        
                        self.roomFrames[i-1] = self.createRoomFrame(self.roomIDs[i-1],self.deptIDs[i-1])
                        self.showFrame(self.roomFrames[i-1], self.homepageFrm)
                return _callback

        


        def createRoomFrame(self, roomID, deptID):
                self.roomID = roomID
                self.deptID = deptID

                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()

                self.c.execute('''SELECT * FROM Room WHERE roomID = ?''',(self.roomID,))

                self.roomDetailsFetch = self.c.fetchall()
                self.roomName = self.roomDetailsFetch[0][1]
                self.roomDesc = self.roomDetailsFetch[0][2]

                self.c.execute('''SELECT department_name FROM Department WHERE departmentID = ?''',(self.deptID,))

                self.deptDetailsFetch = self.c.fetchall()
                self.deptName = self.deptDetailsFetch[0][0]

                self.c.execute('''SELECT itemID FROM ItemRoom WHERE roomID = ?''', (self.roomID,))
                self.itemIDs = self.c.fetchall()
                self.roomSearchFrm = Frame(master = self.master)
                self.roomSearchFrm.config(bg = '#42f5da')
                self.roomSearchFrm.rowconfigure([0,2,3], weight = 1)
                self.roomSearchFrm.rowconfigure([1], weight = 1, minsize = 300)
                self.roomSearchFrm.columnconfigure([0,2], weight = 1)
                self.roomSearchFrm.columnconfigure([1], weight = 1, minsize = 200)
                
                self.roomSearchTop = Label(master = self.roomSearchFrm, text = f'Name of room: {self.roomName}', font = self.userLargeFont, fg = 'black', bg = '#42f5da')
                self.roomSearchTop.grid(row = 0, column = 1,sticky = 'n', pady = 20)
                
                self.roomSearchDisplayFrm = Frame(master = self.roomSearchFrm,bg = 'white', borderwidth = 3)
                self.roomSearchDisplayFrm.grid(row = 1, column = 1, sticky = 'nsew', pady = 20, columnspan = 1)
               

                self.roomSearchRetBtn = Button(master = self.roomSearchFrm, text='Return', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.showFrame(self.homepageFrm, self.roomSearchFrm)])
                self.roomSearchRetBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                #button to return to home page

                self.roomSearchRefreshBtn = Button(master = self.roomSearchFrm, text='Refresh', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.refresh()])
                self.roomSearchRefreshBtn.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'ne')
                #button to return to home page
                
                

                self.roomSearchRoomDetails = Label(master = self.roomSearchFrm,
                                                   text = f'Room ID:{self.roomID}  |  Room Description:{self.roomDesc}\nDepartment: {self.deptName}  |  Department ID: {self.deptID}',
                                                   fg = 'black', bg = '#42f5da', font = self.userLargeFont)
                self.roomSearchRoomDetails.grid(row = 0, column = 1,sticky = 's')

                self.roomSearchItemTop = Label(master = self.roomSearchDisplayFrm, text = 'Items:', fg = 'black', bg = 'white', font = self.userLargeFont)
                self.roomSearchItemTop.pack(side = TOP)

                
                
                for i in range(len(self.itemIDs)):
                        self.c.execute('''SELECT Item.item_name, ItemRoom.item_Quantity FROM Item INNER JOIN ItemRoom ON Item.itemID = ItemRoom.itemID WHERE ItemRoom.itemID = ? AND ItemRoom.roomID = ?''',
                                       (self.itemIDs[i][0], self.roomID))
                        
                        self.itemRoomFetch = self.c.fetchall()
                        self.roomSearchItemText = Label(master = self.roomSearchDisplayFrm, text = f'Item: {self.itemRoomFetch[0][0]}  |  Quantity: {self.itemRoomFetch[0][1]}',
                                                fg = 'black', bg = 'white', font = self.userFont)
                        self.roomSearchItemText.pack(side = TOP)
                



                self.roomSearchAddLbl1 = Label(master = self.roomSearchFrm, text = 'Add items:', font = self.userFont, fg = 'black', bg = '#42f5da')
                self.roomSearchAddLbl1.grid(row = 2, column = 0,sticky = 'w', pady = 10,padx = 10, columnspan = 2)

                
                self.itemNames = self.getItemList(self.deptID)
                self.variable = tk.StringVar(self.master)
                self.variable.set(self.itemNames[0])
                
                        

                self.roomSearchAddMenu = OptionMenu(self.roomSearchFrm, self.variable, *self.itemNames)
                self.roomSearchAddMenu.grid(row = 2, column = 0,pady = 20, sticky = 'e')

                self.roomSearchAddLbl2 = Label(master = self.roomSearchFrm, text = 'Quantity:', font = self.userFont, fg = 'black', bg = '#42f5da')
                self.roomSearchAddLbl2.grid(row = 2, column = 1, sticky = 'w', pady = 10,padx = 10)

                self.roomSearchAddEnt = Entry(master = self.roomSearchFrm, width = 30, fg = 'black', bg = 'white', borderwidth = 2)
                self.roomSearchAddEnt.grid(row = 2, column = 1, padx = 10, sticky = 'e')

                self.roomSearchAddBtn = Button(master = self.roomSearchFrm, text='Add', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.addItems(self.variable.get(), self.roomSearchAddEnt.get(), self.roomID)])
                self.roomSearchAddBtn.grid(row = 2, column = 2, padx = 5, pady = 5)
                



                self.roomSearchRemLbl1 = Label(master = self.roomSearchFrm, text = 'Remove items:', font = self.userFont, fg = 'black', bg = '#42f5da')
                self.roomSearchRemLbl1.grid(row = 3, column = 0,sticky = 'w', pady = 10,padx = 10, columnspan = 2)

                self.itemNames1 = self.getItemList(self.deptID)
                self.variable1 = tk.StringVar(self.master)
                self.variable1.set(self.itemNames[0])

                self.roomSearchRemMenu = OptionMenu(self.roomSearchFrm, self.variable1, *self.itemNames1)
                self.roomSearchRemMenu.grid(row = 3, column = 0,pady = 20, sticky = 'e')

                self.roomSearchRemLbl2 = Label(master = self.roomSearchFrm, text = 'Quantity(max value to remove all):', font = self.userFont, fg = 'black', bg = '#42f5da')
                self.roomSearchRemLbl2.grid(row = 3, column = 1,sticky = 'w', pady = 10,padx = 10)

                self.roomSearchRemEnt = Entry(master = self.roomSearchFrm, width = 30, fg = 'red', bg = 'white', borderwidth = 2)
                self.roomSearchRemEnt.grid(row = 3, column = 1, padx = 10,sticky = 'e')

                self.roomSearchRemBtn = Button(master = self.roomSearchFrm, text='Remove', width = 9, height = 4,font = self.userFont, fg = 'white', bg = 'black', borderwidth = 5,
                                        command=lambda:[self.removeItems(self.variable1.get(), self.roomSearchRemEnt.get())])
                self.roomSearchRemBtn.grid(row = 3, column = 2, padx = 5, pady = 5)

                                                                   
                return self.roomSearchFrm
        


        def addItems(self, itemName, quantity, roomID):
                self.quantity = quantity
                self.itemName = itemName
                self.itemName = self.itemName.replace("(","")
                self.itemName = self.itemName.replace("'","")
                self.itemName = self.itemName.replace(")","")
                self.itemName = self.itemName.replace(",","")
                
                self.roomID = roomID
                if self.quantity == '':
                        self.toplevel = Toplevel()
                        self.toplevel.geometry('250x250')
                        self.toplevel.title('')
                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'No value entered')
                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                    command=lambda:[exit_btn(self.toplevel)])
                        self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                        
                else:   
                        
                        self.quantity = int(quantity)
                        self.userDetails = sqlite.connect(database_pathfile)
                        self.c = self.userDetails.cursor()
                        self.c.execute('''SELECT ItemRoom.item_Quantity FROM ItemRoom INNER JOIN Item ON (Item.itemID = ItemRoom.itemID) WHERE Item.item_name = ? AND ItemRoom.roomID = ?''', (self.itemName, self.roomID))
                        self.itemAdd = self.c.fetchall()

                        try:
                                if self.itemAdd[0][0] != 0:
                                        self.newQuantity = self.itemAdd[0][0] + self.quantity
                                
                                        self.c.execute('''SELECT itemID FROM Item WHERE item_name = ?''', (self.itemName,))

                                        self.itemID = self.c.fetchall()

                                        self.c.execute('''UPDATE ItemRoom SET item_Quantity = ?  WHERE itemID = ? AND roomID = ?''', (self.newQuantity, self.itemID[0][0], self.roomID))

                                        self.userDetails.commit()
                                        self.c.close()

                                        
                                        self.toplevel = Toplevel()
                                        self.toplevel.geometry('250x250')
                                        self.toplevel.title('')
                                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'Item(s) added: {self.itemName}\nx{self.quantity}')
                                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                                    command=lambda:[exit_btn(self.toplevel)])
                                        self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                                elif self.itemAdd[0][0] == 0:
                                        self.c.execute('''SELECT itemID FROM Item WHERE item_name = ?''', (self.itemName,))
                                        self.itemID = self.c.fetchall()
                                        self.c.execute('''UPDATE ItemRoom SET item_Quantity = ?  WHERE itemID = ? AND roomId = ?''', (self.quantity, self.itemID[0][0],self.roomID,))

                                        self.userDetails.commit()
                                        self.c.close()

                                        self.toplevel = Toplevel()
                                        self.toplevel.geometry('250x250')
                                        self.toplevel.title('')
                                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'Item(s) added: {self.itemName}\nx{self.quantity}')
                                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                                    command=lambda:[exit_btn(self.toplevel)])
                        except IndexError:
                                self.c.execute('''SELECT itemID FROM Item WHERE item_name = ?''', (self.itemName,))

                                self.itemID = self.c.fetchall()
                                
                                self.c.execute('''INSERT INTO ItemRoom(itemID, roomID, item_Quantity) VALUES(?,?,?)''', (self.itemID[0][0], self.roomID, self.quantity))
                                self.userDetails.commit()
                                self.c.close()

                                self.toplevel = Toplevel()
                                self.toplevel.geometry('250x250')
                                self.toplevel.title('')
                                self.toplevellbl = tk.Label(master = self.toplevel, text = f'Item(s) added: {self.itemName}\nx{self.quantity}')
                                self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                                command=lambda:[exit_btn(self.toplevel)])
                                

                
        def removeItems(self,itemName, quantity):
                self.quantity = quantity
                self.itemName = itemName
                self.itemName = self.itemName.replace("(","")
                self.itemName = self.itemName.replace("'","")
                self.itemName = self.itemName.replace(")","")
                self.itemName = self.itemName.replace(",","")
                
                if self.quantity == '':
                        self.toplevel = Toplevel()
                        self.toplevel.geometry('250x250')
                        self.toplevel.title('')
                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'No value entered')
                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                    command=lambda:[exit_btn(self.toplevel)])
                        self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                else:
                        self.quantity = int(quantity)
                        self.userDetails = sqlite.connect(database_pathfile)
                        self.c = self.userDetails.cursor()
                        
                        self.c.execute('''SELECT ItemRoom.item_Quantity FROM ItemRoom INNER JOIN Item ON (Item.itemID = ItemRoom.itemID) WHERE Item.item_name = ? AND ItemRoom.roomID = ?''', (self.itemName, self.roomID))
                        self.itemRemove = self.c.fetchall()
                        
                        self.c.execute('''SELECT itemID FROM Item WHERE item_name = ?''', (self.itemName,))

                        self.itemID = self.c.fetchall()

                        try:
                                if self.itemRemove[0][0] <= self.quantity:
                                        self.c.execute('''UPDATE ItemRoom SET item_Quantity= ? WHERE itemID = ? AND roomID = ?''',(0, self.itemID[0][0],self.roomID))
                                        
                                        self.toplevel = Toplevel()
                                        self.toplevel.geometry('250x250')
                                        self.toplevel.title('')
                                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'Items removed: {self.itemName}')
                                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                                    command=lambda:[exit_btn(self.toplevel)])
                                        self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                                        self.userDetails.commit()
                                        self.c.close()
                                        
                                elif self.itemRemove[0][0] > self.quantity:
                                        self.newQuantity = self.itemRemove[0][0] - self.quantity
                                        self.c.execute('''UPDATE ItemRoom SET item_Quantity = ?  WHERE itemID = ? AND roomID = ?''', (self.newQuantity, self.itemID[0][0], self.roomID))
                                        
                                        self.toplevel = Toplevel()
                                        self.toplevel.geometry('250x250')
                                        self.toplevel.title('')
                                        self.toplevellbl = tk.Label(master = self.toplevel, text = f'Items removed: {self.itemName}\nx{self.quantity}')
                                        self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                        self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                                    command=lambda:[exit_btn(self.toplevel)])
                                        self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                                        self.userDetails.commit()
                                        self.c.close()
                                        
                        except IndexError:
                                self.toplevel = Toplevel()
                                self.toplevel.geometry('250x250')
                                self.toplevel.title('')
                                self.toplevellbl = tk.Label(master = self.toplevel, text = f'Item {self.itemName} not in room.')
                                self.toplevellbl.pack(side=TOP, padx = 5, pady = 10)
                                self.toplevelbtn = tk.Button(master = self.toplevel, text = 'Close', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                                        command=lambda:[exit_btn(self.toplevel)])
                                self.toplevelbtn.pack(side=BOTTOM, padx = 5, pady = 30)
                                self.userDetails.commit()
                                self.c.close()


                        
                                
                                
                        





        
        def updateDetails(self, username, password, newPassword):
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.username = username
                self.password = password
                self.newPassword = newPassword
                #connecting to database stored in variable 'database_pathfile' 
                #fetching from database
                self.c.execute('''SELECT user_name, password
                        FROM User
                        WHERE user_name = ? AND password = ?
                        ''',(self.username,self.password)
                        )
                self.fetch = self.c.fetchall()
                #selecting usernames and passwords where it matches the username and password entered by the user
                try:
                        self.throwaway = self.fetch[0][0]
                        #tests if the list self.fetch has any indexes, if it doesn't, then run the code in the Except IndexError block.
                        self.c.execute('''UPDATE User
                                SET password = ?
                                WHERE user_name = ? 
                                ''',(self.newPassword, self.username)
                                )
                        self.userDetails.commit()
                        self.c.close()
                        #update the database with the new password
                        self.successUpdatetp = Toplevel()
                        self.successUpdatetp.title('')
                        self.successUpdatetp.geometry('300x300')
                        self.successUpdateLbl = tk.Label(master = self.successUpdatetp, text = f'Success\nYour new password is\n {self.newPassword}', font = self.userFont)
                        self.successUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.successUpdateBtn = tk.Button(master = self.successUpdatetp, text = 'Close', command=lambda:[exit_btn(self.successUpdatetp)], font = self.userFont)
                        self.successUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)
                        #success window if the username and password match and the details were successfully updated      
                except IndexError:
                        #error window if the self.fetch[0][0] list has no entries(username and password do not match)
                        self.errorUpdatetp = Toplevel()
                        self.errorUpdatetp.title('')
                        self.errorUpdatetp.geometry('300x300')
                        self.errorUpdateLbl = tk.Label(master = self.errorUpdatetp, text = 'Your password does not match your username', font = self.userFont)
                        self.errorUpdateLbl.pack(side=TOP, padx = 10, pady = 10)
                        self.errorUpdateBtn = tk.Button(master = self.errorUpdatetp, text = 'Try again', command=lambda:[exit_btn(self.errorUpdatetp)], font = self.userFont)
                        self.errorUpdateBtn.pack(side=BOTTOM, padx = 20, pady = 20)




        def logoutConfirm(self, windowInput):
                self.windowInput = windowInput
                self.logConfirm = Toplevel()
                self.logConfirm.geometry('250x250')
                self.logConfirm.title('Confirm')
                self.logConfirmLbl = tk.Label(master = self.logConfirm, text = 'Are you sure you want to log out?')
                self.logConfirmLbl.pack(side=TOP, padx = 5, pady = 10)
                self.logConfirmBtn = tk.Button(master = self.logConfirm, text = 'Logout', width = 20, height = 1,font = self.userFont, fg = 'black', bg = 'white',
                                            command=lambda:[exit_btn(self.windowInput), normal_open(), setUserLoggedIn()])
                self.logConfirmBtn.pack(side=BOTTOM, padx = 5, pady = 30)
                
                #pop-up window asking to confirm before logging the user out, takes user back to login - normal_open()

     

        def getItemList(self, deptID):
                self.deptID = deptID
                self.userDetails = sqlite.connect(database_pathfile)
                self.c = self.userDetails.cursor()
                self.c.execute('''SELECT Item.item_name FROM Item INNER JOIN ItemDept ON ItemDept.itemID = Item.itemID WHERE ItemDept.departmentID = ?''',(self.deptID,))
                self.itemNameList = self.c.fetchall()
                        
                
                
                return self.itemNameList


        def refresh(self):
                self.master.destroy()
                userMain()
                #function to refresh the page(by destroying it and re-opening it)

        

        def showFrame(self, frameRaise, frameForget):
                self.frameForget = frameForget
                self.frameForget.forget()
                self.frameRaise = frameRaise
                self.frameRaise.pack(fill = BOTH, expand = True)
                self.frameRaise.tkraise()
                #a function used to raise a frame to the top of the stack(i.e. when the user wants to change screens
                #takes in two parameters, the frame to raise and the frame to drop, forgets one frame and fills the frame to the window







if not os.path.isfile("User_Details.db"):    
    
        first_open()
    #running the initialisation funtion

else:

        normal_open()
    #running the normal login UI function





