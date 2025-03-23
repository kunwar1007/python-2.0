#Iterative approach
num = 6
fact = 1

# Factorial of negative number doesn't exist

if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i

print("Factorial of", num, "is", fact)
# Time complexity: O(N)
# Space complexity: O(1)

#Recursive approach
def getFactorial(num):
    if num == 0:
        return 1

    return num * getFactorial(num - 1)


num = 6
fact = getFactorial(num)

print("Factorial of", num, "is", fact)

# Time complexity: O(N)
# Space complexity: O(1)
# Auxiliary Space complexity(Function call stack): O(N)