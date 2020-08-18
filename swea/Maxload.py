import sys
sys.stdin=open("input.txt","r")
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(n,maps,start):
    result_max=-1
    for point in start:
        s=list()
        s.append([point[0],point[1],1])
        while s:
            x,y,cnt=s.pop()
            result_max=max(result_max,cnt)
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n: continue
                if maps[nx][ny]>=maps[x][y]:continue
                s.append([nx,ny,cnt+1])
    return result_max
T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(n)]
    max_height,result = 0,0
    start=list()
    for i in range(n):
        for j in range(n):
            max_height=max(max_height,maps[i][j])
    for i in range(n):
        for j in range(n):
            if max_height==maps[i][j]:
                start.append([i,j])
    for i in range(n):
        for j in range(n):
            for l in range(k+1):
                maps[i][j]-=l
                result=max(result,dfs(n,maps,start))
                maps[i][j]+=l
    print(f'#{tc} {result}')