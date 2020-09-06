import sys
sys.stdin=open("input.txt","r")
def miro(sx,sy,n,maps):
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    q=[]
    q.append([sx,sy,0])
    while q:
        x,y,cnt=q.pop(0)
        maps[x][y]='1'
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=n or maps[nx][ny] == '1' : continue
            if maps[nx][ny]=='0':
                q.append([nx,ny,cnt+1])
            else: return cnt
    return 0
T=int(input())
for tc in range(1,T+1):
    n,maps,sx,sy=int(input()),[],-1,-1
    for i in range(n):
        temp=list(input())
        for j in range(n):
            if temp[j]=='2': sx,sy=i,j
        maps.append(temp)
    result=miro(sx,sy,n,maps)
    print('#{} {}'.format(tc,result))