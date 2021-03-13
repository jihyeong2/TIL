from sys import stdin
dx,dy=(-1,1,0,0),(0,0,-1,1)

class snake:
    def __init__(self):
        self.dir=3
        self.body=[(0,0)]

def changeDir(curr,next):
    if curr==0:
        return 2 if next=='L' else 3
    elif curr==1:
        return 3 if next=='L' else 2
    elif curr==2:
        return 1 if next=='L' else 0
    else:
        return 0 if next=='L' else 1

n,k=int(stdin.readline()),int(stdin.readline())
maps=[[0]*n for _ in range(n)]

for _ in range(k):
    x,y=map(int, stdin.readline().split())
    maps[x-1][y-1]=1
maps[0][0]=8

l=int(stdin.readline())
dirs=[False]*l

for i in range(l):
    x,c=stdin.readline().split()
    dirs[i]=(int(x),c)

s=snake()
time=0

while True:
    time+=1
    x,y=s.body[0]
    nx,ny=x+dx[s.dir],y+dy[s.dir]

    if nx<0 or ny<0 or nx>=n or ny>=n or maps[nx][ny]==8: # 벽 or 내몸
        break

    if maps[nx][ny]==0: # 빈칸
        a,b=s.body.pop(-1)
        maps[a][b]=0

    maps[nx][ny] = 8
    s.body = [(nx, ny)] + s.body

    if dirs and dirs[0][0]==time:
        s.dir=changeDir(s.dir,dirs[0][1])
        dirs.pop(0)

print(time)