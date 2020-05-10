#Name - Avichal Srivastava, Vikas Kumar, Sumit Saurabh
#Email - avichalsrivastava24@gmail.com
#Python 3.7


from tkinter import *
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image
from tkinter import ttk
import time

login=sqlite.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''


def stock():
    
    application.destroy()
    
    login.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    open_win()

def dailyincome():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    open_win()    
    
def billingitems():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    open_win()
    
def delstock():
    
    application.destroy()
    login.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    open_win()
    
def updatestock():
    
    application.destroy()

    login.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    open_win()
    
def expirycheck():
    
    application.destroy()
    login.close()
    
    import expirycheck
    a = expirycheck.expiry()
    
    open_win()
    
def again():   
    ''' Main Login Window'''
    global un, pwd, WinStat, root, application
    if WinStat=='application':
        application.destroy()
    root=Tk()
    
    root.geometry("800x620")
    root.title('Supermarket Management System')
    root.wm_iconbitmap('favicon.ico')
    root.configure(background="#FFA500")
    img = ImageTk.PhotoImage(Image.open('xx.jpg'))
    panel = Label(root, image = img).grid(row=0, column=0,columnspan=7)
   
    Label(root,text='Supermarket Management System',background="#FFA500",font=("Courier", 24)).grid(row=1,column=1,columnspan=5)
    Label(root,text="NIT Manipur, Langol, Imphal West, Manipur",background="#FFA500",font=("Courier", 12)).grid(row=2,column=1,columnspan=5)
    Label(root,text='----------------------------------------------------------------------------------------------------',background="#FFA500").grid(row=3,column=1,columnspan=5)
    Label(root, text='    USERNAME',background="#FFA500",font=("Courier", 10)).grid(row=4, column=0,columnspan=5)
    un=Entry(root,width=20)
    un.grid(row=4, column=1,columnspan=6)
    Label(root, text='    PASSWORD',background="#FFA500",font=("Courier", 10)).grid(row=5, column=0,columnspan=5)
    pwd=Entry(root,width=20, show="*")
    pwd.grid(row=5, column=1,columnspan=6)
    Label(root,text='',background="#FFA500").grid(row=6,column=0,columnspan=100)
    Button(root,width=6,text='Enter',command=check).grid(row=7, column=0,columnspan=6)
    Button(root,width=6,text='Close',command=root.destroy).grid(row=7, column=1,columnspan=5)
    root.mainloop()
    
def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    u=un.get()
    p=pwd.get()
    if 'admin'!=u or 'admin'!=p:
        top=Tk()
        top.geometry("220x30")
        top.title('Error')
        top.wm_iconbitmap('favicon.ico')
        Label(top,width=30, text='Wrong Username or Password').grid(row=1, column=0)

        top.mainloop()
    else:
        root.destroy()
        open_win()
    
    
        
    

def open_win(): 
    ''' Opens Main Window '''
    global application, WinStat
    WinStat='application'
    application=Tk()
    application.wm_iconbitmap('favicon.ico')
    
  
    application.title("Supermarket Management System")
    application.geometry("720x500")
    
    ''' Main Window Picture '''
    img = ImageTk.PhotoImage(Image.open('d.jpg'))
    panel = Label(application, image = img).grid(row=0, column=0,columnspan=5)
    
   

    
    menu_bar = Menu(application)
    stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=0)
    billing_menu = Menu(menu_bar,tearoff=0)
    '''Stock Maintainance'''
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    billing_menu.add_command(label="Check Today's Income", command=dailyincome)
    
    
    
    
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="Check Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Stock Maintainance", menu=stock_menu)
    menu_bar.add_cascade(label="Logout",command=again)
    application.config(menu=menu_bar)
    
    
    
        
    application.mainloop()

    

    
    
    
    
again()
