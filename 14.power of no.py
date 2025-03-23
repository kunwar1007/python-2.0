#Method 1: Using Pow() Function
num, power = 3, 2
print(pow(num,power))


#Method 2: Using Simple Iteration
num, power = 3, 2
output = 1
for i in range(power):
  output*=num
print(output)