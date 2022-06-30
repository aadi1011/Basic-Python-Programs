#5. Write a function called rotate_word that takes a string and an integer as parameters, and that function should return
#   a new string containing the letters from the original string “rotated” by the given amount. For example, “cheer” rotated 
#   by 7 is “jolly” and “melon” rotated by −10 is “cubed”.

# Creating a function 'encryption' to run the commands to rotate each string
def encryption(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Change uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)     #detects the ASCII values of characters and rotates the value accordingly
 
        # Change lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)   #detects the ASCII values of characters and rotates the value accordingly
 
    return result
 
# main function to take input for defined function
text = input("Enter Word: ")                    #input text from user.
s = int(input("Enter number of rotations: "))   #input key from user
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Rotated Word: " + encryption(text,s))

'''
Enter Word: CHEER
Enter number of rotations: 7
Text  : CHEER
Shift : 7
Rotated Word: JOLLY
'''