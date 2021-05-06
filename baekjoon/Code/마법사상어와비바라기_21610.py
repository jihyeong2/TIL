n,m=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
info=[list(map(int, input().split())) for _ in range(m)]
dx,dy=(0,0,-1,-1,-1,0,1,1,1),(0,-1,-1,0,1,1,1,0,-1)
check=[[0]*n for _ in range(n)]
clouds=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for dir,dist in info:
    # 구름이동
    for i in range(len(clouds)):
        x,y=clouds[i][0],clouds[i][1]
        nx,ny=(x+dx[dir]*dist)%n,(y+dy[dir]*dist)%n
        clouds[i][0],clouds[i][1]=nx,ny
    # 물뿌리기
    for x,y in clouds:
        maps[x][y]+=1

    # 물복사
    for x,y in clouds:
        cnt=0
        for d in range(2,9,2):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n and maps[nx][ny]>0:
                cnt+=1
        maps[x][y]+=cnt
        check[x][y]=1

    # 구름 사라지기
    clouds.clear()

    # 구름 생성
    for i in range(n):
        for j in range(n):
            if check[i][j]==1:
                check[i][j]=0
                continue
            if maps[i][j]>=2:
                clouds.append([i,j])
                maps[i][j]-=2

res=0
for i in range(n):
    for j in range(n):
        res+=maps[i][j]

print(res)