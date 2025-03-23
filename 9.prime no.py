#Method 1: Simple iterative solution
num = 15
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

#Method 2: Optimization by break condition
num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,num):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")