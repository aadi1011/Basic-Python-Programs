# Given two strings, A and B, check if A and B are case-insensitive anagrams. 
# Print "Anagrams" if A and B are anagrams of each other; otherwise, print "Not Anagrams" instead.

a = input("Enter a string: ")
b = input("Enter another string: ")
if sorted(a.lower()) == sorted(b.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")  