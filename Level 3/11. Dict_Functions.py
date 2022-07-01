# Assignment 11
# Create a dictionary that contains usernames as the key and passwords as the associated values. 
# Make up the data for five dictionary entries and demonstrate the use of clear and fromkeys() methods.

# Creates a dictionary with key:value pairs
user_pass={"admin":"password","LHBC":"Weak","teacher":"education","virat":"century","python":"programming"}
print(user_pass)

user_pass.clear()   # .clear() function clears the dictionary
print(user_pass)

usernames={"admin","LHBC","teacher","virat","python"}
passwords={"password"}
new_dict=dict.fromkeys(usernames,passwords)     # dict.fromkeys() stores new key:value pairs given 
print(new_dict)

'''
OUTPUT:
{'admin': 'password', 'LHBC': 'Weak', 'teacher': 'education', 'virat': 'century', 'python': 'programming'}
{}
{'admin': {'password'}, 'python': {'password'}, 'LHBC': {'password'}, 'virat': {'password'}, 'teacher': {'password'}}      
'''