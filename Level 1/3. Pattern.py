#3. Write a program to display the following pattern using nested loops


# This code requires good mathematical understanding.
# Variable n stores the value for the number to print
n=1
for i in range(0,5):        #This loop initializes the number of lines
  for j in range(i+1):      #This loop initializes the number of characters per line
    print(n, end="")        #This prints the number and appends at the 'end'
  n+=1                      # n is incremented the every loop continues
  print("")

n=5
for i in range(0,5):
  for j in range(1,5-i):
    print(" ", end="")
  for k in range(i+1, 0, -1):
    print (k, end="")
  print()


  '''
  OUTPUT:
  1
  22
  333
  4444
  55555
    1
   21
  321
 4321
54321
  '''