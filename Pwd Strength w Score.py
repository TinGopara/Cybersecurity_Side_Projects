import re
uPwd = ""
checker = False
#this is the score the password receives per policy
score = 0

#policies
#1. No blank spaces
#2. At least 8 characters
#3. At least one uppercase character
#4. At least one lowercase character
#5. At least one special character
#6. At least one number

def password_Checker():
    global checker
    global score
    score = 0
    uPwd = input("Enter a password: ")
    #these are all the regex that will be used
    specReg = (re.search(r'[!@#$%^&*]',uPwd))
    lowerReg = (re.search(r'[a-z]',uPwd))
    upperReg = (re.search(r'[A-Z]',uPwd))
    numReg = (re.search('[0-9]',uPwd))
    #these are some error messages if password fails
    errorGeneral = ("The password is weak. Make sure your password "+
         "has at least 8 characters, at least one special "+
         "character, and no spaces.")
    errorBlanks = ("Passwords cannot contain newlines, spaces,"+
               " or be left blank.")
    outputString = ""
    
    #this section will use the regex to check the password
    #testing for blanks is the preliminary requirement, 0 points are awarded
    #for passing this section.
    if(re.search('(\s)',uPwd)):
            print(errorBlanks)
    elif(len(uPwd)==0):
        print(errorBlanks)
        
    #other policy criteria. Up to 5 points are awarded in this section.
    elif(len(uPwd)>=1):
        
        if(specReg): score += 1
        else:
            outputString = outputString + "Use at least one special character. "
        if(lowerReg): score += 1
        else:
           outputString = outputString + "Use at least one lowercase alpha character. " 
        if(upperReg): score += 1
        else:
           outputString = outputString + "Use at least one uppercase alpha character. " 
        if(numReg): score += 1
        else:
           outputString = outputString + "Use at least one digit. "
        if(len(uPwd)>=8): score +=1
        else:
           outputString = outputString + "Passwords must be at least 8 characters long. "
            

    #this wil communicate score results to the user.
           
        if(score == 5):
            print("The password is strong and meets all requirements.")
            checker == True
        
        elif(4>=score): print("Your password has a score of "+str(score)+ " out of 5."+
                              outputString)
        #if(specReg and lowerReg and upperReg and numReg):
            #print("The password is strong"), checker == True
        #else: print(errorGeneral)   
    else: print(errorGeneral)


while checker == False:
    password_Checker()
    if(score == 5):
        break
