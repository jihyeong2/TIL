import sys
sys.stdin=open("input.txt","r")
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result=987654321
n,w,h = 0,0,0
def copy_brick(bricks):
    global w,h
    cop=list()
    for i in range(h):
        temp=list()
        for j in range(w):
            temp.append(bricks[i][j])
        cop.append(temp)
    return cop
def count_brick(bricks):
    global w,h
    cnt=0
    for i in range(h):
        for j in range(w):
            if bricks[i][j]==0:
                continue
            cnt+=1
    return cnt
def falling_brick(bricks):
    global w,h
    for j in range(w):
        temp=list()
        for i in range(h)[::-1]:
            if bricks[i][j]==0:
                continue
            temp.append(bricks[i][j])
            bricks[i][j]=0
        for i in range(len(temp)):
            bricks[h-1-i][j]=temp[i]
def break_brick(x,y,bricks):
    global w,h
    num=bricks[x][y]
    bricks[x][y]=0
    for i in range(1,num):
        for j in range(4):
            nx=x+dx[j]*i
            ny=y+dy[j]*i
            if nx<0 or ny<0 or nx>=h or ny>=w or bricks[nx][ny]==0:
                continue
            break_brick(nx,ny,bricks)
def dfs(z,bricks):
    global result,w,h,n
    if z>=n :
        min=count_brick(bricks)
        if min<result:
            result=min
    else:
        for j in range(w):
            copy=copy_brick(bricks)
            idx=-1
            for i in range(h):
                if copy[i][j]!=0:
                    idx=i
                    break
            if idx==-1:
                dfs(z+1,copy)
            else:
                break_brick(i,j,copy)
                falling_brick(copy)
                dfs(z+1,copy)
T=int(input())
for tc in range(1,T+1):
    n,w,h = map(int, input().split())
    bricks=list()
    result=987654321
    for _ in range(h):
        bricks.append(list(map(int, input().split())))
    dfs(0,bricks)
    print(f'#{tc} {result}')