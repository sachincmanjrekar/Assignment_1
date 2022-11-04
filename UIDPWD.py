#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re
import os

def Validate_emailid(email):                                     #Validate if Given 'MailID' matches with minimum criteria
    pattern_1 =  "^[a-zA-Z]+\w*[@][a-zA-Z]+[.][a-zA-Z]{2,3}$"    #Validation done with help of Regular Expression
    result_1 = re.match(pattern_1, email)
    if(result_1):
        return True
    else:
        return False



def Validate_password(pswd):                                     #Validate if Given 'MailID' matches with minimum criteria
    pattern_2 =  "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d@#$!%*?&]{5,16}$"
    result_2 = re.match(pattern_2, pswd)
    if(result_2):
        return True
    else:
        return False
    
    
def verification(test_mail):                                  #'verification' function return True if given mailID already exist,False otherwise
    DB=os.path.isfile('User.txt')                       
    if(DB):                                                   # 'DB' variable return True Check if 'Database file User.txt' containing 'UserId and Password' exist
        f=open("User.txt","r")
        result_3=False
        for line in f:            
            line=line.rstrip()                                 #By default rstrip removes white spaces at the tail end
            a=line.split()                                     #It will split mailID and password, default splitter is a space(" ")
            if (a[0]==test_mail):                              #a[0] contains mail id, a[1] contains the password
                result_3=True
                f.close()
                return result_3
        f.close()
        return result_3
    else:
        return False

def reg():                                                      #Reg() function is used for Registration
    test_mail = input("\nEnter the new mailID to Register: ")
    RESULT_1=Validate_emailid(test_mail)

    if RESULT_1:
        EXIST=verification(test_mail)
        
        if(EXIST==False):                                       #If Given mailID doesn't exist, then only it go ahead with Registration
            print("Valid mailID")
            test_password = input("\nEnter the Password : ")
            RESULT_2 = Validate_password(test_password)

            if RESULT_2:
                print("Valid Password")
            else:
                print("\n***Invaid Password***\n Password must contain atleast 1 Capital letter,1 Small letter,1 digit,1 Special Charcter each\n")
        else:
            print("\nMail ID already exist , Please register with new mailID")
            print("If you Forgot password, you can choose Retrieve the password or Set new password")
            
    else:
        print("**Invalid MailID**")
    
    if(RESULT_1 and not EXIST and RESULT_2):                    #If Given maiiID doesn't exist in database,Both new mailID and password is valid, then it will Register
        str=test_mail+" "+test_password+"\n"                    #create new string by joining 'EmailId' and 'Password' with space and add newline character(\n) at the end of it
        f=open("User.txt",'a')                            #Append this newstring
        f.write(str)
        f.close()
        print("\n***Registration is Successful***\n")
        
        
def login():                                                    # login() function checks for Successful LOGIN
    test_mail = input("\nEnter the mailID : ")
    RESULT_1=Validate_emailid(test_mail)
    test_password = input("\nEnter the Password : ")
    RESULT_2 = Validate_password(test_password)
    


    if(RESULT_1):
        RESULT_3 = verification(test_mail)
        
        if(not RESULT_3):
            print("\nGiven mailID doesn't exist\n Please Register")
        elif(RESULT_3 and not RESULT_2):
            print("\nUser name FOUND, but Password does not match")
        elif(RESULT_3 and RESULT_2):
            f=open("User.txt","r")
            for line in f:
                line=line.rstrip()
                a=line.split()
                if (a[0]==test_mail):
                    if (a[1]==test_password):
                        print("\nPassword Matches for the given email address, LOGIN SUCCESSFUL ")
                        break
                    else:
                        print("\nUser name FOUND, but Password does not match")
                        break
            
    else:
        print("Invalid MailID")
        
        
def retrive_password():                                         #retrive_password() function is used for retrival of password of existing registered mailID
    test_mail = input("\nEnter the mailID : ")
    RESULT_1=Validate_emailid(test_mail)
    
    if RESULT_1:
        exist=False
        DB=os.path.isfile('User.txt')
        if(DB):
            f=open("User.txt","r")
            for line in f:
                line=line.rstrip()
                a=line.split()
                if(a[0]==test_mail):
                    exist=True
                    print("PassWord for Given mailID is",a[1])
                    break
            if(not exist):
                print("\ngiven mailID doesn't exist in database\n Check mailId that you are entered\nOR\n Please Register first")
        else:
            print("\n'User.txt' Database file about Email Registration doesn't exist'")
    else:
        print("\nInvalid Email,Enter Valid mailID")
        
        
def set_password():                                                #set_password() function is used for setting new password for already registerd mail
    email_id=input("Enter the Registered Email : ")
    RESULT_1=Validate_emailid(email_id)
    RESULT_3=verification(email_id)

    if(RESULT_1==False):
        print("\nInvalid email address")
    elif(RESULT_1 and not RESULT_3):
        print("\n\nGiven Email address is not Registerd, Please Register first")
    elif(RESULT_1 and RESULT_3):
        fel=open("User.txt","r")
        g=fel.readlines()
        t=[]
        PWD_Reset=False
        for i in g:
            i=i.rstrip()
            a=i.split()
            if(a[0]==email_id):
                new_password=input("\nEnter valid new password: ")
                RESULT_2=Validate_password(new_password)
                if(RESULT_2):          
                    s=a[0]+" "+new_password+"\n"
                    t.append(s)
                    PWD_Reset=True
                    continue
                else:
                    print("\n*****New Password is not Valid*****\n")
                    print("Password must contain atleast 1 Special characters,1 digit,1 Capital letter,1 small letter each. Password length must be between 5 to 16")
                    break
            i=i+"\n"
            t.append(i)


        fel.close()

        if(PWD_Reset):                  #if New password valid,then only update it.
            f=open("User.txt","w")
            f.writelines(t)
            print("******Password reset successfully******")
            f.close()
    


print("Please select operation \n1.Registration \n2.Login \n3.Retrive Password if you forget your password\n4.Set New password if you forget your password")
choice=input("\nEnter your choice : ")

if(choice == "1"):
    reg()                          #Choose for Registration
    
if(choice == "2"):
    login()                        #Choose for Login
    
if(choice == "3"):
    retrive_password()             #Choose for Retrive password
    
if(choice == "4"):
    set_password()                 #Choose for Set New Password
    
if(choice not in ["1", "2", "3", "4"]):          
    print("Invalid choice")


# In[ ]:




