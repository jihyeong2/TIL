import sys
sys.stdin=open("input.txt","r")
def cart(z,idx,min_res,visit):
    if z==n-1:
        global result
        min_res+=maps[idx][0]
        result=min(min_res,result)
    else:
        for i in range(n):
            if i==0 or i==idx or visit[i]: continue
            visit[i]=1
            cart(z+1,i,min_res+maps[idx][i],visit)
            visit[i]=0
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int, input().split())) for _ in range(n)]
    result=float('inf')
    visit=[0]*n
    cart(0,0,0,visit)
    print('#{} {}'.format(tc,result))