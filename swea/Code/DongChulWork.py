def perm(z,max_r):
    global result
    if max_r<=result : return
    if z==n:
        result=max(max_r,result)
    else:
        for i in range(n):
            if visit[i]: continue
            visit[i]=1
            perm(z+1,max_r*p[z][i]*0.01)
            visit[i]=0
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    p=[list(map(int, input().split())) for _ in range(n)]
    visit,result=[0]*n,0
    perm(0,100)
    print('#{} {}'.format(tc,'%0.6f'%result))