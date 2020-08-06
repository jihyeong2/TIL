import sys
sys.stdin=open("input.txt","r")
T=int(input())
n,m,k=0,0,0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for tc in range(1,T+1):
    n,m,k=map(int, input().split())
    init_map=[list(map(int,input().split())) for i in range(n)]
    maps=[[0]*350 for _ in range(351)]
    visit=[[False]*350 for _ in range(351)]
    cell=list()
    cell_temp = list()
    for i in range(n):
        for j in range(m):
            if init_map[i][j]==0: continue
            maps[i+150][j+150]=init_map[i][j]
            visit[i+150][j+150]=True
            cell.append([i+150,j+150,init_map[i][j],init_map[i][j],0])
    result=len(cell)
    for time in range(1,k+1):
        for i in range(len(cell_temp)):
            x, y, life, t, state = cell_temp[i]
            if maps[x][y] != life: continue
            cell_temp[i][3]=time+cell_temp[i][2]
            cell.append(cell_temp[i])
            visit[x][y]=True
            result+=1
        cell_temp.clear()
        for i in range(len(cell)):
            if cell[i][4]==-1: continue
            elif cell[i][4]==0:
                if cell[i][3]!=time: continue
                cell[i][4]=1
                cell[i][3]+=cell[i][2]
                for j in range(4):
                    nx=cell[i][0]+dx[j]
                    ny=cell[i][1]+dy[j]
                    if visit[nx][ny]: continue
                    if maps[nx][ny]<cell[i][2]:
                        maps[nx][ny]=cell[i][2]
                        cell_temp.append([nx,ny,cell[i][2],0,0])
            elif cell[i][4]==1:
                if cell[i][3]==time:
                    cell[i][4]=-1
                    result-=1
    print(f'#{tc} {result}')