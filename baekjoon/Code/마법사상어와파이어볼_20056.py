from sys import stdin
dx,dy=(-1,-1,0,1,1,1,0,-1),(0,1,1,1,0,-1,-1,-1)
n,m,k=map(int, stdin.readline().split())
balls=[]
for _ in range(m):
    r,c,m,s,d=map(int, stdin.readline().split())
    balls.append((r-1,c-1,m,s,d))
maps=[[[] for _ in range(n)] for _ in range(n)]

for _ in range(k):
    for i in range(len(balls)):
        r,c,m,s,d=balls[i]
        nr,nc=(r+dx[d]*s)%n,(c+dy[d]*s)%n
        maps[nr][nc].append((nr,nc,m,s,d))
    balls.clear()
    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) == 0 : continue
            elif len(maps[i][j]) == 1:
                balls.append(maps[i][j][0])
            else:
                sumM,sumS=0,0
                odd,even=0,0
                for r,c,m,s,d in maps[i][j]:
                    sumM+=m
                    sumS+=s
                    if d%2==0: even+=1
                    else: odd+=1
                sumM//=5
                sumS//=len(maps[i][j])
                if sumM!=0:
                    if (not odd and even) or (not even and odd) :
                        for dir in range(0,8,2):
                            balls.append((i,j,sumM,sumS,dir))
                    else:
                        for dir in range(1,8,2):
                            balls.append((i,j,sumM,sumS,dir))
            maps[i][j].clear()
result=0
for r,c,m,s,d in balls:
    result+=m

print(result)