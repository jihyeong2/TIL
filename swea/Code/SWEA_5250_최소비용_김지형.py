# dx,dy=(-1,1,0,0),(0,0,-1,1)
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     maps=[list(map(int, input().split())) for _ in range(n)]
#     visit=[[False]*n for _ in range(n)]
#     T[0][0]=0
#     for i in range(n):
#         for j in range(n):
#             minVal,minX,minY=float('inf'),-1,-1
#             for a in range(n):
#                 for b in range(n):
#                     if not visit[a][b] and T[a][b]<minVal:
#                         minVal,minX,minY=T[a][b],a,b
#             visit[minX][minY]=True
#             for dir in range(4):
#                 nx,ny=minX+dx[dir],minY+dy[dir]
#                 if 0<=nx<n and 0<=ny<n:
#                     dist = 1 + maps[nx][ny] - maps[minX][minY] if maps[nx][ny] > maps[minX][minY] else 1
#                     T[nx][ny]=min(T[nx][ny],T[minX][minY]+dist)
#     print('#{} {}'.format(tc,T[n-1][n-1]))

dx,dy=(-1,1,0,0),(0,0,-1,1)
def bfs():
    T[0][0]= 0
    q=[(0,0)]
    while q:
        x,y=q.pop(0)
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                dist = 1 + maps[nx][ny] - maps[x][y] if maps[nx][ny] > maps[x][y] else 1
                if T[x][y]+dist<T[nx][ny]:
                    q.append((nx,ny))
                    T[nx][ny]=T[x][y]+dist

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int, input().split())) for _ in range(n)]
    T = [[float('inf')] * n for _ in range(n)]
    bfs()
    print('#{} {}'.format(tc, T[n - 1][n - 1]))