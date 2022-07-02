# ASSIGNMENT 14
# Write a Python program 
# a. To search the numbers (0–9) of length between 1 to 3 in a given string. 
# b. To find the substrings within a string

# Variable 'data' with random string value filled with characters and integers.
data = "nd39aj w diwd9q3 edn38q2382 wqe83ne qind03 edf q03ie aed98 "
num=''
for i in data:          # Starts initializing each element in string
    if i.isdigit():     # if element is digit/integer, it is appended to 'num'
      num+=i            
    #this repeats until a non-digit is found, following which the ELSE code is executed 
    else:
      # if element is non-digit/character, 'num' is printed and cleared
      if num.isdigit(): 
        print(num)
        num=''


'''
OUTPUT:
39
9
3
38
2382
83
03
03
98
'''