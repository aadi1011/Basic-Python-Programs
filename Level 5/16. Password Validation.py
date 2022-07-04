# Write a program to check validation of password entered by the user (special characters, numbers, length of password). 
# The password also should be present in a text file containing random passwords. 
# (Min. 10 passwords should be there in the file)

'''Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be more than 8 characters long.'''

def password_checker(pwd):
    # Assigning the list of special characters
    SpecialSymb=['@','#','$','%','^','&','*']
    result=True         #default flag set to true. i.e. password is strong

    #Check if password length is less than 8 characters
    if len(pwd)<8: 
        result=False

    #Check if there are no digits in password
    # 'any' ensures that atleast one character meets the condition
    if not any(char.isdigit() for char in pwd):
        result=False

    #Check if there are no uppercase letters in password
    if not any(char.isupper() for char in pwd):
        result=False   

    #Check if there are no lowercase letters in passwords
    if not any(char.islower() for char in pwd):
        result=False   

    #Check if there are no mentioned special characters in password
    if not any(char in SpecialSymb for char in pwd):
        result=False
    
    #Returns the result (TRUE/FALSE)
    if result:
        return result

# Checking one password from user input:
pwd = input("Enter password to check: ")
password_checker(pwd)
if (password_checker(pwd)): #Throws TRUE value
    print("Password is valid")   
else:                       #Throws FALSE value
    print("Password is invalid")

# Checking passwords from a file:
# Edit your .txt file path
pwdfile=open("textfile.txt", 'r') 
for i in range (0,5):
    pwd= pwdfile.readline()     #Reads each password line by line
    print("Password to validate: ",pwd)
    password_checker(pwd)
    if (password_checker(pwd)): #Throws TRUE value
        print("Password is valid")   
    else:                       #Throws FALSE value
        print("Password is invalid")

'''
OUTPUT:
Enter password to check: Python@123
Password is valid
'''
