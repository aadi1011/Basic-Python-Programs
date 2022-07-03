# ASSIGNMENT 15
# Write a python to create a class called library with data attributes like acc_number, publisher, title and author. 
# The methods of the class should include 
# a. read() – acc_number, title, author. 
# b. compute() - to accept the number of days late, calculate and display the fine charged at the rate of $1.50 per day. 
# c. display the data.


# Class Library is created with multiple functions and __init__ variables.
class Library:
  acc_number=''
  publisher=''
  title=''
  author=''
  # function inside class to take input
  def read(self): 
    #acc, title, author, publisher
    self.acc_number=input("Enter your account number: ")
    self.publisher=input("Enter publisher name: ")
    self.title=input("Enter Title of book: ")
    self.author=input("Enter author of book: ")
    
  # function to calculate the days late  
  def compute(self):   
    #accept number of days from user
    self.days=int(input("Enter number of days late: "))
    self.fine=self.days*1.5           #fine of $1.5 per day

  #function to print everything when called
  def display(self):
    print("Account Number: ", self.acc_number)
    print("Title of book: ", self.title)
    print("Publisher: ", self.publisher)
    print("Author of Book: ", self.author)
    print("Number of days late: ", self.days)
    print("Fine amount to be paid: $",self.fine)

obj = Library() # assigning class Library call instance to 'obj' 
obj.read()      # calling .read() function
obj.compute()   # calling .compute() function
obj.display()   # calling .display() function

'''
OUTPUT:
Enter your account number: 42069420
Enter publisher name: Penguin Publishers
Enter Title of book: Harry Potter & The Console of Python
Enter author of book: B.J. Growling
Enter number of days late: 18
Account Number:  42069420
Title of book:  Harry Potter & The Console of Python
Publisher:  Penguin Publishers
Author of Book:  B.J. Growling
Number of days late:  18
Fine amount to be paid: $ 27.0
'''
