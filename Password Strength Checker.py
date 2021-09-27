import re
uPwd = ""
checker = False
errorGeneral = ("The password is weak. Make sure your password "+
         "has at least 8 characters, at least one special "+
         "character, and no spaces.")
errorBlanks = ("Passwords cannot contain newlines, spaces,"+
               " or be left blank.")

#policies
#1. No blank spaces
#2. At least 8 characters
#3. At least one uppercase character
#4. At least one lowercase character
#5. At least one special character

def password_Checker():
    uPwd = input("Enter a password: ")

    #spaceReg
    if(re.search('(\s)',uPwd)):
            print(errorBlanks)

    #zeroReg
    elif(len(uPwd)==0):
        print(errorBlanks)
    
    elif(len(uPwd)>=8):
        if((re.search(r'[!@#$%^&*]',uPwd)) and (re.search(r'[a-z]',uPwd))\
            and(re.search(r'[A-Z]',uPwd)) and re.search('[0-9]',uPwd)):
            print("The password is strong"), checker == True
        else: print(errorGeneral)

    #2fewChar    
    else: print(errorGeneral)

while checker == False:
    password_Checker()
