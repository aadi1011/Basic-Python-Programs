# Experiment 7
# Write a Python program to access the last character of the string with the help of len() function

# Creating a function called 'len' with user input string as argument. 
def len(str1):
  print('Last character is:', last) 

str1 = input('Enter a string: ')
last = str1[-1]     #Performing String Slicing to extract the last character of the string. 
len(str1)           #Calling the function


'''
OUTPUT:
Enter a string: rudolph
Last character is: h
'''
