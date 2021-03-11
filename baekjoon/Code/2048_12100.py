from sys import stdin
from copy import deepcopy

dx,dy=(-1,1,0,0),(0,0,-1,1)

def maxVal(maps):
    res=-1
    for row in maps:
        for x in row:
            res=max(res,x)
    return res

def conflict(blocks):
    arr=[]
    for i in range(len(blocks)-1):
        if blocks[i] and blocks[i]==blocks[i+1]:
            blocks[i]+=blocks[i]
            blocks[i+1]=0
    for val in blocks:
        if val:
            arr.append(val)

    return arr

def tilt(maps,dir):
    tmp=[]
    if dir==0 : # 위로 기울이기
        for j in range(n):
            for i in range(n):
                if maps[i][j]:
                    tmp.append(maps[i][j])
                    maps[i][j]=0
            tmp=conflict(tmp)
            i=0
            while tmp:
                maps[i][j]=tmp.pop(0)
                i+=1

    elif dir==1: # 아래로 기울이기
        for j in range(n):
            for i in range(n-1,-1,-1):
                if maps[i][j]:
                    tmp.append(maps[i][j])
                    maps[i][j]=0
            tmp = conflict(tmp)
            i=n-1
            while tmp:
                maps[i][j]=tmp.pop(0)
                i-=1

    elif dir==2: # 왼쪽으로 기울이기
        for i in range(n):
            for j in range(n):
                if maps[i][j]:
                    tmp.append(maps[i][j])
                    maps[i][j]=0
            tmp = conflict(tmp)
            j=0
            while tmp:
                maps[i][j]=tmp.pop(0)
                j+=1

    else: # 오른쪽으로 기울이기
        for i in range(n):
            for j in range(n-1,-1,-1):
                if maps[i][j]:
                    tmp.append(maps[i][j])
                    maps[i][j]=0
            tmp = conflict(tmp)
            j=n-1
            while tmp:
                maps[i][j]=tmp.pop(0)
                j-=1

def perm(z,lim,dirs):
    if(z==lim):
        global result
        copy_board = deepcopy(board)
        for dir in dirs:
            tilt(copy_board,dir)

        result=max(result,maxVal(copy_board))
    else:
        for d in range(4):
            dirs.append(d)
            perm(z+1,lim,dirs)
            dirs.pop()

n=int(stdin.readline())
board=[list(map(int,stdin.readline().split())) for _ in range(n)]
result=-1
perm(0,5,[])
print(result)