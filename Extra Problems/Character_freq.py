# program to find highest frequency character in a string

def highest_freq(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    max_freq = 0
    max_char = ''
    for char in freq:
        if freq[char] > max_freq:
            max_freq = freq[char]
            max_char = char
    return max_char

text = input("Enter a string: ")
print("Highest frequency character is", highest_freq(text), "with frequency", text.count(highest_freq(text)))