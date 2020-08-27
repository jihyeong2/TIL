import sys
sys.stdin=open("input.txt","r")
def isPal(s,e,str):
    if s>=e: return True
    if str[s]==str[e]: return isPal(s+1,e-1,str)
    else: return False
def find(n,m,arr):
    for i in range(n):
        for j in range(n - m + 1):
            row = arr[i][j:j + m]
            col = [st[i] for st in arr[j:j + m]]
            if isPal(0,m-1,row):
                return ''.join(row)
            if isPal(0,m-1,col):
                return ''.join(col)
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    arr=[list(input()) for _ in range(n)]
    result=find(n,m,arr)
    print('#{} {}'.format(tc,result))