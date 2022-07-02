# ASSIGNMENT 13
# Write a python program that reads the contents of the file and counts 
# the occurrences of each letter. Prompt the user to enter the filename.

# NOTE: A file by the name "SampleText.txt" is present in my Colab Drive. You need to create a new file and input its name.

filename=input("Enter file name: ")
# Opening file using open() function in 'r' read mode.
file1 = open('/content/drive/MyDrive/Colab Notebooks/'+filename, 'r')  
filetext = file1.read() # reading the file and storing its value in variable 'filetext' 
print(filetext)

letter_count = {}       # Empty dictionary letter_count
for i in filetext:      # Holds the first character of the strings of files and checks it with every other character
# if letter present, increments value of letter count until end of string. Continues till all characters checked.
   if i in letter_count:       
      letter_count[i] += 1
   else:
      letter_count[i] = 1
print ("Count of all characters is :\n "+ 
str(letter_count))

'''
OUTPUT:
Enter file name: SampleText.txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Count of all characters is :
 {'L': 1, 'o': 29, 'r': 22, 'e': 37, 'm': 17, ' ': 68, 'i': 42, 'p': 11, 's': 18, 'u': 28, 'd': 18, 'l': 21, 't': 32, 'a': 29, ',': 4, 'c': 16, 'n': 24, 'g': 3, 'b': 3, 'q': 5, '.': 4, '\n': 4, 'U': 1, 'v': 3, 'x': 3, 'D': 1, 'h': 1, 'f': 3, 'E': 1}
'''
