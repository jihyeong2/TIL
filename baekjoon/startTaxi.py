class taxi():
    def __init__(self,x,y,fuel):
        self.x=x
        self.y=y
        self.fuel=fuel
def bfs(maps,t):
    if maps[t.x][t.y] >= 10:
        return (maps[t.x][t.y]-10,0)
    q,visit=[],set()
    dx,dy=(-1,1,0,0),(0,0,-1,1)
    q.append([t.x,t.y,0])
    visit.add((t.x,t.y))
    f_dist,f_num,f_x,f_y=-1,-1,-1,-1
    while q:
        size=len(q)
        while size:
            x,y,dist=q.pop(0)
            for dir in range(4):
                nx,ny=x+dx[dir],y+dy[dir]
                if 0 <= nx < n and 0 <= ny <n and (nx,ny) not in visit:
                    if maps[nx][ny]==1: continue
                    elif maps[nx][ny]==0:
                        q.append([nx,ny,dist+1])
                        visit.add((nx,ny))
                    elif maps[nx][ny]>=10:
                        if f_num==-1:
                            f_dist,f_num,f_x,f_y=dist+1,maps[nx][ny],nx,ny
                        else:
                            if nx<f_x:
                                f_dist,f_num,f_x,f_y=dist+1,maps[nx][ny],nx,ny
                            elif nx==f_x:
                                if ny<f_y:
                                    f_dist,f_num,f_x,f_y=dist+1,maps[nx][ny],nx,ny
            size-=1
        if f_num != -1: break
    if f_num == -1: return (-1,-1)
    return (f_num-10,f_dist)
def bfs2(maps,num):
    q, visit = [], set()
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    q.append([people[num][0], people[num][1], 0])
    visit.add((people[num][0], people[num][1]))
    result=-1
    while q:
        x,y,dist=q.pop(0)
        if x==people[num][2] and y==people[num][3]:
            result=dist
            break
        for dir in range(4):
            nx,ny=x+dx[dir], y+dy[dir]
            if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visit:
                if maps[nx][ny]==1: continue
                q.append([nx,ny,dist+1])
                visit.add((nx,ny))
    return result
n,m,init_fuel=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
taxi_position=list(map(int, input().split()))
people=[list(map(int, input().split())) for _ in range(m)]
t=taxi(taxi_position[0]-1,taxi_position[1]-1,init_fuel)
people_state=[0]*m
for i in range(m):
    people[i][0]-=1
    people[i][1]-=1
    people[i][2]-=1
    people[i][3]-=1
    maps[people[i][0]][people[i][1]]=i+10
result=0
while m:
    num,path1=bfs(maps,t)
    if num == -1 :
        break
    path2=bfs2(maps,num)
    if path2 == -1:
        break
    if t.fuel < path1+path2:
        break
    t.fuel=t.fuel-(path1+path2)+(path2*2)
    t.x,t.y=people[num][2],people[num][3]
    maps[people[num][0]][people[num][1]]=0
    m-=1
if m :
    result=-1
else:
    result=t.fuel
print(result)