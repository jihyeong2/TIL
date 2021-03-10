from sys import stdin
from copy import deepcopy
from collections import deque
dx,dy=(-1,1,0,0),(0,0,-1,1)
def comb(z,idx):
    if z==3:
        global result
        copy_maps=deepcopy(maps)
        q=deque()
        tmp_result=len(blank)-3
        for virus in viruses:
            q.append(virus)
        while q:
            x,y=q.popleft()
            for dir in range(4):
                nx,ny=x+dx[dir],y+dy[dir]
                if 0<=nx<n and 0<=ny<m and copy_maps[nx][ny]==0:
                    copy_maps[nx][ny]=2
                    q.append((nx,ny))
                    tmp_result-=1
        result=max(result,tmp_result)
    else:
        for i in range(idx,len(blank)):
            x,y=blank[i]
            maps[x][y]=1
            comb(z+1,i+1)
            maps[x][y]=0
n,m=map(int,stdin.readline().split())
maps=[list(map(int, stdin.readline().split())) for _ in range(n)]
blank,viruses=[],[]
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            blank.append((i,j))
        elif maps[i][j]==2:
            viruses.append((i,j))
result=float('-inf')
comb(0,0)
print(result)