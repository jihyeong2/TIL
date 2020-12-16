from copy import deepcopy
dx,dy=(-1,1,0,0),(0,0,-1,1)
def bfs(s_cnt,sx,sy,x_x,x_y,board):
    visit=[[0]*n for _ in range(m)]
    visit[sx][sy]=1
    q=[(s_cnt,sx,sy)]
    while q:
        cnt,x,y=q.pop(0)
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if nx<0 or ny<0 or nx>=m or ny>=n or visit[nx][ny] : continue
            if nx==x_x and ny==x_y:
                return cnt+1,nx,ny
            if board[nx][ny]=='.' or board[nx][ny]=='X':
                q.append((cnt+1,nx,ny))
                visit[nx][ny]=1
            else: continue

def dfs(z,lim,n_items):
    global result
    if z==lim:
        cnt,x,y=0,sx,sy
        board=deepcopy(maps)
        for num in n_items:
            cnt,x,y=bfs(cnt,x,y,items[num][0],items[num][1],board)
        cnt,x,y=bfs(cnt,x,y,ex,ey,board)
        result=min(result,cnt)
    else:
        for i in range(len(items)):
            if i not in n_items:
                n_items.append(i)
                dfs(z+1,lim,n_items)
                n_items.pop(-1)

n,m=map(int, input().split())
maps=[list(input()) for _ in range(m)]
items=[]
sx,sy,ex,ey=-1,-1,-1,-1
for i in range(m):
    for j in range(n):
        if maps[i][j]=='S':
            sx,sy=i,j
            maps[i][j]='.'
        elif maps[i][j]=='E':
            ex,ey=i,j
            maps[i][j]='.'
        elif maps[i][j]=='X':
            items.append((i,j))
        else: continue
result=float('inf')
dfs(0,len(items),[])
print(result)
