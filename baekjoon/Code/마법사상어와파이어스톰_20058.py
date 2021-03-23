from sys import stdin

def rotate(x,y,length):
    tmp=[[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            tmp[i][j]=maps[x+length-1-j][y+i]
    for i in range(length):
        for j in range(length):
            maps[x+i][y+j]=tmp[i][j]

def melting():
    copy_maps=[[0]*(2**n) for _ in range(2**n)]
    for i in range(0,2**n):
        for j in range(0,2**n):
            cnt=0
            if maps[i][j]==0:
                continue
            for d in range(4):
                nx,ny=i+dx[d],j+dy[d]
                if 0<=nx<2**n and 0<=ny<2**n and maps[nx][ny]>0:
                    cnt+=1
            copy_maps[i][j]=maps[i][j]-1 if cnt<3 else maps[i][j]
    return copy_maps

def bfs(a,b):
    visit[a][b]=1
    q=[(a,b)]
    cnt=1
    while q:
        x,y=q.pop(0)
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if nx<0 or ny<0 or nx>=2**n or ny>=2**n or maps[nx][ny]<=0 or visit[nx][ny]:
                continue
            q.append((nx,ny))
            visit[nx][ny]=1
            cnt += 1
    return cnt

dx,dy=(-1,1,0,0),(0,0,-1,1)
n,q=map(int, stdin.readline().split())
maps=[list(map(int, stdin.readline().split())) for _ in range(2**n)]
storms=list(map(int, stdin.readline().split()))

for l in storms:
    if l!=0:
        for i in range(0,2**n,2**l):
            for j in range(0,2**n,2**l):
                if i+2**l<=2**n and j+2**l<=2**n:
                    rotate(i,j,2**l)
    maps=melting()

visit=[[0]*(2**n) for _ in range(2**n)]
result1,result2=0,0
for i in range(2**n):
    for j in range(2**n):
        result1+=maps[i][j]
        if maps[i][j]==0 or visit[i][j]: continue
        tmp=bfs(i,j)
        result2=max(result2,tmp)
if result2 == 1 : result2=0
print(result1)
print(result2)