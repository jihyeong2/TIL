dx,dy=(0,-1,1,0,0),(0,0,0,-1,1)
n,m=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
one,two,three=0,0,0
def changeDir(dir):
    if dir==1:
        return 3
    elif dir==2:
        return 4
    elif dir==3:
        return 2
    else:
        return 1

def remove(d,s):
    x,y=n//2,n//2
    for i in range(1,s+1):
        x=x+dx[d]
        y=y+dy[d]
        maps[x][y]=0

def move():
    x, y = n // 2, n // 2
    dir,dist,dist2=3,1,1
    tmp=[]
    while True:

        x+=dx[dir]
        y+=dy[dir]
        if not(0<=x<n and 0<=y<n):
            break
        if maps[x][y]!=0:
            tmp.append(maps[x][y])
            maps[x][y]=0
        dist2 -= 1
        if dist2<=0:
            dir=changeDir(dir)
            if dir==3 or dir==4:
                dist+=1
            dist2=dist
    x, y = n // 2, n // 2
    dir,dist,dist2,idx=3,1,1,0
    while idx<len(tmp):
        x+=dx[dir]
        y+=dy[dir]
        if not(0<=x<n and 0<=y<n):
            break
        dist2 -= 1
        maps[x][y]=tmp[idx]
        idx+=1
        if dist2<=0:
            dir=changeDir(dir)
            if dir==3 or dir==4:
                dist+=1
            dist2=dist


def bomb():
    global one, two, three
    x, y = n // 2, n // 2
    dir,dist,dist2=3,1,1
    before,cnt=-1,0
    tmp=[]
    while True:
        x+=dx[dir]
        y+=dy[dir]
        if not(0<=x<n and 0<=y<n):
            break
        if maps[x][y] != 0:
            if before == -1 or maps[x][y] == before:
                tmp.append((x, y))

            else:
                if len(tmp) >= 4:
                    if before == 1:
                        one += len(tmp)
                    elif before == 2:
                        two += len(tmp)
                    else:
                        three += len(tmp)
                    cnt+=len(tmp)
                    while tmp:
                        nx, ny = tmp.pop()
                        maps[nx][ny] = 0
                tmp.clear()
                tmp.append((x,y))
            before = maps[x][y]

        dist2 -= 1
        if dist2<=0:
            dir=changeDir(dir)
            if dir==3 or dir==4:
                dist+=1
            dist2=dist
    if len(tmp)>=4:
        if before == 1:
            one += len(tmp)
        elif before == 2:
            two += len(tmp)
        else:
            three += len(tmp)
        while tmp:
            nx, ny = tmp.pop()
            maps[nx][ny] = 0
    return cnt

def relocation():
    x, y = n // 2, n // 2
    dir,dist,dist2=3,1,1
    tmp=[]
    before,cnt=-1,0
    while True:
        x+=dx[dir]
        y+=dy[dir]
        if not(0<=x<n and 0<=y<n):
            break
        if maps[x][y] != 0:
            if before==-1 or maps[x][y]==before:
                cnt+=1
            else:
                tmp.append((cnt,before))
                cnt=1
            before=maps[x][y]

        dist2 -= 1
        maps[x][y]=0
        if dist2<=0:
            dir=changeDir(dir)
            if dir==3 or dir==4:
                dist+=1
            dist2=dist
    if before==-1: return
    tmp.append((cnt,before))
    x, y = n // 2, n // 2
    dir, dist, dist2 = 3, 1, 1
    idx,cnt,tmp2 = 0,0,[]
    while True:
        x+=dx[dir]
        y+=dy[dir]
        if not(0<=x<n and 0<=y<n):
            break
        if idx>=len(tmp) and cnt==0:
            break
        if cnt==0:
            val1,val2=tmp[idx]
            tmp2.append(val1)
            tmp2.append(val2)
            idx+=1
        maps[x][y]=tmp2[cnt]
        cnt+=1
        if cnt>=2:
            cnt=0
            tmp2.clear()
        dist2 -= 1

        if dist2<=0:
            dir=changeDir(dir)
            if dir==3 or dir==4:
                dist+=1
            dist2=dist

for _ in range(m):
    d,s=map(int, input().split())
    remove(d,s)
    move()
    while True:
        tmp=bomb()
        move()
        if tmp==0:
            break
    relocation()

print(one+(2*two)+(3*three))
