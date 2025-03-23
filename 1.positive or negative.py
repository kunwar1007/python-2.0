'''
Method 1: Using Brute Force
Method 2: Using Nested if-else Statements
Method 3: Using ternary operator'
'''

num = 15
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')


num = 15
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")