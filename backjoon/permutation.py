# import sys
# sys.stdin=open("input.txt", "r")
n,k=map(int,input().split())
arr=list(map(int,input().split()))
result=0
for i in range(k):
    result+=arr[i]
tmp=result
for i in range(k,n):
    tmp=tmp-arr[i-k]+arr[i]
    result=max(result,tmp)
print(result)