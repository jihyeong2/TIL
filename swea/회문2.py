import sys
sys.stdin=open("input.txt","r")
def isPal1(row,s,e,arr) :
    if s>=e: return True
    if arr[row][s]==arr[row][e]: return isPal1(row,s+1,e-1,arr)
    else: return False
def isPal2(col,s,e,arr):
    if s>=e: return True
    if arr[s][col]==arr[e][col]: return isPal2(col,s+1,e-1,arr)
    else: return False
for _ in range(10):
    tc=int(input())
    arr=[list(input()) for _ in range(100)]
    result=0
    for i in range(100):
        for l in range(100,0,-1):
            for s in range(100-l+1):
                if isPal1(i,s,s+l-1,arr):
                    result=max(result,l)
    for j in range(100):
        for l in range(100,0,-1):
            for s in range(100-l+1):
                if isPal2(j,s,s+l-1,arr):
                    result=max(result,l)
    print('#{} {}'.format(tc,result))
