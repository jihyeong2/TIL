from sys import stdin

dx,dy=(-1,1,0,0),(0,0,-1,1)
def dfs(z,x,y,maxResult):
    if z==3:
        global result
        result=max(result,maxResult)
    else:
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m or visit[nx][ny]: continue
            visit[nx][ny]=True
            dfs(z+1,nx,ny,maxResult+maps[nx][ny])
            visit[nx][ny]=False

def exceptionCheck(x,y):
    global result
    if 0<=y-1 and y+1<m and x+1<n:
        result=max(result,maps[x][y-1]+maps[x][y]+maps[x][y+1]+maps[x+1][y])
    if 0<=y-1 and y+1<m and 0<=x-1:
        result=max(result,maps[x][y-1]+maps[x][y]+maps[x][y+1]+maps[x-1][y])
    if 0<=x-1 and x+1<n and 0<=y-1:
        result=max(result,maps[x-1][y]+maps[x+1][y]+maps[x][y]+maps[x][y-1])
    if 0<=x-1 and x+1<n and y+1<m:
        result=max(result,maps[x-1][y]+maps[x+1][y]+maps[x][y]+maps[x][y+1])

n,m=map(int,stdin.readline().split())
maps=[list(map(int, stdin.readline().split())) for _ in range(n)]
visit=[[False]*m for _ in range(n)]
result=-1
for i in range(n):
    for j in range(m):
        visit[i][j]=True
        dfs(0,i,j,maps[i][j])
        exceptionCheck(i,j)
        visit[i][j]=False
print(result)