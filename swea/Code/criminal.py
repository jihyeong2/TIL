import sys
sys.stdin=open("input.txt","r")
ternel=[[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def isPossible(a,b,x,y,maps):
    next=maps[a][b]-1
    for dir in ternel[next]:
        nx,ny=a+dx[dir],b+dy[dir]
        if nx<0 or ny<0 or nx>=n or ny>=m: continue
        if nx==x and ny==y: return True
    return False
def bfs(r,c,n,m,l,maps):
    q=list()
    q.append([r,c])
    visit=set()
    visit.add((r,c))
    t,res=1,1
    while q:
        t+=1
        if t>l: break
        size=len(q)
        while size:
            x,y=q.pop(0)
            current=maps[x][y]-1
            for dir in ternel[current]:
                nx,ny=x+dx[dir],y+dy[dir]
                if nx<0 or ny<0 or nx>=n or ny>=m:  continue
                if maps[nx][ny]==0 or (nx,ny) in visit: continue
                if isPossible(nx,ny,x,y,maps):
                    res+=1
                    q.append([nx,ny])
                    visit.add((nx,ny))
            size-=1
    return res

T=int(input())
for tc in range(1,T+1):
    n,m,r,c,l=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(n)]
    print('#{} {}'.format(tc, bfs(r,c,n,m,l,maps)))
