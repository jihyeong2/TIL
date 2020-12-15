dr,dc=(0,1,0,-1),(-1,0,1,0)
sand_dr=[(0,1,-1,1,-1,2,-2,1,-1),(2,1,1,0,0,0,0,-1,-1),
         (0,-1,1,-1,1,-2,2,-1,1),(-2,-1,-1,0,0,0,0,1,1)]
sand_dc=[(-2,-1,-1,0,0,0,0,1,1),(0,1,-1,1,-1,2,-2,1,-1),
         (2,1,1,0,0,0,0,-1,-1),(0,-1,1,-1,1,-2,2,-1,1)]
sand_prop=(0.05,0.1,0.1,0.07,0.07,0.02,0.02,0.01,0.01)
n=int(input())
maps=[list(map(int, input().split())) for _ in range(n)]
r,c,dir,cnt,result=n//2,n//2,0,1,0
flag=False
while True:
    for _ in range(cnt):
        r+=dr[dir]
        c+=dc[dir]
        sum=0
        if r<0 or c<0 or r>=n or c>=n :
            flag=True
            break
        if maps[r][c]==0: continue
        for d in range(9):
            nr,nc,prop=r+sand_dr[dir][d],c+sand_dc[dir][d],sand_prop[d]
            tmp = int(maps[r][c] * prop)
            sum+=tmp
            if nr<0 or nc<0 or nr>=n or nc>=n:
                result+=tmp
            else:
                maps[nr][nc]+=tmp
        maps[r][c]-=sum
        nr,nc=r+dr[dir],c+dc[dir]
        if nr<0 or nc<0 or nr>=n or nc>=n:
            result+=maps[r][c]
        else:
            maps[nr][nc]+=maps[r][c]
        maps[r][c]=0
    if flag: break
    dir=(dir+1)%4

    if dir==0 or dir==2:
        cnt+=1

print(result)