import sys
sys.stdin=open("input.txt","r")
dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]
def isPossible(x,y,color,color2,dir,maps,temp):
    nx,ny,cnt=x,y,1
    while True:
        nx,ny=x+dx[dir]*cnt,y+dy[dir]*cnt
        cnt+=1
        if nx<1 or ny<1 or nx>n or ny>n:
            break
        if maps[nx][ny]==0:
            break
        elif maps[nx][ny]==color2:
            temp.append([nx,ny])
        else:
            if len(temp)>0:
                return True
            else:
                return False
    return False
def ocello(x,y,color,maps,ends,result):
    no_cnt,color2 = 0, 1 if color==2 else 2
    for dir in range(8):
        temp=list()
        if isPossible(x,y,color,color2,dir,maps,temp):
            for nx,ny in temp:
                maps[nx][ny]=color
                result[color]+=1
                result[color2]-=1
        else: no_cnt+=1
    if no_cnt>=8:
        ends[color]=1
    else:
        maps[x][y]=color
        result[color]+=1

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    maps=[[0]*(n+1) for _ in range(n+1)]
    ends,result=[0]*3,[2]*3
    maps[n//2][n//2],maps[n//2+1][n//2+1]=2,2
    maps[n//2][n//2+1],maps[n//2+1][n//2]=1,1
    for _ in range(m):
        x,y,color=map(int,input().split())
        if (ends[1] and ends[2]) or result[1] + result[2] >= n * n: break
        if ends[color]: continue
        ocello(x,y,color,maps,ends,result)
    print('#{} {} {}'.format(tc,result[1],result[2]))