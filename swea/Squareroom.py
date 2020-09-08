import sys
sys.stdin=open("input.txt","r")
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,maps):
    global max_cnt,room,n
    q=list()
    cnt=0
    q.append([x,y])
    while q:
        size=len(q)
        cnt+=1
        for _ in range(size):
            xx,yy=q.pop(0)
            for i in range(4):
                nx=xx+dx[i]
                ny=yy+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n: continue
                if maps[nx][ny]-maps[xx][yy]!=1: continue
                q.append([nx,ny])
    if cnt>max_cnt:
        max_cnt=cnt
        room=maps[x][y]
    elif cnt==max_cnt and maps[x][y]<room:
        room=maps[x][y]
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int,input().split())) for _ in range(n)]
    max_cnt,room=-1,-1
    for i in range(n):
        for j in range(n):
            bfs(i,j,maps)
    print(f'#{tc} {room} {max_cnt}')