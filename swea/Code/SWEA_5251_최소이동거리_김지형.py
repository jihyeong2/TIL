import heapq
T=int(input())
for tc in range(1,T+1):
    n,e=map(int,input().split())
    g=[[] for _ in range(n+1)]
    cost=[[] for _ in range(n+1)]
    for _ in range(e):
        s,e,w=map(int,input().split())
        g[s].append((e,w))
    heap,visit=[(0,0)],[False]*(n+1)
    T=[float('inf')]*(n+1)
    T[0]=0
    while heap:
        dist,cur=heapq.heappop(heap)
        if visit[cur]: continue
        visit[cur]=True
        for next,n_dist in g[cur]:
            if T[next]>dist+n_dist:
                T[next]=dist+n_dist
                heapq.heappush(heap,(T[next],next))
    print('#{} {}'.format(tc,T[n]))