n=4
arr=[1,2,3,4]
for i in range(1<<n):
    sum=0
    for j in range(n):
        if i&(1<<j)!=0:
            sum+=arr[j]
    if sum==0: break