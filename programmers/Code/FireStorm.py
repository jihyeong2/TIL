def bfs(x,y,visit):
    res=1
    q=[(x,y)]
    visit[x][y]=True
    while q:
        r,c=q.pop(0)
        for dir in range(4):
            nr,nc=r+dx[dir],c+dy[dir]
            if nr<0 or nc<0 or nr>=2**n or nc>=2**n or visit[nr][nc] or maps[nr][nc]<=0: continue
            res+=1
            q.append((nr,nc))
            visit[nr][nc]=True
    return res
n,q=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(2**n)]
magics=list(map(int, input().split()))
dx,dy=(-1,1,0,0),(0,0,-1,1)
for l in magics:
    if l>0:
        tmp = [[0] * (2 ** l) for _ in range(2 ** l)]
        for i in range(0,2**n,2**l):
            for j in range(0,2**n,2**l):
                for r in range(2**l):
                    for c in range(2**l):
                        tmp[c][2**l-1-r]=maps[i+r][j+c]
                for r in range(2**l):
                    for c in range(2**l):
                        maps[i+r][j+c]=tmp[r][c]
    melting=[]
    for r in range(2**n):
        for c in range(2**n):
            if maps[r][c]==0: continue
            cnt=0
            for dir in range(4):
                nr,nc=r+dx[dir],c+dy[dir]
                if nr<0 or nc<0 or nr>=2**n or nc>=2**n : continue
                if maps[nr][nc]<=0: continue
                cnt+=1
            if cnt<3:
                melting.append((r,c))
    for x,y in melting:
        maps[x][y]-=1
remain=0
for row in maps:
    remain+=sum(row)
lump_cnt=0
visit=[[False]*(2**n) for _ in range(2**n)]
for x in range(2**n):
    for y in range(2**n):
        if not visit[x][y] and maps[x][y]!=0:
            lump_cnt=max(bfs(x,y,visit),lump_cnt)
if lump_cnt==1: lump_cnt=0
print(remain)
print(lump_cnt)