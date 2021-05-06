from itertools import permutations
from collections import deque
from copy import deepcopy

import sys
def solution(board, r, c):
    answer = [sys.maxsize]

    def findTarget(x,y,nx,ny,copy_map):
        dr,dc=(-1,1,0,0),(0,0,-1,1)
        q=deque()
        visit=[[0]*4 for _ in range(4)]
        q.append((x,y,0))
        visit[x][y]=1
        while q:
            r,c,cnt=q.popleft()
            if r==nx and c==ny:
                return cnt+1
            for dir in range(4):
                nr,nc=r+dr[dir],c+dc[dir]
                if 0<=nr<4 and 0<=nc<4 and not visit[nr][nc]:
                    q.append((nr,nc,cnt+1))
                    visit[nr][nc]=1
                    nr,nc=r,c
                    while True:
                        nnr,nnc=nr+dr[dir],nc+dc[dir]
                        if nnr<0 or nnc<0 or nnr>=4 or nnc>=4:
                            if not visit[nr][nc]:
                                q.append((nr, nc, cnt + 1))
                                visit[nr][nc] = 1
                            break
                        if copy_map[nnr][nnc]>0 and not visit[nnr][nnc]:
                            q.append((nnr,nnc,cnt+1))
                            visit[nnr][nnc]=1
                            break
                        nr,nc=nnr,nnc


    def findCard(z,lim,res,x,y,char_perm_list,maps):

        if res>answer[0]:
            return
        if z==lim:
            answer[0]=min(answer[0],res)

        else:
            copy_map=deepcopy(maps)
            target=char_perm_list[z]
            dist=findTarget(x,y,targets_loc[target][0][0],targets_loc[target][0][1],copy_map)
            dist+=findTarget(targets_loc[target][0][0],targets_loc[target][0][1],targets_loc[target][1][0],targets_loc[target][1][1],copy_map)
            for r,c in targets_loc[target]:
                copy_map[r][c]=0
            findCard(z+1,lim,res+dist,targets_loc[target][1][0],targets_loc[target][1][1],char_perm_list,copy_map)
            for r,c in targets_loc[target]:
                copy_map[r][c]=target
            dist=findTarget(x,y,targets_loc[target][1][0],targets_loc[target][1][1],copy_map)
            dist+=findTarget(targets_loc[target][1][0],targets_loc[target][1][1],targets_loc[target][0][0],targets_loc[target][0][1],copy_map)
            for r,c in targets_loc[target]:
                copy_map[r][c]=0
            findCard(z + 1, lim, res + dist, targets_loc[target][0][0], targets_loc[target][0][1], char_perm_list, copy_map)

    targets_loc = [[],[],[],[],[],[],[]]
    char_list= []
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                char_list.append(board[i][j])
                targets_loc[board[i][j]].append((i,j))
    char_list=list(set(char_list))
    char_perm=list(map(list,permutations(char_list,3)))
    for chars in char_perm:
        findCard(0,len(chars),0,r,c,chars,board)
    print(answer[0])
    return answer[0]

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1)


