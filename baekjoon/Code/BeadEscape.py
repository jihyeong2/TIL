# class bead():
#     def __init__(self,x,y,dist):
#         self.x=x
#         self.y=y
#         self.dist=dist
# def reverse_dir(dir):
#     if dir%2==0:
#         return dir+1
#     else:
#         return dir-1
# def tilt(z,max_z,dirs,before):
#     dx,dy=[-1,1,0,0,],[0,0,-1,1]
#     if z==max_z:
#         red,blue=bead(rx,ry,0),bead(bx,by,0)
#         for dir in dirs:
#             while True:
#                 blue.x+=dx[dir]
#                 blue.y+=dy[dir]
#                 blue.dist+=1
#                 # print(dir,blue.x,blue.y,maps[blue.x][blue.y])
#                 if maps[blue.x][blue.y]=='.': continue
#                 elif maps[blue.x][blue.y]=='#':
#                     blue.x-=dx[dir]
#                     blue.y-=dy[dir]
#                     blue.dist-=1
#                     break
#                 else:
#                     return False
#             while True:
#                 red.x+=dx[dir]
#                 red.y+=dy[dir]
#                 red.dist+=1
#                 # print(dir,red.x,red.y,maps[red.x][red.y])
#                 if maps[red.x][red.y]=='.': continue
#                 elif maps[red.x][red.y]=='#':
#                     red.x -= dx[dir]
#                     red.y -= dy[dir]
#                     red.dist -= 1
#                     break
#                 else:
#                     return True
#             if red.x==blue.x and red.y==blue.y:
#                 if red.dist>blue.dist:
#                     red.x-=dx[dir]
#                     red.y-=dy[dir]
#                 else:
#                     blue.x-=dx[dir]
#                     blue.y-=dy[dir]
#             red.dist,blue.dist=0,0
#     else:
#         for dir in range(4):
#             if z>0 and (before==dir or reverse_dir(before)==dir):
#                 continue
#             dirs.append(dir)
#             if tilt(z+1,max_z,dirs,dir):
#                 return True
#             dirs.pop(-1)
#         return False
# n,m=map(int, input().split())
# maps=[]
# rx,ry,bx,by=0,0,0,0
# for i in range(n):
#     temp=list(input())
#     maps.append(temp)
#     if 'R' in temp:
#         rx,ry=i,temp.index('R')
#         maps[rx][ry]='.'
#     if 'B' in temp:
#         bx,by=i,temp.index('B')
#         maps[bx][by] = '.'
# for t in range(1,11):
#     if tilt(0,t,[],-1):
#         result=t
#         break
# else:
#     result=-1
# print(result)
def reverse_dir(x):
    if x%2==0: return x+1
    else: return x-1
def move(x,y,dir):
    cnt=0
    while maps[x+dx[dir]][y+dy[dir]]!='#' and maps[x][y]!='O':
        x+=dx[dir]
        y+=dy[dir]
        cnt+=1
    return x,y,cnt
def bfs(visit, q):
    while q:
        rx, ry, bx, by, before_dir1, dist = q.pop(0)
        before_dir2=reverse_dir(before_dir1)
        if dist >= 10:
            break
        for dir in range(4):
            if before_dir1==dir or before_dir2==dir:
                continue
            n_rx, n_ry, r_cnt = move(rx, ry, dir)
            n_bx, n_by, b_cnt = move(bx, by, dir)
            if maps[n_bx][n_by] == 'O':
                continue
            if maps[n_rx][n_ry] == 'O':
                return dist+1
            if n_rx==n_bx and n_ry==n_by:
                if r_cnt>b_cnt:
                    n_rx-=dx[dir]
                    n_ry-=dy[dir]
                else:
                    n_bx-=dx[dir]
                    n_by-=dy[dir]
            if not visit[n_rx][n_ry][n_bx][n_by]:
                visit[n_rx][n_ry][n_bx][n_by]=True
                q.append((n_rx,n_ry,n_bx,n_by,dir,dist+1))
    return -1
n,m=map(int, input().split())
maps=[list(input()) for _ in range(n)]
visit=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q=[]
dx,dy=(-1,1,0,0),(0,0,-1,1)
for i in range(n):
    for j in range(m):
        if maps[i][j]=='R':
            Rx,Ry=i,j
            maps[i][j]='.'
        if maps[i][j]=='B':
            Bx,By=i,j
            maps[i][j]='.'
q.append((Rx,Ry,Bx,By,-1,0))
visit[Rx][Ry][Bx][By]=True
result=bfs(visit,q)
print(result)