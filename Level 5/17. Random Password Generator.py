#Creating a random password generator with digits, uppercase, lowercase and special symbols

#importing required python libraries
import random
import array

MAX_LEN=8   #Length of the password. Modify this value if you want your password to be of different length

#Listing the various characters to be included.
DIGITS=['0','1','2','3','4','5','6','7','8','9']
LOCASE_CHARECTERS=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS=['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<']

#Concatenating all the different types into one variable
COMBINED_LIST=DIGITS+UPCASE_CHARACTERS+LOCASE_CHARECTERS+SYMBOLS

#Randomly choosing one character from each type to ensure there is one of each type
rand_digit=random.choice(DIGITS)
rand_upper=random.choice(UPCASE_CHARACTERS)
rand_lower=random.choice(LOCASE_CHARECTERS)
rand_symbol=random.choice(SYMBOLS)

#Creating a new string with the random 4 characters
temp_pass=rand_digit+rand_upper+rand_lower+rand_symbol

#generating the random password. 4 characters are subtracted as we already picked 4 characters in line 25 under temp_pass variable
for x in range(MAX_LEN-4):
    temp_pass=temp_pass+random.choice(COMBINED_LIST)    #Updating temp_pass appending them with more random characters from the complete set from COMBINED_LIST

temp_pass_list=array.array('u',temp_pass)           # 'U' --> stand for Unicode. This basically converts all your elements in string. Hence removes the encoding

#prevent a pattern of the password (random digit->random->loCase->random UpCase->Symbol) as definited in Combined List
random.shuffle(temp_pass_list)                      

password=" "
for x in temp_pass_list:
    password=password+x     #Transferring characters from temp_pass_list to password and printing it

print(password)

'''
3 OUTPUTS:
<W#B<Td9
wYK4$%B:
6<e.%tBN
'''
