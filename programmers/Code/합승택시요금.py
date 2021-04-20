import heapq
def solution(n, s, a, b, fares):
    g=[[] for _ in range(n+1)]
    answer=[]
    for x,y,cost in fares:
        g[x].append((cost,y))
        g[y].append((cost,x))
    for i in range(1,n+1):
        heap=[(0,i)]
        T=[1000001]*(n+1)
        visit=[0]*(n+1)
        T[i]=0
        while heap:
            dist, curr = heapq.heappop(heap)
            if visit[curr]: continue
            visit[curr]=1
            for n_dist, next in g[curr]:
                if T[next]>dist+n_dist:
                    T[next]=dist+n_dist
                    heapq.heappush(heap,(T[next],next))
        answer.append(T[a]+T[b]+T[s])
    return min(answer)