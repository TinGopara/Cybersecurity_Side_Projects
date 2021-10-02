import re
uPwd = ""
checker = False
#this is the score the password receives per policy
score = 0

#policies
#1. No blank spaces - bare minimum

#valid password
#2. At least 8 characters
#3. At least one uppercase character
#4. At least one lowercase character
#5. At least one special character
#6. At least one number
#strong password
#7. Discourage 3 or more repeating characters
#8. Discourage dictionary words

def repeatChar(uPwd):
    counter = 0
    patCount = 0
    repeated = False
    first = ''
    second = ''
    pattern = ''
    pat = None
    
    for i in range(len(uPwd)):
        #checks repeating Characters
        if i < (len(uPwd)):
            first = uPwd[i]
            second = uPwd[i-1]
        if(first == second):
            counter+=1
        elif(first!=second):
            counter==0
    if(counter == 3):
            repeated = True
            return repeated
    return repeated

def repeatPatt(uPwd):
    pattern = ''
    checker = False
    #checks repeating substring patterns    
    for x in range(len(uPwd)):
        pat = None
        for y in range(len(uPwd)):
            pattern = (str(uPwd[x:y])).lower()
            if (y >= x+1):
                pat = (re.search(r'str(pattern*3)',uPwd))
                if(bool(pat) == True):
                    checker = True
                    return checker
            
    return checker

def password_Checker():
    global checker
    global score
    uPwd = input("\nEnter a password: ")
    #these are all the regex that will be used
    specReg = (re.search(r'[!@#$%^&*<>.,?]',uPwd))
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
        score = 0
        #SPECREG
        if(specReg): score = score+1
        else:
            outputString = outputString + ("\nUse at least one of these special characters:"+
            "\n!@#$%^&*<>.,?. ")

        #LOWERREG
        if(lowerReg): score = score+1
        else:
           outputString = outputString + "\nUse at least one lowercase alpha character. " 

        #UPPERREG
        if(upperReg): score = score+1
        else:
           outputString = outputString + "\nUse at least one uppercase alpha character. " 

        #NUMREG
        if(numReg): score = score+1
        else:
           outputString = outputString + "\nUse at least one digit. "

        #LENGTHCHECK
        if(len(uPwd)>=8): score = score+1
        else:
           outputString = outputString + "\nPasswords must be at least 8 characters long. "

        #REPEATCHAR
        if(repeatChar(uPwd)== False and repeatPatt(uPwd)==False):
            if(score == 5):
                score = score+1
        else:
            outputString = outputString + ("\nFor strong passwords,"+
            " it is recommended that you \navoid using three or more repeating patterns of \nletters;"+
            "(for example: Caaat or catcatcat).")


    #This section wil communicate score results to the user.   
        if(5 >= score >= 4):
            print("Your password has a score of "+str(score)+ " out of 6. "+
                  "This password meets most requirements, but can be stronger. "+
                  outputString)
        elif(score == 6):
            print("Your password has a score of "+str(score)+ " out of 6. "+
                  "This is a strong password. ")
        else: print("Your password is weak, it has a score of "+
                              str(score)+ " out of 6. " + outputString)  
    else: print(errorGeneral)


while checker == False:
    score = 0
    password_Checker()
    if(score == 6):
        break
