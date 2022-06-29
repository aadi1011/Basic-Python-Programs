#2. Write a python program to convert temperature from centigrade (read it as float value) to Fahrenheit.

# variable cel stores value of celcius unit taken from user
cel = float(input("Enter celcius temperature: "))
fahr = cel*1.8+32                   # variable fahr stores value of converted celcius using formula
print("Fahrenheit value = ",fahr)