import copy
arr=[]
dx=[0,-1,-1,0,1,1,1,0,-1]
dy=[0,0,-1,-1,-1,0,1,1,1]
def positions_fishes(maps,x,y):
    positions=[]
    dir=maps[x][y][1]
    while True:
        x+=dx[dir]
        y+=dy[dir]
        if 0<=x<4 and 0<=y<4 :
            if 1<=maps[x][y][0]<=16:
                positions.append([x,y])
        else: break
    return positions
def find_fish(maps,num):
    for i in range(4):
        for j in range(4):
            if maps[i][j][0]==num:
                return i,j
def move_fish(maps,s_x,s_y):
    for i in range(1,17):
        position=find_fish(maps,i)
        if position==None: continue
        f_x,f_y=position
        f_dir=maps[f_x][f_y][1]
        for dir in range(8):
            n_dir=(f_dir+dir)
            if n_dir>8 : n_dir-=8
            nx,ny=f_x+dx[n_dir],f_y+dy[n_dir]
            if 0<=nx<4 and 0<=ny<4 :
                if not(nx==s_x and ny==s_y):
                    maps[f_x][f_y][0],maps[nx][ny][0]=maps[nx][ny][0],maps[f_x][f_y][0]
                    maps[f_x][f_y][1],maps[nx][ny][1]=maps[nx][ny][1],n_dir
                    break
def dfs(total,maps,s_x,s_y):
    global result
    copy_maps=copy.deepcopy(maps)
    num=copy_maps[s_x][s_y][0]
    copy_maps[s_x][s_y][0]=-1
    move_fish(copy_maps,s_x,s_y)
    positions=positions_fishes(copy_maps,s_x,s_y)
    result=max(result,total+num)
    for nx,ny in positions:
        dfs(total+num,copy_maps,nx,ny)
for i in range(4):
    temp=list(map(int, input().split()))
    arr.append([])
    for j in range(0,8,2):
        arr[i].append([temp[j],temp[j+1]])
result=0
dfs(0,arr,0,0)
print(result)