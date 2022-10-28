import re
from turtle import delay
from unicodedata import unidata_version
import time
def sing_up():
    fname =input("Enter full name: ")
    uname= input("Enter Username: ")
    valid_uname= re.match(r"[a-z]+(\d+)[a-z]*(\d*)$",uname)
    if valid_uname and len(uname)>=6:    
        print(valid_uname.group()+ " is a valid Username ")
    else:
        print(uname+" is invalid Username\nCharacter must start with lowercase alphabet [a-z] and Should have atleast 1 digit [0-9] and Should be 6 Characters long\nRetry...")
        sing_up()
    passw=input("Enter Valid Password: ")
    cnf_pass=input("Confirm the Password: ")
    if re.search(r"[a-z]+",passw) and re.search(r"[A-Z]+",passw) and re.search(r"(\d+)",passw) and len(passw)>=8: 
        if passw==cnf_pass:
            print("Valid password...\n\nCreating Account...")
            time.sleep(1)
            print("...processing.....")
            time.sleep(2)
            print("Account Created Successfully ;-)")

        else: 
            print("Passwoed Valid but Doesn't Matches")
    else:
        print("Invalid Password\nPassword must contain atleast a lowercase & UPPERCASE Alphabet [A-Z,a-z] and a Digit [0-9]...\nRetry...")
        sing_up()

sing_up()