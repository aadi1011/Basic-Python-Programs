#Write a python program that has the dictionary of your friends’ names as keys and phone numbers as its values. 
#Print the dictionary in a sorted order. Prompt the user to enter the name and check if it is present in the dictionary. 
#If the name is not present, then enter the details in the dictionary.

# Creating a dictionary with 3 key:value pairs
dict={"Aadith": "2569874582", "Arnoob": "6589854125", "ElonDusk":"5214986369"}
y=sorted(dict.keys())       #sorted() function sorts the dictionary's keys
print(y)
findname=input("Enter a name: ")
if findname in dict:
  x = dict[findname]        #stores value for key provided if found in variable 'x'
  print (x)
else:
  new_number=input("Enter number: ")    # prompts for new value if key not found and stores in variable 'new_number'
  dict[findname]=new_number
print(dict)

'''
OUTPUT:
['Aadith', 'Arnoob', 'ElonDusk']
Enter a name: Arnoob
6589854125
{'Aadith': '2569874582', 'Arnoob': '6589854125', 'ElonDusk': '5214986369'}
'''