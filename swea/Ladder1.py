import sys
sys.stdin=open("input.txt","r")
dy=[-1,1]
def goDown(x,y,lad):
    res=0
    if x>=99:
        if lad[x][y]==2:
            return 1
    else:
        flag=0
        for d in dy:
            ny=y+d
            if ny<0 or ny>=100 or lad[x][ny]==0: continue
            while True:
                ny+=d
                if ny < 0 or ny >= 100 or lad[x][ny] == 0: break
            res+=goDown(x+1,ny-d,lad)
            flag=1
        if flag==0:
            res+=goDown(x+1,y,lad)
    return res

for _ in range(10):
    tc=int(input())
    lad=[list(map(int,input().split())) for _ in range(100)]
    for j in range(100):
        if lad[0][j]==0: continue
        if goDown(0,j,lad):
            result=j
            break
    print('#{} {}'.format(tc,result))