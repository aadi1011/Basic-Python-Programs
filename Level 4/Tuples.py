# ASSIGNMENT 12
# Write a python program 
# a. To check whether an item exists within a tuple. 
# b. To create a list containing three elements, and then create a tuple from that list.

# Creating a tuple with 5 elements
tuple1 = (1, 2, 3, 4, 5 )
item=int(input("Enter number to check in tuple: "))
if item in tuple1:
  print("Element present")
else:
  print("Element missing")

list1=['Watermelon','Sugar','OreoShake']    # Creating a list with 3 elements
print(tuple(list1))                         # converting the list to a tuple and printing it

'''
OUTPUT:
Enter number to check in tuple: 4
Element present
('Watermelon', 'Sugar', 'OreoShake')
'''
