#Method 1 : Using Nested loop
def fun(l1,l2):
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if(l1[i]==l2[j]):
                return False
    return True

l1=list(map(int,input("Enter array1").split()))
l2=list(map(int,input("Enter array2").split()))
if(fun(l1,l2)):
    print("Disjoint")

else:
    print("Not disjoint")