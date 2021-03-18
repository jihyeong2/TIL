dr,dc=(-1,0,1,0),(0,1,0,-1)
def check(r,c,d):
    for i in range(1,5):
        dir=d-i if d-i>=0 else d-i+4
        nr,nc=r+dr[dir],c+dc[dir]
        if 0<=nr<n and 0<=nc<m and maps[nr][nc]!=1 and not visit[nr][nc]:
            return dir
    return -1

n,m=map(int, input().split())
r,c,d=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            visit[i][j]=2
result=0
while True:
    if not visit[r][c] :
        result+=1
        visit[r][c]=1
    x=check(r,c,d)
    print('({} {} {}) ->'.format(r,c,d),end=' ')
    if x==-1: # 네 방향 모두 X
        nr,nc=r+dr[(d+2)%4],c+dc[(d+2)%4]
        if nr<0 or nc<0 or nr>=n or nc>=m or maps[nr][nc]==1:
            break
        r,c=nr,nc
    else:
        d=x
        r+=dr[d]
        c+=dc[d]
    print('({} {} {})'.format(r,c,d))
    for row in visit:
        print(row)
    print()

print(result)