import sys
sys.stdin=open("input.txt","r")
blockDir=[[],[1,3,0,2],[3,0,1,2],[2,0,3,1],[1,2,3,0],[1,0,3,2]]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def game(i,j,k,maps,warmhole):
    x,y,dir,sum=i,j,k,0
    while True:
        x,y=x+dx[dir],y+dy[dir]
        if x<0 or y<0 or x>=n or y>=n:
            sum+=1
            dir=blockDir[5][dir]
            continue
        if (i==x and j==y) or (maps[x][y]==-1):
            return sum
        if 1<=maps[x][y]<=5:
            sum+=1
            dir=blockDir[maps[x][y]][dir]
        elif 6<=maps[x][y]<=10:
            for hole in warmhole[maps[x][y]-6]:
                if hole[0]!=x or hole[1]!=y:
                    x,y=hole[0],hole[1]
                    break
    return sum
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int,input().split())) for _ in range(n)]
    warmhole=[[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if 6<=maps[i][j]<=10:
                warmhole[maps[i][j]-6].append([i,j])
    print(warmhole)
    result=0
    for i in range(n):
        for j in range(n):
            if maps[i][j]!=0:continue
            for k in range(4):
                score=game(i,j,k,maps,warmhole)
                result=max(result,score)
    print(f'#{tc} {result}')