from copy import deepcopy
def rotation(n_maps,i):
    r,c,s=rots[i][0]-1,rots[i][1]-1,rots[i][2]
    dx,dy=(0,1,0,-1),(1,0,-1,0)
    for d in range(s,0,-1):
        x,y,dir,tmp=r-d,c-d,0,n_maps[r-d][c-d]
        while dir<4:
            nx,ny=x+dx[dir],y+dy[dir]
            if r-d<=nx<=r+d and c-d<=ny<=c+d:
                n_maps[nx][ny],tmp=tmp,n_maps[nx][ny]
                x,y=nx,ny
            else:
                dir+=1


def perm(z,maps, check):
    if z==k:
        global result
        for row in maps:
            result=min(result,sum(row))
    else:
        for i in range(k):
            n_maps = deepcopy(maps)
            if check[i]: continue
            check[i]=True
            rotation(n_maps,i)
            perm(z+1,n_maps,check)
            check[i]=False

n,m,k=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
rots=[list(map(int, input().split())) for _ in range(k)]
check=[False for _ in range(k)]
result=float('inf')
perm(0,arr,check)
print(result)