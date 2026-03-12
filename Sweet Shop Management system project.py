
import mysql.connector
print("""
-----------------------------------------------------------
   WELCOME TO SWEETSHOP MANAGEMENT SYSTEM
-----------------------------------------------------------""")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="78654")                                                                                    
mycursor=mydb.cursor()
mycursor.execute("create database if not exists Sweet_Shop")                                                                                            
mycursor.execute("use Sweet_Shop")
mycursor.execute("create table if not exists login(username varchar(25)not null,password varchar(25)not null)")                                                                       
mycursor.execute("create table if not exists purchase(odate date not null,name varchar(25)not null, s_id int not null,amount int not null)")
mycursor.execute("create table if not exists stock( s_id int not null, s_name varchar(25) not null,quantity int not null,price int not null)")
mydb.commit()
a=0
mycursor.execute("select*from login")
for i in mycursor:
    a=a+1
if(a==0):
    mycursor.execute("insert into login values('Trijit Roy','3063')")
    mydb.commit()
while True:
    print("""
                               LOGIN AS
          1.Owner
          2.Customer
          3.Exit""")
    c=int(input("Enter your choice:-"))
    if(c==1):
        p=input("Enter your password:-")
        mycursor.execute("select*from login")
        for i in mycursor:
            username,password=i
            if(p==password):
                print("WELCOME")
                loop2='y'
                if(loop2=='Y' or loop2=='y'):
                    print("""
                        1. Add New Sweet
                        2. Update Sweet Information
                        3. Delete Sweet
                        4. Display All Sweets
                        5.Change password
                        6.Logout
                        """) 
                     

                ch=int(input("Enter your choice:-"))
                if(ch==1):
                    """Add a new sweet to the list."""
                    loop='y'
                    while (loop=='Y' or loop=='y'):
                        s_id=input("Enter Sweet ID :-")
                        s_name=input("Enter Sweet Name:-")
                        quantity=int(input("Enter Sweet quantity:-"))
                        price=int(input("Enter Sweet price:-"))
                        mycursor.execute("insert into stock values('"+str(s_id)+"','"+s_name+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print("Data Successfully Inserted...")
                        loop=input("Do you want to Enter more Sweets (y/n):-")                                                            
                        loop2=input("Do you want to Continue Editing Stock of Sweets (y/n):-")
                elif(ch==2):
                    """Update details of an existing sweet."""
                    loop='y'
                    while (loop2=='Y' or loop2=='y'):     
                        s_id=int(input("Enter Sweet ID:-"))
                        new_price=int(input("Enter Sweet price:-"))
                        mycursor.execute("update stock set price='"+str(new_price)+"'where s_id='"+str(s_id)+"'")
                        mydb.commit()
                        print("Data Successfully Updated...")
                        loop=input("Do you want to Change price of any sweets (y/n):-")
                        loop2=input("Do you want to Continue Editing Stock of Sweets (y/n):-")
                elif(ch==3):
                    """Delete a sweet from the list."""
                    loop='y'
                    while (loop2=='Y' or loop2=='y'):
                            s_id =input("Enter Sweet ID :-")
                            mycursor.execute("delete from stock where s_id='"+str(s_id)+"'")
                            mydb.commit()
                            print("Data Successfully Deleted...")
                            loop=input("Do you want to Delete any other Sweets (y/n):-")
                            loop2=input("Do you want to Continue Editing Stock (y/n):-")
                elif(ch==4):
                    """Display all sweets from the list."""
                    mycursor.execute("select*from stock")
                    print("s_id||s_name||quantity||price")
                    for i in mycursor:
                        t_code,t_name,t_quan,t_price=i
                        print(f"{t_code}||{t_name}||{t_quan}||{t_price}")
                elif(ch==5):
                    """Change the Pasword of system."""
                    old_pass=input("Enter your old password:-")
                    mycursor.execute("select*from login")
                    for i in mycursor:
                        username,password=i
                    if(old_pass==password):
                        new_pass=input("Enter your new password:-")
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
                        print("Passord Successfully Changed...")
                elif(ch==6):
                    break
            else:
                 print("Please Enter Correct Password")
                     
    elif(c==2):
        print("""
               1.Item Bucket
               2.Payment
               3.View available items
               4.Exit """)
        ch2=int(input("Enter your choice:-"))
        if(ch2==1):
            name=input("Enter your Name:-")
            s_id=int(input("Enter Sweet ID:-"))
            quantity=int(input("Enter Sweet Quantity:-"))
            mycursor.execute("select * from stock where s_id="+str(s_id))
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
            amount=t_price*quantity
            net_quan=t_quan-quantity
            mycursor.execute(f"update stock set quantity= '{net_quan}' where s_id like '{s_id}'")
            mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(s_id)+"','"+str(amount)+"')")
            mydb.commit()
            print("Sweet added to your bucket...")
        elif(ch2==2):
            name=input("Enter your Name:-")
            mycursor.execute(f"select * from purchase where name like '{name}'")
            for i in mycursor:
                od,nm,sid,amount=i
            print(f"Amount to be paid:- '{amount}'")
            print("Thank You,Visit Again")
        elif(ch2==3):  
            print("ID||NAME||PRICE")
            mycursor.execute("select * from stock")
            for i in mycursor:
                sid,snm,Q,P=i
                print(f"{sid} || {snm} || {Q} || {P}")
        elif(ch2==4):
            break
    elif(c==3):
        break
