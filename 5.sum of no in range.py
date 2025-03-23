#using brute force 
num1, num2 = 3, 6
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)

#using formula
num1, num2 = 3, 6
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)