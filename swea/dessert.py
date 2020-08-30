import sys
sys.stdin=open("input.txt","r")
def goCafe(x,y,r,c,maps):
    xx,yy=x+r+c,y+c-r
    visit=set()
    for i in range(0,r):
        nx1,ny1=x+i,y-i
        nx2,ny2=xx-i,yy+i
        if maps[nx1][ny1] in visit: return -1
        visit.add(maps[nx1][ny1])
        if maps[nx2][ny2] in visit: return -1
        visit.add(maps[nx2][ny2])
    for i in range(1,c+1):
        nx1,ny1=x+i,y+i
        nx2,ny2=xx-i,yy-i
        if maps[nx1][ny1] in visit: return -1
        visit.add(maps[nx1][ny1])
        if maps[nx2][ny2] in visit: return -1
        visit.add(maps[nx2][ny2])
    return len(visit)
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int, input().split())) for _ in range(n)]
    result=-1
    for i in range(n-2):
        for j in range(1,n-1):
            for r in range(1,n-1):
                for c in range(1,n-1):
                    if j-r<0 or j+c>=n or i+r+c>=n: continue
                    result=max(result,goCafe(i,j,r,c,maps))
    print('#{} {}'.format(tc,result))