from sys import stdin

dx,dy=(0,0,0,-1,1),(0,1,-1,0,0)
def rolling(dir,dice):
    tmp=[x for x in dice]
    eastWest=[4,1,5,3]
    if dir==1: #동
        for i in range(4):
            idx=3 if i-1<0 else i-1
            tmp[eastWest[i]]=dice[eastWest[idx]]
    elif dir==2: #서
        for i in range(4):
            idx=(i+1)%4
            tmp[eastWest[i]] = dice[eastWest[idx]]
    elif dir==3: #북
        for i in range(4):
            idx=(i+1)%4
            tmp[i]=dice[idx]
    else: #남
        for i in range(3,-1,-1):
            idx=3 if i-1<0 else i-1
            tmp[i]=dice[idx]
    return tmp

n,m,x,y,k=map(int, stdin.readline().split())
maps=[list(map(int,stdin.readline().split())) for _ in range(n)]
moveDir=list(map(int,stdin.readline().split()))
dice=[0]*6
# 0: 북, 1: 위, 2: 남, 3: 아래, 4: 서, 5: 동
for dir in moveDir:
    nx,ny=x+dx[dir],y+dy[dir]
    if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
    dice=rolling(dir,dice)
    if maps[nx][ny]==0:
        maps[nx][ny]=dice[3]
    else:
        dice[3]=maps[nx][ny]
        maps[nx][ny]=0
    print(dice[1])
    x,y=nx,ny