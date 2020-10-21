import sys
sys.stdin=open("input.txt","r")
T=int(input())
def Bsearch(p,val):
    s,e,cnt=1,p,0
    while s<e:
        mid=(s+e)//2
        if mid==val:break
        elif mid<val: s=mid
        else: e=mid
        cnt+=1
    return cnt
for tc in range(1,T+1):
    p,a,b=map(int,input().split())
    s,e=1,p
    result=''
    cntA=Bsearch(p,a)
    cntB=Bsearch(p,b)
    if cntA>cntB: result+='B'
    elif cntA<cntB: result+='A'
    else: result+='0'
    print(f'#{tc} {result}')