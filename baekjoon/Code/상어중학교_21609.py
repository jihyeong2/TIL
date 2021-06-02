from collections import deque

def bfs(i,j,val,visit):
    global blockGroup,info

    dx,dy=(-1,1,0,0),(0,0,-1,1)
    visit[i][j]=1
    q=deque()
    q.append((i,j))
    temp=[(i,j)]
    t_stX,t_stY=i,j
    cnt=0

    while q:
        x,y=q.popleft()
        if maps[x][y]==0:
            cnt += 1
        if maps[x][y]==val:
            if x>t_stX:
                t_stX,t_stY=x,y
            elif x==t_stX and y>t_stY:
                t_stY=y

        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and maps[nx][ny]>=0:
                if maps[nx][ny]==0 or maps[nx][ny]==val :
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    temp.append((nx,ny))
    flag=False
    if len(temp)<2: return
    if len(temp)>len(blockGroup):
        flag=True
    elif len(temp)==len(blockGroup):
        if info[0]>cnt:
            flag=True
        elif info[0]==cnt:
            if info[1]<t_stX:
                flag=True
            elif info[1]==t_stX and info[2]<t_stY:
                flag=True
    if flag:
        blockGroup = temp
        info = [cnt, t_stX, t_stY]

def gravity():
    for j in range(n):
        tmp=[]
        for i in range(n):
            if maps[i][j]==-2: continue
            elif maps[i][j]==-1:
                idx = i-1
                while tmp:
                    maps[idx][j] = tmp.pop()
                    idx-=1
            else:
                tmp.append(maps[i][j])
                maps[i][j]=-2
        idx=n-1
        while tmp:
            maps[idx][j]=tmp.pop()
            idx-=1

def rotate():
    temp=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=maps[j][n-1-i]
    return temp
def show():
    for i in range(n):
        for j in range(n):
            print(maps[i][j],end=' ')
        print()

n,m=map(int,input().split())
maps=[list(map(int, input().split())) for i in range(n)]

blockGroup=[]
info=[0,n,n]

score=0
while(True):
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j]<=0 or visit[i][j]==1: continue
            bfs(i,j,maps[i][j],visit)
    if len(blockGroup)==0: break
    print(blockGroup)
    score+=(len(blockGroup)**2)

    for x,y in blockGroup:
        maps[x][y]=-2
    blockGroup.clear()
    info = [0, n, n]
    print('없애기')
    show()
    gravity()
    print('중력')
    show()
    maps=rotate()
    print('회전')
    show()
    gravity()
    print('중력2')
    show()

print(score)