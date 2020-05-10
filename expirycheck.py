#Name - Avichal Srivastava, Vikas Kumar, Sumit Saurabh
#Email - avichalsrivastava24@gmail.com
#Python 3.7

from tkinter import *
from sqlite3 import dbapi2 as sqlite
import time


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()



def expiry():
    ''' Expiry GUI '''
    global expirychk, expdate,c, cur, flag
    total=0.0
    today=str(time.localtime()[2])+'/'+str(time.localtime()[1])+'/'+str(time.localtime()[0])
    
    flag='expirychk'
    groitem=[]
    cur.execute("select * from grocerylist")
    for i in cur:
        groitem.append(i[1])
    c.commit()
    expirychk=Tk()
    expirychk.title('EXPIRY')
    expirychk.wm_iconbitmap('favicon.ico')
    Label(expirychk,text='Date: '+today,font=("Courier", 10)).grid(row=0,column=0,columnspan=3)
    Label(expirychk,text='').grid(row=4, column=0)
    Label(expirychk,text='-'*50,font=("Courier", 10)).grid(row=2, column=0,columnspan=3)
    expdate=Spinbox(expirychk,values=groitem,font=("Courier", 10))
    expdate.grid(row=3, column=0)
    
    Button(expirychk,text='Check Expiry Date', command=chkexpiry,font=("Courier", 10)).grid(row=3, column=1)
    Label(expirychk,text='-'*50,font=("Courier", 10)).grid(row=6, column=0,columnspan=3)
    
    Button(expirychk,text='Main Menu',command=mainmenu,font=("Courier", 10)).grid(row=4, column=1,)
    expirychk.mainloop()
    
def chkexpiry():    
    ''' Check Expiry Date button will navigate here '''
    global c, cur, expdate, expirychk
    cur.execute("select * from grocerylist")
    for i in cur:
        if(i[1]==expdate.get()):
            Label(expirychk, text="Expiry: "+i[5],font=("Courier", 10)).grid(row=4, column=0)
    c.commit()
    
    
def mainmenu():
    if flag=='expirychk':
        expirychk.destroy()
    
    
