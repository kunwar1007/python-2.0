#Method 1: Using Simple Iteration I
n = 28
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

#Method 2: Using Simple Iteration II
num = 28
sum = 0

i = 1
while i < num:
    if num % i == 0:
        sum += i

    i += 1

if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")