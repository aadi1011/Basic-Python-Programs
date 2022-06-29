#1. Surface area of a prism can be calculated if the lengths of the three sides are known. 
#   Write a python program that takes the sides as input (read it as integer) and prints 
#   the surface area of the prism (Surface Area = 2ab + 2bc + 2ca).

# The values of 3 sides are assigned to variables a,b,c respectively
a = int(input("Enter side one dimension: "))  
b = int(input("Enter side two dimension: "))
c = int(input("Enter side three dimension: "))

# variable "SurfaceArea" calculates the surface area according to formula and stores the value
SurfaceArea = (2*a*b)+(2*b*c)+(2*c*a)       #Surface area formula = 2(side1*side2)+2(side2*side3)+2(side1*side3)
print ("Surface Area = ", SurfaceArea)      #Prints Surface area


### OUTPUT ###
# Enter side one dimension: 2
# Enter side two dimension: 4
# Enter side three dimension: 3
# Surface Area =  52
