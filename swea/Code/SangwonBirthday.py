def bfs(x):
    q=[(x,0)]
    visit=[0]*(n+1)
    visit[x]=1
    cnt=0
    while q:
        cur,dist=q.pop(0)
        for next in g[cur]:
            if visit[next] :continue
            visit[next]=1
            cnt+=1
            if dist+1<2:
                q.append((next,dist+1))
    return cnt
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    g=[[] for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    result=bfs(1)
    print('#{} {}'.format(tc,result))