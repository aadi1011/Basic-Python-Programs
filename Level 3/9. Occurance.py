# Experiment 9
# Write a function that finds the number of occurrences of a specified character in a string.

# Creating a function with two arguments (main string, string to search in main string)
def char_occurrence(str2, char1):
  occurrence = 0                # setting default token to 0
  for i in str2:                # loop checks every character for string          
    if i == char1:              
        occurrence += 1         # increments 'occurrence' value everytime substring is detected
  return occurrence

str2 = input('Enter a string: ')        # user input for main string
char1 = input('Enter character to find occurrence: ')   # user input for substring to search
repeat=char_occurrence(str2, char1)                     # calls functions and stores returned value to 'repeat' variable
print(repeat)