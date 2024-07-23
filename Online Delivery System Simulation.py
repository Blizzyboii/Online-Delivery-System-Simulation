from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='Sunay123!')
if mycon.is_connected():
    print('SUCCESSFUL')

cursor=mycon.cursor()
cursor.execute("use ELECTRONICS")
window=Tk()

p=0
def openNewWindow():
    global s,p
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(x=540,y=460)

    progress_bar["value"] = 0  # Reset progress bar
    for i in range(11):  # Iterate from 0% to 100%
        window.update_idletasks()  # Update the GUI
        progress_bar["value"] = i * 10
        import time
        time.sleep(0.2)  # Wait for 1 second
    window.destroy()

    root=Tk()
    root.title("Electronics Delivery System")
    root.geometry("1920x1080+0+0")

        #==========================================FRAMES========================================

    def newopenWINDOW():
        cursor.execute("select * from customer")
        f=cursor.fetchall()
            
        if p>0 and f!=None:
            root.destroy()

            root1=Tk()
            root1.title("Electronics Delivery System")
            root1.geometry("1920x1080")

            checkouttitle = Label(root1, text="CHECKOUT", bg="red", fg="cyan", bd=10, relief=RIDGE,font=("times new roman", 30, "bold"), padx=2, pady=6)
            checkouttitle.pack(side=TOP,fill=X)

            frameleft=Frame(root1,bd=10,relief=RIDGE,padx=20,bg="light green")
            frameleft.place(x=0,y=80,width=1270,height=610)

            trv=ttk.Treeview(root1,selectmode="browse")
            trv.pack(padx=20,pady=20)
            style = ttk.Style()
            style.configure("Treeview.Heading", font=(None, 20))
            style.configure("Treeview", background="light blue")
            trv["columns"]=("1","2","3")
            trv["show"]="headings"
            trv.column("1",width=200,anchor="c")
            trv.column("2",width=100,anchor="c")
            trv.column("3",width=150,anchor="c")
            trv.heading("1",text="PRODUCT")
            trv.heading("2",text="PRICE")
            trv.heading("3",text="QUANTITY")

            cursor.execute("select * from customer")
            data=cursor.fetchall()
            for i in data:
                trv.insert("","end",iid=i[0],text=i[0],values=(i[0],i[1],i[2]))

            cursor.execute("select sum(price*quantity) from customer")
            data2=cursor.fetchall()
            for i in data2:
                x=i[0]
            x=str(x)
            x="₹"+x
            End=Label(root1,text="TOTAL PRICE IS",bg="light green",fg="#257DAD",bd=5,font=("times new roman",25,"bold"))
            End.place(x=450,y=350,width=400,height=50)
            my_string_variable = StringVar()
            my_string_variable.set(x)
            priceval = Label(root1, textvariable=my_string_variable,fg="#FF5733",bg="light green",bd=5,font=("times new roman",25,"bold"))
            priceval.place(x=580,y=400)

            def placeorder():
                k=Label(root1, text="YOUR ORDER HAS BEEN PLACED SUCCESSFULLY \n IT WILL REACH YOUR HOUSE IN 3 DAYS !",bg="light green",fg="#257DAD",font=("times new roman",25,"bold"))
                k.place(x=240,y=540)
                cursor.execute("delete from customer")
                mycon.commit()
            #def cancelorder():
                #messagebox.showinfo("cancelled","Your order has been cancelled")
                
            order=Button(root1,text="PLACE ORDER !",bg="purple",fg="white",font=("times new roman",25,"bold"),command=placeorder).place(x=500,y=450)
        elif p==0:
            messagebox.showerror("Error","Kindly select one method of payment and confirm your details to checkout")
        elif f==None:
            messagebox.showerror("Error","Kindly select atleast one item to checkout")


        #==========================================FRAMES========================================


    lbltitle=Label(root,text="ONLINE DELIVERY SYSTEM",bg="red",fg="cyan",bd=10,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
    lbltitle.pack(side=TOP,fill=X)

    frameleft=Frame(root,bd=10,relief=RIDGE,padx=20,bg="light green")
    frameleft.place(x=0,y=80,width=700,height=610)

    frameup=LabelFrame(root,text="Types of Electronics available:",bg="light green",fg="blue",bd=10,relief=RIDGE,font=("algerian",27))
    frameup.place(x=10,y=90,width=680,height=280)

    framedown=LabelFrame(root,text="Products available:",bg="light green",fg="blue",bd=10,relief=RIDGE,font=("algerian",27))
    framedown.place(x=10,y=370,width=680,height=310)


    frameright=Frame(root,bd=10,relief=RIDGE,padx=20,bg="light green")
    frameright.place(x=700,y=80,width=570,height=610)

    frameupr=LabelFrame(root,text="CUSTOMER DETAILS",bg="light green",fg="blue",bd=10,relief=RIDGE,font=("algerian",27))
    frameupr.place(x=710,y=90,width=550,height=280)

    framedownright=LabelFrame(root,text="Cart",bg="light green",fg="blue",bd=10,relief=RIDGE,font=("algerian",27))
    framedownright.place(x=710,y=370,width=550,height=310)



                #==========================================LABELS======================================

    phone=Label(frameup,text="PHONES",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    phone.place(x=7,y=7,width=200,height=50)

    tablet=Label(frameup,text="TABLETS",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    tablet.place(x=7,y=57,width=200,height=50)

    laptop=Label(frameup,text="LAPTOP",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    laptop.place(x=7,y=107,width=200,height=50)


    AC=Label(frameup,text="AIR CONDITIONERS",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    AC.place(x=272,y=7,width=340,height=50)

    refri=Label(frameup,text="REFRIGERATORS",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    refri.place(x=272,y=57,width=340,height=50)

    light=Label(frameup,text="LIGHTS",bg="#FF5733",fg="#257DAD",bd=5,relief=RIDGE,font=("times new roman",25,"bold"))
    light.place(x=272,y=107,width=340,height=50)

    name=Label(framedown,text="NAME",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
    name.place(x=10,y=10,width=280)

    price=Label(framedown,text="PRICE",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
    price.place(x=291,y=10,width=100)

                #=========================================BUTTONS=========================================

    s = 0
    def remove1():
        global s
        lbl_value1.destroy()
        btn_increase1.destroy()
        btn_decrease1.destroy()
        name1.destroy()
        removebutton1.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        confbutton1.destroy()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase1():
        global lbl_value1
        value = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value + 1}"
    def decrease1():
        global lbl_value1
        value = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value - 1}"
    def confirm1():
        global lbl_value1
        i=lbl_value1.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('SAMSUNG 12', {}, {})".format(13000,lbl_value1.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def SamSung12():
        global s,lbl_value1,btn_increase1,btn_decrease1,name1,confbutton1,removebutton1
        lbl_value1 = Label(framedownright, text="0")
        btn_decrease1 =Button(framedownright, text="-", command=decrease1)
        btn_increase1 = Button(framedownright, text="+", command=increase1)
        name1=Label(framedownright,text="SamSung 12",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton1=Button(framedownright,text="✓",command=confirm1)
        removebutton1=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove1)
        if s==0:
            name1.place(x=0,y=10,width=200,height=40)
            lbl_value1.place(x=220,y=15,height=25,width=20)
            btn_increase1.place(x=240,y=15,width=20)
            btn_decrease1.place(x=200,y=15,width=20)
            confbutton1.place(x=270,y=15)
            removebutton1.place(x=300,y=15)
        if s==1:
            name1.place(x=0,y=50,width=200,height=40)
            lbl_value1.place(x=220,y=55,height=25,width=20)
            btn_increase1.place(x=240,y=55,width=20)
            btn_decrease1.place(x=200,y=55,width=20)
            confbutton1.place(x=270,y=55)
            removebutton1.place(x=300,y=55)
        if s==2:
            name1.place(x=0,y=90,width=200,height=40)
            lbl_value1.place(x=220,y=95,height=25,width=20)
            btn_increase1.place(x=240,y=95,width=20)
            btn_decrease1.place(x=200,y=95,width=20)
            confbutton1.place(x=270,y=95)
            removebutton1.place(x=300,y=95)
        if s==3:
            name1.place(x=0,y=130,width=200,height=40)
            lbl_value1.place(x=220,y=135,height=25,width=20)
            btn_increase1.place(x=240,y=135,width=20)
            btn_decrease1.place(x=200,y=135,width=20)
            confbutton1.place(x=270,y=135)
            removebutton1.place(x=300,y=135)
        s+=1
    def remove2():
        global s
        lbl_value2.destroy()
        btn_increase2.destroy()
        btn_decrease2.destroy()
        name2.destroy()
        removebutton2.destroy()
        confbutton2.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase2():
        global lbl_value2
        value = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value + 1}"
    def decrease2():
        global lbl_value2
        value = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value - 1}"
    def confirm2():
        global lbl_value2
        i=lbl_value2.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('iPhone 13', {}, {})".format(80000,lbl_value2.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def iPhone13():
        global s,lbl_value2,btn_increase2,btn_decrease2,name2,removebutton2,confbutton2
        lbl_value2 = Label(framedownright, text="0")
        btn_decrease2 =Button(framedownright, text="-", command=decrease2)
        btn_increase2 = Button(framedownright, text="+", command=increase2)
        name2=Label(framedownright,text="iPhone 13",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton2=Button(framedownright,text="✓",command=confirm2)
        removebutton2=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove2)
        if s==0:
            name2.place(x=0,y=10,width=200,height=40)
            lbl_value2.place(x=220,y=15,height=25,width=20)
            btn_increase2.place(x=240,y=15,width=20)
            btn_decrease2.place(x=200,y=15,width=20)
            confbutton2.place(x=270,y=15)
            removebutton2.place(x=300,y=15)
        if s==1:
            name2.place(x=0,y=50,width=200,height=40)
            lbl_value2.place(x=220,y=55,height=25,width=20)
            btn_increase2.place(x=240,y=55,width=20)
            btn_decrease2.place(x=200,y=55,width=20)
            confbutton2.place(x=270,y=55)
            removebutton2.place(x=300,y=55)
        if s==2:
            name2.place(x=0,y=90,width=200,height=40)
            lbl_value2.place(x=220,y=95,height=25,width=20)
            btn_increase2.place(x=240,y=95,width=20)
            btn_decrease2.place(x=200,y=95,width=20)
            confbutton2.place(x=270,y=95)
            removebutton2.place(x=300,y=95)
        if s==3:
            name2.place(x=0,y=130,width=200,height=40)
            lbl_value2.place(x=220,y=135,height=25,width=20)
            btn_increase2.place(x=240,y=135,width=20)
            btn_decrease2.place(x=200,y=135,width=20)
            confbutton2.place(x=270,y=135)
            removebutton2.place(x=300,y=135)
        s+=1
    def remove3():
        global s
        lbl_value3.destroy()
        btn_increase3.destroy()
        btn_decrease3.destroy()
        name3.destroy()
        removebutton3.destroy()
        confbutton3.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase3():
        global lbl_value3
        value = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value + 1}"
    def decrease3():
        global lbl_value3
        value = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value - 1}"
    def confirm3():
        global lbl_value3
        i=lbl_value3.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('MI Y3', {}, {})".format(10000,lbl_value3.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def MiY3():
        global s,lbl_value3,btn_increase3,btn_decrease3,name3,removebutton3,confbutton3
        lbl_value3 = Label(framedownright, text="0")
        btn_decrease3 =Button(framedownright, text="-", command=decrease3)
        btn_increase3 = Button(framedownright, text="+", command=increase3)
        name3=Label(framedownright,text="MI Y3",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton3=Button(framedownright,text="✓",command=confirm3)
        removebutton3=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove3)
        if s==0:
            name3.place(x=0,y=10,width=200,height=40)
            lbl_value3.place(x=220,y=15,height=25,width=20)
            btn_increase3.place(x=240,y=15,width=20)
            btn_decrease3.place(x=200,y=15,width=20)
            confbutton3.place(x=270,y=15)
            removebutton3.place(x=300,y=15)
        if s==1:
            name3.place(x=0,y=50,width=200,height=40)
            lbl_value3.place(x=220,y=55,height=25,width=20)
            btn_increase3.place(x=240,y=55,width=20)
            btn_decrease3.place(x=200,y=55,width=20)
            confbutton3.place(x=270,y=55)
            removebutton3.place(x=300,y=55)
        if s==2:
            name3.place(x=0,y=90,width=200,height=40)
            lbl_value3.place(x=220,y=95,height=25,width=20)
            btn_increase3.place(x=240,y=95,width=20)
            btn_decrease3.place(x=200,y=95,width=20)
            confbutton3.place(x=270,y=95)
            removebutton3.place(x=300,y=95)
        if s==3:
            name3.place(x=50,y=130,width=200,height=40)
            lbl_value3.place(x=220,y=135,height=25,width=20)
            btn_increase3.place(x=240,y=135,width=20)
            btn_decrease3.place(x=200,y=135,width=20)
            confbutton3.place(x=270,y=135)
            removebutton3.place(x=300,y=135)
        s+=1
    def remove4():
        global s
        lbl_value4.destroy()
        btn_increase4.destroy()
        btn_decrease4.destroy()
        name4.destroy()
        removebutton4.destroy()
        confbutton4.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase4():
        global lbl_value4
        value = int(lbl_value4["text"])
        lbl_value4["text"] = f"{value + 1}"
    def decrease4():
        global lbl_value4
        value = int(lbl_value4["text"])
        lbl_value4["text"] = f"{value - 1}"
    def confirm4():
        global lbl_value4
        i=lbl_value4.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('iPad Pro', {}, {})".format(65000,lbl_value4.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def ipadpro():
        global s,lbl_value4,btn_increase4,btn_decrease4,name4,removebutton4,confbutton4
        lbl_value4 = Label(framedownright, text="0")
        btn_decrease4 =Button(framedownright, text="-", command=decrease4)
        btn_increase4 = Button(framedownright, text="+", command=increase4)
        name4=Label(framedownright,text="IPAD PRO",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton4=Button(framedownright,text="✓",command=confirm4)
        removebutton4=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove4)
        if s==0:
            name4.place(x=0,y=10,width=200,height=40)
            lbl_value4.place(x=220,y=15,height=25,width=20)
            btn_increase4.place(x=240,y=15,width=20)
            btn_decrease4.place(x=200,y=15,width=20)
            confbutton4.place(x=270,y=15)
            removebutton4.place(x=300,y=15)
        if s==1:
            name4.place(x=0,y=50,width=200,height=40)
            lbl_value4.place(x=220,y=55,height=25,width=20)
            btn_increase4.place(x=240,y=55,width=20)
            btn_decrease4.place(x=200,y=55,width=20)
            confbutton4.place(x=270,y=55)
            removebutton4.place(x=300,y=55)
        if s==2:
            name4.place(x=0,y=90,width=200,height=40)
            lbl_value4.place(x=220,y=95,height=25,width=20)
            btn_increase4.place(x=240,y=95,width=20)
            btn_decrease4.place(x=200,y=95,width=20)
            confbutton4.place(x=270,y=95)
            removebutton4.place(x=300,y=95)
        if s==3:
            name4.place(x=0,y=130,width=200,height=40)
            lbl_value4.place(x=220,y=135,height=25,width=20)
            btn_increase4.place(x=240,y=135,width=20)
            btn_decrease4.place(x=200,y=135,width=20)
            confbutton4.place(x=270,y=135)
            removebutton4.place(x=300,y=135)
        s+=1
    def remove5():
        global s
        lbl_value5.destroy()
        btn_increase5.destroy()
        btn_decrease5.destroy()
        name5.destroy()
        removebutton5.destroy()
        confbutton5.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase5():
        global lbl_value5
        value = int(lbl_value5["text"])
        lbl_value5["text"] = f"{value + 1}"
    def decrease5():
        global lbl_value5
        value = int(lbl_value5["text"])
        lbl_value5["text"] = f"{value - 1}"
    def confirm5():
        global lbl_value5
        i=lbl_value5.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('SAMSUNG TAB', {}, {})".format(50000,lbl_value5.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def samsungtab():
        global s,lbl_value5,btn_increase5,btn_decrease5,name5,removebutton5,confbutton5
        lbl_value5 = Label(framedownright, text="0")
        btn_decrease5 =Button(framedownright, text="-", command=decrease5)
        btn_increase5 = Button(framedownright, text="+", command=increase5)
        name5=Label(framedownright,text="SamSung Tab",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton5=Button(framedownright,text="✓",command=confirm5)
        removebutton5=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove5)
        if s==0:
            name5.place(x=0,y=10,width=200,height=40)
            lbl_value5.place(x=220,y=15,height=25,width=20)
            btn_increase5.place(x=240,y=15,width=20)
            btn_decrease5.place(x=200,y=15,width=20)
            confbutton5.place(x=270,y=15)
            removebutton5.place(x=300,y=15)
        if s==1:
            name5.place(x=0,y=50,width=200,height=40)
            lbl_value5.place(x=220,y=55,height=25,width=20)
            btn_increase5.place(x=240,y=55,width=20)
            btn_decrease5.place(x=200,y=55,width=20)
            confbutton5.place(x=270,y=55)
            removebutton5.place(x=300,y=55)
        if s==2:
            name5.place(x=0,y=90,width=200,height=40)
            lbl_value5.place(x=220,y=95,height=25,width=20)
            btn_increase5.place(x=240,y=95,width=20)
            btn_decrease5.place(x=200,y=95,width=20)
            confbutton5.place(x=270,y=95)
            removebutton5.place(x=300,y=95)
        if s==3:
            name5.place(x=0,y=130,width=200,height=40)
            lbl_value5.place(x=220,y=135,height=25,width=20)
            btn_increase5.place(x=240,y=135,width=20)
            btn_decrease5.place(x=200,y=135,width=20)
            confbutton5.place(x=270,y=135)
            removebutton5.place(x=300,y=135)
        s+=1
    def remove6():
        global s
        lbl_value6.destroy()
        btn_increase6.destroy()
        btn_decrease6.destroy()
        name6.destroy()
        removebutton6.destroy()
        confbutton6.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase6():
        global lbl_value6
        value = int(lbl_value6["text"])
        lbl_value6["text"] = f"{value + 1}"
    def decrease6():
        global lbl_value6
        value = int(lbl_value6["text"])
        lbl_value6["text"] = f"{value - 1}"
    def confirm6():
        global lbl_value6
        i=lbl_value6.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('MI Tab', {}, {})".format(40000,lbl_value6.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Mitab():
        global s,lbl_value6,btn_increase6,btn_decrease6,name6,removebutton6,confbutton6
        lbl_value6 = Label(framedownright, text="0")
        btn_decrease6 =Button(framedownright, text="-", command=decrease6)
        btn_increase6 = Button(framedownright, text="+", command=increase6)
        name6=Label(framedownright,text="MI Tab",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton6=Button(framedownright,text="✓",command=confirm6)
        removebutton6=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove6)
        if s==0:
            name6.place(x=0,y=10,width=200,height=40)
            lbl_value6.place(x=220,y=15,height=25,width=20)
            btn_increase6.place(x=240,y=15,width=20)
            btn_decrease6.place(x=200,y=15,width=20)
            confbutton6.place(x=270,y=15)
            removebutton6.place(x=300,y=15)
        if s==1:
            name6.place(x=0,y=50,width=200,height=40)
            lbl_value6.place(x=220,y=55,height=25,width=20)
            btn_increase6.place(x=240,y=55,width=20)
            btn_decrease6.place(x=200,y=55,width=20)
            confbutton6.place(x=270,y=55)
            removebutton6.place(x=300,y=55)
        if s==2:
            name6.place(x=0,y=90,width=200,height=40)
            lbl_value6.place(x=220,y=95,height=25,width=20)
            btn_increase6.place(x=240,y=95,width=20)
            btn_decrease6.place(x=200,y=95,width=20)
            confbutton6.place(x=270,y=95)
            removebutton6.place(x=300,y=95)
        if s==3:
            name6.place(x=0,y=130,width=200,height=40)
            lbl_value6.place(x=220,y=135,height=25,width=20)
            btn_increase6.place(x=240,y=135,width=20)
            btn_decrease6.place(x=200,y=135,width=20)
            confbutton6.place(x=270,y=135)
            removebutton6.place(x=300,y=135)
        s+=1
    def remove7():
        global s
        lbl_value7.destroy()
        btn_increase7.destroy()
        btn_decrease7.destroy()
        name7.destroy()
        removebutton7.destroy()
        confbutton7.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase7():
        global lbl_value7
        value = int(lbl_value7["text"])
        lbl_value7["text"] = f"{value + 1}"
    def decrease7():
        global lbl_value7
        value = int(lbl_value7["text"])
        lbl_value7["text"] = f"{value - 1}"
    def confirm7():
        global lbl_value7
        i=lbl_value7.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('LENOVO', {}, {})".format(80000,lbl_value7.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Lenovo():
        global s,lbl_value7,btn_increase7,btn_decrease7,name7,removebutton7,confbutton7
        lbl_value7 = Label(framedownright, text="0")
        btn_decrease7 =Button(framedownright, text="-", command=decrease7)
        btn_increase7 = Button(framedownright, text="+", command=increase7)
        name7=Label(framedownright,text="Lenovo",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton7=Button(framedownright,text="✓",command=confirm7)
        removebutton7=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove7)
        if s==0:
            name7.place(x=0,y=10,width=200,height=40)
            lbl_value7.place(x=220,y=15,height=25,width=20)
            btn_increase7.place(x=240,y=15,width=20)
            btn_decrease7.place(x=200,y=15,width=20)
            confbutton7.place(x=270,y=15)
            removebutton7.place(x=300,y=15)
        if s==1:
            name7.place(x=0,y=50,width=200,height=40)
            lbl_value7.place(x=220,y=55,height=25,width=20)
            btn_increase7.place(x=240,y=55,width=20)
            btn_decrease7.place(x=200,y=55,width=20)
            confbutton7.place(x=270,y=55)
            removebutton7.place(x=300,y=55)
        if s==2:
            name7.place(x=0,y=90,width=200,height=40)
            lbl_value7.place(x=220,y=95,height=25,width=20)
            btn_increase7.place(x=240,y=95,width=20)
            btn_decrease7.place(x=200,y=95,width=20)
            confbutton7.place(x=270,y=95)
            removebutton7.place(x=300,y=95)
        if s==3:
            name7.place(x=0,y=130,width=200,height=40)
            lbl_value7.place(x=220,y=135,height=25,width=20)
            btn_increase7.place(x=240,y=135,width=20)
            btn_decrease7.place(x=200,y=135,width=20)
            confbutton7.place(x=270,y=135)
            removebutton7.place(x=300,y=135)
        s+=1
    def remove8():
        global s
        lbl_value8.destroy()
        btn_increase8.destroy()
        btn_decrease8.destroy()
        name8.destroy()
        removebutton8.destroy()
        confbutton8.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase8():
        global lbl_value8
        value = int(lbl_value8["text"])
        lbl_value8["text"] = f"{value + 1}"
    def decrease8():
        global lbl_value8
        value = int(lbl_value8["text"])
        lbl_value8["text"] = f"{value - 1}"
    def confirm8():
        global lbl_value8
        i=lbl_value8.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) ('MACBOOK', {}, {})".format(150000,lbl_value8.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Macbook():
        global s,lbl_value8,btn_increase8,btn_decrease8,name8,removebutton8,confbutton8
        lbl_value8 = Label(framedownright, text="0")
        btn_decrease8 =Button(framedownright, text="-", command=decrease8)
        btn_increase8 = Button(framedownright, text="+", command=increase8)
        name8=Label(framedownright,text="MacBook",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton8=Button(framedownright,text="✓",command=confirm8)
        removebutton8=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove8)
        if s==0:
            name8.place(x=0,y=10,width=200,height=40)
            lbl_value8.place(x=220,y=15,height=25,width=20)
            btn_increase8.place(x=240,y=15,width=20)
            btn_decrease8.place(x=200,y=15,width=20)
            confbutton8.place(x=270,y=15)
            removebutton8.place(x=300,y=15)
        if s==1:
            name8.place(x=0,y=50,width=200,height=40)
            lbl_value8.place(x=220,y=55,height=25,width=20)
            btn_increase8.place(x=240,y=55,width=20)
            btn_decrease8.place(x=200,y=55,width=20)
            confbutton8.place(x=270,y=55)
            removebutton8.place(x=300,y=55)
        if s==2:
            name8.place(x=0,y=90,width=200,height=40)
            lbl_value8.place(x=220,y=95,height=25,width=20)
            btn_increase8.place(x=240,y=95,width=20)
            btn_decrease8.place(x=200,y=95,width=20)
            confbutton8.place(x=270,y=95)
            removebutton8.place(x=300,y=95)
        if s==3:
            name8.place(x=0,y=130,width=200,height=40)
            lbl_value8.place(x=220,y=135,height=25,width=20)
            btn_increase8.place(x=240,y=135,width=20)
            btn_decrease8.place(x=200,y=135,width=20)
            confbutton8.place(x=270,y=135)
            removebutton8.place(x=300,y=135)
        s+=1
    def remove9():
        global s
        lbl_value9.destroy()
        btn_increase9.destroy()
        btn_decrease9.destroy()
        name9.destroy()
        removebutton9.destroy()
        confbutton9.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase9():
        global lbl_value9
        value = int(lbl_value9["text"])
        lbl_value9["text"] = f"{value + 1}"
    def decrease9():
        global lbl_value9
        value = int(lbl_value9["text"])
        lbl_value9["text"] = f"{value - 1}"
    def confirm9():
        global lbl_value9
        i=lbl_value9.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('DELL', {}, {})".format(70000,lbl_value9.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def dell():
        global s,lbl_value9,btn_increase9,btn_decrease9,name9,removebutton9,confbutton9
        lbl_value9 = Label(framedownright, text="0")
        btn_decrease9 =Button(framedownright, text="-", command=decrease9)
        btn_increase9 = Button(framedownright, text="+", command=increase9)
        name9=Label(framedownright,text="DELL",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton9=Button(framedownright,text="✓",command=confirm9)
        removebutton9=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove9)
        if s==0:
            name9.place(x=0,y=10,width=200,height=40)
            lbl_value9.place(x=220,y=15,height=25,width=20)
            btn_increase9.place(x=240,y=15,width=20)
            btn_decrease9.place(x=200,y=15,width=20)
            confbutton9.place(x=270,y=15)
            removebutton9.place(x=300,y=15)
        if s==1:
            name9.place(x=0,y=50,width=200,height=40)
            lbl_value9.place(x=220,y=55,height=25,width=20)
            btn_increase9.place(x=240,y=55,width=20)
            btn_decrease9.place(x=200,y=55,width=20)
            confbutton9.place(x=270,y=55)
            removebutton9.place(x=300,y=55)
        if s==2:
            name9.place(x=0,y=90,width=200,height=40)
            lbl_value9.place(x=220,y=95,height=25,width=20)
            btn_increase9.place(x=240,y=95,width=20)
            btn_decrease9.place(x=200,y=95,width=20)
            confbutton9.place(x=270,y=95)
            removebutton9.place(x=300,y=95)
        if s==3:
            name9.place(x=0,y=130,width=200,height=40)
            lbl_value9.place(x=220,y=135,height=25,width=20)
            btn_increase9.place(x=240,y=135,width=20)
            btn_decrease9.place(x=200,y=135,width=20)
            confbutton9.place(x=270,y=135)
            removebutton9.place(x=300,y=135)
        s+=1
    def remove10():
        global s
        lbl_value10.destroy()
        btn_increase10.destroy()
        btn_decrease10.destroy()
        name10.destroy()
        removebutton10.destroy()
        confbutton10.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase10():
        global lbl_value10
        value = int(lbl_value10["text"])
        lbl_value10["text"] = f"{value + 1}"
    def decrease10():
        global lbl_value10
        value = int(lbl_value10["text"])
        lbl_value10["text"] = f"{value - 1}"
    def confirm10():
        global lbl_value10
        i=lbl_value10.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('GODREJ AC', {}, {})".format(35000,lbl_value10.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def godrej():
        global s,lbl_value10,btn_increase10,btn_decrease10,name10,removebutton10,confbutton10
        lbl_value10 = Label(framedownright, text="0")
        btn_decrease10 =Button(framedownright, text="-", command=decrease10)
        btn_increase10 =Button(framedownright, text="+", command=increase10)
        name10=Label(framedownright,text="Godrej One Ton AC",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton10=Button(framedownright,text="✓",command=confirm10)
        removebutton10=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove10)
        if s==0:
            name10.place(x=0,y=10,width=200,height=40)
            lbl_value10.place(x=220,y=15,height=25,width=20)
            btn_increase10.place(x=240,y=15,width=20)
            btn_decrease10.place(x=200,y=15,width=20)
            confbutton10.place(x=270,y=15)
            removebutton10.place(x=300,y=15)
        if s==1:
            name10.place(x=0,y=50,width=200,height=40)
            lbl_value10.place(x=220,y=55,height=25,width=20)
            btn_increase10.place(x=240,y=55,width=20)
            btn_decrease10.place(x=200,y=55,width=20)
            confbutton10.place(x=270,y=55)
            removebutton10.place(x=300,y=55)
        if s==2:
            name10.place(x=0,y=90,width=200,height=40)
            lbl_value10.place(x=220,y=95,height=25,width=20)
            btn_increase10.place(x=240,y=95,width=20)
            btn_decrease10.place(x=200,y=95,width=20)
            confbutton10.place(x=270,y=95)
            removebutton10.place(x=300,y=95)
        if s==3:
            name10.place(x=0,y=130,width=200,height=40)
            lbl_value10.place(x=220,y=135,height=25,width=20)
            btn_increase10.place(x=240,y=135,width=20)
            btn_decrease10.place(x=200,y=135,width=20)
            confbutton10.place(x=270,y=135)
            removebutton10.place(x=300,y=135)
        s+=1
    def remove11():
        global s
        lbl_value11.destroy()
        btn_increase11.destroy()
        btn_decrease11.destroy()
        name11.destroy()
        removebutton11.destroy()
        confbutton11.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase11():
        global lbl_value11
        value = int(lbl_value11["text"])
        lbl_value11["text"] = f"{value + 1}"
    def decrease11():
        global lbl_value11
        value = int(lbl_value11["text"])
        lbl_value11["text"] = f"{value - 1}"
    def confirm11():
        global lbl_value11
        i=lbl_value11.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('MITSUBISHI AC', {}, {})".format(55000,lbl_value11.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def mitsubishi():
        global s,lbl_value11,btn_increase11,btn_decrease11,name11,removebutton11,confbutton11
        lbl_value11 = Label(framedownright, text="0")
        btn_decrease11 =Button(framedownright, text="-", command=decrease11)
        btn_increase11 = Button(framedownright, text="+", command=increase11)
        name11=Label(framedownright,text="Mitsubishi",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton11=Button(framedownright,text="✓",command=confirm11)
        removebutton11=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove11)
        if s==0:
            name11.place(x=0,y=10,width=200,height=40)
            lbl_value11.place(x=220,y=15,height=25,width=20)
            btn_increase11.place(x=240,y=15,width=20)
            btn_decrease11.place(x=200,y=15,width=20)
            confbutton11.place(x=270,y=15)
            removebutton11.place(x=300,y=15)
        if s==1:
            name11.place(x=0,y=50,width=200,height=40)
            lbl_value11.place(x=220,y=55,height=25,width=20)
            btn_increase11.place(x=240,y=55,width=20)
            btn_decrease11.place(x=200,y=55,width=20)
            confbutton11.place(x=270,y=55)
            removebutton11.place(x=300,y=55)
        if s==2:
            name11.place(x=0,y=90,width=200,height=40)
            lbl_value11.place(x=220,y=95,height=25,width=20)
            btn_increase11.place(x=240,y=95,width=20)
            btn_decrease11.place(x=200,y=95,width=20)
            confbutton11.place(x=270,y=95)
            removebutton11.place(x=300,y=95)
        if s==3:
            name11.place(x=0,y=130,width=200,height=40)
            lbl_value11.place(x=220,y=135,height=25,width=20)
            btn_increase11.place(x=240,y=135,width=20)
            btn_decrease11.place(x=200,y=135,width=20)
            confbutton11.place(x=270,y=135)
            removebutton11.place(x=300,y=135)
        s+=1
    def remove12():
        global s
        lbl_value12.destroy()
        btn_increase12.destroy()
        btn_decrease12.destroy()
        name12.destroy()
        removebutton12.destroy()
        confbutton12.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase12():
        global lbl_value12
        value = int(lbl_value12["text"])
        lbl_value12["text"] = f"{value + 1}"
    def decrease12():
        global lbl_value12
        value = int(lbl_value12["text"])
        lbl_value12["text"] = f"{value - 1}"
    def confirm12():
        global lbl_value12
        i=lbl_value12.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('LG TWO TON AC', {}, {})".format(60000,lbl_value12.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def LG():
        global s,lbl_value12,btn_increase12,btn_decrease12,name12,removebutton12,confbutton12
        lbl_value12 = Label(framedownright, text="0")
        btn_decrease12 =Button(framedownright, text="-", command=decrease12)
        btn_increase12 = Button(framedownright, text="+", command=increase12)
        name12=Label(framedownright,text="LG TWO TON AC",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton12=Button(framedownright,text="✓",command=confirm12)
        removebutton12=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove12)
        if s==0:
            name12.place(x=0,y=10,width=200,height=40)
            lbl_value12.place(x=220,y=15,height=25,width=20)
            btn_increase12.place(x=240,y=15,width=20)
            btn_decrease12.place(x=200,y=15,width=20)
            confbutton12.place(x=270,y=15)
            removebutton12.place(x=300,y=15)
        if s==1:
            name12.place(x=0,y=50,width=200,height=40)
            lbl_value12.place(x=220,y=55,height=25,width=20)
            btn_increase12.place(x=240,y=55,width=20)
            btn_decrease12.place(x=200,y=55,width=20)
            confbutton12.place(x=270,y=55)
            removebutton12.place(x=300,y=55)
        if s==2:
            name12.place(x=0,y=90,width=200,height=40)
            lbl_value12.place(x=220,y=95,height=25,width=20)
            btn_increase12.place(x=240,y=95,width=20)
            btn_decrease12.place(x=200,y=95,width=20)
            confbutton12.place(x=270,y=95)
            removebutton12.place(x=300,y=95)
        if s==3:
            name12.place(x=0,y=130,width=200,height=40)
            lbl_value12.place(x=220,y=135,height=25,width=20)
            btn_increase12.place(x=240,y=135,width=20)
            btn_decrease12.place(x=200,y=135,width=20)
            confbutton12.place(x=270,y=135)
            removebutton12.place(x=300,y=135)
        s+=1
    def remove13():
        global s
        lbl_value13.destroy()
        btn_increase13.destroy()
        btn_decrease13.destroy()
        name13.destroy()
        removebutton13.destroy()
        confbutton13.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase13():
        global lbl_value13
        value = int(lbl_value13["text"])
        lbl_value13["text"] = f"{value + 1}"
    def decrease13():
        global lbl_value13
        value = int(lbl_value13["text"])
        lbl_value13["text"] = f"{value - 1}"
    def confirm13():
        global lbl_value13
        i=lbl_value13.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('LG REFRIGERATOR', {}, {})".format(35000,lbl_value13.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def LGref():
        global s,lbl_value13,btn_increase13,btn_decrease13,name13,removebutton13,confbutton13
        lbl_value13 = Label(framedownright, text="0")
        btn_decrease13 =Button(framedownright, text="-", command=decrease13)
        btn_increase13 = Button(framedownright, text="+", command=increase13)
        name13=Label(framedownright,text="LG Refrigerator",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton13=Button(framedownright,text="✓",command=confirm13)
        removebutton13=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove13)
        if s==0:
            name13.place(x=0,y=10,width=200,height=40)
            lbl_value13.place(x=220,y=15,height=25,width=20)
            btn_increase13.place(x=240,y=15,width=20)
            btn_decrease13.place(x=200,y=15,width=20)
            confbutton13.place(x=270,y=15)
            removebutton13.place(x=300,y=15)
        if s==1:
            name13.place(x=0,y=50,width=200,height=40)
            lbl_value13.place(x=220,y=55,height=25,width=20)
            btn_increase13.place(x=240,y=55,width=20)
            btn_decrease13.place(x=200,y=55,width=20)
            confbutton13.place(x=270,y=55)
            removebutton13.place(x=300,y=55)
        if s==2:
            name13.place(x=0,y=90,width=200,height=40)
            lbl_value13.place(x=220,y=95,height=25,width=20)
            btn_increase13.place(x=240,y=95,width=20)
            btn_decrease13.place(x=200,y=95,width=20)
            confbutton13.place(x=270,y=95)
            removebutton13.place(x=300,y=95)
        if s==3:
            name13.place(x=0,y=130,width=200,height=40)
            lbl_value13.place(x=220,y=135,height=25,width=20)
            btn_increase13.place(x=240,y=135,width=20)
            btn_decrease13.place(x=200,y=135,width=20)
            confbutton13.place(x=270,y=135)
            removebutton13.place(x=300,y=135)
        s+=1
    def remove14():
        global s
        lbl_value14.destroy()
        btn_increase14.destroy()
        btn_decrease14.destroy()
        name14.destroy()
        removebutton14.destroy()
        confbutton14.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase14():
        global lbl_value14
        value = int(lbl_value14["text"])
        lbl_value14["text"] = f"{value + 1}"
    def decrease14():
        global lbl_value14
        value = int(lbl_value14["text"])
        lbl_value14["text"] = f"{value - 1}"
    def confirm14():
        global lbl_value14
        i=lbl_value14.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('SAMSUNG REFRIGERATOR', {}, {})".format(30000,lbl_value14.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def SamSungref():
        global s,lbl_value14,btn_increase14,btn_decrease14,name14,removebutton14,confbutton14
        lbl_value14 = Label(framedownright, text="0")
        btn_decrease14 =Button(framedownright, text="-", command=decrease14)
        btn_increase14 = Button(framedownright, text="+", command=increase14)
        name14=Label(framedownright,text="SamSung Refrigerator",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton14=Button(framedownright,text="✓",command=confirm14)
        removebutton14=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove14)
        if s==0:
            name14.place(x=0,y=10,width=200,height=40)
            lbl_value14.place(x=220,y=15,height=25,width=20)
            btn_increase14.place(x=240,y=15,width=20)
            btn_decrease14.place(x=200,y=15,width=20)
            confbutton14.place(x=270,y=15)
            removebutton14.place(x=300,y=15)
        if s==1:
            name14.place(x=0,y=50,width=200,height=40)
            lbl_value14.place(x=220,y=55,height=25,width=20)
            btn_increase14.place(x=240,y=55,width=20)
            btn_decrease14.place(x=200,y=55,width=20)
            confbutton14.place(x=270,y=55)
            removebutton14.place(x=300,y=55)
        if s==2:
            name14.place(x=0,y=90,width=200,height=40)
            lbl_value14.place(x=220,y=95,height=25,width=20)
            btn_increase14.place(x=240,y=95,width=20)
            btn_decrease14.place(x=200,y=95,width=20)
            confbutton14.place(x=270,y=95)
            removebutton14.place(x=300,y=95)
        if s==3:
            name14.place(x=0,y=130,width=200,height=40)
            lbl_value14.place(x=220,y=135,height=25,width=20)
            btn_increase14.place(x=240,y=135,width=20)
            btn_decrease14.place(x=200,y=135,width=20)
            confbutton14.place(x=270,y=135)
            removebutton14.place(x=300,y=135)
        s+=1
    def remove15():
        global s
        lbl_value15.destroy()
        btn_increase15.destroy()
        btn_decrease15.destroy()
        name15.destroy()
        removebutton15.destroy()
        confbutton15.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase15():
        global lbl_value15
        value = int(lbl_value15["text"])
        lbl_value15["text"] = f"{value + 1}"
    def decrease15():
        global lbl_value15
        value = int(lbl_value15["text"])
        lbl_value15["text"] = f"{value - 1}"
    def confirm15():
        global lbl_value15
        i=lbl_value15.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('GODREJ REFRIGERATOR', {}, {})".format(40000,lbl_value15.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Godrejref():
        global s,lbl_value15,btn_increase15,btn_decrease15,name15,removebutton15,confbutton15
        lbl_value15 = Label(framedownright, text="0")
        btn_decrease15 =Button(framedownright, text="-", command=decrease15)
        btn_increase15 = Button(framedownright, text="+", command=increase15)
        name15=Label(framedownright,text="Godrej Refrigerator",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton15=Button(framedownright,text="✓",command=confirm15)
        removebutton15=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove15)
        if s==0:
            name15.place(x=0,y=10,width=200,height=40)
            lbl_value15.place(x=220,y=15,height=25,width=20)
            btn_increase15.place(x=240,y=15,width=20)
            btn_decrease15.place(x=200,y=15,width=20)
            confbutton15.place(x=270,y=15)
            removebutton15.place(x=300,y=15)
        if s==1:
            name15.place(x=0,y=50,width=200,height=40)
            lbl_value15.place(x=220,y=55,height=25,width=20)
            btn_increase15.place(x=240,y=55,width=20)
            btn_decrease15.place(x=200,y=55,width=20)
            confbutton15.place(x=270,y=55)
            removebutton15.place(x=300,y=55)
        if s==2:
            name15.place(x=0,y=90,width=200,height=40)
            lbl_value15.place(x=220,y=95,height=25,width=20)
            btn_increase15.place(x=240,y=95,width=20)
            btn_decrease15.place(x=200,y=95,width=20)
            confbutton15.place(x=270,y=95)
            removebutton15.place(x=300,y=95)
        if s==3:
            name15.place(x=0,y=130,width=200,height=40)
            lbl_value15.place(x=220,y=135,height=25,width=20)
            btn_increase15.place(x=240,y=135,width=20)
            btn_decrease15.place(x=200,y=135,width=20)
            confbutton15.place(x=270,y=135)
            removebutton15.place(x=300,y=135)
        s+=1
    def remove16():
        global s
        lbl_value16.destroy()
        btn_increase16.destroy()
        btn_decrease16.destroy()
        name16.destroy()
        removebutton16.destroy()
        confbutton16.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase16():
        global lbl_value16
        value = int(lbl_value16["text"])
        lbl_value16["text"] = f"{value + 1}"
    def decrease16():
        global lbl_value16
        value = int(lbl_value16["text"])
        lbl_value16["text"] = f"{value - 1}"
    def confirm16():
        global lbl_value16
        i=lbl_value16.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('CROMPTON LIGHTS', {}, {})".format(500,lbl_value16.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Crompton():
        global s,lbl_value16,btn_increase16,btn_decrease16,name16,removebutton16,confbutton16
        lbl_value16 = Label(framedownright, text="0")
        btn_decrease16 =Button(framedownright, text="-", command=decrease16)
        btn_increase16 = Button(framedownright, text="+", command=increase16)
        name16=Label(framedownright,text="Crompton Lights",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton16=Button(framedownright,text="✓",command=confirm16)
        removebutton16=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove16)
        if s==0:
            name16.place(x=0,y=10,width=200,height=40)
            lbl_value16.place(x=220,y=15,height=25,width=20)
            btn_increase16.place(x=240,y=15,width=20)
            btn_decrease16.place(x=200,y=15,width=20)
            confbutton16.place(x=270,y=15)
            removebutton16.place(x=300,y=15)
        if s==1:
            name16.place(x=0,y=50,width=200,height=40)
            lbl_value16.place(x=220,y=55,height=25,width=20)
            btn_increase16.place(x=240,y=55,width=20)
            btn_decrease16.place(x=200,y=55,width=20)
            confbutton16.place(x=270,y=55)
            removebutton16.place(x=300,y=55)
        if s==2:
            name16.place(x=0,y=90,width=200,height=40)
            lbl_value16.place(x=220,y=95,height=25,width=20)
            btn_increase16.place(x=240,y=95,width=20)
            btn_decrease16.place(x=200,y=95,width=20)
            confbutton16.place(x=270,y=95)
            removebutton16.place(x=300,y=95)
        if s==3:
            name16.place(x=0,y=130,width=200,height=40)
            lbl_value16.place(x=220,y=135,height=25,width=20)
            btn_increase16.place(x=240,y=135,width=20)
            btn_decrease16.place(x=200,y=135,width=20)
            confbutton16.place(x=270,y=135)
            removebutton16.place(x=300,y=135)
        s+=1
    def remove17():
        global s
        lbl_value17.destroy()
        btn_increase17.destroy()
        btn_decrease17.destroy()
        name17.destroy()
        removebutton17.destroy()
        confbutton17.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase17():
        global lbl_value17
        value = int(lbl_value17["text"])
        lbl_value17["text"] = f"{value + 1}"
    def decrease17():
        global lbl_value17
        value = int(lbl_value17["text"])
        lbl_value17["text"] = f"{value - 1}"
    def confirm17():
        global lbl_value17
        i=lbl_value17.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('PHILIP LIGHTS', {}, {})".format(100,lbl_value17.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful","Updated and added item to the cart !")
    def Philip():
        global s,lbl_value17,btn_increase17,btn_decrease17,name17,removebutton17,confbutton17
        lbl_value17 = Label(framedownright, text="0")
        btn_decrease17 =Button(framedownright, text="-", command=decrease17)
        btn_increase17 = Button(framedownright, text="+", command=increase17)
        name17=Label(framedownright,text="Philip Lights",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton17=Button(framedownright,text="✓",command=confirm17)
        removebutton17=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove17)
        if s==0:
            name17.place(x=0,y=10,width=200,height=40)
            lbl_value17.place(x=220,y=15,height=25,width=20)
            btn_increase17.place(x=240,y=15,width=20)
            btn_decrease17.place(x=200,y=15,width=20)
            confbutton17.place(x=270,y=15)
            removebutton17.place(x=300,y=15)
        if s==1:
            name17.place(x=0,y=50,width=200,height=40)
            lbl_value17.place(x=220,y=55,height=25,width=20)
            btn_increase17.place(x=240,y=55,width=20)
            btn_decrease17.place(x=200,y=55,width=20)
            confbutton17.place(x=270,y=55)
            removebutton17.place(x=300,y=55)
        if s==2:
            name17.place(x=0,y=90,width=200,height=40)
            lbl_value17.place(x=220,y=95,height=25,width=20)
            btn_increase17.place(x=240,y=95,width=20)
            btn_decrease17.place(x=200,y=95,width=20)
            confbutton17.place(x=270,y=95)
            removebutton17.place(x=300,y=95)
        if s==3:
            name17.place(x=0,y=130,width=200,height=40)
            lbl_value17.place(x=220,y=135,height=25,width=20)
            btn_increase17.place(x=240,y=135,width=20)
            btn_decrease17.place(x=200,y=135,width=20)
            confbutton17.place(x=270,y=135)
            removebutton17.place(x=300,y=135)
        s+=1
    def remove18():
        global s
        lbl_value18.destroy()
        btn_increase18.destroy()
        btn_decrease18.destroy()
        name18.destroy()
        removebutton18.destroy()
        confbutton18.destroy()
        cursor.execute("DELETE from customer where NAME='SAMSUNG 12'")
        mycon.commit()
        messagebox.showinfo("Successful","Removed item from the cart !")
        s-=1
    def increase18():
        global lbl_value18
        value = int(lbl_value18["text"])
        lbl_value18["text"] = f"{value + 1}"
    def decrease18():
        global lbl_value18
        value = int(lbl_value18["text"])
        lbl_value18["text"] = f"{value - 1}"
    def confirm18():
        global lbl_value18
        i=lbl_value18.cget("text")
        cursor.execute("INSERT INTO customer (NAME, PRICE, QUANTITY) VALUES ('SWAROVSKI CHANDELIERS', {}, {})".format(15000,lbl_value18.cget("text")))
        mycon.commit()
        messagebox.showinfo("Successful"," Updated and added item to the cart !")
    def swarovski():
        global s,lbl_value18,btn_increase18,btn_decrease18,name18,removebutton18,confbutton18
        lbl_value18 = Label(framedownright, text="0")
        btn_decrease18 =Button(framedownright, text="-", command=decrease18)
        btn_increase18 = Button(framedownright, text="+", command=increase18)
        name18=Label(framedownright,text="SWAROVSKI CHANDELIERS",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
        confbutton18=Button(framedownright,text="✓",command=confirm18)
        removebutton18=Button(framedownright,text="REMOVE FROM CART",bg="black",fg="white",bd=1,font=("times new roman",15,"bold"),command=remove18)
        if s==0:
            name18.place(x=0,y=10,width=200,height=40)
            lbl_value18.place(x=220,y=15,height=25,width=20)
            btn_increase18.place(x=240,y=15,width=20)
            btn_decrease18.place(x=200,y=15,width=20)
            confbutton18.place(x=270,y=15)
            removebutton18.place(x=300,y=15)
        if s==1:
            name18.place(x=0,y=50,width=200,height=40)
            lbl_value18.place(x=220,y=55,height=25,width=20)
            btn_increase18.place(x=240,y=55,width=20)
            btn_decrease18.place(x=200,y=55,width=20)
            confbutton18.place(x=270,y=55)
            removebutton18.place(x=300,y=55)
        if s==2:
            name18.place(x=0,y=90,width=200,height=40)
            lbl_value18.place(x=220,y=95,height=25,width=20)
            btn_increase18.place(x=240,y=95,width=20)
            btn_decrease18.place(x=200,y=95,width=20)
            confbutton18.place(x=270,y=95)
            removebutton18.place(x=300,y=95)
        if s==3:
            name18.place(x=0,y=130,width=200,height=40)
            lbl_value18.place(x=220,y=135,height=25,width=20)
            btn_increase18.place(x=240,y=135,width=20)
            btn_decrease18.place(x=200,y=135,width=20)
            confbutton18.place(x=270,y=135)
            removebutton18.place(x=300,y=135)
        s+=1
            

    def conf():
        global framedownright
        if var1.get()==1:
                        cursor.execute("select * from ITEMS where TYP='PHONE'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart1=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=SamSung12).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart2=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=iPhone13).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart3=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=MiY3).place(x=450,y=145,width=100)

                            
        if var2.get()==1:
                        cursor.execute("select * from ITEMS where TYP='TABLETS'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart4=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=ipadpro).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart5=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=samsungtab).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart6=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Mitab).place(x=450,y=145,width=100)
        if var3.get()==1:
                        cursor.execute("select * from ITEMS where TYP='LAPTOP'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart7=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Lenovo).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart8=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Macbook).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart9=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=dell).place(x=450,y=145,width=100)
        if var4.get()==1:
                        cursor.execute("select * from ITEMS where TYP='AIR CONDITIONERS'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart10=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=godrej).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart11=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=mitsubishi).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart12=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=LG).place(x=450,y=145,width=100)
        if var5.get()==1:
                        cursor.execute("select * from ITEMS where TYP='REFRIGERATORS'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart13=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=LGref).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart14=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=SamSungref).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart15=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Godrejref).place(x=450,y=145,width=100)
        if var6.get()==1:
                        cursor.execute("select * from ITEMS where TYP='LIGHTS'")
                        data1=cursor.fetchall()
                        b,c,d=data1
                        text1=Label(framedown,text=b[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=40,width=280,height=40)
                        text7=Label(framedown,text=b[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=40,width=100,height=40)
                        Addtocart16=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Crompton).place(x=450,y=45,width=100)
                        text1=Label(framedown,text=c[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=90,width=280,height=40)
                        text7=Label(framedown,text=c[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=90,width=100,height=40)
                        Addtocart17=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=Philip).place(x=450,y=95,width=100)
                        text1=Label(framedown,text=d[0],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text1.place(x=10,y=140,width=280,height=40)
                        text7=Label(framedown,text=d[2],bg="black",fg="white",bd=1,font=("times new roman",15,"bold"))
                        text7.place(x=291,y=140,width=100,height=40)
                        Addtocart18=Button(framedown,text="ADD TO CART",bg="black",fg="yellow",font=("times new roman",10,"bold"),command=swarovski).place(x=450,y=145,width=100)

    var1 = IntVar()
    Checkbutton(frameup,variable=var1,bg="light green").place(x=230,y=17)
    var2 = IntVar()
    Checkbutton(frameup, variable=var2,bg="light green").place(x=230,y=67)
    var3 = IntVar()
    Checkbutton(frameup,variable=var3,bg="light green").place(x=230,y=117)
    var4 = IntVar()
    Checkbutton(frameup,variable=var4,bg="light green").place(x=620,y=17)
    var5 = IntVar()
    Checkbutton(frameup,variable=var5,bg="light green").place(x=620,y=67)
    var6 = IntVar()
    Checkbutton(frameup,variable=var6,bg="light green").place(x=620,y=117)

    var7=IntVar()
    Checkbutton(frameupr,variable=var7,bg="light green").place(x=90,y=130)
    var8=IntVar()
    Checkbutton(frameupr,variable=var8,bg="light green").place(x=330,y=130)
    var9=IntVar()
    Checkbutton(frameupr,variable=var9,bg="light green").place(x=500,y=130)
                
    Confirm=Button(frameup,text="CONFIRM",bg="black",fg="yellow",font=("times new roman",20,"bold"),command=conf).place(x=370,y=167,width=150)
    p=0

    def done():
        global p
        if name.get().isdigit() or not phone.get().isdigit() or ((var7.get()==0 and var8.get()==0 and var9.get()==0) or(var7.get()==1 and var8.get()==1) or (var8.get()==1 and var9.get()==1) or (var7.get()==1 and var9.get()==1) or (var7.get()==1 and var8.get()==1 and var9.get()==1)):
            messagebox.showerror("Error","Kindly fill in required details and select one method of payment")
        else:
            messagebox.showinfo("Message","Saved Details !")
            p+=1

    Namelabel=Label(frameupr,text="NAME:",bg="light green",fg="black",font=("times new roman",20,"bold")).place(x=0,y=0,width=140,height=25)
    PhoneLabel=Label(frameupr,text="PHONE:",bg="light green",fg="black",font=("times new roman",20,"bold")).place(x=0,y=30,width=140,height=25)
    AddressLabel=Label(frameupr,text="ADDRESS:",bg="light green",fg="black",font=("times new roman",20,"bold")).place(x=0,y=60,width=140,height=25)
    PaymentLabel=Label(frameupr,text="MODE OF PAYMENT:",bg="light green",fg="black",font=("times new roman",20,"bold")).place(x=00,y=100,width=290,height=25)
    CashLabel=Label(frameupr,text="CASH",bg="light green",fg="dark red",font=("times new roman",20,"bold")).place(x=0,y=130,width=90,height=25)
    CreditLabel=Label(frameupr,text="CREDIT/DEBIT",bg="light green",fg="dark red",font=("times new roman",20,"bold")).place(x=130,y=130,width=200,height=25)
    GpayLabel=Label(frameupr,text="GPAY/UPI",bg="light green",fg="dark red",font=("times new roman",20,"bold")).place(x=355,y=130,width=150,height=25)

    Confirmdetails=Button(frameupr,text="CONFIRM",bg="black",fg="yellow",font=("times new roman",20,"bold"),command=done).place(x=160,y=170,width=140,height=50)
    Checkout=Button(framedownright,text="CHECKOUT",bg="black",fg="yellow",font=("times new roman",20,"bold"),command=newopenWINDOW).place(x=340,y=200)

            
                #========================================ENTRY=============================================
    name=Entry(frameupr)
    name.place(x=160,y=0,width=250,height=25)
    phone=Entry(frameupr)
    phone.place(x=160,y=30,width=250,height=25)
    address=Entry(frameupr)
    address.place(x=160,y=60,width=250,height=25)

    
img = ImageTk.PhotoImage(Image.open(r"C:\Users\samih\Downloads\WebsiteJpg_XL-FELEC_Main Visual_Purple_Website(1).jpg"))
label11 = Label(window, image = img)
label11.place(x=0,y=0)
header=Label(text="Online Delivery System",width=40,height=2,font=('Algerian', 50, 'bold'),fg="blue",bg="orange")
header.pack()
username=Label(text="Username",font=("Comic Sans",20,"bold"),fg="#408A42")
username.place(x=500,y=300)
usernameentry=Entry()
usernameentry.place(x=650,y=300,width=180,height=40)
password=Label(text="Password",font=("Comic Sans",20,"bold"),fg="#408A42")
password.place(x=500,y=350)
passwordentry=Entry()
passwordentry.place(x=650,y=350,width=180,height=40)
OK=Button(text='LOGIN',font=("Comic Sans",17,"bold"),fg="#408A42",command=openNewWindow)
OK.place(x=595,y=410)







