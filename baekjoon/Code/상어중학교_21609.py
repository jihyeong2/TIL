from collections import deque
dx,dy=(-1,1,0,0),(0,0,-1,1)

def bfs(i,j,val):
    visit = [[0] * n for _ in range(n)]
    q=deque()
    q.append((i,j))
    visit[i][j]=1
    group=[(i,j)]
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir], y+dy[dir]
            if 0<=nx<n and 0<=ny<n :
                if visit[nx][ny]!=0 or maps[nx][ny]<0: continue
                if maps[nx][ny]!=0 and maps[nx][ny]!=val: continue
                q.append((nx,ny))
                group.append((nx,ny))
                visit[nx][ny]=1
    if len(group) < 2:
        return -1,-1,-1,-1

    x,y,cnt = n,n,0
    for a,b in group:
        if maps[a][b] == 0:
            cnt+=1
        else:
            if a<x:
                x,y=a,b
            elif a==x:
                if b<y:
                    x,y=a,b

    return group,x,y,cnt

def gravity():
    for j in range(n):
        tmp=[]
        for i in range(n):
            if maps[i][j]==-2: continue
            elif maps[i][j]==-1:
                tmp.append(-1)
            else:
                tmp.append(maps[i][j])
                maps[i][j]=-2
        flag=True
        for i in range(n-1,-1,-1):
            if len(tmp)<=0:
                break
            if flag==True:
                val=tmp.pop()
                if val == -1:
                    flag=False
            if flag == False:
                if maps[i][j] == -1:
                    flag=True
                continue
            maps[i][j]=val


def rotate():
    global maps
    tmp_maps=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp_maps[i][j] = maps[j][n-1-i]
    maps=tmp_maps

n,m=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
result=0
while True:
    blockGroup,stX,stY,rainbowCnt = [],-1,-1,-1
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                tmpGroup,tmpX,tmpY,tmpRainbowCnt = bfs(i,j,maps[i][j])
                if tmpGroup == -1:
                    continue
                if len(tmpGroup) > len(blockGroup):
                    blockGroup,stX,stY,rainbowCnt = tmpGroup,tmpX,tmpY,tmpRainbowCnt
                elif len(tmpGroup) == len(blockGroup):
                    if tmpRainbowCnt > rainbowCnt:
                        blockGroup, stX, stY, rainbowCnt = tmpGroup, tmpX, tmpY, tmpRainbowCnt
                    elif tmpRainbowCnt == rainbowCnt:
                        if tmpX > stX:
                            blockGroup, stX, stY, rainbowCnt = tmpGroup, tmpX, tmpY, tmpRainbowCnt
                        elif tmpX == stX:
                            if tmpY > stY:
                                blockGroup, stX, stY, rainbowCnt = tmpGroup, tmpX, tmpY, tmpRainbowCnt
    if len(blockGroup)==0:
        break
    result+=len(blockGroup)**2
    for x,y in blockGroup:
        maps[x][y]=-2
    gravity()
    rotate()
    gravity()

print(result)