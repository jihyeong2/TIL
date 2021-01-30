from collections import deque
n,m,T=map(int,input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
visit=[[0 for _ in range(m)] for _ in range(n)]
q=deque()
q.append((0,0,0))
dx,dy=(-1,1,0,0),(0,0,-1,1)
result=float('inf')
while q:
    x,y,t=q.popleft()
    if x==n-1 and y==m-1:
        result=min(result,t)
        break
    if t+1>T : break
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
            if maps[nx][ny]==1: continue
            elif maps[nx][ny]==0:
                visit[nx][ny]=True
                q.append((nx,ny,t+1))
            else:
                visit[nx][ny]=True
                tmp=t+1+abs(nx-(n-1))+abs(ny-(m-1))
                if tmp<=T:
                    result=tmp
if result>T:
    print("Fail")
else:
    print(result)