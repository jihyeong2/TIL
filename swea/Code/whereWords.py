import sys
sys.stdin=open("input.txt","r")
def check(rc,maps):
    res,cnt1,cnt2=0,0,0
    for i in range(n-1,-1,-1):
        if maps[rc][i]==1:cnt1+=1
        else:
            if cnt1==k:  res+=1
            cnt1=0
        if maps[i][rc]==1: cnt2+=1
        else:
            if cnt2==k:  res+=1
            cnt2=0
    if cnt1==k:  res+=1
    if cnt2==k:  res+=1
    return res
T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    maps=[list(map(int, input().split())) for _ in range(n)]
    result=0
    for i in range(n):
        result+=check(i,maps)
    print('#{} {}'.format(tc,result))