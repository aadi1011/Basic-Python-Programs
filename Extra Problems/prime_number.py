# Write a program, to check if a given number is prime or not

def prime(num):
    flag = True
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            return True
        else:
            return False

# num = int(input("Enter a number: "))
# print(prime(num))

for i in range(1, 50000):
    if prime(i):
        print(i, end=", ")
