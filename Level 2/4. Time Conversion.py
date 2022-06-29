#4. Convert milliseconds to hours, minutes and seconds

# Creating a function convert() to perform time conversion operations.

def convert(milli):
  sec, milli = divmod(milli,10)             # modulo divides milliseconds by 10 and stores in sec
  minute, sec = divmod(sec, 60)             # modulo divides seconds by 60 and stores in min
  hour, minute = divmod(minute, 60)         # modulo divides minutes by 60 and stores in hour
  return "%d:%d:%d"%(hour, minute, sec)     # prints time in hr:min:sec format

# Outside the function, take value of milliseconds from user and store in variable 'given_time' 
given_time=int(input("Enter value in milliseconds: "))
print("Time in hrs:mins:secs = ",convert(given_time))   # Runs function and prints output

'''
OUTPUT:
Enter value in milliseconds: 69420
Time in hrs:mins:secs =  1:55:42
'''
