dx,dy=(-1,1,0,0,0),(0,0,-1,1,0)

def move_water(waters):
    n_waters=[]
    for x,y in waters:
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny]=='.':
                n_waters.append((nx,ny))
                maps[nx][ny]='*'
    return n_waters

def dfs(biber,waters,time):
    global result
    time+=1
    if len(biber)==0:
        return False
    n_waters=move_water(waters)
    next=[]

    for x,y in biber:
        for dir in range(5):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<r and 0<=ny<c :
                if maps[nx][ny]=='D':
                    result=time
                    return True
                if maps[nx][ny]=='.' and (nx,ny) not in next:
                    next.append((nx,ny))
    if dfs(next,n_waters,time):
        return True
    return False


r,c=map(int, input().split())
maps=[list(input()) for _ in range(r)]
water=[]
sx,sy,ex,ey=-1,-1,-1,-1
for i in range(r):
    for j in range(c):
        if maps[i][j]=='D':
            ex,ey=i,j
        elif maps[i][j]=='S':
            sx,sy=i,j
            maps[i][j]='.'
        elif maps[i][j]=='*':
            water.append((i,j))
        else: continue
result="KAKTUS"
dfs([(sx,sy)],water,0)
print(result)