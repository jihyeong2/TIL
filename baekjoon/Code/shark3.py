class shark():
    def __init__(self,x,y,dir,state):
        self.x=x
        self.y=y
        self.dir=dir
        self.state=state
dx,dy=(-1,1,0,0),(0,0,-1,1)
def change_dir(x):
    if x%2==0: return x+1
    else: return x-1

def move_shark(maps,s,smell_cnt,prio_dirs):
    for i in range(1,m+1):
        if s[i].state == 1: continue
        cx,cy,cd=s[i].x,s[i].y,s[i].dir
        nx2,ny2,nd2=-1,-1,-1
        for d in range(4):
            nx,ny,nd=cx+dx[prio_dirs[i-1][cd][d]-1],cy+dy[prio_dirs[i-1][cd][d]-1],prio_dirs[i-1][cd][d]-1
            if 0 <= nx < n and 0 <= ny < n:
                if smell_cnt[nx][ny]==0:
                    if maps[nx][ny]==0 or i < maps[nx][ny]:
                        maps[nx][ny]=i
                    s[i].x, s[i].y, s[i].dir = nx, ny, nd
                    break
                else:
                    if maps[nx][ny]==i :
                        if nx2==-1:
                            nx2,ny2,nd2=nx,ny,nd
        else:
            s[i].x,s[i].y,s[i].dir=nx2,ny2,nd2
def smell(maps,s,smell_cnt):
    for i in range(1,m+1):
        if s[i].state == 1: continue
        x,y=s[i].x,s[i].y
        if maps[x][y]!=i:
            s[i].state = 1
        else:
            smell_cnt[x][y]=k+1
            maps[x][y]=i

def smell_down(maps,smell_cnt):
    for i in range(n):
        for j in range(n):
            if smell_cnt[i][j] == 0: continue
            smell_cnt[i][j]-=1
            if smell_cnt[i][j] == 0:
                maps[i][j]=0
def count_shark(s):
    cnt=0
    for i in range(1,m+1):
        if s[i].state==0:
            cnt+=1
    return cnt
n,m,k = map(int, input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
s_dirs=list(map(int, input().split()))
prio_dirs=[[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
smell_cnt=[[0]*n for _ in range(n)]
s=[shark(0,0,0,0) for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        num=maps[i][j]
        if num!=0:
            smell_cnt[i][j]=k
            s[num].x,s[num].y,s[num].dir=i,j,s_dirs[num-1]-1
result=0
for time in range(1,1001):
    move_shark(maps,s,smell_cnt,prio_dirs)
    smell(maps,s,smell_cnt)
    smell_down(maps, smell_cnt)
    count=count_shark(s)
    if count==1:
        result=time
        break
else:
    result=-1
print(result)