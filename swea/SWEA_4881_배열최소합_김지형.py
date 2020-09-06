import sys
sys.stdin=open("input.txt","r")
def get_minsum(z,sum,maps,visit):
    global result
    if sum>result: return
    if z==n:
        result=min(sum,result)
    for i in range(n):
        if visit[i]: continue
        visit[i]=1
        get_minsum(z+1,sum+maps[z][i],maps,visit)
        visit[i]=0
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int, input().split())) for _ in range(n)]
    visit,result=[0]*n,987654321
    get_minsum(0,0,maps,visit)
    print('#{} {}'.format(tc,result))