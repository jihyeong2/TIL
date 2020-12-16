dx,dy=(-1,1,0,0),(0,0,-1,1)
def findDot(dots,dir,target):
    global result
    x,y=dots[-1]
    if dir==-1:
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==target:
                findDot(dots+[(nx,ny)],d,target)
                if result=='Yes': return
    else:
        nx,ny=x+dx[dir],y+dy[dir]
        next=(dir,2,3) if dir<=1 else (dir,0,1)
        for d in next:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == target:
                if (nx,ny)==dots[0] and len(dots)>=4:
                    result='Yes'
                    return
                else:
                    if (nx,ny) not in dots :
                        findDot(dots + [(nx, ny)], d, target)
                        if result == 'Yes': return
n,m=map(int, input().split())
maps=[list(input()) for _ in range(n)]
result=''
for i in range(n):
    for j in range(m):
        findDot([(i,j)],-1,maps[i][j])
        if result=='Yes': break
    if result=='Yes': break
else:
    result='No'
print(result)
