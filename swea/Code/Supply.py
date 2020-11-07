import heapq
dx,dy=(-1,1,0,0),(0,0,-1,1)
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int,input())) for _ in range(n)]
    heap=[]
    T=[[float('inf')]*n for _ in range(n)]
    T[0][0]=0
    heapq.heappush(heap,(0,0,0))
    while heap:
        d,x,y=heapq.heappop(heap)
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<n:
                if T[nx][ny]>d+maps[nx][ny]:
                    T[nx][ny]=d+maps[nx][ny]
                    heapq.heappush(heap,(T[nx][ny],nx,ny))
    print('#{} {}'.format(tc,T[n-1][n-1]))