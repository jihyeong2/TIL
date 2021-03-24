from sys import stdin
n=int(stdin.readline())
maps=[list(map(int, stdin.readline().split())) for _ in range(n)]
dx,dy=(0,1,0,-1),(-1,0,1,0)
tornadoX=[(0,-1,1,-2,-1,1,2,-1,1),(2,1,1,0,0,0,0,-1,-1),(0,-1,1,-2,-1,1,2,-1,1),(-2,-1,-1,0,0,0,0,1,1)]
tornadoY=[(-2,-1,-1,0,0,0,0,1,1),(0,-1,1,-2,-1,1,2,-1,1),(2,1,1,0,0,0,0,-1,-1),(0,-1,1,-2,-1,1,2,-1,1)]
sand=(0.05,0.1,0.1,0.02,0.07,0.07,0.02,0.01,0.01)

tx,ty=n//2,n//2
dir,dist=0,1
result=0
flag=False
while True:
    for _ in range(dist):
        # 이동 & 모래뿌리기
        nx,ny=tx+dx[dir],ty+dy[dir]
        sumSand=0
        for d in range(9):
            nx2,ny2=nx+tornadoX[dir][d],ny+tornadoY[dir][d]
            tmpSand=int(maps[nx][ny]*sand[d])
            sumSand+=tmpSand
            if nx2<0 or ny2<0 or nx2>=n or ny2>=n:
                result+=tmpSand
            else:
                maps[nx2][ny2]+=tmpSand
        maps[nx][ny]-=sumSand
        nx3,ny3=nx+dx[dir],ny+dy[dir]
        if nx3<0 or ny3<0 or ny3>=n or nx3>=n:
            result+=maps[nx][ny]
        else:
            maps[nx3][ny3]+=maps[nx][ny]
        maps[nx][ny]=0
        tx,ty=nx,ny

        if tx == 0 and ty == 0:
            flag=True
            break

    if flag: break
    if dir==1 or dir==3:
        dist+=1
    dir=(dir+1)%4

print(result)