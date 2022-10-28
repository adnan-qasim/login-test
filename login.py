import re
import time

def register():
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
            cr_acc(fname,uname,e_mail,passw)

        else: 
            print("Passwoed Valid but Doesn't Matches")
            register()
    else:
        print("Invalid Password\nPassword must contain atleast a lowercase & UPPERCASE Alphabet [A-Z,a-z] and a Digit [0-9]...\nRetry...")
        register()


def cr_acc(name,user,mail,passw):
    acc_list=dict()
    same_m=False
    same_u=False
    if len(acc_list)>0:
        for i,j in acc_list:
            if i==user:
                same_u=True
            if j[2]==mail:
                same_m=True
    if same_m==False :
        if same_u==False:
            acc_list[user]=[name,mail,passw]
            print("Account with \nUsername: "+user+"\nEmail: "+mail+"\nPassword: "+passw+"\nHas been Created Successfully ;)")
        else:
            print("Username "+user+" Is Already in Use...\nRetry...")
            register()
    else:
        print("Email "+mail+" Is Already in Use...\nRetry...")
        register()
    print(acc_list)
register()