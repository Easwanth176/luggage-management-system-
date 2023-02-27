import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
root=tk.Tk()
global x
x='light blue'
import mysql.connector
mydb = mysql.connector.connect(user='root',host='localhost',password='1234',database='cherry')
mycursor=mydb.cursor()


try:   
        mycursor.execute("create table agents(id int,agentid int,name varchar(20),password varchar(20),primary key(agentid))")
        mycursor.execute("insert into agents values(1,12106096,'easwanth','5544')")
        mycursor.execute("insert into agents values(2,12106097,'Hemanth','1234')")
        mycursor.execute("insert into agents values(3,12106098,'Pavan','5678')")
        mycursor.execute("insert into agents values(4,12106099,'Kiran','0000')")
        

        mydb.commit()
except:
        pass


try:
      mycursor.execute("create table customer(customerid int AUTO_INCREMENT,name varchar(20),mail varchar(25),mobile varchar(20),password varchar(20),primary key(customerid))")
      mycursor.execute("insert into customer values(12106096,'easwanth','easwanth12@gmail.com',7777912365,'5544')")
      mydb.commit()
except:
      pass



try:
            mycursor.execute("create table locations(locationid int,state varchar(20),city varchar(20),distance int,primary key(locationid))")
            mycursor.execute("insert into locations values(1,'tamilnadu','chennai',2700)")
            mycursor.execute("insert into locations values(2,'telengana','hyderabad',2200)")
            mycursor.execute("insert into locations values(3,'Andhra pradesh','trichy',2300)")
            mycursor.execute("insert into locations values(4,'kerala','kochi',2400)")
            mycursor.execute("insert into locations values(5,'karnataka','bangalore',2500)")
            mycursor.execute("insert into locations values(6,'uttar pradesh','varanasi',1600)")   
            mydb.commit()
except:
      pass


try:
      mycursor.execute("create table items(itemid int ,customerid int,weight int,quantity int,itype varchar(20),primary key(itemid),foreign key(customerid) references customer(customerid))") 
      mydb.commit()
except:
      pass


try:
      mycursor.execute("create table payment(paymentid int,customerid int,itemid int,amount int,card int,ptype varchar(20),primary key(paymentid),foreign key(customerid) references customer(customerid),foreign key(itemid) references items(itemid))")
      mydb.commit()
except:
      pass


try:
      mycursor.execute("create table orders(orderid int,locationid int,customerid int,paymentid int,itemid int,primary key(orderid),foreign key(locationid) references locations(locationid),foreign key(customerid) references customer(customerid),foreign key(paymentid) references payment(paymentid),foreign key(itemid) references items(itemid))")
      mydb.commit()
except:
      pass



def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()



def alogin():
      clear_frame()
      global username,password
      label=tk.Label(root,text="AGENT LOGIN",font=("Arial",30),bg=x)
      label.place(x=150,y=40)
      label1=tk.Label(root,text="Agent Id",bg=x,font=("Arial",20))
      label1.place(x=100,y=190)
      username=ttk.Entry(root,width=16,font=("Arial",18))
      username.place(x=300,y=190)
      label2=tk.Label(root,text="Password",font=("Arial",20),bg=x)
      label2.place(x=100,y=290)
      password=tk.Entry(root,width=16,font=("Arial",18),show="*")
      password.place(x=300,y=290)
      button2=tk.Button(root,text="Back",command=home,width=10,height=2)
      button2.place(x=150,y=450)
      button3=tk.Button(root,text="Login",command=validation,width=10,height=2)
      button3.place(x=370,y=450)


def validation():
      global username1,password1
      username1=username.get()
      password1=password.get()
      clear_frame()
      msg=''
      mycursor.execute("select * from agents where agentid=%s and password=%s",(username1,password1))
      result=mycursor.fetchall()
      print(result)
      if result == []:
            alogin()
            msg='invalid username or password'
            messagebox.showinfo('error',msg)
            
      if msg=='':
            agent() 


def payment():
      clear_frame()
      global entry1
      label=tk.Label(root,text="PAYMENT DETAILS",font=("Arial",30),bg=x)
      label.place(x=120,y=40)
      label=tk.Label(root,text="Payment Number",font=("Arial",20),bg=x)
      label.place(x=80,y=180)
      entry1=tk.Entry(root,width=20,font=("Arial",15))
      entry1.place(x=300,y=185)
      button1=tk.Button(root,text="PAYMENT STATUS",font=("Arial",15),command=print1)
      button1.place(x=280,y=300)
      button2=tk.Button(root,text="Back",font=("Arial",15),command=agent)
      button2.place(x=80,y=300)


def print1():
      entry2=entry1.get()
      clear_frame()
      mycursor.execute("select * from payment where paymentid=%s",(entry2,))
      result=mycursor.fetchall()
      print(result)
      label=tk.Label(root,text='PAYMENT STATUS',font=("Arial",30),bg=x)
      label.place(x=150,y=40)
      label=tk.Label(root,text="Payment id ",font=("Arial",20),bg=x)
      label.place(x=80,y=150)
      label1=tk.Label(root,text=result[0][0],font=("Arial",20),bg=x)
      label1.place(x=300,y=150)
      label2=tk.Label(root,text="Customer name ",font=("Arial",20),bg=x)
      label2.place(x=80,y=200)
      mam=result[0][1]
      mycursor.execute("select * from customer where customerid=%s",(mam,))
      result1=mycursor.fetchall()
      label3=tk.Label(root,text=result1[0][1],font=("Arial",20),bg=x)
      label3.place(x=300,y=200)
      label4=tk.Label(root,text="Toatal amount ",font=("Arial",20),bg=x)
      label4.place(x=80,y=250)
      label5=tk.Label(root,text=result[0][3],font=("Arial",20),bg=x)
      label5.place(x=300,y=250)
      label6=tk.Label(root,text="Payment type ",font=("Arial",20),bg=x)
      label6.place(x=80,y=300)
      label7=tk.Label(root,text=result[0][5],font=("Arial",20),bg=x)
      label7.place(x=300,y=300)
      label8=tk.Label(root,text="Payment status ",font=("Arial",20),bg=x)
      label8.place(x=80,y=350)
      label9=tk.Label(root,text='Sucess',font=("Arial",20),bg=x)
      label9.place(x=300,y=350)
      lable10=tk.Label(root,text="Item id ",font=("Arial",20),bg=x)
      lable10.place(x=80,y=400)
      lable11=tk.Label(root,text=result[0][2],font=("Arial",20),bg=x)
      lable11.place(x=300,y=400)

      button1=tk.Button(root,text="back",font=("Arial",20),command=agent)
      button1.place(x=200,y=500)
           
          
def item():
      clear_frame()
      global entry
      label=tk.Label(root,text="ITEM DETAILS",font=("Arial",30),bg=x)
      label.place(x=120,y=40)
      label=tk.Label(root,text="Item number",font=("Arial",20),bg=x)
      label.place(x=80,y=180)
      entry=tk.Entry(root,width=20,font=("Arial",15))
      entry.place(x=300,y=185)
      button1=tk.Button(root,text="Item STATUS",font=("Arial",15),command=print2)
      button1.place(x=300,y=300)
      button2=tk.Button(root,text="Back",font=("Arial",15),command=agent)
      button2.place(x=100,y=300)

def print2():
      entry1=entry.get()
      clear_frame()
      mycursor.execute("select * from items where itemid=%s",(entry1,))
      result=mycursor.fetchall()
      print(result)
      label=tk.Label(root,text='ITEM STATUS',font=("Arial",30),bg=x)
      label.place(x=150,y=40)
      label=tk.Label(root,text="Item id ",font=("Arial",20),bg=x)
      label.place(x=80,y=200)
      label1=tk.Label(root,text=result[0][0],font=("Arial",20),bg=x)
      label1.place(x=280,y=200)
      nam=result[0][1]
      print(nam)
      mycursor.execute("select * from customer where customerid=%s",(nam,))
      result1=mycursor.fetchall()
      label2=tk.Label(root,text="customer name ",font=("Arial",20),bg=x)
      label2.place(x=80,y=150)
      label3=tk.Label(root,text=result1[0][1],font=("Arial",20),bg=x)
      label3.place(x=300,y=150)
      label4=tk.Label(root,text="item weight ",font=("Arial",20),bg=x)
      label4.place(x=80,y=250)
      label5=tk.Label(root,text=result[0][2],font=("Arial",20),bg=x)
      label5.place(x=300,y=250)
      label6=tk.Label(root,text="item quantity ",font=("Arial",20),bg=x)
      label6.place(x=80,y=300)
      label7=tk.Label(root,text=result[0][3],font=("Arial",20),bg=x)
      label7.place(x=300,y=300)
      label8=tk.Label(root,text="item type ",font=("Arial",20),bg=x)
      label8.place(x=80,y=350)
      label9=tk.Label(root,text=result[0][4],font=("Arial",20),bg=x)
      label9.place(x=300,y=350)
      button1=tk.Button(root,text="back",font=("Arial",20),command=agent)
      button1.place(x=200,y=450)

def customerdetails():
      global entry5
      clear_frame()
      label=tk.Label(root,text="Customer details",font=("Arial",30),bg=x)
      label.place(x=120,y=40)
      label1=tk.Label(root,text="customer id",font=("Arial",20),bg=x)
      label1.place(x=80,y=180)
      entry5=tk.Entry(root,width=20,font=("Arial",15))
      entry5.place(x=300,y=185)
      button1=tk.Button(root,text="customer details",font=("Arial",15),command=print3)
      button1.place(x=300,y=300)
      button2=tk.Button(root,text="back",font=("Arial",15),command=agent)
      button2.place(x=100,y=300)

def print3():
      entry6=[(entry5.get())]
      clear_frame()    
      label=tk.Label(root,text="Customer details",font=("Arial",30),bg=x)
      label.place(x=150,y=50) 
      mycursor.execute("select * from customer where customerid=%s",(entry6))
      result=mycursor.fetchall()
      label=tk.Label(root,text="customer id ",font=("Arial",20),bg=x)
      label.place(x=80,y=150)
      label1=tk.Label(root,text=result[0][0],font=("Arial",20),bg=x)
      label1.place(x=280,y=150)
      label2=tk.Label(root,text="Name ",font=("Arial",20),bg=x)
      label2.place(x=80,y=200)
      label3=tk.Label(root,text=result[0][1],font=("Arial",20),bg=x)
      label3.place(x=280,y=200)
      label4=tk.Label(root,text="Mail ",font=("Arial",20),bg=x)
      label4.place(x=80,y=250)
      label5=tk.Label(root,text=result[0][2],font=("Arial",20),bg=x)
      label5.place(x=280,y=250)
      label6=tk.Label(root,text="Phone no ",font=("Arial",20),bg=x)
      label6.place(x=80,y=300)
      label7=tk.Label(root,text=result[0][3],font=("Arial",20),bg=x)
      label7.place(x=280,y=300)
      label8=tk.Label(root,text="Orders Placed",font=("Arial",20),bg=x)
      label8.place(x=80,y=350)
      label9=tk.Label(root,text="5",font=("Arial",20),bg=x)
      label9.place(x=280,y=350)
      button1=tk.Button(root,text="Back",font=("Arial",20),command=agent)
      button1.place(x=200,y=450)

def agent():

      clear_frame()
      label=tk.Label(root,text="AGENT PORTAL",font=("Arial",30),bg=x)
      label.place(x=150,y=40)
      button1=tk.Button(root,text="PAYMENT STATUS",font=("Arial",15),command=payment,width=20,height=2)
      button1.place(x=200,y=130)
      button2=tk.Button(root,text="ITEM DETAILS",font=("Arial",15),command=item,width=20,height=2)
      button2.place(x=200,y=230)
      button3=tk.Button(root,text="LOGOUT",font=("Arial",15),command=home,width=20,height=2)
      button3.place(x=200,y=430)
      button4=tk.Button(root,text="CUSTOMER DETAILS",font=("Arial",15),command=customerdetails,width=20,height=2)
      button4.place(x=200,y=330)
         
def signup():
      clear_frame()
      global name,mail,mobile,password
      label=tk.Label(root,text="COUSTMER SIGN UP ",font=("Arial",30),bg=x)
      label.place(x=100,y=40)
      label1=tk.Label(root,text=" Name",font=("Arial",20),bg=x)
      label1.place(x=100,y=150)
      name=tk.Entry(root,width=15,font=("Arial",18))
      name.place(x=300,y=150)
      label2=tk.Label(root,text="Mail",font=("Arial",20),bg=x)
      label2.place(x=100,y=250)
      mail=ttk.Entry(root,width=16,font=("Arial",18))
      mail.place(x=300,y=250)
      label3=tk.Label(root,text="Mobile",font=("Arial",20),bg=x)
      label3.place(x=100,y=350)
      mobile=ttk.Entry(root,width=16,font=("Arial",18))
      mobile.place(x=300,y=350)
      label4=tk.Label(root,text="Password",font=("Arial",20),bg=x)
      label4.place(x=100,y=450)
      password=tk.Entry(root,width=16,font=("Arial",18))
      password.place(x=300,y=450)
      button1=tk.Button(root,width=10,text="back",command=home,height=2)
      button1.place(x=180,y=530)
      button2=tk.Button(root,text="sign up",width=10,command=signup1,height=2)
      button2.place(x=370,y=530)

def signup1():
      global name1,mail1,mobile1,password1
      name1=name.get()
      mail1=mail.get()
      mobile1=mobile.get()
      password1=password.get()
      clear_frame()
      msg=''
      mycursor.execute("select * from customer where mail=%s",(mail1,))
      result=mycursor.fetchall()
      print(result)
      
      if mail1=='' or password1=='' or name1=='' or mobile1=='':
            signup()
            msg='please fill all the details'
            messagebox.showinfo('error',msg)
            

      if result != []:
            signup()
            msg='mail already exist'
            messagebox.showinfo('error',msg)


      if msg=='':
            ulogin()
            mycursor.execute("insert into customer(name,mail,mobile,password) values(%s,%s,%s,%s)",(name1,mail1,mobile1,password1))
            mycursor.execute("commit")
            messagebox.showinfo('success','signup successfully')
            
def placeorder():
      clear_frame()
      global producttype,weight,quantity,price,selected_type
      l1=tk.Label(root,text="PLACE ORDER",font=("Arial",30),bg=x)
      l1.place(x=150,y=50)
      l2=tk.Label(root,text="Enter location",font=("Arial",20),bg=x)
      l2.place(x=60,y=150)
      selected_type = tk.StringVar()
      location=ttk.Combobox(root,width=16,textvariable=selected_type,font=("Arial",15),state='readonly')
      mycursor.execute("select * from locations")
      result=mycursor.fetchall()
      location['values']=result[0][2],result[1][2],result[2][2],result[3][2],result[4][2],result[5][2]
      location.place(x=310,y=150)
      l3=tk.Label(root,text="Enter type",font=("Arial",20),bg=x)
      l3.place(x=60,y=370)
      producttype=ttk.Combobox(root,width=16,font=("Arial",15),state='readonly')
      producttype['values']='liquid','solid','other'
      producttype.place(x=310,y=370)
      l4=tk.Label(root,text="Enter weight",font=("Arial",20),bg=x)
      l4.place(x=60,y=220)
      weight=tk.Entry(root,width=16,font=("Arial",16))
      weight.place(x=310,y=220)
      l5=tk.Label(root,text="Enter quantity",font=("Arial",20),bg=x)
      l5.place(x=60,y=300)
      quantity=ttk.Entry(root,width=16,font=("Arial",16))
      quantity.place(x=310,y=300)
      button1=tk.Button(root,text="Back",command=home,width=15,height=2)
      button1.place(x=150,y=480)
      button2=tk.Button(root,text="place order",width=15,height=2,command=lambda:placeorder1(location.get(),producttype.get(),weight.get(),quantity.get()))
      button2.place(x=350,y=480)

def placeorder1(location,producttype,weight,quantity):
      username=username1
      global price,id
      id=random.randint(1000,9999)
      price=int(float(weight))*int(float(quantity))
      if location=='' or producttype=='' or weight=='' or quantity=='':
            placeorder()
            messagebox.showinfo('error','please fill all the details')
      else:
            mycursor.execute("insert into items(itemid,customerid,weight,quantity,itype)values(%s,%s,%s,%s,%s)",(id,username,weight,quantity,producttype))
            mydb.commit()
            pay()

def pay():
      st=selected_type.get()
      clear_frame()
      paymentid=random.randint(1000,9999)
      l1=tk.Label(root,text="PAYMENT PAGE",font=("Arial",30),bg=x)
      l1.place(x=150,y=50)
      l2=tk.Label(root,text=" Payment Method",font=("Arial",20),bg=x)
      l2.place(x=60,y=150)
      payment=ttk.Combobox(root,width=16,font=("Arial",18),state='readonly')
      payment['values']='cash on delivery','online payment','paytm','phonepe','google pay'
      payment.place(x=300,y=150)
      l3=tk.Label(root,text="Enter cvv",font=("Arial",20),bg=x)
      l3.place(x=60,y=220)
      cvv=ttk.Entry(root,width=16,font=("Arial",18))
      cvv.place(x=300,y=220)
      l4=tk.Label(root,text="Total Ammount",font=("Arial",20),bg=x)
      l4.place(x=60,y=280)
      l5=tk.Label(root,text=price,font=("Arial",20),state='disabled',bg=x)
      l5.place(x=300,y=280)
      l4=tk.Label(root,text="From Location",font=("Arial",20),bg=x)
      l4.place(x=60,y=340)
      l6=tk.Label(root,text="Jalandhar",font=("Arial",20),state='disabled',bg=x)
      l6.place(x=300,y=340)  
      l4=tk.Label(root,text="TO Location",font=("Arial",20),bg=x)
      l4.place(x=60,y=400)
      l6=tk.Label(root,text=st,font=("Arial",20),state='disabled',bg=x)
      l6.place(x=300,y=400)      
      button1=tk.Button(root,text="Back",command=home,width=10,height=2)
      button1.place(x=200,y=500)
      button2=tk.Button(root,text="Pay",width=10,height=2,command=lambda:pay1(payment.get(),cvv.get()))
      button2.place(x=300,y=500)

def pay1(payment,cvv):
      username=username1
      paymentid=random.randint(1000,9999)
      ammount=price
      if payment=='' or cvv=='':
            pay()
            messagebox.showinfo('error','please fill all the details')
      else:
            mycursor.execute("insert into payment values(%s,%s,%s,%s,%s,%s)",(paymentid,username,id,ammount,cvv,payment))
            mydb.commit()
            messagebox.showinfo('success','payment successfully')
            messagebox.showinfo('payment id',paymentid)
            home()

def ulogin():
      clear_frame()
      global username,password
      label=tk.Label(root,text="CUSTOMER LOGIN",bg=x,font=("Arial",30))
      label.place(x=120,y=40)
      label1=tk.Label(root,text="Customer Id",bg=x,font=("Arial",20))
      label1.place(x=100,y=190)
      username=tk.Entry(root,width=16,font=("Arial",18))
      username.place(x=300,y=190)
      label2=tk.Label(root,text="Password",font=("Arial",20),bg=x)
      label2.place(x=100,y=290)
      password=tk.Entry(root,width=16,font=("Arial",18),show="*")
      password.place(x=300,y=290)
      button1=tk.Button(root,text="Back",font=("Arial",20),command=home,width=10,height=1)
      button1.place(x=100,y=450)
      button2=tk.Button(root,text="Login",font=("Arial",20),command=cvalidation,width=10,height=1)
      button2.place(x=370,y=450)

def cvalidation():
      global username1,password1
      username1=username.get()
      password1=password.get()
      mycursor.execute("select * from customer where customerid=%s and password=%s",(username1,password1))
      result=mycursor.fetchall()
      print(result)
      if result != []:
            placeorder()
      else:
            ulogin()
            messagebox.showinfo('error','invalid username or password')
            
def customer():
      clear_frame()
      label=tk.Label(root,text="CUSTOMER PORTAL",font=("Arial",30),bg=x)
      label.place(x=100,y=60)
      button1=tk.Button(root,text="signup",font=("Arial",20),command=signup,width=10,height=2)
      button1.place(x=70,y=250)
      button2=tk.Button(root,text="login",font=("Arial",20),command=ulogin,width=10,height=2)
      button2.place(x=370,y=250)

def home():
      clear_frame()
      label=tk.Label(root,text="LAUGGAUGE MANAGEMENT SYSTEM",font=("Arial",22),bg=x)
      label.place(x=40,y=50)
      button1=tk.Button(root,text="customer",font=("Arial",20),command=customer,width=10,height=2)
      button1.place(x=190,y=180)
      button2=tk.Button(root,text="agent",font=("Arial",20),command=alogin,width=10,height=2)
      button2.place(x=190,y=350)

 

root.geometry("600x600")
root.resizable(False, False)
root.configure(background='light blue')
home()
root.mainloop()