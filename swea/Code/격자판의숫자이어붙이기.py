# import sys
# sys.stdin=open("input.txt","r")
# def bfs(a,b,maps,num):
#     q=[[a,b,0,maps[a][b]]]
#     dx,dy=[-1,1,0,0],[0,0,-1,1]
#     while q:
#         x,y,dist,tmp_num=q.pop(0)
#         if dist==6:
#             num.add(tmp_num)
#         else:
#             for dir in range(4):
#                 nx,ny=x+dx[dir],y+dy[dir]
#                 if nx<0 or ny<0 or nx>=4 or ny>=4: continue
#                 q.append([nx,ny,dist+1,tmp_num*10+maps[nx][ny]])
# T=int(input())
# for tc in range(1,T+1):
#     maps=[list(map(int,input().split())) for _ in range(4)]
#     num=set()
#     for i in range(4):
#         for j in range(4):
#             bfs(i,j,maps,num)
#     print('#{} {}'.format(tc,len(num)))

import sys
sys.stdin = open("input.txt","r")
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def DFS(a,b,k,char):
    global result
    if k==6:
        result.add(char)
    else:
        for dir in range(4):
            nr,nc=a+dr[dir],b+dc[dir]
            if 0<=nr<4 and 0<=nc<4:
                DFS(nr,nc,k+1,char+str(arr[nr][nc]))
T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int,input().split())) for _ in range(4) ]
    result=set()
    for i in range(4):
        for j in range(4):
            DFS(i,j,0,str(arr[i][j]))
    print(len(result))