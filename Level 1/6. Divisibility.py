# Experiment 6
# Write a program that creates a list of numbers 1–100 that are either divisible by 5 or 6

for n in range(1, 101):     # Creates a range of numbers from 1 to 100
  if (n%6==0 or n%5==0):    # if a number gives remained zero, it is divisble by the divisor
    print (n)               # prints the number

'''
OUTPUT:
5
6
10
12
15
18
20
24
25
30
35
36
40
42
85
90
95
96
100
'''
