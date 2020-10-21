state_dir=((0,2),(1,2),(0,1,2))
dx,dy=(0,1,1),(1,0,1)
check=(((0,1),),((1,0),),((0,1),(1,1),(1,0)))
n=int(input())
maps=[list(map(int, input().split())) for _ in range(n)]
dp=[[[0]*n for _ in range(n)] for _ in range(n)]
dp[0][1][0]=1
for y in range(2,n):
    if maps[0][y]==0:
        dp[0][y][0]=dp[0][y-1][0]
for x in range(1,n):
    for y in range(1,n):
        if maps[x][y]==0 and maps[x-1][y]==0 and maps[x][y-1]==0:
            dp[x][y][2]=dp[x-1][y-1][0]+dp[x-1][y-1][1]+dp[x-1][y-1][2]
        if maps[x][y]==0:
            dp[x][y][0]=dp[x][y-1][0]+dp[x][y-1][2]
            dp[x][y][1]=dp[x-1][y][1]+dp[x-1][y][2]
print(dp[n-1][n-1][0]+dp[n-1][n-1][1]+dp[n-1][n-1][2])