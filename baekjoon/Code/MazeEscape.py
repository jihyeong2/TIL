maps=[list(input()) for _ in range(8)]
def bfs():
    q=[(7,0)]
    dir=((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1),(0,0))
    result=0
    while q:
        size=len(q)
        visit=[[False]*8 for _ in range(8)]
        while size:
            x,y=q.pop(0)
            if x==0 and y==7:
                return 1
            if maps[x][y]!='#':
                for dx,dy in dir:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=8 or ny>=8 or maps[nx][ny]=='#' or visit[nx][ny]: continue
                    visit[nx][ny]=True
                    q.append((nx,ny))
            size-=1

        for i in range(7,0,-1):
            maps[i]=maps[i-1]
        maps[0]=list('.'*8)

    return 0

print(bfs())