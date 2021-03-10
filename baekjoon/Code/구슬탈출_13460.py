dx,dy=(-1,1,0,0),(0,0,-1,1)

def constDir(x):
    if x%2==0:
        return x+1
    return x-1

def perm(z,lim,beforeDir1,beforeDir2,dirs):
    if z==lim:
        bx,by,rx,ry=b_x,b_y,r_x,r_y
        for dir in dirs:
            bCnt, rCnt = 0, 0
            while True:
                n_bx,n_by=bx+dx[dir],by+dy[dir]
                if board[n_bx][n_by]=='#':
                    break
                elif board[n_bx][n_by]=='O':
                    return False
                bx,by=n_bx,n_by
                bCnt+=1
            while True:
                n_rx,n_ry=rx+dx[dir],ry+dy[dir]
                if board[n_rx][n_ry]=='#':
                    break
                elif board[n_rx][n_ry]=='O':
                    return True
                rx,ry=n_rx,n_ry
                rCnt+=1

            if bx==rx and by==ry:
                if bCnt<=rCnt:
                    rx-=dx[dir]
                    ry-=dy[dir]
                else:
                    bx-=dx[dir]
                    by-=dy[dir]

    else:
        for i in range(4):
            if i==beforeDir1 or i==beforeDir2:
                continue
            dirs.append(i)
            if perm(z+1,lim,i,constDir(i),dirs):
                return True
            dirs.pop()

    return False

def bfs():
    def tilt(x,y,dir):
        dist=0
        while True:
            nx,ny=x+dx[dir],y+dy[dir]
            if board[nx][ny]=='#':
                break
            x,y=nx,ny
            dist+=1
            if board[nx][ny]=='O':
                break
        return (x,y,dist)

    q=[(r_x,r_y,b_x,b_y,-1,0)]
    visit=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visit[r_x][r_y][b_x][b_y]=True

    while q:
        rx,ry,bx,by,beforeDir1,tiltCnt=q.pop()
        beforeDir2=constDir(beforeDir1)
        if tiltCnt>=10: break
        for dir in range(4):
            if dir==beforeDir1 or dir==beforeDir2:
                continue
            n_rx,n_ry,r_dist=tilt(rx,ry,dir)
            n_bx,n_by,b_dist=tilt(bx,by,dir)
            if visit[n_rx][n_ry][n_bx][n_by]:
                continue
            if board[n_bx][n_by]=='O':
                continue
            if board[n_rx][n_ry]=='O':
                return tiltCnt+1
            if n_rx==n_bx and n_ry==n_by:
                if r_dist>b_dist:
                    n_rx-=dx[dir]
                    n_ry-=dy[dir]
                else:
                    n_bx-=dx[dir]
                    n_by-=dy[dir]

            q.append((n_rx,n_ry,n_bx,n_by,dir,tiltCnt+1))
            visit[n_rx][n_ry][n_bx][n_by]=True
    return -1

n,m=map(int, input().split())
board=[list(input()) for _ in range(n)]
b_x,b_y,r_x,r_y = -1,-1,-1,-1
for i in range(n):
    for j in range(m):
        if board[i][j]=='B':
            b_x,b_y=i,j
            board[i][j]='.'
        elif board[i][j]=='R':
            r_x,r_y=i,j
            board[i][j]='.'
result=-1
for i in range(1,11):
    if perm(0,i,-1,-1,[]):
        result=i
        break
# result=bfs()
print(result)
