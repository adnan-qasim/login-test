import re
import time
from tkinter import N
import acc_db
from acc_db import acc_crud

class register:

    def __init__(self):
        fname =input("Enter full name: ")
        uname= input("Enter Username: ")
        valid_uname= re.match(r"[a-z]+(\d+)[a-z]*(\d*)$",uname)
        if valid_uname and len(uname)>=6:    
            print(valid_uname.group()+ " is a valid Username ")
        else:
            print(uname+" is invalid Username\nCharacter must start with lowercase alphabet [a-z] and Should have atleast 1 digit [0-9] and Should be 6 Characters long\nRetry...")
            register()
        e_mail=input("Enter Valid email address: ")
        if re.search(r'(\w{3,})@([a-z]+).([a-z]+)',e_mail):
            print("Valid Email Address...")
        else:
            print("Invalid Email....\nRETRY")
            register()
        passw=input("Enter Valid Password: ")
        cnf_pass=input("Confirm the Password: ")
        if re.search(r"[a-z]+",passw) and re.search(r"[A-Z]+",passw) and re.search(r"(\d+)",passw) and len(passw)>=8: 
            if passw==cnf_pass:
                print("Valid password...\n\nCreating Account...")
                time.sleep(1)
                print("...processing.....")
                time.sleep(2)
                self.cr_acc(fname,uname,e_mail,passw)

            else: 
                print("Passwoed Valid but Doesn't Matches")
                register()
        else:
            print("Invalid Password\nPassword must contain atleast a lowercase & UPPERCASE Alphabet [A-Z,a-z] and a Digit [0-9]...\nRetry...")
            register()

    def cr_acc(self,name,user,mail,passw):
        if acc_crud.same_mail(mail)==False:
            if acc_crud.same_acc(user)==False:
                accId= acc_crud.add_acc(name,user,mail,passw)
                print(f"Account with \nUsername: {user}\nEmail: {mail}"
                f"\nPassword: {passw}\nHas been Created Successfully at Id: {accId}  ;)")
            else:
                print("Username "+user+" Is Already in Use...\nRetry...")
                register()
        else:
            print("Email "+mail+" Is Already in Use...\nRetry...")
            register()


class login:

    def __init__(self):
        uname = input("Enter Your Username(or type NONE to Register)")
        if uname.upper =='NONE':
            register()
            menu()
        passw=acc_crud.acc_pass(uname)
        if passw==None:
            print(f'Any User with Username: {uname} can not be found....\nRedirecting you to Menu...')
            time.sleep(3)
            menu()
        elif passw!=None:
            in_pass=input(f"Enter password for the User {uname}: ")
            if in_pass==passw:
                print("Login Succesful ;)")
                #login into something... new function... idk
            else:
                yn=input("Wrong Passowrd...\nWant to retry??(y/n)")
                if yn.lower=='y':
                    login()


class update:

    def __init__(self):
        uname = input("Enter Your Username to Update")
        passw=acc_crud.acc_pass(uname)
        if passw==None:
            print(f'Any User with Username: {uname} can not be found....\nRedirecting you to Menu...')
            time.sleep(3)
            menu()
        elif passw!=None:
            in_pass=input(f"Enter password for the User {uname}: ")
            if in_pass==passw:
                print("Enter the fields you want to update (leave empty to keep old data)")
                self.up_data("Full Name",uname)
                self.up_data("Username",uname)
                self.up_data("Email Address",uname)
                self.up_data("Password",uname)

    def up_data(self,field,user):
        new_data=input(f'Enter new {field}: ')
        if new_data=='':
            pass
        else:
            res=acc_crud.up_acc(user,field,new_data)
            print(f"User's {field} update result: {res.acknowledged}")



class menu:
    def __init__(self):
        i=0
        while i<10:
            c=int(input("==============MENU==============\n"
            "1. Create new Account\n2. Login into a Exsisting Account\n3. Delete Your Account\n4. Update Account\n5. EXIT\nEnter Choice: "))
            if c==1:
                register()
            elif c==2:
                login()
            elif c==3:
                pass #del_acc()
            elif c==4:
                update()
            elif c==5:
                break
            else:
                print("Enter Valid Choice...")
                menu()
        
menu()