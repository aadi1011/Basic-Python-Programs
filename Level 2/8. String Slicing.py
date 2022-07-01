# Experiment 8
# Make a list of the first eight letters of the alphabet, then using the slice operation do the following operations: 
# a. Print the first three letters of the alphabet. 
# b. Print any three letters from the middle. 
# c. Print the letters from any particular index to the end of the list

# Creating list called 'alphabet' with first 8 letters
alphabet=['a','b','c','d','e','f','g','h']  
print(alphabet[0:3])  # String slicing to print elements 0 to 3 in alphabet list
print(alphabet[5:8])  # String slicing to print elements 5 to 8 in alphabet list
index_number=int(input("Enter a number from 0 to 8: ")) # User input to take integer and store in 'index_number' variable
print(alphabet[index_number-1:9])   # String slicing. -1 includes the starting element as well