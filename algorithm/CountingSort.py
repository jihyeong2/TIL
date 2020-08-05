def countSort(A,B,k):
    count=[0]*k
    for i in range(len(A)):
        count[A[i]]+=1
    for i in range(len(count)-1):
        count[i+1]+=count[i]
    for i in range(len(B)-1,-1,-1):
        B[count[A[i]]-1]=A[i]
        count[A[i]]-=1
data = [0,4,1,3,1,2,4,1]
result=[0]*len(data)
countSort(data,result,10)
print(result)